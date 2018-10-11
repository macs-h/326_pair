/*Converting python to c*/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define LEN(arr) ((int) (sizeof (arr) / sizeof (arr)[0]))
#define MAX_LENGTH 9000000

int getNextValue(int , int *, int);
int cycle(int , int *, int *, int);

void clearPrimeFactDic(int **primeFactDic, size_t length){
    int i;
    for (i=0; i<length; i++){
        memset(primeFactDic[i], 0, 2*sizeof(int));
    }
}
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
int sumPrimeFactors(int **primeFactDic, size_t primeFactLength, int initalVal){
    int returnVal = 1;
    int key, power, val, tempVal = 0;

    for (key = 2;key<primeFactLength;key++){

        val = primeFactDic[key][1];
        /*printf("primeInsi@=%16x\n", primeFactDic); --- prints out adress*/
        if(val == 0){ /*could be optimised*/
            continue;
        }
        tempVal = 0;

        /*--this for loop breaks the program with seg fault---*/
        for(power = 0; power <= val; power++){
            tempVal += pow(key, power);
        }
        
        returnVal *= tempVal;
        
    }
    
    if (returnVal == 1) {
        return 1;
    }
    // printf("\t%d\t%d\n", returnVal, initalVal);
    // printf("%d\n",returnVal-initalVal);
    return returnVal-initalVal;
}


int sumFactorsof(int n, int **primeFactDic, size_t primesFactLength,int *primesArray, int *primesLength){
    int initalVal = n;
    int limit = pow(initalVal, 0.5);
    int i, key;
   
    if(primesArray[n] != 0){
        /*is a prime stop*/
        return 1;
    }

    while (n%2 == 0){
        primeFactDic[2][1] = primeFactDic[2][1]+1; /*-----When its even you want to increase 2???*/
        n /= 2;
    }
     
    if(n == 1){
        //printf("Calling here\n");
        return sumPrimeFactors(primeFactDic, primesFactLength, initalVal);
    }


    for(i= 0; i<*primesLength; i++){
        key = primesArray[i];

        //if(key == 0){continue;} /*value not a prime*/

        while(n % key == 0){
            primeFactDic[key][1] = primeFactDic[key][1]+1;
            n /= key;
        }
        // if(key > limit){
        //     break;
        // }

        if(n ==1){
            return sumPrimeFactors(primeFactDic, primesFactLength, initalVal);
        }
    }

    

    if(n > 2){
        primeFactDic[n][1] = primeFactDic[n][1]+1;
        // printf("added prime %d\n", n);
        primesArray[*primesLength] = n;
        *primesLength+=1;
    }

    // printf("---- %d is a prime! ----\n", initalVal);
    return sumPrimeFactors(primeFactDic, primesFactLength, initalVal);
    
}


// // Function to calculate sum of all  
// //divisors of a given number 
// int divSum(int n) 
// { 
//     // Sum of divisors 
//     int result = 0; 
   
//     // find all divisors which divides 'num' 
//     for (int i = 2; i <= sqrt(n); i++) 
//     { 
//         // if 'i' is divisor of 'n' 
//         if (n % i == 0) 
//         { 
//             // if both divisors are same 
//             // then add it once else add 
//             // both 
//             if (i == (n / i)) 
//                 result += i; 
//             else
//                 result += (i + n/i); 
//         } 
//     } 
   
//     // Add 1 and n to result as above loop 
//     // considers proper divisors greater  
//     // than 1. 
//     return (result + n + 1); 
// } 


