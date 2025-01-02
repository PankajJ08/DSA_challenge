arr1 = [5, 6, 7, 0, 0, 0]
arr2 = [1, 2, 3]

m = len(arr1)
n = len(arr2)
p = m - n
i = p - 1
j = n - 1
k = m - 1

if m <= 0:
    if n > 0:
        print(arr2)
    else:
        print("Both arrays are empty!")
elif n <= 0:
    if m > 0:
        print(arr1)
    else:
        print("Both arrays are empty!")
        
while k >= 0 and i >= 0 and j >= 0:
    if arr1[i] >= arr2[j]:
        arr1[k] = arr1[i]
        i -= 1
    else:
        arr1[k] = arr2[j]
        j -= 1
    k -= 1

if j >= 0:
    arr1[0: j+ 1] = arr2[0: j + 1]

print(arr1)
