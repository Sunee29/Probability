import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for i in range(count):
                self.contents.append(color)
        
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        
        balls_drawn = []
        for i in range(num_balls):
            index = random.randint(0, len(self.contents)-1)
            balls_drawn.append(self.contents.pop(index))
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_matches = 0
    
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        
        expected_balls_copy = copy.deepcopy(expected_balls)
        match = True
        for color in expected_balls_copy.keys():
            if balls_drawn.count(color) < expected_balls_copy[color]:
                match = False
                break
            else:
                balls_drawn.remove(color)
        if match:
            num_matches += 1
    
    return num_matches / num_experiments
