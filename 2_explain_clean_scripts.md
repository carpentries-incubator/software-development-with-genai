---
title: "Explain and clean scripts"
teaching: 30 # teaching time in minutes
exercises: 3 # exercise time in minutes
---

:::::::::::::::::::::::::::::::::: questions

- How do you use an LLM chatbot for explaining code?
- What modifications can change the readability of code without altering its functionality?

::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::: objectives

- Ask for explanations of a snippet of code to a chatbot.
- Analyse the explanations of a chatbot for understanding the snippet.
- Adapt the script to improve its clarity, modularity, and reusability.

::::::::::::::::::::::::::::::::::::::::::::

A browser-based LLM chatbot is a low-friction way to understand unfamiliar code, but the responsibility for understanding and verification stays with you. If you cannot explain the code to a colleague, you should not rely on it. To manage cognitive load when a chatbot produces long explanations, anchor your understanding by reading the code alongside the explanation and testing small parts when something is unclear.

In general, attempting to understand a new codebase, whether it's your first week on a project or one you have inherited from another source, can be difficult.
This can be due to many reasons; documentation may be incomplete, architectural decisions may be undocumented, and the people who know the system may be unavailable or have left the organisation.

We can use a chatbot to build our understanding and confidence about our codebase by asking natural-language questions about the code. It helps you:

- Build a high-level mental model of the system, which with complex codebases is often a huge task!
- Identify where key functionality is located in the code
- Understand naming conventions, patterns, and dependencies
- Reduce the cognitive load of first contact with unfamiliar code

:::callout

## Sounds great, but...

It's important to understand that no LLM is an absolute source of truth,
but more of a guide to help build your own understanding of a codebase.
:::

## Asking for explanations

Now that Helen has been able to execute the code to generate the plots, she wants to understand and clean the script.
Even though the code executes without errors, Helen struggles to understand what each section is doing.

Let's use an LLM to help us investigate how our existing script works.

1. Open `files/code/code.py`, copy the script, and paste it into your browser chatbot.
2. Ask for a high-level explanation first, then a line-by-line walkthrough. For example:
   `Explain what this script does, the expected input and output files, and any assumptions it makes. Then walk through each block of code.`
3. Follow up on anything unclear. Good follow-up prompts include:
   `Can you explain what line 5 is doing with the transpose?` and `What does line 15 do to missing values?`
4. Verify the explanation against the code. Write a short summary in your own words that describes the inputs, processing steps, and outputs.

## Analyzing the explanation

1. Identify two statements in the chatbot's explanation and point to the exact lines in the script that support them.
2. Find one place where the explanation is vague or makes an assumption (inputs, outputs, or edge cases). Ask a follow-up question to clarify.
3. Note one potential risk or gap in the explanation (for example, handling missing values or unexpected columns).
4. Write a short evaluation (2–3 sentences) of how trustworthy and complete the explanation is, based on your checks.


## Cleaning the script

1. Ask the chatbot for a refactor that improves readability and modularity without changing behavior. Example:
   `Refactor this script to improve readability and modularity. Keep the same inputs, outputs, and libraries. Do not change behavior.`
1. Apply small, safe changes only. Typical improvements include:
   - Move all imports to the top of the file.
   - Rename variables (`d`, `x`, `y0`) to meaningful names.
   - Extract repeated logic into functions (loading data, computing series, plotting).
   - Add a short module docstring describing what the script does.
1. Compare the refactored version to the original. If you can run the script, generate the plot with the same input and confirm the output is unchanged.

## Challenges

::::::::::::::::::::::::::::::::::::::::: challenge 

## Challenge 1: Verify a refactor

Ask the chatbot to refactor the script. Pick two changes it suggests and explain how you would confirm that each change did not alter the script's behavior.

:::::::::::::::::::::::::::::::::::: 
:::::::::::::::::::::::::::::::::::: solution 

Compare outputs on the same input (e.g., run both versions and compare the plot), and review the diff to ensure only structural changes were made (renames, function extraction, and docstrings) without altering calculations or file outputs.

::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge 

## Challenge 2: Mitigate risks

List three practices that reduce risk when accepting chatbot-driven refactors.

:::::::::::::::::::::::::::::::::::: 
:::::::::::::::::::::::::::::::::::: solution 

- Keep prompts specific and scope-limited.
- Review and understand every suggested change before accepting it.
- Compare outputs against the original version
- Re-run available tests if they exist, if none exist, add them.

::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::: keypoints

- Ask for explanations before you reuse or modify code, and verify them against the source.
- If you cannot explain the code to a colleague, do not trust it.
- Keep refactors small and behavior-preserving; modular, readable code is easier to verify.
- Reduce risk by keeping prompts specific and confirming outputs after changes.

::::::::::::::::::::::::::::::::::::
