from pynput.mouse import Button, Controller, Listener
import time
import json


count = 0

def on_click(x, y, button, pressed):
    if pressed and button == Button.middle:
        positions.append((x, y))
        print(f"Saved position: {x}, {y}")
        global count
        count += 1
        if count == 7:
            print("All positions saved. Writing a yaml file with the positions.")
            return False  # Stop listening 
            


print("Loading ...")
time.sleep(2)
print("Mining Bitcoin ...")
time.sleep(2)
print("Programm ready!")

positions = []

print("Press the middle mouse button to save positions please click only one time per position and in the following correct order in order to let the Dishwasher correctly do this job!")
print("1. Position: Button where you can buy the dirty plate")
print("2. Position: TOP LEFT corner of the areas where the dirty plates spawn (if you are unsure just buy a buch of them")
print("3. Position: TOP RIGHT corner of the areas where the dirty plates spawn")
print("4. Position: BOTTOM RIGHT corner of the areas where the dirty plates spawn")
print("5. Position: BOTTOM LEFT corner of the areas where the dirty plates spawn")
print("6. Position: In the middle of the screen where the dirty plate appears")
print("7. Position: Button where you can collect the money after washing the dirty plate")
with Listener(on_click=on_click) as listener:
    listener.join()


json_dict = {
    "buy_dirty_plate": positions[0],
    "top_left": positions[1],
    "top_right": positions[2],
    "bottom_right": positions[3],
    "bottom_left": positions[4],
    "dirty_plate_middle": positions[5],
    "collect_money_button": positions[6]
} 
with open("positions.json", "w") as file:
    json.dump(json_dict, file)