#!/bin/bash

printf "Compiling main.swift...\n\n"
swiftc etude03/main.swift > /dev/null 2>&1

cat io_testing/input.txt | swift etude03/main.swift 1> io_testing/actual_output.txt 2> stderr_output.txt

printf "Running diff on ACTUAL vs EXPECTED output...\n"

diff io_testing/actual_output.txt io_testing/expected_output.txt

