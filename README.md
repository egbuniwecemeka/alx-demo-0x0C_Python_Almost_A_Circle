# PYTHON ALMOST A CIRCLE

This repository is a personal written note of what I learnt in the ALX Python Project. Feel free to correct me where I am wrong

__*args and **kwargs__ are two variable parameters in the function definition that can be used when a definite length of function parameter to be supplied as input is unknown.

P.S: __*args and **kwargs__ are not constants but a commonly used naming convention. It could as well be __*f_arg and **f_length__ this will work just fine

## TESTS

Contain tests for learnt functions/codes.

from "path" import "function" - Very important syntax in test.txt file as it enables tests to pathfile. Also i explained the various expected test errors in short concise points. I understood this and tests started to make more sense for the first time! :)

python "test_file.txt" -used to run test on the terminal

* Importing test function from another directory/parent directory

This is possible through:

    - relative import: from "..path" import "function"

    - package structures: To this the project must be tured to a package. This can be done by creating an empty __init__.py files in each directory.

python -m "test_file.txt" - test file as relative modules. (Although this was not supported in my VSCode. Hmm, Investigation ongoing...)

In conclusion I test but putting my .py files into my tests/ before executing or running test. Stressful Ooops :(

## *args

    - *args is used to send a **non-keyworded** variable length of argument list to the function.

### **kwargs

    - **kwargs sends **keyworded** variable length of argument to the function
    P.S iteritems() in older versions of python have been changed to items() in python3