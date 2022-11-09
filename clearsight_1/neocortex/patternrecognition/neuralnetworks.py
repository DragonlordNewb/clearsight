import random

class FeedforwardNeuron:
    def __init__(self, function):
        self.inputs = []
        self.outputs = []
        self.weight = 0
        self.bias = 0
        self.function = function
        self._history = []

    def run(self):
        self.outputs = [x + self.weight - self.bias for x in self.function(self.inputs)]
        if len(self.outputs) == 1:
            self.outputs = self.outputs[0]

    def weight(self, value):
        # Weight the neuron
        self.weight += value
        self.history.append([True, value])

    def bias(self, value):
        # Bias the neuron
        self.bias += value
        self.history.append([False, value])

    def reverse(self, n=1):
        # Reverse changes done to the neuron
        for _ in range(n):
            # Pop the last change off of the neuron's history
            lastChange = self._history.pop()

            if lastChange[0]:
                # Change was a weight
                self.weight(-1 * lastChange[1])
            else:
                # Change was a bias
                self.bias(-1 * lastChange[1])

class FeedforwardNeuralNetworkLayer:
    def __init__(self, neuron, width):
        self.neurons = [neuron for _ in range(width)]

    def setInputs(self, *inputs):
        for neuron in self.neurons:
            neuron.inputs = inputs

    def getOutputs(self):
        output = []
        for neuron in self.neurons:
            output.append(neuron.outputs)
        return output

    def run(self):
        for neuron in self.neurons:
            neuron.run()

    def weight(self, value):
        for neuron in self.neurons:
            neuron.weight(value)

    def bias(self, value):
        for neuron in self.neurons:
            neuron.bias(value)

    def randomize(self, charge=1):
        for neuron in self.neurons:
            if bool(random.getrandbits(1)):
                neuron.weight(random.random() * charge)
            else:
                neuron.bias(random.random() * charge)

class FeedforwardNeuralNetwork:
    def __init__(self, *layers):
        self.layers = layers
        self.optimizer = optimizer

    def run(self, *inputs):
        self.layers[0].setInputs(*inputs)
        self.layers[0].run()

        for layerIndex in range(len(self.layers[1:])):
            self.layers[layerIndex].setInputs(self.layers[layerIndex - 1].getOutputs())
            self.layers[layerIndex].run()

        return self.layers[-1].getOutputs()

    def matchPattern(self, **patterns):
        # Monte Carlo optimizer

        pass
