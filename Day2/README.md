# Merging Two Sorted Arrays In-Place

## Problem Statement

You are given two integer arrays, `arr1` and `arr2`, both sorted in non-decreasing order, and two integers, `m` and `n`, representing the number of elements in `arr1` and `arr2`, respectively.

- The array `arr1` has a total size of `m + n`, where the last `n` elements are initialized to `0` to accommodate the merge.
- Your task is to merge `arr2` into `arr1` in non-decreasing order **in-place**.

---

## Example

### Input:
```plaintext
arr1 = [1, 2, 3, 0, 0, 0]
arr2 = [2, 5, 6]
```

### Output:
```[1, 2, 2, 3, 5, 6]```