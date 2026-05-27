# Essay Question: design serial vs parallel execution for a data pipeline

## Question
Assume you are building a pipeline that must collect data from multiple online repositories and then run analytics on the collected data.

Explain how you would design execution for this pipeline.

Your answer must explicitly discuss:
- which parts are I/O-bound and which parts are CPU-bound
- which parts should run serially and which parts should run in parallel
- tradeoffs, including:
  - process overhead
  - rate limits and failed requests
  - reproducibility and fairness of timing comparisons
- practical pipeline architecture, including:
  - stages (for example: fetch -> clean -> analyze)
  - where to place timing and checkpoints

Do not write code. Focus on reasoning and design decisions.

## Instructions for Students
Write 10-14 lines.

## Instructor Name
Stelios

## Hint
🤔 Hint: A good design is not only about speed. It should also be robust, measurable, and reproducible.

## Evaluation Criteria (Total: 4 points)
1. **Workload classification accuracy (1 point)**  
- Correctly distinguishes I/O-bound work (for example network/data collection) from CPU-bound work (for example analytics/computation).  
- We expect both categories to be identified explicitly.  
- We expect at least one correct example for each category.
2. **Execution strategy choice (1 point)**  
- Clearly explains which stages should be serial and which should be parallel.  
- We expect reasoning tied to task independence, ordering requirements, and resource constraints.  
- We expect a context-aware plan rather than “parallelize everything.”
3. **Tradeoff analysis quality (1 point)**  
- Discusses process overhead, rate limits/failed requests, and reproducibility/fair timing.  
- We expect at least one concrete risk and one mitigation idea (for example retries/backoff, fixed workload for timing, repeated runs).  
- We expect recognition that faster is not always better if reliability is reduced.
4. **Pipeline architecture and clarity (1 point)**  
- Presents a clear stage-based flow (for example fetch -> clean -> analyze).  
- We expect explicit mention of where timing and checkpoints are placed.  
- We expect concise, well-structured writing with correct terminology.

## Reference Answer
A practical design begins by separating workload types.

Data collection from online repositories is mainly I/O-bound because the program spends time waiting on network responses. Analytics after data is collected is mainly CPU-bound because it performs computation over local data.

For execution strategy, I would parallelize independent fetch tasks (for example multiple repository downloads at once) but keep ordering-sensitive stages serial when needed (for example final merge, validation, or checkpoint commits). In analytics, I would use controlled parallelism only when workloads are large enough to offset process overhead.

Key tradeoffs:
- Process overhead can dominate small tasks, so aggressive parallelism can be slower.
- External rate limits and request failures require retry logic, backoff, and failure tracking.
- Reproducibility and fair timing require fixed input sets, same environment, and repeated runs (not single-run conclusions).

Pipeline structure example:
1. Fetch (parallel where independent).
2. Clean/validate (serial or controlled parallel, with explicit checks).
3. Analyze (serial baseline, then controlled parallel benchmark).
4. Report (timings + quality checks).

Checkpoints should be placed after fetch and after clean so errors are isolated early and re-runs are controlled.

## AI Evaluation Rules
Evaluate only by the rubric above.
Do not use external knowledge.
Score = (points achieved / 4) x 100.
Accept equivalent phrasing and related concepts, not only exact wording from the reference answer.
Award credit when the student uses correct ideas with different terminology (for example "waiting on network", "compute-heavy stage", "ordered merge step", "retry/backoff", "repeat trials", "same input for fair benchmarking").
Do not penalize minor wording differences if the reasoning is correct and complete.
When partially correct, give partial credit in the relevant criterion and explain exactly what is missing.

## Output Format
Score: XX%

Feedback:
- What the student did well
- What is missing
- 1-2 suggestions for improvement
