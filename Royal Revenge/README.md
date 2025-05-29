**Solution to "Royal Revenge"**

We want to count the number of lattice paths from $(0,0)$ to $(n,n)$ taking only steps right $(1,0)$ or up $(0,1)$, such that the path never crosses above the diagonal $y=x$.  These numbers are known as the **Catalan numbers**.  Denote by $P_n$ the number of valid paths for a given $n$.  We have:

1. **Base case**:

   $$
   P_0 = 1
   $$

2. **Recurrence** (the standard Catalan convolution):

   $$
   P_n
   = \sum_{i=0}^{n-1} P_i \, P_{n-1-i},
   \qquad n \ge 1.
   $$

   Intuition:  If the path first returns to the diagonal at $(i+1,i+1)$, then the portion before that is any valid path of length $i$ and the remainder is a valid path of length $n-1-i$.  Summing over all possible $i$ gives the total.

3. **Modulo arithmetic**:

   We work modulo
   $M = 10^9+7,$
   a prime.  All additions and multiplications should be done modulo $M$ to keep numbers within bounds.

4. **Dynamic programming implementation**:

   * Create an array `P` of size $n+1$.
   * Initialize `P[0] = 1`.
   * For `k` from $1$ to $n$:

     * Compute `P[k] = sum(P[i] * P[k-1-i] for i in 0..k-1) % M`.
   * After filling the array, `P[k]` holds the answer for each $k$.

5. **Time complexity**:

   * Each $P_k$ requires $O(k)$ multiplications and additions.
   * Total time to compute all $P_1$ through $P_n$ is $O(n^2)$, which is fast for $n\le100$.

**Code Explanation**:

* We store all previously computed values in the array `P` to avoid recomputing the same Catalan numbers repeatedly.
* By taking each multiplication and addition modulo $10^9+7$, we guarantee that values never exceed the typical 32‑ or 64‑bit integer limits.
* The solution runs in $O(n^2)$ time and uses $O(n)$ space, easily handling $n=100$.

This completes the computation of $P_n\bmod 10^9+7$ for $n=1,2,\dots,100$.
