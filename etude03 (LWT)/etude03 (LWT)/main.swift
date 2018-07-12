//
//  main.swift
//  etude03 (LWT)
//
//  Created by Max Huang and Sam Paterson on 11/07/18.
//  Copyright © 2018 Max Huang. All rights reserved.
//

import Foundation

var noVerb : Bool = false
var noPronoun : Bool = false
var unknownVerb : String?
let EnglishPronounArray : [String] = ["i", "me", "you", "he", "she", "him", "her", "we",
                                      "us", "they", "them"]
let EnglishVerbArray : [String] = [ "go", "going", "gone",
                                    "make", "making", "made",
                                    "see", "seeing", "seen",
                                    "want", "wanting", "wanted",
                                    "call", "calling", "called",
                                    "ask", "asking", "asked",
                                    "read", "reading", "read",
                                    "learn", "learning", "learned"]
let MaoriVerbArray : [String] =   [ "haere",
                                    "hanga",
                                    "kite",
                                    "hiahia",
                                    "karanga",
                                    "pātai",
                                    "pānui",
                                    "ako"]

var inputString : String = ""

// API for checking tense.
// Reads in lines of input till no further input.
while let stdin = readLine() {
    inputString = stdin.lowercased()
    
    let tagger = NSLinguisticTagger(tagSchemes: [.lexicalClass], options: 0)
    tagger.string = inputString
    let range = NSRange(location: 0, length: inputString.utf16.count)
    let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace]
    tagger.enumerateTags(in: range, unit: .word, scheme: .lexicalClass, options: options) { tag, tokenRange, _ in
        if let tag = tag {
            let word = (inputString as NSString).substring(with: tokenRange)
            print("\(word): \(tag.rawValue)")
            
            if tag.rawValue.lowercased() == "verb" {
                // Gives the corresponding Maori verb
                if EnglishVerbArray.contains(word) {
    //                print(EnglishVerbArray.index(of: word)! / 3)
                    print(MaoriVerbArray[EnglishVerbArray.index(of: word)! / 3])
                } else {
                    noVerb = true
                }
            } else if tag.rawValue.lowercased() == "pronoun" {
                if EnglishPronounArray.contains(word) {
                    print(EnglishPronounArray.index(of: word)!)
                } else {
                    noPronoun = true
                }
            }
            
            
        }
    }
    
    
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
