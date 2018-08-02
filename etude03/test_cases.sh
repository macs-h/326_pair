#!/bin/bash

swift etude03/main.swift #> /dev/null

{
    echo "We (3 excl) are going"
    echo "I am going"
    echo "They (2 excl) are reading"
    echo "You (2 incl) are reading"
    echo "I went"
    echo "I will go"
    echo "gibberish"
    echo "We are coming"
} | ./etude03/main.swift > diff expected_output.txt
