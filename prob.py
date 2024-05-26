def find_probabilities(N):
    if N == 0:
        return "0/1"
    
    # Initialize base cases
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    
    A[0] = 1
    if N > 0:
        A[1] = 2
    if N > 1:
        A[2] = 4
    if N > 2:
        A[3] = 8
    
    B[1] = 1
    if N > 1:
        B[2] = 2
    if N > 2:
        B[3] = 4
    
    for i in range(4, N + 1):
        A[i] = A[i-1] + A[i-2] + A[i-3] + A[i-4]
        B[i] = A[i-1] + A[i-2] + A[i-3]
    
    total_ways = A[N]
    miss_graduation_ways = B[N-1]
    
    return f"{miss_graduation_ways}/{total_ways}"

# Test cases
print(find_probabilities(5))  # Output: 14/29
print(find_probabilities(10)) # Output: 372/773
