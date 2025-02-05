def number_pattern_a(n):
    for i in range(1, n + 1):  
        print(" " * (n - i) + "12345"[:i])  


number_pattern_a(5)
