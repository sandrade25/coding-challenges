# coding-challenges for the sake of studying/practicing for FAANG related tests

## setup:
- clone repo to your local machine
- cd into directory
- run `pip install -r requirements.txt`
- run `python complete_answers.py` and when prompted press `y`
- run `pytest`
  - should see X tests passed. all green. All tests passed.
- run `python revert_worksheets.py` and when prompted press `y`
- ready to go

## Instructions:
- complete all the worksheets in directory `./worksheets/`
- system uses pytest for validating answers. 
  - run `pytest` to test everything. 
  - run `pytest tests/test_worksheets/test_{worksheet section}.py` to test a specific section you are working on. 
  - you can add `::Test{class name}::test_{function name}` to test a specific function worksheet you are working on.
- if you wish to revert your worksheets back to empty, run: `python revert_worksheets.py`
- if you wish to see all the answers populated into the worksheets, run: `python complete_answers.py`
- ATTENTION! 
  - You should only have to modify the code within the files in `worksheets/` if you believe you have to touch any of the other files outside that directory, please contact owner.
  - or if you feel comfortable and have the appropriate access, you can submit an issue, or put in a PullRequest for a new branch as needed.
----

## Material covered:
Worksheets are grouped into categories (a_basics, b_traversal .. z_category) and ordered by group level (a, b, c .. z)

### basics:
- dynamic programming
- recursion
- heaps
- linked lists
- tri

### traversal:
- breadth first traversal
- depth first traversal

### search:
- binary search on sorted array

### sorting:
- heap sort
- insertion sort
- merge sort
- quick sort

### algo group 1
- various challenges

### algo group 2
- various challenges

