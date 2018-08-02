//
//  main.swift
//  etude03
//
//  Created by Max Huang and Sam Paterson on 11/07/18.
//  Copyright © 2018 Max Huang. All rights reserved.
//

import Foundation

enum WordTense: String {
    case past
    case present
    case future
    case notFound
}

/**
    Holds the past, present, and future tense words for a given lemma.
 */
class Tense {
    
    // STORED PROPERTIES
    let past: String
    let present: String
    let future: String
    let maoriVerb: String
    
    
    /**
        Designated initialiser.
 
        - parameters:
            - past:     Past tense words of the lemma.
            - present:  Pressent tense words of the lemma.
            - future:   Future tense words of the lemma.
    */
    init(_ past: String, _ present: String, _ future: String, _ maoriVerb: String) {
        self.past = past
        self.present = present
        self.future = future
        self.maoriVerb = maoriVerb
    }
    
    /**
        Determines the tense of the verb.
     
        - parameter word: The verb to be determined.
     
        - returns: an enum which indicates the tense of the verb, or not found.
    */
    func getTense(_ word: String) -> WordTense {
        if (self.past == word) {
            return WordTense.past
        } else if (self.present == word) {
            return WordTense.present
        } else if (self.future == word) {
            return WordTense.future
        } else {
            return WordTense.notFound
        }
    }
    
    /**
        Returns the corresponding Maori verb.
 
        - returns: String - a Maori verb.
    */
    func getMaoriVerb() -> String {
        return self.maoriVerb
    }
}

var noVerb: Bool
var noPronoun: Bool
var unknownVerb: String?
let englishPronounArray: [String] = ["i", "me", "you", "he", "she", "him", "her", "we",
                                      "us", "they", "them"]
let englishVerbArray: [String] = [ "go", "going", "gone",
                                    "make", "making", "made",
                                    "see", "seeing", "seen",
                                    "want", "wanting", "wanted",
                                    "call", "calling", "called",
                                    "ask", "asking", "asked",
                                    "read", "reading", "read",
                                    "learn", "learning", "learned"]

let maoriTenseArray: [String] = ["I", "Kei te", "Ka"]
let maoriVerbArray: [String] =   [ "haere",
                                    "hanga",
                                    "kite",
                                    "hiahia",
                                    "karanga",
                                    "pātai",
                                    "pānui",
                                    "ako"]

let maoriPronoun: [[String]] = [["none", "au", "koe", "ia"],
                                 ["tāua", "māua", "kōrua", "rāua"],
                                 ["tātou","mātou", "koutou", "rātou"],]
var inputString: String = ""
var numberIndex: Int = 0
var inputArray: [String] = []

var tenseDictionary: Dictionary = [ "went": "I",
                                    "going": "Kei te",
                                    "will": "Ka"]

let maoriStartArray: [String] = ["I", "Kei te", "Ka"]

let verbTenseDict: Dictionary = [ "go":     Tense("went", "going", "go", "haere"),
                                  "make":   Tense("made", "making", "make", "hanga"),
                                  "see":    Tense("saw", "see", "seen", "kite"),
                                  "want":   Tense("wanted", "wanting", "want", "hiahia"),
                                  "call":   Tense("called", "calling", "call", "karanga"),
                                  "ask":    Tense("asked", "asking", "ask", "pātai"),
                                  "read":   Tense("read", "reading", "read", "pānui"),
                                  "learn":  Tense("learned", "learning", "learn", "ako") ]

var verbNotFound: String = ""


func getMatrixPos(number: Int, includer: String, words: [String]) -> (row: Int, col: Int) {
    let words = words.joined(separator: " ")
    var col = 0, row = 0
    if number > 1{
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
    }else{
        if words == "i" || words == "me"{
            col = 1
        }else if words == "you"{
            col = 2
        }else{
            col = 3
        }
    }
    row = number-1
    return (row: row, col: col)
}

//
func lemmatize(_ word: String) -> String {
    var returnString:String = ""
    let tagger = NSLinguisticTagger(tagSchemes: [.lemma], options: 0)
    tagger.string = word
    let range = NSMakeRange(0, word.utf16.count)
    let options: NSLinguisticTagger.Options = [.omitWhitespace, .omitPunctuation]
    
    tagger.enumerateTags(in: range, unit: .word, scheme: .lemma, options: options) { (tag, tokenRange, stop) in
//        let word = (sentence as NSString).substring(with: tokenRange)
        if let lemma = tag?.rawValue {
            returnString = lemma
        } else {
            returnString = word
        }
    }
    return returnString
}
//


// Reads in lines of input till no further input.
while let stdin = readLine() {
    
    inputString = stdin.lowercased()
    noVerb = true
    noPronoun = true
    var i = 0
    var sentenceStarter: String = ""
    var outputArray: [String] = []
    
    let tagger = NSLinguisticTagger(tagSchemes: [.lexicalClass], options: 0)
    tagger.string = inputString
    let range = NSRange(location: 0, length: inputString.utf16.count)
    let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace]
    tagger.enumerateTags(in: range, unit: .word, scheme: .lexicalClass, options: options) { tag, tokenRange, _ in
        if let tag = tag {
            let word = (inputString as NSString).substring(with: tokenRange)
            inputArray.append(word)
            
//            print("\(word): \(tag.rawValue)")
            
            // verbs
            if tag.rawValue.lowercased() == "verb" {
//                print(">> lemma: \(lemmatize(word))")
                if let t = verbTenseDict[lemmatize(word)] {
                    noVerb = false
                    outputArray.insert(maoriStartArray[t.getTense(word).hashValue], at: 0)
//                    print("> word:", word)
//                    print("> Hash:", t.getTense(word).rawValue)
                    outputArray.insert(t.getMaoriVerb(), at: outputArray.endIndex)
                } else {
                    noVerb = true
                    verbNotFound = word
                }
                
            } else if let number = Int(word) {
                numberIndex = i
            }
            
            if tag.rawValue.lowercased() == "pronoun" {
                noPronoun = false
            }
            
            i += 1
        }
        
    }
    
    
    var matrix: (Int, Int)
    if numberIndex > 0{
        var number = Int(inputArray[numberIndex])!
//        print("\(number) \t is index \(numberIndex)")
        matrix = getMatrixPos(number: number, includer: inputArray[numberIndex+1], words: Array(inputArray.prefix(numberIndex)))
    }else{
        //no number
        matrix = getMatrixPos(number: 1, includer: "nil", words: Array(inputArray.prefix(1)))
    }
    maoriPronoun[matrix.0][matrix.1]
//    print("matrix pos = \(matrix)")
    outputArray.insert(maoriPronoun[matrix.0][matrix.1], at: outputArray.endIndex)
    
//    print(">", outputArray)
    
    if (noPronoun == true) {
        print("invalid sentence")
    } else if (noVerb == true) {
        print("unknown verb \"\(verbNotFound)\"")
    } else {
        print(outputArray.joined(separator: " "))
    }
    
    numberIndex = 0
    inputArray.removeAll()
    outputArray.removeAll()

}




