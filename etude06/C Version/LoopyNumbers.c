/*Converting python to c*/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define LEN(arr) ((int) (sizeof (arr) / sizeof (arr)[0]))
int primes[9000000];


void sieve(int n, int primes[])
{
    int i, j;
    for (i=0;i<n;i++)
        primes[i]=1; // we initialize the sieve list to all 1's (True)
    primes[0]=0,primes[1]=0; // Set the first two numbers (0 and 1) to 0 (False)
    for (i=2;i<sqrt(n);i++) // loop through all the numbers up to the sqrt(n)
        for (j=i*i;j<n;j+=i) // mark off each factor of i by setting it to 0 (False)
            primes[j] = 0;

    for(i=2;i<n+1;i++){
        if(primes[i] == 1){
            primes[i] = i;
        }
    }
}


int sumPrimeFactors(int **primeFactDic,int initalVal){
    int returnVal = 1;
    for (int i = 0;i<LEN(primeFactDic);i++){
        if(primeFactDic[i][1] == 0){ /*could be optimised*/
            continue;
        }
        int tempVal = 0;
        for(int power = 0; power<primeFactDic[i][1]+1;power++){
            tempVal += pow(i, power);
        }
        returnVal += tempVal;
    }
    return returnVal-initalVal;
}
int sumFactorsof(int n){
    int initalVal = n;
    int limit = pow(initalVal, 0.5);
    int primeFactDic[limit][2];
    /*might not need this*/
    for(int row = 0; row < LEN(primeFactDic);row++){
        for(int col = 0; col < LEN(primeFactDic[0]);col++){
            primeFactDic[row][col] = 0;
        }
    }
    while (n%2 == 0){
        primeFactDic[2][1] = primeFactDic[2][1]+1; /*-----When its even you want to increase 2???*/
        n /= 2;
    }

    if(n == 1){
        return sumPrimeFactors(primeFactDic, initalVal);
    }

    for (row = 0; row<LEN(primes);row++){
        int prime = primes[row]; /*used to be named key*/
        if(prime == 0){
            /*primes array contains 0s*/
            continue;
        }
        while( n % prime == 0){
                primeFactDic[prime][1] = primeFactDic[prime][1]+1;
            n /= prime;
        }
        if (prime > limit){ /*should it not be at top of loop*/
            break;
        }
    }

    if (n == 1){
        return sumPrimeFactors(primeFactDic, initalVal);
    }

    if(n > 2){
        primeFactDic[n][1] = primeFactDic[n][1]+1;
    }
    
    return sumPrimeFactors(primeFactDic, initalVal);
    
}


int main(){
    int startVal = 2;
    int endVal = 9000000;
    sieve(endVal, primes);
    // for (int i=0; i<endVal; i++){
    //     printf("%d ", primes[i]);
    // }
    int fullArray[endVal];
    printf("start\n");
    for (int i=startVal; i<endVal; i++){
        if(i% 100000 == 0){
            printf("--- %d\n", i);
        }
        fullArray[i] = sumFactorsof(i);
    }


    return 0;
}
