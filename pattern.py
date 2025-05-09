def print_half_pyramid(n):
    for i in range(1,n+1):
        print(" " * (n - i), end=" ")
    for j in range(i):
        print(f"{i+j} ", end= " ")
print()
print_half_pyramid(6)