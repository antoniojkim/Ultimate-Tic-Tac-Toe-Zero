
import torch
import numpy as np

import time

class Memory():

    def __init__(self, max_memory_size, buckets=True, **kwargs):
        self.max_memory_size = max_memory_size
        self.buckets = buckets
        self.memory = []

    def __getitem__(self, i):
        return self.memory[i]

    def __len__(self):
        return len(self.memory)

    def remember(self, items):
        if self.buckets:
            self.memory.append(items)
        else:
            self.memory.extend(items)

        if self.max_memory_size is not None:
            excess = len(self.memory) - self.max_memory_size
            if excess > 0: del self.memory[:excess]

    def sample(self, num):
        if len(self.memory) > 0:
            indices = list(np.random.randint(len(self.memory), size=num))
            if not self.buckets:
                return [self.memory[i] for i in indices]
            else:
                indices = [(i, np.random.randint(len(self.memory[i]))) for i in indices]
                return [self.memory[i][j] for i, j in indices]

        return []


class BaseModel(torch.nn.Module):

    def __init__(self, max_size=None, buckets = True, 
                batch_size=1, mini_batch_size = 64, discount=0.95,
                verbose=False, 
                **kwargs):

        super(BaseModel, self).__init__()

    
    def load_weights(self, state_dict_path: str):
        self.load_state_dict(torch.load(state_dict_path))
        self.eval()

    def save_weights(self, state_dict_path: str):
        torch.save(self.state_dict(), state_dict_path)

    
    def conv_out_shape(self, input, kernel, stride):
        c = 1 # input[0]
        h = (input[0]-(kernel-1)-1)/stride+1
        w = (input[1]-(kernel-1)-1)/stride+1
        if h%1 != 0:
            print(input, "->", (c, h, w))
            raise Exception("Height out is not an integer")
        if w%1 != 0:
            print(input, "->", (c, h, w))
            raise Exception("Width out is not an integer")
        return int(h), int(w)


    def transform(self, x):
        return np.array(x)


    def forward(self, x):
        return x


    def predict(self, x, device=None):
        if device is None:
            return self.forward(torch.tensor(torch.from_numpy(self.transform(x)), dtype=torch.double)).detach().numpy()

        return self.forward(torch.tensor(torch.from_numpy(self.transform(x)), dtype=torch.double).to(device)).cpu().detach().numpy()



class Trainer:

    def __init__(self, model, device, **kwargs):
        self.model = model
        self.device = device

        self.memory = Memory(**kwargs)
        self.init_trainer(**kwargs)
        self.init_batch(**kwargs)

    
    def init_trainer(self, learning_rate, milestones, momentum=0, loss="MSELoss", **kwargs):
        self.optimizer = torch.optim.SGD(self.model.parameters(), lr=learning_rate, momentum=momentum)
        self.criterion = getattr(torch.nn, loss)()
        self.scheduler = torch.optim.lr_scheduler.MultiStepLR(self.optimizer, milestones=milestones)


    def init_batch(self, batch_size, mini_batch_size, discount=0.95, **kwargs):
        self.batch_size = batch_size
        self.mini_batch_size = mini_batch_size
        self.discount = discount

    
    def experience_replay(self):
        if len(self.memory) > 0:
            batches = []
            for _ in range(min(self.batch_size, len(self.memory))): # np.random.randint(1, 2)
                sample = self.memory.sample(self.mini_batch_size)

                values = self.model.predict([s[0] for s in sample], self.device)
                predictions = [0 for v in values] # self.model.predict([s[4] for s in sample], self.device)

                batch_input = []
                batch_label = []
                for s, value, prediction in zip(sample, values, predictions):
                    state, action, reward, terminal, next_state = s
                    batch_input.append(state)

                    label = value
                    label[action] = reward+(self.discount*np.amin(prediction) if not terminal else 0)
                    batch_label.append(label)

                batches.append((self.model.transform(batch_input), np.array(batch_label)))
                
            if len(batches) > 0:
                self.scheduler.step()
                running_loss = 0
                for batch_input, batch_label in batches:
                    input_tensor = torch.from_numpy(batch_input).double().to(self.device)
                    label_tensor = torch.from_numpy(batch_label).double().to(self.device)
            
                    self.optimizer.zero_grad()
                    outputs = self.model.forward(input_tensor)
                    loss = self.criterion(outputs, label_tensor)
                    loss.backward()
                    self.optimizer.step()
                    running_loss += loss.item()

                    if running_loss > 1000000000:
                        # print([list(map(float, x)) for x in [list(batch_input[0].ravel())]])  
                        # print([list(map(float, x)) for x in list(batch_input)])  
                        print([list(map(float, x)) for x in list(outputs.cpu().detach().numpy())])   
                        # print([list(map(float, x)) for x in [batch_label]])   
                        print([list(map(float, x)) for x in list(batch_label)])   
                        exit(1)

                return running_loss / len(batches)
                



def argmax(x):
    return np.random.choice(np.flatnonzero(x == x.max()))


current_time_milli = lambda: int(round(time.time() * 1000))