#ifndef __TSP_H__
#define __TSP_H__

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

struct tsp
{
    double** matrix_adj;
    size_t size;
};

typedef struct tsp tsp;

double euclidean_distance(double x1, double x2, double y1, double y2);

// constructor (paramater is a path to file)
tsp *create_tsp(char *arq);

#endif