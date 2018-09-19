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
    print("from: \(from) to: \(to)")
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
    }else{
        print("error moving empty space \(from)\n\n")
    }
    return array
}

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

func alternate5(array: [Character]) -> (array: [Character], moves: Int){
    var moves = 0
    var coins = array
    print("pre coins \(coins)")
    coins = Tools.swapPair(from: 1, to: 5, coins)
    moves+=1
    coins = Tools.swapPair(from: 4, to: 1, coins)
    moves+=1
    coins = Tools.swapPair(from: 0, to: 4, coins)
    moves+=1
    print("post coins \(coins)")

    return(coins, moves)
}

//func alternate6(array: [Character]) -> (array: [Character], moves: Int){
//    var moves = 0
//    var coins = array
//    print("pre coins \(coins)")
//    coins = Tools.swapPair(from: 1, to: 5, coins)
//    moves+=1
//    coins = Tools.swapPair(from: 4, to: 1, coins)
//    moves+=1
//    coins = Tools.swapPair(from: 0, to: 4, coins)
//    moves+=1
//    print("post coins \(coins)")
//
//    return(coins, moves)
//}


func firstMovesarray(array: [Character], move: Int) -> (array: [Character], moves: Int){
    
    var moves = move
    var coins = array
    let n = array.count
    print("n= \(n)")
    coins = swapPair(from: 0, to: n, coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    coins = swapPair(from: n-1, to: 0, coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    coins = swapPair(from: n - Int((n+2) / 2), to: n-1, coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    coins = swapPair(from: n - (n/2)+1, to:  n - Int((n+2) / 2), coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    return(coins, moves)
}



func flipLoop(array: [Character], m: Int) -> (array: [Character], moves: Int){
    var moves = m
    var coins = array
    let n = array.count
    print("n= \(n)")
    var p = n - 5//(n/2)
    var s = 0
    print("pre loop coins \(coins)")
    while(!evaluateCoins(array: coins)){
        coins = swapPair(from: s, to: p-1, coins)
        moves += 1
        p = p-2
        print("move \(moves) resulted in \(coins)")
        coins = swapPair(from: p-1, to: s, coins)
        moves += 1
        s = s+1
        print("move \(moves) resulted in \(coins)")
        if(s >= p){
            print("pointers collided at \(s)")
            break
        }
    }
    print("after loop coins \(coins)")
    return(coins, moves)
}


func endFlips(array: [Character], m: Int) -> (array: [Character], moves: Int){
    var moves = m
    var coins = array
    if(coins[0] != coins[1]){
        //alternate
        if(coins[1] != coins[4]){
            coins = swapPair(from: 0, to: 2, coins)
            moves+=1
        }
    }
    
    return(coins, moves)
}

func alternateCoins(fullCoins: inout [Character], low:Int, high:Int){
    var coins = Array(fullCoins[low...high])
    print("coins \(coins)")
    var moves = 0
    if(coins.count == 5){
        (coins, moves) = alternate5(array: coins)
    }else{
        (coins, moves) = firstMovesarray(array: coins, move: 0)
        (coins, moves) = flipLoop(array: coins, m: moves)
        (coins, moves) = endFlips(array: coins, m: moves)
    }
    fullCoins[low...high] = ArraySlice(coins)
    //print("after first \(moves) coins is \(coins)")
}

func breakUpCoins(mCoins: [Character], n:Int) -> [Character]{
    if(n<5){
        return mCoins
    }
    var coins = mCoins
    //coins = breakUpCoins(mCoins: coins, n: n/2)
    coins = swapPair(from: 0, to: coins.count, coins)
    print("after end swap \(coins)")
    alternateCoins(fullCoins: &coins, low: n+3, high: coins.count-1)
    print("after first alternate swap \(coins)")
    alternateCoins(fullCoins: &coins, low: 2, high: n+2)
    return coins
}

print("How many heads?")
let inp = readLine()
var n = Int(inp!)!
var coins: [Character] = []
for i in 0..<(n*2){
    if(i < n){
        coins.append("H")
    }else{
        coins.append("T")
    }
    
}
//print(coins[n...n*2-1])
//if( n >= 5 ){
//    n = n/2
breakUpCoins(mCoins: coins, n: n)
//print("coins after alternate\(coins)")
//
//}



