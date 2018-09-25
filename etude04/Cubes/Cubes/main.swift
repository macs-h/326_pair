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

func rotateClockwise(layer:Int, array: [[Int]]) -> [[Int]]{
    print("before right clockwise rotation \(array)")
    let temp = array[layer][3]
    var cube = array
    cube[layer][3] = cube[layer][2]
    cube[layer][2] = cube[layer][0]
    cube[layer][0] = cube[layer][1]
    cube[layer][1] = temp
    return cube
}

func rotateUp(array: [[Int]]) -> [[Int]]{
    print("before up rotation \(array)")
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


func FoundUniqueCube(cubeLet: [[Int]], uniqueCombinations: [[[Int]]: Int])-> Bool{
    var cube = cubeLet
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
    print("\n\ncube:\t\(cube)\ncublet:\t\(cubeLet)\n\n")
    return true
}
var uniqueCombinations = [[[Int]]: Int]()
//var cube = [[1,0,0,0],[0,0,0,0]]
var cube = [[Int](repeating: 0, count: 4), [Int](repeating: 0, count: 4)]
//for i in 0..<cube[0].count{
//    for _ in 0..<4{
//        if FoundUniqueCube(cubeLet: cube, uniqueCombinations: uniqueCombinations){
//            //Uninque combination so add to dic
//            print("------ unique cube---")
//            uniqueCombinations[cube] = 1
//        }
//    }
//    cube[0][i] = 1
//}

var listOfCubes = [[[Int]]: [[Int]]]()


for i in 0..<4{
    print("> i: \(i)\tpt1 move")
    for j in i..<4{
        print(">> j: \(j)\tpt1 change index")
        var tempCube = cube
        tempCube[0][j] = 1
        for k in 0..<4{
            print(">>> k: \(k)\tpt2 move")
            for n in k..<4{
                print(">>>> n: \(n)\tpt2 change index")
//                var temp1Cube = cube
                var temp1Cube = tempCube
                temp1Cube[1][n] = 1
//                if FoundUniqueCube(cubeLet: temp1Cube, uniqueCombinations: uniqueCombinations){
//                    //Uninque combination so add to dic
////                    print("------ unique cube---")
//                    uniqueCombinations[temp1Cube] = 1
//                }
                print("cube: \(temp1Cube)")
                if listOfCubes[temp1Cube] == nil{
                    listOfCubes[temp1Cube] = temp1Cube
                    print("---- found cube \(temp1Cube)")
                }
                print()
            }
//            cube[1][k] = 1
            tempCube[1][k] = 1
            print("====\n")
        }
        cube[1] = [Int](repeating: 0, count: 4)
    }
    cube[0][i] = 1
}
print("cubes \(listOfCubes.count)")

for (cu, _) in listOfCubes{
    if FoundUniqueCube(cubeLet: cu, uniqueCombinations: uniqueCombinations){
        //Uninque combination so add to dic
//                    print("------ unique cube---")
        uniqueCombinations[cu] = 1
    }
}

print("cube dict \(uniqueCombinations.count)")
