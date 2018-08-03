#!/bin/bash

printf "Compiling main.swift...\n"
swiftc etude03/main.swift > .compiletime_output.txt

if [ -s .compiletime_output.txt ]
then
    printf "Compile-time warnings and/or errors:\n"
    cat .compiletime_output.txt
else
    printf "No compile-time warnings or errors.\n"
fi

cat io_testing/input.txt | swift etude03/main.swift 1> \
io_testing/actual_output.txt 2> .runtime_output.txt

if [ -s .runtime_output.txt ]
then
    printf "Run-time warnings and/or errors:\n"
    cat .runtime_output.txt

else
    printf "No run-time warnings or errors.\n"
    echo "-----------------------------------"
    echo ""
fi

printf "Running diff on ACTUAL vs EXPECTED output...\n"

diff io_testing/actual_output.txt io_testing/expected_output.txt
