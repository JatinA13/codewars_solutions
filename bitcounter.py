def count_bits(n):
    binary = bin(n)[2:]
    counter = 0
    for i in str(binary):
        if i == str(1):
            counter+=1
    return counter
