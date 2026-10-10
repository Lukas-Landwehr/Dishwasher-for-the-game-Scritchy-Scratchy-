import mouse
from pynput.mouse import Button, Controller
import time
import numpy as np
import json
import argparse

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int, default=1000)
args = parser.parse_args()

with open("positions.json", "r") as file:
    positions = json.load(file)
print(positions)



time.sleep(2)
m = Controller()
for i in range(args.number):
    print(f"####### Iteration: {i}   #######")
    rng = np.random.default_rng()
    x = rng.integers(low=positions["top_left"][0], high=positions["top_right"][0])
    y = rng.integers(low=positions["top_left"][1], high=positions["bottom_left"][1])

    print("Moving Mouse to buy dirty ahhh plate")
    mouse.move(positions["buy_dirty_plate"][0], positions["buy_dirty_plate"][1], absolute=True, duration=0.2)
    print("Buying dirty ahhh plate")
    m.click(Button.left)


    time.sleep(2)

    print("Moving Mouse to wash dirty ahhh plate")
    mouse.move(x, y, absolute=True, duration=0.2)
    print("Washing dirty ahhh plate")

    time.sleep(1)
    
    m.press(Button.left)
    time.sleep(1)
    m.release(Button.left)


    m.press(Button.left)
    time.sleep(14)
    m.release(Button.left)

    time.sleep(1)


    print("Collecting the bag after washing dirty ahhh plate")
    mouse.move(positions["collect_money_button"][0], positions["collect_money_button"][1], absolute=True, duration=0.2)
    m.click(Button.left)




