import random
import math
from collections.abc import Callable
from ..common import Problem
from ..common import Neighborhood

def simulated_anneling(
    problem: Problem,
    start_solution: object,
    neighborhood_function: Neighborhood,
    start_temp: float,
    cooling_rate: float,
    k_max: float|int,
    rng: random.Random,
    max_iter: float=math.inf,
    eps: float=1e-6,
    cb: Callable[[int,object,int|float],None]=lambda iter, solution, obj: None
) -> tuple[object,int|float]:
    
    best_solution = start_solution
    best_obj = problem.evaluate(best_solution)
    solution = start_solution
    solution_obj = best_obj
    iter = 0
    cb(iter, best_solution, best_obj)
    temp = start_temp
    while iter < max_iter:
        iter += 1
        for k in range(1, k_max + 1):
            neighbor, neighbor_obj = neighborhood_function.find_any(problem, solution, solution_obj, rng)
            delta = neighbor_obj - solution_obj
            if delta <= 0:
                solution = neighbor
                solution_obj = neighbor_obj
                if best_obj > solution_obj:
                    best_solution = solution
                    best_obj = solution_obj
                    cb(iter, best_solution, best_obj)
            else:
                r = rng.random()
                if r < math.exp(- delta / temp):
                    solution = neighbor
                    solution_obj = neighbor_obj
        temp = cooling_rate * temp
        if temp < eps:
            temp = start_temp
    return best_solution, best_obj