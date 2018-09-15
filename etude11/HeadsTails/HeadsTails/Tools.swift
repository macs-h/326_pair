//
//  tools.swift
//  HeadsTails
//
//  Created by Sam Paterson on 11/09/18.
//

import Foundation

class Tools{
    
    /**
        Swaps the the items in pos i, i+1 and j, j+1
        - Returns:    resulting array
    */
    static func swapPair(from:Int, to:Int, _ ar: [Character])-> [Character]{
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
}


