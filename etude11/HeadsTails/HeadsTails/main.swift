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
    array.swapAt(from, to)
    array.swapAt(from+1, to+1)
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

//func alternate5(array: [Character]) -> (array: [Character], moves: Int){
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


func firstMovesarray(array: [Character]) -> (array: [Character], moves: Int){
    var moves = 0
    var coins = array
    let n = array.count
    coins = swapPair(from: 0, to: n, coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    coins = swapPair(from: n-1, to: 0, coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    coins = swapPair(from: Int(n / 2)-1, to: n-1, coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    print("n-4 = \(n-4)")
    coins = swapPair(from: n-4, to: Int(n / 2)-1, coins)
    moves += 1
    print("move \(moves) resulted in \(coins)")
    return(coins, moves)
}



func flipLoop(array: [Character]) -> (array: [Character], moves: Int){
    var moves = 0
    var coins = array
    let n = array.count
    var p = n-5
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
print("coins \(coins)")
var moves = 0
(coins, moves) = firstMovesarray(array: coins)
(coins, moves) = flipLoop(array: coins)
print("after first \(moves) coins is \(coins)")


