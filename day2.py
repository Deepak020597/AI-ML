def multiply(*args):
    result = 1
    for num in args:
        result *= num
        return result
    
    print(multiply(1, 2, 3, 4, 5, 6))




import numpy as np

zeros_array = np.zeros((2, 3))
print("Zeros array:\n", zeros_array)

ones_array = np.ones((2, 3))
print("ones array:\n", ones_array)

range_array = np.arange(10, 20)
print("Range array:", range_array)

linspace_array = np.linspace(10, 20, 5)
print("Linspace array:", linspace_array)


data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Reshaping arrays
reshaped_array =data.reshape(2,5)
print("Reshaped Array:\n", reshaped_array)

# Flattening arrays
flattened_array = reshaped_array.flatten()


import pandas as pd

# creating a Dataframe from a dictionary
data = {
    'Name': ['deepak', 'sai', 'aditya'],
    'Age': [26, 25, 27],
    'score': [99, 75, 64] # type: ignore
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Adding a new column
df['pass'] = df['score' ] >= 80
print("DataFrame with pass column:\n", df)