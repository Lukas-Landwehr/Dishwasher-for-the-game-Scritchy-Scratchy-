# Dishwasher for the game Scritchy Scratchy
https://store.steampowered.com/app/3948120/Scritchy_Scratchy/


Automatic Dishwasher for washing the  dirty dishes using python to controll the mouse

# Requirements

```
pip install numpy
pip install mouse
pip install pynput
```
The Python libraries for controlling the mouse don't work with wayland, but it works with x11

# How to run

![screenshot](image.png)


Use Position_grabber.py to get the position for each button, the program will guide you in the temrinal. All positions will be saved in positions.json, which the Dishwasher.py uses for washing the dirty dishes :)
```
python Position_grabber.py
```


```
python Dishwasher.py
```
Default iterations is 1000, you can change it with -n "your number"
