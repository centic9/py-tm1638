#!/usr/bin/env python

# TM1638 playground

import TM1638
import time

# These are the pins the display is connected to. Adjust accordingly.
# In addition to these you need to connect to 5V and ground.

DIO = 17
CLK = 27
STB = 22

display = TM1638.TM1638(DIO, CLK, STB)

display.enable(1)

count = 0.1
while True:
    display.set_text(str(count)[-8:])
    count /= 10
    time.sleep(1.00)

