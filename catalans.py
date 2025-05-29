MOD = 10**9 + 7

# Precompute P[0..100]
max_n = 100
P = [0] * (max_n + 1)
P[0] = 1

for k in range(1, max_n + 1):
    total = 0
    # Here we sum up all pairs of earlier Catalan counts to build the next one
    for i in range(k):
        total = (total + P[i] * P[k - 1 - i]) % MOD
    P[k] = total

# Now P[n] holds the number of valid paths for each n from 1 to 100
# Example: print all the results
for n in range(1, max_n + 1):
    print(f"P_{n} = {P[n]}")
