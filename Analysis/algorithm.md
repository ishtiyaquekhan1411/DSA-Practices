# Steps to construct an algorithm.

1. Problem Definition
- Understand the problem statement you have to understand which algorithm can be applied to solve the issue.
2. Design algorithm
- Identify which algorithm we will introduce to solve the problem.
- There are different algorithm which we can use to design the algorithm
i. Divide & conquer
ii. Greedy algorithm
iii. Dynamic programming
iv. Many more
3. Draw flowchart
4. Testing
- You will get test cases with input and output which we can use to confirm if our approach is correct or not.
5. Implementation
6. Analysis
- We need to consider both space and time complexity
- Time complexity have high priority than space complexity and should be consider over space complexity.

## Asymptotic notation
1. Big oh notation (worst case scenario)
2. Omega notation (best case scenario)
3. Theta notation (average case scenario)

## Types of analysis
1. Apostiary analysis
- depends on language of compiler
- depends types of hardware
- we always work for exact result.
2. Apriori analysis
- Independent on hardware and compiler
- Focuses on code logic
- Considers Approximate answers using notation likes, Big oh notation (Any Asymptotic notation)
- For example, if we have n^2 + n + 1 - consider high order value (n^2) for time complexity which states approximate answer.
- We follow Apriori analysis as we don't depends on Hardware but logic.

### Apriori analysis:
- It depends on orders of magnitude of statement that means how many times an statement will be executed.

### Rules:
- Time complexity is dependant on loops
- The more complex nested loop the more time complexity.
- If no loop exists, the time complexity will be constant O(1)

## Complexity classes (time complexity increases in below order)
1) constant - O(1)
2) Logarithm - O(logn)
3) Linear - O(n)
4) Quadratic - O(n^2)
5) Cubic - O(n^3)
6) Polynomial - O(n^c)
7) Exponential - O(c^n)
8) Factorial - n! < n^n
9) n^n (very high complexity)
- n! < n^n, 2^n < n^n, n! < 2^n (2^n < n! < n^n)
10) logn < n
- (logn)^2 < n => (logn)^3 < n => (logn)^4 < n
- (logn^logn > n)
11) log2n > log3n (lower the based higher the complexity)

## Asymptotic Notation
1) Bigoh -> worst case scenario
- f(n) -> Actual running time of function
- G(n) - Time represented by Notation.

- f(n) = O(g(n)) where f(n) & g(n) are functions and f(n) <= c.g(n) and c > 0 and n0 >= 1
2) Omega -> best case scenario
- f(n) = Omega(g(n)) where f(n) & g(n) are functions and f(n) >= c.g(n) and c > 0 and n0 >= 1
3) Theta -> Average case scenario
