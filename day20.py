from utilities import get_lines
from copy import deepcopy
from functools import reduce
from queue import Queue

# low = False, high = True
def product(input: list):
    return reduce(lambda x, y: x * y, input)

class Module():
    queue = None
    num_pulses = [0, 0]

    def __init__(self, name, inputs, outputs) -> None:
        self.name = name
        self.inputs = inputs[:]
        self.outputs = outputs[:]
        self.queue = Module.queue

    def send_pulse(self, is_high):
        for output in self.outputs:
            Module.num_pulses[is_high] += 1
            self.queue.put((output, is_high, self))

    def receive_pulse(self, is_high, from_neighbor):
        pass

    def __str__(self) -> str:
        return f'{self.name} - {type(self).__name__}'
    
    def __repr__(self) -> str:
        return self.__str__()

class FlipFlop(Module):
    def __init__(self, name, inputs, outputs) -> None:
        super().__init__(name, inputs, outputs)
        self.on = False

    def receive_pulse(self, is_high: bool, from_neighbor = None):
        if not is_high:
            self.on = not self.on
            self.send_pulse()

    def send_pulse(self):
        super().send_pulse(self.on)

class Conjunction(Module):
    def __init__(self, name, inputs, outputs) -> None:
        super().__init__(name, inputs, outputs)
        self.memory = {}
        for input in inputs:
            self.memory[input] = False

    def receive_pulse(self, is_high: bool, from_neighbor: Module):
        self.memory[from_neighbor.name] = is_high
        self.send_pulse()

    def send_pulse(self):
        if all([x for x in self.memory.values()]):
            super().send_pulse(False)
        else:
            super().send_pulse(True)

class Broadcaster(Module):
    def __init__(self, name, inputs, outputs) -> None:
        super().__init__(name, inputs, outputs)
        self.on = False

    def receive_pulse(self, is_high: bool, from_neighbor = None):
        self.on = is_high
        self.send_pulse()

    def send_pulse(self):
        super().send_pulse(self.on)
        
def build_modules(all_lines):
    modules: dict[str, Module] = {}
    for line in all_lines:
        module, outputs = line.split(' -> ')
        outputs = outputs.split(', ')
        if module[0] == 'b':
            modules['broadcaster'] = Broadcaster('broadcaster', [], outputs)
        if module[0] == '%':
            modules[module[1:]] = FlipFlop(module[1:], [], outputs)
        if module[0] == '&':
            modules[module[1:]] = Conjunction(module[1:], [], outputs)

    # check outputs for uncreated Modules
    # solely for the sample?
    module_copy = list(modules.values())
    for module in module_copy:
        for output in module.outputs:
            if output not in modules:
                modules[output] = Module(output, [module], [])

    # update inputs
    for target_name, target_module in modules.items():
        inputs = []
        for name, module in modules.items():
            if target_name in module.outputs:
                inputs.append(name)
        target_module.inputs = inputs
        if isinstance(target_module, Conjunction):
            target_module.memory = {name: False for name in inputs}
        
        target_module.outputs = [modules[name] for name in target_module.outputs]
    return modules

import math
def part2(is_test: bool = True):
    all_lines = get_lines(20, is_test)
    
    Module.queue = Queue()
    modules = build_modules(all_lines)

    message_queue = Module.queue
    push = 0
    firsts = {}
    seconds = {}
    while True:
        Module.num_pulses[False] += 1
        push += 1
        message_queue.put((modules['broadcaster'], False, 'button'))

        while not message_queue.empty():
            receiver, value, sender = message_queue.get()
            if receiver.name in ['sg', 'lm', 'dh', 'db'] and not value:
                print(receiver.name, push)

            if receiver.name == 'rx' and value == False:
                return push
            receiver.receive_pulse(value, sender)


if __name__ == "__main__":
    print(part2(False))