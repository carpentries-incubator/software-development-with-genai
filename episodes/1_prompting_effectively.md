---
title: "Prompting effectively"
teaching: 35 # teaching time in minutes
exercises: 4 # exercise time in minutes
---

:::::::::::::::::::::::::::::::::::::: questions

- How does implementing prompting strategies affect the result for research code?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Apply the CLEAR framework for effective prompting.
- Apply introspection to refine code.
- Employ prompt design patterns

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

Helen has received the code and datasets from her colleague, and he has mentioned that his code should be able to run with the three provided datasets. She is aware that the provided code should generate a plot for each dataset.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Prompt as usual

Write and execute a prompt for running the code in all the datasets.

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution

## Output

A possible prompt is:

```text
Hey, I have this code "code.py" and three datasets "data1.csv", "data2.csv", and "data3.csv", please write the code to run the code in each dataset.
```

Notice that you can communicate the same intention in many other ways. Similarly, because the response of these models is not deterministic, you will receive different results even if you use the same prompt in the same model! In our case, using ChatGPT on May 10th, 2026, we received this answer:

```python
import subprocess

# List of datasets
datasets = ["data1.csv", "data2.csv", "data3.csv"]

# Run code.py for each dataset
for dataset in datasets:
    print(f"Running code.py with {dataset}...")
    
    subprocess.run(
        ["python", "code.py", dataset],
        check=True
    )

print("All datasets processed.")
```

_This assumes that `code.py` accepts the dataset filename as a command-line argument, for example:_

```python
# inside code.py
import sys

dataset_path = sys.argv[1]

print(f"Processing {dataset_path}")
```

_You can run the launcher script with:_

```bash
python run_all.py
```

Notice that in the original prompt, we wrote "... write the code to run the code...", while this is a way of doing it, it already primed the generative model to write a script to write the original code three times.

A small tweak in the prompt can set the model into writing a simpler approach.

Prompt:

```text
Hey, I have this code "code.py" and three datasets "data1.csv", "data2.csv", and "data3.csv", please help me execute the code in each dataset.
```

Output:

_If `code.py` accepts a dataset file as an argument, the simplest way is usually:_

```bash
python code.py data1.csv
python code.py data2.csv
python code.py data3.csv
```

_Or automate it with a small shell loop:_

```bash
for file in data1.csv data2.csv data3.csv
do
    python code.py "$file"
done
```

_If your `code.py` instead expects named arguments, it could look like:_

```bash
python code.py --input data1.csv
```

_in which case the loop becomes:_

```bash
for file in data1.csv data2.csv data3.csv
do
    python code.py --input "$file"
done
```

_You can also do it directly inside Python:_

```python
import subprocess

datasets = ["data1.csv", "data2.csv", "data3.csv"]

for dataset in datasets:
    subprocess.run(["python", "code.py", dataset])
```

_If you paste the contents of `code.py`, I can give you the exact command for your specific script._

:::::::::::::::::::::::::::::::::

Notice that the response of the LLM usually finishes by asking for more context, as you continue the conversation it can better tailor its responses, as we will see now with the CLEAR framework.

:::::::::::::::::::::::::::::::::::::: discussion

In groups of three, talk about how you usually prompt.

- What works for you? What errors or mistakes have you caught?
- What differences did you find in your prompts before and after applying the CLEAR framework?
- Did the model's response improve?

:::::::::::::::::::::::::::::::::::::::::::::::::

## The CLEAR framework

