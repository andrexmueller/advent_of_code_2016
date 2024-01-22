@echo off

setlocal enabledelayedexpansion

REM Check if the first argument is provided
if "%1"=="" (
    echo To run a test type -t, to run the input type -d.
    goto :end
)

REM Extract the file number from the first argument
set "file_number=%1"

REM Default input file prefix
set "input_file_prefix=input_"

REM Check if the second argument is provided and set input file prefix accordingly
if /i "%2"=="-t" (
    set "input_file_prefix=test_"
) else if /i "%2"=="-d" (
    set "input_file_prefix=input_"
)

REM Construct the Python command
set "python_command=python day_%file_number%.py < %input_file_prefix%%file_number%.txt"

REM Run the Python command
%python_command%

:end