#include <stdio.h>
#include "../include/tsp.h"

int main(int argc, char **argv)
{
    // for (size_t i = 0; i < argc; i++)
    // {
    //     printf("%s\n", argv[i]);
    // }

    char *filename;

    // scanf("%s", filename);

    tsp *tsp1 = create_tsp(filename);

    free(tsp1);
    return 0;
}