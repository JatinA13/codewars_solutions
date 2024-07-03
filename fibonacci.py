def all_fibonacci_numbers(n=30):
    sequence = [1,1]
    skip = True
    for i in range (0,n-1):
        if skip:
           # sequence.append(sequence[i]+sequence[i])
            skip=False
            continue
            
        sequence.append(sequence[i]+sequence[i-1])
    print(sequence)
    return sequence
