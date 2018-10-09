//
//  main.swift
//  LoopyNumbers
//
//  Created by Samuel Paterson on 10/9/18.
//  Copyright © 2018 Sam Paterson. All rights reserved.
//

import Foundation





func sieve_of_eratosthenes(n: Int) -> [Int]? {
    var numbers = [Int](2..<n)
    for i in 0..<n-2 {
        let prime = numbers[i]
        guard prime > 0 else { continue }
        for multiple in stride(from: 2 * prime-2, to: n-2, by: prime) {
            numbers[multiple] = 0
        }
    }
    return numbers.filter { $0 > 0 }
//    guard limit > 1 else {
//        return nil
//    }
//
//    var primes =  [Bool](repeating: true, count: limit+1)
//
//    for i in 0..<2 {
//        primes[i] = false
//    }
//
//    for j in 2..<primes.count where primes[j] {
//        for k in (2..<primes.count) where k*j < primes.count{
//            primes[k*j] = false
//        }
//
////        for var k = 2; k*j < primes.count; k++ {
////            primes[k*j] = false
////        }
//    }
//
//    return primes.enumerated().compactMap { (index: Int, element: Bool) -> Int? in
//        if element {
//            return index
//        }
//        return nil
//    }
}

var startNum = 2
var endNum = 1000000
var fullArray:[Int] = [Int](repeating: 0, count: endNum)
var seenFactors: [Int:Int] = [:]
print("primes started")
var primes = sieve_of_eratosthenes(n: endNum)
print("primes done")
func sumPrimeFactors(primeFactorDic: [Int:Int], initalValue: Int)-> Int{
    var returnVal = 1
    
    for (key,val) in primeFactorDic{
        var tempVal = 0
        for power in 0..<val+1{
            tempVal += Int(pow(double_t(key), double_t(power)))
        }
        returnVal += tempVal
    }
    returnVal -= initalValue
    return returnVal
}

func sumFactorsOf(num: Int) -> Int{
    var n = num
    var initalVal = n
    var primeFactDic : [Int:Int] = [2:0] //will break if doesnt have 2
    
    while n % 2 == 0{
        primeFactDic[2] = primeFactDic[2]!+1 //-----When its even you want to increase 2???
        n /= 2
    }
    
    if n == 1{
        return sumPrimeFactors(primeFactorDic: primeFactDic, initalValue: initalVal)
    }
    let limit = Int(pow(double_t(initalVal),0.5)) //----are you sure you want to round down???
    
    
    for key in primes!{
        while n % key == 0{
            if primeFactDic[key] != nil{
                primeFactDic[key]! += 1
            }else{
                primeFactDic[key] = 1
            }
            n /= key
        }
        if key > limit{ //--- this outside while loop??
            break
        }
    }
    if n == 1{
        return sumPrimeFactors(primeFactorDic: primeFactDic, initalValue: initalVal)
    }
    
    if n > 2{ //want to increment it if its a prime??
        if primeFactDic[n] != nil{
            primeFactDic[n]! += 1
        }else{
            primeFactDic[n] = 1
        }
    }
    
    return sumPrimeFactors(primeFactorDic: primeFactDic, initalValue: initalVal)
}

var startTime = NSDate()


for i in startNum..<endNum{
    if i % 100000 == 0{
        print("---\(i)")
    }
    fullArray[i] = sumFactorsOf(num: i)
}
var endTime = NSDate()
print(endTime.timeIntervalSince(startTime as Date))

