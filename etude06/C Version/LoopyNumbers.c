/*Converting python to c*/
#include <stdio.h>
#include <math.h>

int sumPrimeFactors(int n){
    return 1;
}
int sumFactorsof(int n){
    int initalVal = n;
    int limit = pow(initalVal, 0.5);
    int primeFactDic[limit][1];
    printf("%d\n",primeFactDic[0]);
    return 1;
    // while (n% 2 == 0){
    //     primeFactDic[2][0]
    // }
}

int main(){
    int startVal = 2;
    int endVal = 10;
    int primes[endVal]; 
    int fullArray[endVal];
    printf("start\n");
    for (int i=startVal; i<endVal; i++){
        if(i% 10000 == 0){
            printf("--- %d\n", i);
        }
        fullArray[i] = sumFactorsof(i);
    }


    return 0;
}
