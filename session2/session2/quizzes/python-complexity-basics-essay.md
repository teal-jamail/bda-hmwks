# Essay Question: Complexity Basics

## Question
Describe the `time` complexity of:
A) searching a number in an unsorted list
B) searching a number in a sorted list using binary search
C) sorting a list using bubble sort

Provide a brief explanation for each case (for example, justify why the complexity is O(n)).

## Instructions for Students
Answer in 5-8 lines. Use Big-O notation.

## Instructor Name
Stelios

## Hint
Think about how many elements may need to be checked as `n` grows.

## Evaluation Criteria (Total: 6 points)
1. **A: Linear search (2 points)**
- Correctly states time complexity as `O(n)`.
- We expect a brief explanation (e.g. the algorithm may need to check each element once in the worst case).
2. **B: Binary search (2 points)**
- Correctly states time complexity as `O(log n)`.
- Mentions that binary search requires the list to be **sorted**.
- We expect a brief explanation (e.g. the search space is halved at each step).
3. **C: Bubble sort (2 points)**
- Correctly states average and worst-case time complexity as `O(n^2)` - accept O(n2) as correct.
- Optional bonus detail: best case is `O(n)` when using an optimization (e.g. early-stop flag).
- We expect a brief explanation (e.g. repeated pairwise comparisons across the list).

## Reference Answer
A) `O(n)` for searching in an unsorted list.
B) `O(log n)` for binary search on sorted data.
C) Bubble sort is `O(n^2)` on average and worst case.

## AI Evaluation Rules
Grade only by criteria above. Do not use external assumptions.
Accept equivalent wording when the underlying complexity idea is correct.
If a student gives correct complexity but misses the sorted-list condition for binary search, deduct only from criterion B.

## Output Format
Return JSON with points, did_well, missing, suggestions.
