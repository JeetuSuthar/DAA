# --- Recursive DP (Top-Down with Memoization) ---
def fibbo_rec(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibbo_rec(n - 1, dp) + fibbo_rec(n - 2, dp)
    return dp[n]


# --- Non-Recursive DP (Bottom-Up Tabulation) ---
def fibbo(n):
    if n <= 1:
        return n
    dp2 = [0] * (n + 1)
    dp2[0] = 0
    dp2[1] = 1
    for i in range(2, n + 1):
        dp2[i] = dp2[i - 1] + dp2[i - 2]
    return dp2[n]


# --- Main Program ---
n = int(input("Enter n: "))

# For recursive DP
dp = [-1] * (n + 1)

print("Fibonacci using Recursive DP:", fibbo_rec(n, dp))
print("Fibonacci using Non-Recursive DP:", fibbo(n))
