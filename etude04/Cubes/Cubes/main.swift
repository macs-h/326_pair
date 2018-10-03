//
//  main.swift
//  Cubes
//
//  Created by Sam Paterson on 24/09/18.
//  Copyright © 2018 Sam Paterson. All rights reserved.
//

import Foundation

func rotateRight(array: [[String]]) -> [[String]]{
    //print("before right rotation \(array)")
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


func rotateUp(array: [[String]]) -> [[String]]{
    //print("before up rotation \(array)")
    var cube = array
    let tempRow = [cube[0][0], cube[0][2]]
    cube[0][0] = cube[0][1]
    cube[0][2] = cube[0][3]
    cube[0][1] = cube[1][1]
    cube[0][3] = cube[1][3]
    cube[1][1] = cube[1][0]
    cube[1][3] = cube[1][2]
    cube[1][0] = tempRow[0]
    cube[1][2] = tempRow[1]
    return cube
}


func FoundUniqueCube(cubeLet: [[String]], uniqueCombinations: [[[String]]: Int])-> Bool{
    var cube = cubeLet
    for _ in 0..<4{
        cube = rotateRight(array: cube)
        for _ in 0..<4{
            cube = rotateUp(array: cube)
            for _ in 0..<4{
                cube = rotateRight(array: cube)
                if uniqueCombinations[cube] != nil{
                    //found it in the dict so has already been counted
                    return false
                }
            }
        }
    }
    return true
}
var uniqueCombinations = [[[String]]: Int]()


var listOfCubes = [[[String]]]()





//count upto 255 in binary and convert to array (128 cubes)

for num in 0...255{
    let binaryString = String(num,radix: 2).map { String($0) }
    var binaryArray = [String](repeatElement("0", count: 8))
    var i = 7
    var j = 0
    for _ in 0..<binaryString.count{
        binaryArray[i] = binaryString[j]
        i -= 1
        j += 1
    }
    
    let bArray = [Array(binaryArray[0...3]),Array(binaryArray[4...7])]
    //print(bArray)
    listOfCubes.append(bArray)
}

//print("cubes \(listOfCubes.count)")

for cu in listOfCubes{
    if FoundUniqueCube(cubeLet: cu, uniqueCombinations: uniqueCombinations){
        //Uninque combination so add to dic
//                    print("------ unique cube---")
        uniqueCombinations[cu] = 0
    }
}

//for d in uniqueCombinations{
//    print("dict: \(d)")
//}
print("Number of unique cubes \(uniqueCombinations.count)")
