//
//  main.swift
//  Cubes
//
//  Created by Sam Paterson on 24/09/18.
//  Copyright © 2018 Sam Paterson. All rights reserved.
//

import Foundation

func rotateRight(array: [[Int]]) -> [[Int]]{
    print("before right rotation \(array)")
    var cube = array
    let tempRow = [cube[0][2], cube[0][3]]
    cube[0][2] = cube[0][0]
    cube[0][3] = cube[0][1]
    cube[0][0] = cube[1][0]
    cube[0][1] = cube[1][1]
    cube[1][0] = cube[1][2]
    cube[1][1] = cube[1][3]
    cube[1][2] = tempRow[0]
    cube[1][3] = tempRow[1]
    return cube
}


var uniqueCombinations = [[[Int]]: Int]()
var cube = [[0,1,0,0],[0,0,0,0]]
for _ in Range(0..<4){
    cube = rotateRight(array: cube)
    if uniqueCombinations[cube] != nil{
        //found it in the dict so has already been counted
        break
    }
}

print("cube end \(cube)")
