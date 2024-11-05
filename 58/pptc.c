double* array = (double*) malloc(2 * sizeof(double));
if (array != NULL) {
        array[0] = 1;
        array[1] = 2;
        printf("Array: %d %d", array[0], array[1]);
 
       free(array);
}