The CLEAR framework, developed by [Leo Lo](https://doi.org/10.1016/j.acalib.2023.102720), provides a structured approach to prompt engineering:

```mermaid
graph LR
    C[Concise] --> L[Logical]
    L --> E[Explicit]
    E --> A[Adaptive]
    A --> R[Reflective]
    R -->|Feedback Loop| A
    style R fill:#bbf,stroke:#333,stroke-width:2px
```

Effective prompts are concise and logical, prioritizing important information and following a sequence of steps. They are also explicit, specifying the scope, persona, and tone of the output. When the AI produces poor results, be adaptive by rephrasing or splitting tasks. Finally, be reflective—evaluate the output and verify facts using other sources rather than trusting the response.

The quality of AI-generated code depends heavily on how you ask for it.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: Rewrite the prompt

Rewrite the prompt using the CLEAR framework, execute the refined prompt, and compare the model's response with its previous version.

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution
A possible new prompt is as follows. We added the CLEAR framework stamps for emphasizing its use, but these are not necessary in the final prompt.
Prompt:

```text
[C] Concise:
I have a Python script, `code.py`, and three datasets:
`co2_per_capita.csv`, `life_expectancy.csv`, and `gdp_per_capita.csv`.

[L] Logical:
I want to execute the code for each dataset.

[E] Explicit:
My colleague said that `code.py` accepts the dataset path as an argument.

Use a beginner-friendly explanation.

[A] Adaptive:
If there is a more scalable or maintainable approach for handling many datasets, include it as an alternative and explain when it would be preferable.

```

[R] Reflective:

(Wait for the answer and evaluate its output. Check other sources if necessary or refine your prompt and try again.)

### Reflection

- How much longer was your refined prompt compared to your first one?
- How much time does it take to write the prompt in comparison to implementing the solution if you know it?

This serves as illustration of the CLEAR framework, but you will tailor your prompts according to your experience and the complexity of your task.

:::::::::::::::::::::::::::::::::

## Introspection

The CLEAR framework guides your input, but you can also force the AI to critique its own output. This is often called self-correction.

::::::::::::::::::::::::::::::::::::::::: instructor

## The introspection concept

Emphasize this section. Most learners treat AI output as final. The idea that they can ask the AI to fix its own work is often a new concept. It is like asking a student, "Are you sure you checked your work?"—they often find their own mistakes when asked.

::::::::::::::::::::::::::::::::::::::::::::::::::

AI models are often better at verifying code than writing it. Never accept the first draft. Follow up with an introspection prompt:

- "Review the code you just wrote. Are there any edge cases or security vulnerabilities?"
- "Did you hardcode any file paths?"
- "Critique your own implementation. Is there a more efficient way?"

:::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: The introspection loop

Test the AI as a verifier principle. Ask the AI to find flaws in its code before you run it.

1. **Generate a script** — type this prompt in your chat

```text
    Write a script that reads 'gdp_per_capita.csv' and generates a timeseries of the 10 years rolling average for a country that is passed as argument in the terminal. Handle missing values.
```

2. **Force introspection:** Once the code is generated, do not run it. Follow up in the same session:

```text
    Review the script you just wrote. Are there any edge cases (like having fewer than 10 years of consecutive data) where this would fail? If so, provide an updated version.
```

3. **Compare:** Did the AI find a mistake in its first draft? Did it add a correction?

::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::: solution

AI models are often more accurate when asked to critique logic than when asked to generate it. This second pass is part of the editor mindset and reduces manual debugging.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Prompt patterns - Plan before you act

As tasks grow more complex, asking the agent to write code immediately leads to more rewrite time. The emerging best practice is to request a plan first, review it, and approve it before any files are written.

### The think-then-do pattern

Start any multi-step task with an explicit planning prompt:

```text
Before writing any code, describe your approach in numbered steps. Do not write any files yet.
```

Review the plan, push back on steps you disagree with, and ask for alternatives. Once you are satisfied, say "proceed with step 1."

### Checkpoint prompts

Break large tasks into explicit phases so you review the output at each stage before moving forward:

```text
Step 1 only: read the three CSV files and tell me what inconsistencies you find. Do not write any code yet.
```

This is especially valuable in research because it catches misunderstandings about your data before they propagate into broken code.

### The plan file

For complex projects, ask the agent to write a `PLAN.md` first:

```text
Write a PLAN.md outlining the steps to clean and merge these files. I will review and edit it before you write any code.
```

This makes the plan a reviewable, editable artifact — a more formal version of the Bootstrap Workflow. Once approved, refer back to it in follow-up prompts: "Proceed with step 2 from PLAN.md."

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Plan before you clean

Practice the think-then-do pattern before moving on to the code cleaning episode. Inside your chat session, type:

```text
I have a script without comments, consistent variable names, and information for the plots it generates. Before writing any code, outline a step-by-step plan for cleaning this file. Do not write any code yet.
```

Review the plan. Does it include an audit step? Does it address missing values? Revise the plan in the conversation until you are satisfied, then save it by asking: "Write this plan to PLAN.md."

::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::: solution

## What a good plan could include

- An audit step — inspect files before changing them
- A re naming of variables
- A documentation step
- A missing value strategy
- An output verification step

If the agent skipped any of these, ask it to revise before you proceed. The goal is to catch gaps in the plan, not in the code.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: callout
There are more patterns that can be used to guide LLMs. See [Prompt Pattern Catalog to Enhance Prompt Engineering](https://arxiv.org/pdf/2302.11382)
::::::::::::::::::::::::::::::::::::::::::::::::::

## Concrete examples: From bad to good

| Aspect | Bad prompt | Good prompt |
| :--- | :--- | :--- |
| Vague vs specific | "Clean this data." | "In `data.csv`, remove rows with missing values in the 'age' column and save as `clean_data.csv`." |
| No context vs context | "Write a plot script." | "I am building a report for a climate study. Write a Python script using seaborn to create a line plot of 'temp' over 'year' from `results.csv`." |
| Silent vs validated | "Run a t-test." | "Perform a paired t-test between 'pre' and 'post' columns. Print the t-statistic, p-value, and an interpretation of the result at alpha=0.05." |

::::::::::::::::::::::::::::::::::::::: keypoints

- Be specific and provide context.
- The better your prompt, the better the result you will obtain.
- Introspection improves code quality.
- Plan before you act: request a numbered plan and approve it before any files are written.

::::::::::::::::::::::::::::::::::::::::::::::::::
