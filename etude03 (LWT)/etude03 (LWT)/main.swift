//
//  main.swift
//  etude03 (Look Who's Talking)
//
//  Created by Max Huang and Sam Paterson on 11/07/18.
//  Copyright © 2018 Max Huang. All rights reserved.
//

import Foundation

var noVerb : Bool
var noPronoun : Bool
var unknownVerb : String?
let englishPronounArray : [String] = ["i", "me", "you", "he", "she", "him", "her", "we",
                                      "us", "they", "them"]
let englishVerbArray : [String] = [ "go", "going", "gone",
                                    "make", "making", "made",
                                    "see", "seeing", "seen",
                                    "want", "wanting", "wanted",
                                    "call", "calling", "called",
                                    "ask", "asking", "asked",
                                    "read", "reading", "read",
                                    "learn", "learning", "learned"]

let maoriTenseArray : [String] = ["I", "Kei te", "Ka"]
let maoriVerbArray : [String] =   [ "haere",
                                    "hanga",
                                    "kite",
                                    "hiahia",
                                    "karanga",
                                    "pātai",
                                    "pānui",
                                    "ako"]

var inputString : String = ""
var numberIndex : Int = 0
var inputArray : [String] = []
// API for checking tense.
// Reads in lines of input till no further input.
while let stdin = readLine() {
    inputString = stdin.lowercased()
    noVerb = false
    noPronoun = false
    var i = 0
    
    let tagger = NSLinguisticTagger(tagSchemes: [.lexicalClass], options: 0)
    tagger.string = inputString
    let range = NSRange(location: 0, length: inputString.utf16.count)
    let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace]
    tagger.enumerateTags(in: range, unit: .word, scheme: .lexicalClass, options: options) { tag, tokenRange, _ in
        if let tag = tag {
            let word = (inputString as NSString).substring(with: tokenRange)
            inputArray.append(word)
            
            print("\(word): \(tag.rawValue)")
            
            // verbs
            if tag.rawValue.lowercased() == "verb" {
                // Gives the corresponding Maori verb
                if englishVerbArray.contains(word) {
                    print(maoriVerbArray[englishVerbArray.index(of: word)! / 3])
                } else {
                    noVerb = true
                }
            } else if let number = Int(word) {
                numberIndex = i
            }
            
            
            
        }
        i += 1
    }
    
    
    
    if numberIndex > 0{
        print("Num Index: \(numberIndex)")
        var number = Int(inputArray[numberIndex])
        print("\(number) \t\(numberIndex)")
    }
    numberIndex = 0
    
    
}


// for loop: loop through each word in the sentence.
    // CONVERT TO LOWER CASE!

    // switch: checking for verbs.
        // default case = flag and store in variable.

    // if: check if word is pronoun in predefined array.
    // else: flag.


    //if (noVerb && noPronoun) {
    //    print("Invalid sentence")
    //} else if (noVerb) {
    //    print("Unknown verb \"\(String(describing: unknownVerb))\"")
    //}

// use "readline()" to parse input from CLI
