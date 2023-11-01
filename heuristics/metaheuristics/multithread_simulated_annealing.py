import random
import math
import threading
from collections.abc import Callable
from ..common import Problem
from ..common import Neighborhood

def multithread(
    iter: int,
    threadbestsolutions: list,
    threadsolutions: list,
    temp: float,
    k_max: float|int,
    neighborhood_function: Neighborhood,
    problem: Problem,
    rng: random.Random,
    thread: int,
    cb: Callable[[int,object,int|float],None]=lambda iter, solution, obj: None       
):
    for k in range(1, k_max + 1):

        neighbor, neighbor_obj = neighborhood_function.find_any(problem, threadsolutions[thread][0], threadsolutions[thread][1], rng)
        delta = neighbor_obj - threadsolutions[thread][1]
        if delta <= 0:
            threadsolutions[thread] = (neighbor, neighbor_obj)
            if threadbestsolutions[thread][1] > threadsolutions[thread][1]:
                best_solution = threadsolutions[thread][0]
                best_obj = threadsolutions[thread][1]
                threadbestsolutions[thread] = (best_solution, best_obj)
                cb(iter, best_solution, best_obj)
        else:
            r = rng.random()
            if r < math.exp(- delta / temp):
                threadsolutions[thread] = (neighbor, neighbor_obj)


def multithread_simulated_anneling(
    problem: Problem,
    start_solution: object,
    neighborhood_function: Neighborhood,
    start_temp: float,
    cooling_rate: float,
    k_max: float|int,
    threads: int,
    rng: random.Random,
    max_iter: float=math.inf,
    eps: float=1e-6,
    cb: Callable[[int,object,int|float],None]=lambda iter, solution, obj: None
) -> tuple[object,int|float]:
    
    threadlist = []

    obj = problem.evaluate(start_solution)
    threadbestsolutions = [(start_solution, obj)]*threads
    threadsolutions = [(start_solution, obj)]*threads

    iter = 0
    cb(iter, start_solution, obj)
    temp = start_temp
    while iter < max_iter:
        iter += 1

        for thread in range(threads):
            thr = threading.Thread(target=multithread, args=(iter, threadbestsolutions, threadsolutions, temp, k_max, neighborhood_function, problem, rng, thread, cb))
            threadlist.append(thr)
            thr.start()

        for thread in range(threads):
            threadlist[thread].join()

        temp = cooling_rate * temp
        if temp < eps:
            temp = start_temp
        
        best_solution, best_obj = min(threadbestsolutions, key=lambda x: x[1])

    return best_solution, best_obj