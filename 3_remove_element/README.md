# Remove Element from Array

## Problem Statement

You are given an integer array `nums` and an integer `val`. Your task is to remove all occurrences of `val` in `nums` **in-place**, and return the number of elements in `nums` that are not equal to `val`.

To meet the requirements:
1. Modify the array such that the first `k` elements of `nums` contain the elements that are not equal to `val`.
2. The remaining elements of `nums` can be ignored and are not important.
3. Return the value of `k`, which is the count of elements in `nums` that are not equal to `val`.

### Constraints:
- The array should be modified in-place with O(1) extra space.
- The order of the elements can be changed, but only the first `k` elements will be considered valid.

---

## Example

### Input:
```plaintext
nums = [3, 2, 2, 3]
val = 3
```

### Output:
```plaintext
k = 2
nums = [2, 2, _, _]
```