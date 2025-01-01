numbers = [100, 4, 200, 1, 3, 2]

numbers_set = set(numbers)
seen = set()
longest_seq = 0

for num in numbers:
    if num in seen:
        continue

    prev = num - 1
    next = num + 1

    if prev not in numbers_set:
        seq = 1
        seen.add(num)

        while next in numbers_set:
            seq += 1
            seen.add(next)
            next += 1
        
        if seq > longest_seq:
            longest_seq = seq
    
print(longest_seq)