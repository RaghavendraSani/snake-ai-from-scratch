import numpy as np

class NeuralNetwork:
    def __init__(self):
        self.input_size = 8
        self.hidden_size = 16
        self.output_size = 4

        self.w1 = np.random.randn(self.input_size, self.hidden_size)
        self.w2 = np.random.randn(self.hidden_size, self.output_size)

        self.b1 = np.zeros((1,self.hidden_size))
        self.b2 = np.zeros((1,self.output_size))

    def forward(self,x):
        hidden = np.dot(x, self.w1) + self.b1
        output = np.dot(hidden, self.w2) + self.b2
        return output


nn = NeuralNetwork()
state = np.array([[0,1,0,0,0,1,0,0]])
print(nn.forward(state))

def get_action(self, state):
    output = self.forward(state)
    action = np.argmax(output)
    print(action)
    return action
#    return np.argmax(output)
