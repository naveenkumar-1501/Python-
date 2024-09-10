n = 20
current_number = 1

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end=" ")
    
    # Print numbers
    for j in range(1, i + 1):
        if current_number > n:
            break
        print(f"{current_number:2}", end="  ")  # Adjust width for alignment
        current_number += 1
    
    print()  # Move to the next line
    if current_number > n:
        break
