---
title: "Testing and refactoring scripts"
teaching: 40 # teaching time in minutes
exercises: 4 # exercise time in minutes
---

:::::::::::::::::::::::::::::::::::::: questions

- How to safely extend the functionality of a working script?
- How do I make sure that my code is still working when its size grows?
- How do I restructure my code so that it is readable, modular and reusable?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Develop a suite of tests that checks the correct functioning of the generated code.
- Evaluate the quality of the tests.
- Extend the functionality of the generated code by devising a plan and using test driven development.
- Modify the structure of the generated code to improve its quality without breaking its functionality.

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

Helen has succesfully extended her script to include her survey. Nevertheless, the original script has grown. Even though it has more functionality, it will be difficult to maintain and make sure that new changes do not break old behaviour. Consequently, Helen has decided to invest some time in writing some tests and refactoring her code. 

## Testing code

Start with a minimal pytest suite for the Episode 3 script. Identify the script's core behaviors,
create a small set of fixtures (sample inputs and expected outputs), and write tests that verify
those behaviors. Run the tests from your IDE or the terminal to establish a reliable baseline before
you make any changes.

:::::::::::::::::::::::::::::::: challenge

## Challenge 1: Build the first test suite

Create at least three tests for the Episode 3 script that confirm it produces the expected outputs
for typical inputs and handles at least one error case. Keep the tests small and focused on behavior,
not implementation.

:::::::::::::::::::: solution

## Solution

One possible suite is: 1. a "happy path" test that checks a known input produces a known output,
2. a test that verifies the script rejects missing or malformed inputs, and 3. a test that asserts
the output shape or key summary statistics remain stable.

::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::

### Evaluating test quality

Good tests are specific, deterministic, and fail for the right reasons. Look for tests that are easy
to understand, cover critical branches, and guard against regressions without being so brittle that
they fail on harmless refactors.

:::::::::::::::::::::::::::::::: challenge

## Challenge 2: Evaluate test quality

Review your tests and note one improvement you could make to increase their reliability or coverage.
Then update the suite to implement that improvement.

:::::::::::::::::::: solution

## Solution

Common improvements include: 1. adding a fixture to reduce repeated setup, 2. asserting on precise
outputs rather than vague checks, or 3. adding a test for a boundary case you identified during review.

::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::

### Test-driven development (TDD)

With TDD, you define the behavior first, watch the test fail (red), implement the minimum code to
pass (green), and then refactor while keeping the tests green.

:::::::::::::::::::::::::::::::: challenge

## Challenge 3: Extend the script with TDD

Choose a small feature for the Episode 3 script, such as a new command-line option or an additional
summary statistic. Write a failing test first, implement the feature to make the test pass, and then
refactor if needed.

:::::::::::::::::::: solution

## Solution

A solid TDD loop includes: 1. writing a test that captures the new behavior, 2. implementing the
smallest change that makes the test pass, and 3. cleaning up the code while re-running the test suite
to confirm nothing regresses.

::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::

## Refactoring code

:::{discussion}
### Why modular development matters even more with AI

When you generate code in small, testable pieces:

- You can verify each piece works before moving on
- Errors are easier to localize and fix
- You maintain understanding of what each part does
- The AI has clearer context for each request
:::

### Refactor without breaking behavior

Refactoring is safest when you make one small change at a time and keep the tests passing. Break the
script into small functions, then into modules if needed, and run the test suite after every change.

:::::::::::::::::::::::::::::::: challenge

## Challenge 4: Refactor with confidence

Split one large function or block of the Episode 3 script into two or more functions. After each
small change, run the tests and fix any failures before moving on.

:::::::::::::::::::: solution

## Solution

A common approach is to extract pure functions first, then move I/O into a thin wrapper. If the tests
stay green at each step, the refactor preserved behavior.

::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::

