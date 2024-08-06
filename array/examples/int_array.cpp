#include <stdio.h>

int main(){
    int n = 3;
    int* p = &n;
    int narray[4] = {10, 11, 12, 13};

    printf("n value: %d, n address: %p \n", n, p);

    printf("narray values: ");
    for(int i=0; i < 4; i++)
        printf("%d ", narray[i]);
    printf(", narray address: %p ", narray);
    
    printf("\n narray address +0: %p ", narray+0);
    printf("\n narray address +1: %p ", narray+1);
    printf("\n narray address +2: %p ", narray+2);
    printf("\n narray address +3: %p ", narray+3);

    printf("\n narray address &0: %p ", &narray[0]);
    printf("\n narray address &1: %p ", &narray[1]);
    printf("\n narray address &2: %p ", &narray[2]);
    printf("\n narray address &3: %p ", &narray[3]);

}
