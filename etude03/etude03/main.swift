//
//  main.swift
//  etude03
//
//  Version: 2.0
//  Created by Max Huang and Sam Paterson on 11/07/18.
//  Copyright © 2018 Max Huang. All rights reserved.
//

import Foundation

/**
    Enums describing the tense of the word, or `notFound`.
 */
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
    let present: [String]
    let future: String
    let maoriVerb: String
    
    
    /**
        Designated initialiser.
 
        - parameters:
            - past:         Past tense words of the lemma.
            - present:      Pressent tense words of the lemma.
            - future:       Future tense words of the lemma.
            - maoriVerb:    The corresponding Maori verb.
    */
    init(_ past: String, _ present: [String], _ future: String, _ maoriVerb: String) {
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
        } else if (self.present.contains(word)) {
            return WordTense.present
        } else if (self.future == word) {
            return WordTense.future
        } else {
            return WordTense.present
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
var inputString: String
var numberIndex: Int = 0
var inputArray: [String] = []

var t_future: Bool = false
var t_past: Bool = false
var tense: WordTense?

let maoriPronoun: [[String]] = [ ["none", "au", "koe", "ia"],
                                 ["tāua", "māua", "kōrua", "rāua"],
                                 ["tātou","mātou", "koutou", "rātou"] ]

//var tenseDictionary: Dictionary = [ "went": "I",
//                                    "going": "Kei te",
//                                    "will": "Ka"]

let maoriStartArray: [String] = ["I", "Kei te", "Ka"]

let verbTenseDict: Dictionary = [ "go":     Tense("went", ["going"], "go", "haere"),
                                  "make":   Tense("made", ["making"], "make", "hanga"),
                                  "see":    Tense("saw", ["see", "seeing"], "seen", "kite"),
                                  "want":   Tense("wanted", ["wanting"], "want", "hiahia"),
                                  "call":   Tense("called", ["calling"], "call", "karanga"),
                                  "ask":    Tense("asked", ["asking"], "ask", "pātai"),
                                  "read":   Tense("read", ["reading"], "read", "pānui"),
                                  "learn":  Tense("learned", ["learning"], "learn", "ako") ]

/**
    Gets the Maori pronoun for the corresponding English pronoun.
 
    - parameters:
        - number:   The number of people specified if more 1
        - includer: Assigned either "incl" or "excl" depedning on if the
                    listener is included or not
        - words:    The words before the '(' to help indicate pronoun
 
    - returns:  The tuple made out of `row` and `col` position so pronoun can
                be selected
 */
func getMatrixPos(number: Int, includer: String, words: [String]) -> (row: Int, col: Int) {
    let words = words.joined(separator: " ")
    var col = 0, row = 0
    if number > 1 {
        if includer == "incl" {
            if words == "you"{
                col = 2
            } else {
                col = 0
            }
        } else if includer == "excl" {
            //excludes the listener (col 1 or 3)
            if words == "they" || words == "them" {
                col = 3
            } else {
                col = 1
            }
        }
    } else {
        if words == "i" || words == "me" {
            col = 1
        } else if words == "you" {
            col = 2
        } else {
            col = 3
        }
    }
    var tempNum = number
    if number > 3{ //accounts for more than 3 people
        tempNum = 3
    }
    row = tempNum-1
    return (row: row, col: col)
}

/**
    Determines the lemma of the word.
 
    - parameter word: word to be lemmatized.
 
    - returns: the lemma of the word.
 */
func lemmatize(_ word: String) -> String {
    var returnString:String = ""
    let tagger = NSLinguisticTagger(tagSchemes: [.lemma], options: 0)
    tagger.string = word
    let range = NSMakeRange(0, word.utf16.count)
    let options: NSLinguisticTagger.Options = [.omitWhitespace, .omitPunctuation]
    
    tagger.enumerateTags(in: range, unit: .word, scheme: .lemma, options: options) { (tag, tokenRange, stop) in
        if let lemma = tag?.rawValue {
            returnString = lemma
        } else {
            returnString = word
        }
    }
    return returnString
}


// MAIN

// Reads in lines of input till no further input.
while let stdin = readLine() {
    
    inputString = stdin.lowercased()
    noVerb = true
    noPronoun = true
    var i = 0
    var outputArray: [String] = []
    
    let tagger = NSLinguisticTagger(tagSchemes: [.lexicalClass], options: 0)
    tagger.string = inputString
    let range = NSRange(location: 0, length: inputString.utf16.count)
    let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace]
    tagger.enumerateTags(in: range, unit: .word, scheme: .lexicalClass, options: options) { tag, tokenRange, _ in
        if let tag = tag {
            let word = (inputString as NSString).substring(with: tokenRange)
            inputArray.append(word)
            
            if word == "will" {
                t_past = false
                t_future = true
            } else if word == "went" {
                t_future = false
                t_past = true
            }
            
            // If word is a verb...
            if tag.rawValue.lowercased() == "verb" {
                if let t = verbTenseDict[lemmatize(word)] {
                    noVerb = false
                    
                    if !t_future || !t_past {
                        tense = t.getTense(word)
                    }
                    outputArray.insert(t.getMaoriVerb(), at: outputArray.endIndex)
                    
                } else {
                    noVerb = true
                    unknownVerb = word
                }
                
            } else if Int(word) != nil {
                numberIndex = i
            }
            
            // If word is a pronoun...
            if tag.rawValue.lowercased() == "pronoun" {
                noPronoun = false
            }
            
            i += 1
        }
        
    }
    
    
    var matrix: (Int, Int)
    if numberIndex > 0 {
        let number = Int(inputArray[numberIndex])!
        if number < 1{
            noPronoun = true
            break
        }
        matrix = getMatrixPos(number: number, includer: inputArray[numberIndex+1], words: Array(inputArray.prefix(numberIndex)))
    } else {
        // no number
        matrix = getMatrixPos(number: 1, includer: "nil", words: Array(inputArray.prefix(1)))
    }
    
    outputArray.insert(maoriPronoun[matrix.0][matrix.1], at: outputArray.endIndex)
    
    if noPronoun == true {
        print("invalid sentence")
    } else if noVerb == true {
        print("unknown verb \"\(unknownVerb!)\"")
    } else {
        if t_future {
            outputArray.insert(maoriStartArray[WordTense.future.hashValue], at: 0)
        } else if t_past {
            outputArray.insert(maoriStartArray[WordTense.past.hashValue], at: 0)
        } else {
            outputArray.insert(maoriStartArray[tense!.hashValue], at: 0)
        }
        print(outputArray.joined(separator: " "))
    }
    
    numberIndex = 0
    t_future = false
    t_past = false
    inputArray.removeAll()
    outputArray.removeAll()

}
