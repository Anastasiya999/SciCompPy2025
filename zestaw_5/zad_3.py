#Create the generator random_walk(start) for a 1D random walker.
#If a position at a certain moment is x, then the next position can be x+1 or x-1 with equal probabilities.
#Find the final position after 100 moves (start=0). Repeat experiments.
import random

def random_walk(start):
    x = start
    while True:
        yield x
        x += random.choice([-1, 1])

def run_walk( start, steps):
    random_walker = random_walk(start)
    next_x = start
    for _ in range(steps):
        next_x = next(random_walker)
    return next_x

if __name__ == "__main__":
    experiments = 5
    for i in range(experiments):
        final_position = run_walk(0, 100)
        print(f"Experiment {i+1}: Final random walker position is {final_position}")

