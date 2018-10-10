/*Converting python to c*/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#define LEN(arr) ((int) (sizeof (arr) / sizeof (arr)[0]))
#define MAX_LENGTH 9000000

/*Tested and works*/
void sieve(int n, int *primes)
{
    int i, j;
    for (i=0;i<n;i++)
        primes[i]=1; /* we initialize the sieve list to all 1's (True)*/
    primes[0]=0,primes[1]=0; /* Set the first two numbers (0 and 1) to 0 (False)*/
    for (i=2;i<sqrt(n);i++) /* loop through all the numbers up to the sqrt(n)*/
        for (j=i*i;j<n;j+=i) /* mark off each factor of i by setting it to 0 (False) */
            primes[j] = 0;

    for(i=2;i<n+1;i++){
        if(primes[i] == 1){
            primes[i] = i;
        }
        /*else it is a 0*/
    }
}


//int sumPrimeFactors(size_t limit, int primeFactDic[limit][2],int initalVal){
int sumPrimeFactors(int **primeFactDic, size_t limit, int initalVal){
    int returnVal = 1;
    int i;
    int power;
    int tempVal = 0;
    int amount;
    printf("size of dic %d\n", limit);
    for (i = 0;i<limit;i++){
        amount = primeFactDic[i][1];
        printf("amount= %d \n", amount);
        if(amount == 0){ 
            continue;
        }

        printf("after \n");

        /*--this for loop breaks the program with seg fault---*/
        for(power = 0; power <= amount; power++){
            printf("power \n");
        }
    }
    return returnVal-initalVal;
}




int main(){
    int startVal = 2;
    int endVal = MAX_LENGTH;
    int *primesArray;
    int **primeFactDic;
    int primeFactLength = 10;
    int *fullArray;
    int i;

    primesArray = malloc(MAX_LENGTH * sizeof primesArray[0]);
    primeFactDic = malloc(primeFactLength* sizeof primesArray[0]);
    fullArray = malloc(MAX_LENGTH * sizeof fullArray[0]);
    if (NULL == primesArray || NULL == primeFactDic || NULL == fullArray) {
        fprintf(stderr, "memory allocation failed!\n");
        return EXIT_FAILURE;
    }
    for(i = 0; i<primeFactLength;i++){
        primeFactDic[i] = malloc(2* sizeof primesArray[0]);
        if (NULL == primeFactDic[i]) {
            fprintf(stderr, "memory allocation failed!\n");
            return EXIT_FAILURE;
        }
    }
    sieve(endVal, primesArray);
    for (i=0; i<primeFactLength; i++){
        memset(primeFactDic[i], 0, 2*sizeof(int));
    }
    
    printf("-------start--------\n");
    int result = sumPrimeFactors(primeFactDic,primeFactLength, 1);
    printf("%d\n",primeFactDic[4][1]);

    free(primesArray);
    free(primeFactDic);
    free(fullArray);

    return EXIT_SUCCESS;
}
