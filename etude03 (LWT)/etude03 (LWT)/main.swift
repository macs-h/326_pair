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
var unknownVerb : String? = ""
let pronounArray : [String] = ["i", "me", "you", "he", "she", "him", "her", "we", "us",
                                "they", "them"]
let verbArray : [String] = ["go", "going", "gone",
                            "make", "making", "made",
                            "see", "seeing", "seen",
                            "want", "wanting", "wanted",
                            "call", "calling", "called",
                            "ask", "asking", "asked",
                            "read", "reading",
                            "learn", "learning", "learned"]

// API for checking tense.

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
