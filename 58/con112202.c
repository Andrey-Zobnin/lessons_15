#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, k = 0, res = 0;
    scanf("%d %d", &a, &b);
   
    if (b < 0) {
        k = 1;
        b = -b;
    }
    
    for (int i = 1; i <= b; i++)
        res += a;
        
    if (k) 
        printf("%d\n", -res);
    else 
        printf("%d\n", res);
    
    system("pause");
    return 0;
}

