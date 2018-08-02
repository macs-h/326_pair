//: Playground - noun: a place where people can play

import Cocoa




let includer = "incl"
let number = 1 //1 by default incase no number
let words = "we"
var col, row : Int

//if a bracket is found
if includer == "incl"{
    //includes the listener (col 0 or 2)
    if words == "you two"{
        col = 2
        //row = 1
    }else if words == "you" && number != 2{
        col = 2
    }else{
        col = 0
    }
}else if includer == "excl"{
    //excludes the listener (col 1 or 3)
   if words == "they" || words == "them"{
        col = 3
    }else{
        col = 1
    }
}
//else{
    if words == "i" || words == "me"{
        col= 1
    else if words == "you"{
        col = 2
    }else{
        col = 3
    }
//}
row = number-1
