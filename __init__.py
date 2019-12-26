# __init__.py
# from . import operation # call operation module in this calcpkg  | . means current package
# from . import geometry  # call geometry module in this calcpkg   | . means current package
# from .operation import add, mul # bring function in the current package in module operation
# from .geometry import triangle_area, rectangle_area
from .operation import * # bring all class, fun, variable in module in peration in current package (. = calcpkg)
from .geometry import *
