//
//  main.swift
//  HeadsTails
//
//  Created by Sam Paterson on 11/09/18.
//

import Foundation


/**
 Swaps the the items in pos i, i+1 and j, j+1
 - Returns:    resulting array
 */
func swapPair(from:Int, to:Int, _ ar: [Character])-> [Character]{
    var array = ar
    if to >= array.count{
        array.append(" ")
        array.append(" ")
        
    }else if to < 0{
        array.insert(" ", at: 0)
        array.insert(" ", at: 1)
    }
    if(array[from] == " "){
        //need to move two over
        array.swapAt(from-2, from)
        array.swapAt(from-1, to+1)
    }
    if(array[from] != " " && array[from+1] != " "){
        array.swapAt(from, to)
        array.swapAt(from+1, to+1)
    }
    return array
}

//evaluates if the coins are alternating or not yet
func evaluateCoins(array: [Character])-> Bool{
    var lastCoin: Character = " "
    for coin in array{
        if(coin == lastCoin && (lastCoin != " " || coin != " ") ){
            return false
        }
        lastCoin = coin
    }
    return true
    
}

//Set up that needs to be done at the start for iterative to work
func firstMovesarray(array: [Character], move: Int, nCoins: Int, even: Int) -> (array: [Character], moves: Int){
    
    var moves = move
    var coins = array
    let n = nCoins
    coins = swapPair(from: 0, to: n, coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    coins = swapPair(from: n-1, to: n+2, coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    coins = swapPair(from: (n/2)-even, to: n-1, coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    return(coins, moves)
}


//Interative part in the middle
func flipLoop(array: [Character], m: Int, nCoins: Int, even: Int) -> (array: [Character], moves: Int){
    var moves = m
    var coins = array
    let n = nCoins
    var p = n-3
    var s = (n/2)-even
    while(!evaluateCoins(array: coins)){
        coins = swapPair(from: p, to: s, coins)
        moves += 1
        print("move \(moves) resulted in \(coins)")
        if(evaluateCoins(array: coins)){
            break
        }
        s = s-1
        coins = swapPair(from: s, to: p, coins)
        moves += 1
        print("move \(moves) resulted in \(coins)")
        p = p-2
        
        if(s >= p){
            break
        }
    }
    return(coins, moves)
}



while true{
    print("How many heads?")
    var inpArray: Array<Substring> = []
    while true{
        let inp = readLine()
        if inp == ""{
            exit(1)
        }
        inpArray = inp!.split(separator: " ")
        if Int(inpArray[0]) != nil{
            break
        }
        print("Enter a valid number of heads")
    }
    var coins: [Character] = []
    var n = 0
    var moves = 0
    if inpArray.count == 1{
        //equal number of heads and tails
        n = Int(inpArray[0])!
        for i in 0..<(n*2){
            if(i < n){
                coins.append("H")
            }else{
                coins.append("T")
            }
        }
        
        (coins,moves) = firstMovesarray(array: coins, move: moves, nCoins: n*2, even: 1)
        (coins, moves) = flipLoop(array: coins, m: moves, nCoins: n*2, even: 1)
        coins.removeSubrange(0..<4)
        
        
    }else{
        //n heads and n-1 tails
        n = Int(inpArray[0])!
        for i in 0..<(n*2)-1{
            if(i < n){
                coins.append("H")
            }else{
                coins.append("T")
            }
        }
        n *= 2
        n -= 1
        print(coins)
        
        (coins,moves) = firstMovesarray(array: coins, move: moves, nCoins: n, even: 0)
        (coins, moves) = flipLoop(array: coins, m: moves, nCoins: n, even: 0)
        if n > 5 {
            coins = swapPair(from: coins.count-2, to: 3, coins)
            coins.removeSubrange((coins.count-2)...)
        }else{
            coins.removeSubrange(0..<2)
        }
        coins.removeSubrange(0..<2)
        
    }
    print("\nFinal coins \(coins)")
    print("Total moves = \(moves)\n")
  
}



