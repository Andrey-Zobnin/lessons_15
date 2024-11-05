#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    if (N <= 0)
    {
        return 1;
    }

    for (int i = 1; i <= N; i++) 
    {
        printf("%d", i * 2);
        if (i < N) {
            printf(" ");
        }
    }

    return 0;
}
