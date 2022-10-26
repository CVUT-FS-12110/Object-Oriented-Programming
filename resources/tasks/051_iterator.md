# 5.1 - Distance Iterator

Your task is to implement your own iterator which will iterate over all distances between provided list of numbers. Both positive and negative numbers are allowed (distance of `1` and `-2` is `3`). You will have to implement following methods:

Some examples:

1. empty list `numbers=[]` should result in no distances.
1. list with one number (example `numbers=[40]`) should result in no distances.
1. list of two numbers (example `numbers=[-1,2]`) should result in one distance (result of example `result=[3]`)
1. list of three numbers (example `numbers=[4,2,-2]`) should result in 3 distances (result of example `result=[2,6,4]`)

Note that ordering is also important. If I have `numbers=[4,2,-2]`, then first distance is `|2-4|=2`, second distance is `|-2-4|=6` and last one is `|-2-2|=4`.  

* `__init__` - initialization of an iterator
* `__iter__` - magic method for for loop
* `__next__` - `next` magic method

For your solution use this [template](051_distance_iterator.py) and check `assert` statements for clarification.
