from .problem import TSP

from .heuristics.random_heuristic import random_heuristic
from .heuristics.nearest_neighbor import nearest_neighbor_heuristic
from .heuristics.farthest_insertion import farthest_insertion_heuristic
from .heuristics.nearest_insertion import nearest_insertion_heuristic

from .neighborhoods.ns_switch import Switch
from .neighborhoods.ns_shift import Shift
