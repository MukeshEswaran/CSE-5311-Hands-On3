# CSE-5311-Hands-On3

1. Finding the runtime mathematically.

   - The function f(n) runs two nested loops.
   - Outer loop runs from 1 to n and Inner loop runs from 1 to n, for each iteration the inner loop the variable x increment by 1.
   - The total number executions of x = x + 1 is
     ![formula](https://github.com/user-attachments/assets/1166d32b-fa8d-4c8e-b7c0-1dd87bc14d46)
     so, the algorithm has quadratic complexity.

2. Time the function for various values of n and Plot.
   ![Output2](https://github.com/user-attachments/assets/9ad9a8c4-487f-48be-b273-4b21f73d931d)

3. - From the summation analysis, we determined the runtime of the function is T(n) = n^2.
   - This means the function's runtime grows quadratically in both upper and lower bounds. 

4. Finding n0
   ![Output3](https://github.com/user-attachments/assets/e04c1fb9-8f5f-445a-8dc4-6c8c14ff9e9b)


The modified function questions

4. The algorithm will take slightly longer.
  - by the additional line y = i + j, it's like adding extra one more constant-time operation however it does not change the overall structure of the loop, still the total number of operation in n^2 but since there is one extra constant-time operation, it will slightly increase the total runtime.

5. Will it affect the result from #1
  - The time complexity of the modified algorithm is still n^2 so it does not change the the overall quadratic nature of the algorithm. so it does not affect the result from #1.

6. Implementation of merge sort

  - Output:
    ![Screenshot 2024-09-10 125147](https://github.com/user-attachments/assets/47006e2f-9e13-4af8-a4fb-b5ad1362a50d)
