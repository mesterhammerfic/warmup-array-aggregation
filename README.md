

```python
from tests import MultiplyTest, ArrayTest
```

# For today's warmup, please solve the following code problems:

## Exercise #1

The function below doesn't work. Figure out why and fix the code.


```python
def multiply(a, b):
    a * b
```

*Run the cell below to see if your code is successful!*


```python
evaluate = MultiplyTest()
evaluate.run(multiply)
```

Once you have passed the above tests, run the cell below to test your code on 100 randomly generated tests


```python
evaluate.run(multiply, random=True)
```

**Extra Credit:** Instead of summing individual numbers, see if you can edit your ```multiply``` function so that it is [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) two arrays.

This version of your function should receive two inputs:
1. An array containing three numbers
2. An array containing three numbers

The output of the array should contain three numbers

```
[1,2,3] * [4,5,6] ---> [4,10,18]```


```python
def multiply(arr1, arr2):
    pass
```


```python
evaluate.run(multiply, random=True, broadcast=True)
```

# Exercise #2

Please fill in the code for the ```array_plus_array``` function below.

The function should have two inputs:
1. An array containing at least three numbers
2. An array containing at least three numbers

The function should return a single digit that sums all digits within both arrays


```python
def array_plus_array(arr1, arr2):
    pass
```

*Run the following cell to test your function!*


```python
evaluate = ArrayTest()
evaluate.run(array_plus_array)
```

Once you have managed to pass all of the tests, run the cell above to see if you function can pass 100 randomly generated tests!


```python
evaluate.run(array_plus_array, random=True)
```

**Extra Credit:** Instead of summing all numbers in your array, see if you can edit the ```array_plus_array``` function so that it is broadcasting two arrays.

```
[1,2,3] + [4,5,6] ----> [5,7,9]```


```python
def array_plus_array(arr1, arr2):
    pass
```

Test your code by running the cell below


```python
evaluate = ArrayTest()
evaluate.run(array_plus_array, random=True, broadcast=True)
```


```python

```
