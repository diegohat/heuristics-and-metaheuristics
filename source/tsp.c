#include "../include/tsp.h"

double euclidean_distance(double x1, double x2, double y1, double y2)
{
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

tsp *create_tsp(char *arq)
{
    FILE *fptr;
    fptr = fopen("files/Tnm82.tsp", "r");
    if (fptr == NULL)
    {
        printf("\nNot able to open the file. Exiting...\n");
        exit(EXIT_FAILURE);
    }

    tsp *new_tsp = (tsp *)malloc(sizeof(tsp));
    if (new_tsp == NULL)
    {
        printf("\nMemory allocation for tsp struct failed. Exiting...\n");
        free(new_tsp);
        exit(EXIT_FAILURE);
    }

    char line[1024];

    while (fgets(line, sizeof(line), fptr) != NULL)
    {
        if (sscanf(line, "DIMENSION : %d", &new_tsp->size) == 1)
        {
            break;
        }
    }

    printf("DIMENSION = %d\n", new_tsp->size);

    int city, x, y;
    double x_pos_array[new_tsp->size];
    double y_pos_array[new_tsp->size];

    while (fgets(line, sizeof(line), fptr) != NULL)
    {
        if (sscanf(line, "%d %d %d", &city, &x, &y) == 3)
        {
            x_pos_array[city - 1] = x / 100;
            y_pos_array[city - 1] = y / 100;
        }
    }

    for (size_t i = 0; i < new_tsp->size; i++)
    {
        printf("Cidade = %d\n", i + 1);
        printf("x = %f\n", x_pos_array[i]);
        printf("y = %f\n\n", y_pos_array[i]);
    }

    new_tsp->matrix_adj = (double **)malloc(new_tsp->size * sizeof(double *));

    if (new_tsp->matrix_adj == NULL)
    {
        printf("\nMemory allocation for tsp struct matrix failed. Exiting...\n");
        free(new_tsp);
        exit(EXIT_FAILURE);
    }

    for (size_t i = 0; i < new_tsp->size; i++)
    {
        new_tsp->matrix_adj[i] = (double *)malloc(new_tsp->size * sizeof(double));
        if (new_tsp->matrix_adj == NULL)
        {
            printf("\nMemory allocation for tsp struct matrix element failed. Exiting...\n");
            free(new_tsp);
            exit(EXIT_FAILURE);
        }
        for (size_t j = 0; j < new_tsp->size; j++)
        {
            new_tsp->matrix_adj[i][j] = euclidean_distance(x_pos_array[i], x_pos_array[j], y_pos_array[i], y_pos_array[j]);
            printf("%.2f\t", new_tsp->matrix_adj[i][j]);
        }
        printf("\n");
    }
    fclose(fptr);
    return new_tsp;
}
