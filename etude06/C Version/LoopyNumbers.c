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
        /*printf("primeInsi@=%16x\n", primeFactDic); --- prints out adress*/
        if(amount == 0){ /*could be optimised*/
            continue;
        }

        printf("after \n");

        /*--this for loop breaks the program with seg fault---*/
        for(power = 0; power <= amount; power++){
            //printf("power %d \n", power);
            tempVal += pow(i, power);
        }
        returnVal += tempVal;
    }
   // primeFactDic[4][1] = 99;
    printf("sum %d\n",returnVal-initalVal);
    return returnVal-initalVal;
}


// int sumFactorsof(int n){
//     int initalVal = n;
//     int limit = pow(initalVal, 0.5);
//     printf("limit %d\n", limit);
//     int primeFactDic[limit][2];
//     printf("primeFact@=%16x\n", &primeFactDic);
//     /*printf("primeFact@=%16x\n", &primeFactDic[0][0]);
//     printf("primeFact@=%16x\n", &primeFactDic[0][1]);
//     printf("primeFact@=%16x\n", &primeFactDic[1][0]);
//     printf("primeFact@=%16x\n", &primeFactDic[1][1]);*/

//     // int **primeFactDic;
//     // primeFactDic = malloc(limit * sizeof(primeFactDic[0]));
//     // if (!primeFactDic) {
//     //     // printf("oops\n");
//     // } else {
//     //     // printf("malloc didn't fail\n");
//     // }
//     // for (int i = 0; i < limit; i++) {
//     //     primeFactDic[i] = malloc(2 *sizeof(primeFactDic[i][0]));
//     //     memset(primeFactDic, 0, 2*sizeof(int));
//     // }

//     // for (i = 0; i < limit; i++) {
//     //     // printf("%s %d\n", "this should be a zero", primeFactDic[i][0]); 
//     // }
//     /*might not need this*/
//     for(int row = 0; row < limit;row++){
//         for(int col = 0; col < 2;col++){
//             primeFactDic[row][col] = 0;
//         }
//     }
//     while (n%2 == 0){
//         primeFactDic[2][1] = primeFactDic[2][1]+1; /*-----When its even you want to increase 2???*/
//         n /= 2;
//     }
    
//     if(n == 1){
//         printf("Calling here\n");
//         return sumPrimeFactors(limit,primeFactDic, initalVal);
//         //  int returnVal = 1;
//         // printf("entered sumprimefac funciton oooo\n");
//     //     printf("%d\n", sizeof(primeFactDic[0]));
//     //     for (int i = 0;i<LEN(primeFactDic);i++){
        
//     //         if(primeFactDic[i][1] == 0){ /*could be optimised*/
//     //             continue;
//     //         }
//     //         int tempVal = 0;
//     //         for(int power = 0; power<primeFactDic[i][1]+1;power++){
//     //             tempVal += pow(i, power);
//     //     }
//     //     returnVal += tempVal;
//     // }
//     }
    
//     for (row = 0; row<LEN(primes);row++){
//         int prime = primes[row]; /*used to be named key*/
//         //int prime = *(prime+row);
//         printf(" primes loop %d\n", prime);
//         if(prime == 0){
//             /*primes array contains 0s*/
//             continue;
//         }
//         while( n % prime == 0){
//                 primeFactDic[prime][1] = primeFactDic[prime][1]+1;
//             n /= prime;
//         }
//         if (prime > limit){ /*should it not be at top of loop*/
//             break;
//         }
//     }
//     printf("2nd sum called\n");
//     if (n == 1){
//         return sumPrimeFactors(limit,primeFactDic, initalVal);
//     }

//     if(n > 2){
//         primeFactDic[n][1] = primeFactDic[n][1]+1;
//     }
//     printf("last sum  call\n");
//     // printf("%d\n",sumPrimeFactors(primeFactDic, initalVal));
//     return sumPrimeFactors(limit,primeFactDic, initalVal);
    
// }


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


    // for (int i=startVal; i<endVal+1; i++){
    //     if(i% 1000000 == 0){
    //         printf("--- %d\n", i);
    //     }
    //     fullArray[i] = sumFactorsof(i);
    //     printf("full array %d\n",fullArray[i]);
    // }
    free(primesArray);
    free(primeFactDic);
    free(fullArray);

    return EXIT_SUCCESS;
}
