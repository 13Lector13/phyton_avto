import math
import os
from math import pi
from pathlib import Path
from json import *
from random import *
import datetime as dt
import sys as system

import pytest
from pytest import mark
from pytest import *
import pytest as pt

import my_math
import logging
from my_math import add
from my_math import subtract
from my_math import *
from logging import *
import my_math as mm
from my_math import add as my_add

print("Math PI:", math.pi)
print("PI from direct import:", pi)

current_path = Path(".")
print("Current path:", current_path.resolve())

print("Random number:", randint(1, 10))
print("Current datetime:", dt.datetime.now())

print("OS name:", os.name)
print("Python executable:", system.executable)

print("Add works:", add(2, 3) == 5)

print("Pytest mark exists:", hasattr(mark, "smoke"))
print("Pytest alias works:", hasattr(pytest, "__version__"))

print("Add from my_math:", add(3, 4))
print("Subtract from my_math:", subtract(10, 3))
print("Add via alias:", my_add(5, 6))
print("Module alias works:", mm.add(1, 2))

logging.info("Logging import works")


