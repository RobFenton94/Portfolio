import unittest


# Defining the binary search.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


"""Binary search was a good choice because it efficiently narrows down the
search space by repeatedly halving it, making it ideal for sorted arrays.
It eliminates half of the remaining elements, leading to a significantly
faster search compared to linear search especially for larger datasets."""


# Defining the insertion sort.
def insertion_sort(arr):
    for i in range(1, len(arr)):  # Iterate through the array.
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Initial array.
arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target = 9
sorted_arr = sorted(arr)
result_binary = binary_search(sorted_arr, target)

if result_binary != -1:
    print(f"Binary Search: Element {target} is present at index "
          f"{result_binary} after sorting.")
else:  # If target not found using binary search.
    print(f"Binary Search: Element {target} is not present in the "
          f"array after sorting.")

insertion_sort(arr)  # Sorting the original array using insertion sort.
print("After insertion sort:", arr)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:  # If target found at current index.
            return i
    return -1  # Return -1 if not found.


result_linear = linear_search(arr, target)  # Linear search result.

if result_linear != -1:
    print(f"Linear Search: Element {target} is present at index "
          f"{result_linear} after sorting.")
else:  # If target not found using linear search.
    print(f"Linear Search: Element {target} is not present in the "
          f"array after sorting.")

"""Linear searching is used when searching for a specific item in a small list
or array. Checking if a particular value exists in a simple database or data
structure."""


# Defining the test class.
class TestSortingAndSearching(unittest.TestCase):

    # Testing for element present in an array of integers.
    def test_search_element_present(self):
        arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
        target = 9
        sorted_arr = sorted(arr)
        result = binary_search(sorted_arr, target)
        self.assertNotEqual(result, -1)
        self.assertEqual(sorted_arr[result], target)

    # Testing if the element is not present in the array.
    def test_search_element_not_present(self):
        arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
        target = 99
        sorted_arr = sorted(arr)
        result = binary_search(sorted_arr, target)
        self.assertEqual(result, -1)

    # Test case for use of insertion sort.
    def test_insertion_sort(self):
        arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
        expected_arr = sorted(arr)
        insertion_sort(arr)
        self.assertEqual(arr, expected_arr)


# Running the tests.
if __name__ == '__main__':
    unittest.main()
