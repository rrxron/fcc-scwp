import copy
import random

class Hat:

    def __init__(self, **kwargs):
        # retrieve keyword arguments
        hat = {}
        for k, v in kwargs.items():
            hat[k] = hat.get(k, v)

        # setup list of balls to contents
        self.contents = []
        for k, v in hat.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, num_of_balls_drawn):
        # if the number exceeds supply, return all balls
        if len(self.contents) < num_of_balls_drawn:
            return self.contents

        # retrieve random balls and use that to remove the one from list
        listReturn = []
        for _ in range(num_of_balls_drawn):
            listReturn.append(\
                self.contents.pop(random.randrange(len(self.contents))))

        return listReturn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # setup our initial values for the experiment to determine probability
    N = num_experiments
    M = 0

    # do N number of experiments
    for _ in range(N):
        # prepare test, use deepcopy so future tests are not affected
        # then use the .draw() method to get our draw_test data
        draw_test = copy.deepcopy(hat).draw(num_balls_drawn)

        # assume we have good draw_test from the start
        good_test = True
        # verify good_test
        for k,v in expected_balls.items():
            # if expected_balls value > draw_test, then discard draw_test
            # meaning, the balls we acquired are less than the expected
            if v > draw_test.count(k):
                good_test = False
                break
        # if verified draw_test was good, then add to M
        if good_test: M += 1

    # calculate probability
    return M/N