int main(){
    int startVal = 2;
    int endVal = 100000;
    int *primesArray;
    int *primesLength = malloc(1* sizeof(int));
    int **primeFactDic;
    int primeFactLength = endVal;
    int *fullArray;
    int *seenValues;
    int i, cycleLen = 0, loopCount = 0, longestCycle = 0;
    clock_t startTime = clock();


    primesArray = malloc(MAX_LENGTH * sizeof primesArray[0]);
    primeFactDic = malloc(primeFactLength* sizeof primeFactDic[0]);
    fullArray = malloc(endVal * sizeof fullArray[0]);
    seenValues = malloc(endVal * sizeof seenValues[0]);
    if (NULL == primesArray || NULL == primeFactDic || NULL == fullArray || NULL == seenValues) {
        fprintf(stderr, "memory allocation 1 failed!\n");
        return EXIT_FAILURE;
    }
    for(i = 0; i<primeFactLength;i++){
        primeFactDic[i] = malloc(2* sizeof primeFactDic[0][0]);
        if (NULL == primeFactDic[i]) {
            fprintf(stderr, "memory allocation 2 failed!\n");
            return EXIT_FAILURE;
        }
    }
    //sieve(endVal, primesArray);
    for (i=0; i<primeFactLength; i++){
        memset(primeFactDic[i], 0, 2*sizeof(int));
    }

    primesArray[0] = 2;
    *primesLength =1;



    // printf("-------start--------\n");
    for (i=startVal; i<endVal; i++){
        if(i% 10000 == 0){
            printf("--- %d\n", i);
        }
        fullArray[i] =  sumFactorsof(i, primeFactDic, i+1, primesArray, primesLength);
        // printf("%d\n",fullArray[i]);
        clearPrimeFactDic(primeFactDic, i+1);
    }

    /*check cycles*/
    for(i =startVal; i< endVal; i++){
        if(i %10000 == 0){
            printf("cycle--- %d\n", i);
        }
        if(seenValues[i] == 1){
            continue;
        }
        cycleLen = cycle(i, fullArray, seenValues, endVal);
        // printf("%d\n", cycleLen);
        if (cycleLen > 0){
            // printf("is loop of len %d", cycleLen);
            loopCount+=1;

            if(cycleLen > longestCycle){
                longestCycle = cycleLen;
            }
        }

    }
    printf("-----\nRange:\t%d to %d\n",startVal, endVal);
    printf("Time:\t%f\n",(clock() - startTime)/ (double)CLOCKS_PER_SEC);
    printf("Cycles:\t%d\nMax:\t%d\n-----\n",loopCount, longestCycle);
    printf("\n");
    printf("prime length = %d\n", *primesLength);

    free(primesArray);
    free(primeFactDic);
    free(fullArray);

    return EXIT_SUCCESS;
}



int cycle(int n, int *fullArray, int *seenValues,int endNum){
    int length = 1, nextValue, loopStart;
    
    int *loopSeen;
    loopSeen = malloc(endNum* sizeof(loopSeen[0]));
    memset(loopSeen, 0, endNum*sizeof(int));


    nextValue = getNextValue(n ,fullArray, endNum);
    while(1){
        if(nextValue > endNum || nextValue == 1 || nextValue == 0){
            return 0;
        }

        

        if(loopSeen[nextValue] == 1){
            /*found loop*/
            loopStart = nextValue;
            break;
        }

        if(seenValues[nextValue] == 1){ /*value has been seen before*/
            return 0;
        }
        
        seenValues[nextValue] = 1; /*Means its been seen before*/
        loopSeen[nextValue] = 1;
        nextValue = getNextValue(nextValue ,fullArray, endNum);
        // printf("next val - %d\n", nextValue);
    }

    printf("loop found at %d for %d\n", loopStart,n);
    /*there is a loop if it got to here*/
    
    nextValue = getNextValue(loopStart ,fullArray, endNum);
    while(nextValue != loopStart){
        length++;
        nextValue = getNextValue(nextValue ,fullArray, endNum);
    }
    // hare = getNextValue(tort, fullArray, endNum);
    // while(tort != hare){
    //     hare = getNextValue(hare, fullArray, endNum);
    //     length +=1;
    //     seenValues[hare] = 1;
    // }
    printf("length= %d\n",length);
    free(loopSeen);
    return length;
}



// int cycle(int n, int *fullArray, int *seenValues,int endNum){
//     int tort, hare, length = 0;
//     tort = getNextValue(n, fullArray, endNum);
//     hare = getNextValue(tort, fullArray, endNum);
//     if(hare == 0){ /*Covers tort too because if tort == 0 hare ==0*/
//         //return 0??????
//     }
//     printf("just before while for num %d\n", n);

//     while(tort != hare){
//         tort = getNextValue(tort, fullArray, endNum);
//         hare = getNextValue(hare, fullArray, endNum);
//         hare = getNextValue(hare, fullArray, endNum); /*hare jumps twice*/

//         // if(hare > endNum){
//         //     return 0;
//         // }

//         if(hare == 0 || hare == 1 || tort == 0 || tort == 1){ /*Covers tort too because if tort == 0 hare ==0*/
//             return 0;
//         }
//         printf("tort = %d hare = %d\n", tort, hare);

//         if(hare > endNum || seenValues[tort] == 1){ /*1 means has been seen*/
//             return 0;
//         }
//         seenValues[tort] = 1;
//     }

//     /*there is a loop if it got to here*/
//     printf("is loop at %d\n", n);
//     hare = getNextValue(tort, fullArray, endNum);
//     while(tort != hare){
//         hare = getNextValue(hare, fullArray, endNum);
//         length +=1;
//         seenValues[hare] = 1;
//     }

//     return length;
// }

int getNextValue(int n, int *fullArray,int endNum){
    if(n > endNum || n == 0){
        return 0;
    }else{
        return fullArray[n];
    }
}


/*
18 loops under 100000,
max 5
---------
9000000
106 loops
28 max
*/
