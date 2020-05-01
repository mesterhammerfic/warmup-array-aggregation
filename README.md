
# For today's warmup, please solve the following code problems:

## Exercise #1

The function below doesn't work. Figure out why and fix the code.


```python

def multiply(a,b):
    return a * b
```

*Run the cell below to see if your code is successful!*

Once you have passed the above tests, run the cell below to test your code on 100 randomly generated tests

**Extra Credit:** Instead of summing individual numbers, see if you can edit your ```multiply``` function so that it is [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) two arrays.

This version of your function should receive two inputs:
1. An array containing three numbers
2. An array containing three numbers

The output of the array should contain three numbers

```
[1,2,3] * [4,5,6] ---> [4,10,18]```


```python

import numpy as np

def multiply(arr1, arr2):
    arr1 = np.asarray(arr1)
    arr2 = np.asarray(arr2)
    
    return arr1 * arr2
```

# Exercise #2

Please fill in the code for the ```array_plus_array``` function below.

The function should have two inputs:
1. An array containing at least three numbers
2. An array containing at least three numbers

The function should return a single digit that sums all digits within both arrays


```python

def array_plus_array(arr1, arr2):
    
    
    return sum(arr1) + sum(arr2)
```

*Run the following cell to test your function!*

Once you have managed to pass all of the tests, run the cell above to see if you function can pass 100 randomly generated tests!

**Extra Credit:** Instead of summing all numbers in your array, see if you can edit the ```array_plus_array``` function so that it is broadcasting two arrays.

```
[1,2,3] + [4,5,6] ----> [5,7,9]```


```python

import numpy as np

def array_plus_array(arr1, arr2):
    arr1 = np.asarray(arr1)
    arr2 = np.asarray(arr2)
    
    return arr1 + arr2
```

Test your code by running the cell below
