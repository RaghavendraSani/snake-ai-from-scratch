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
        self.hidden = np.dot(x, self.w1) + self.b1
        self.hidden = self.relu(self.hidden)
        self.output = np.dot(self.hidden, self.w2) + self.b2
        return self.output

    def get_action(self, state):
        output = self.forward(state)
        action = np.argmax(output)
        print(action)
        return action
    #    return np.argmax(output)

    def relu(self, x):
        return np.maximum(0, x)

    def mse_loss(self, prediction, target):
        return np.mean((prediction - target) ** 2)


nn = NeuralNetwork()

prediction = np.array([2, 5])
target = np.array([2, 9])
print(nn.mse_loss(prediction, target))

"""
test = np.array([[-4, 7, -1, 3, 0]])
print(nn.relu(test))
"""
"""
def get_action(self, state):
    output = self.forward(state)
    action = np.argmax(output)
    print(action)
    return action
    return np.argmax(output)
"""
