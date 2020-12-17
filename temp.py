import numpy as np

arr = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4]

    ]
)
# From the second element, slice elements from index 1 to index 4 (not included):
# print("1 output", arr[1, 1:4])

# From both elements, return index 2:
print("2 out put ", arr[1:3, 2])
