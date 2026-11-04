---
title: "Guiding agents from script to codebase"
teaching: 50 # teaching time in minutes
exercises: 2 # exercise time in minutes
---

::::::::::::::::::::::::::::::::: questions

- How do agentic tools help move from a script to a shareable codebase?
- How do you supervise agent work with specs, plans, and Pull Request reviews?
- How do you reduce risk with sandboxing and permission controls?

:::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::: objectives

- Explain how agentic AI coding tools work.
- Relate identified risks of agentic methods to practical safeguards that mitigate them.
- Make use of version control by implementing Git and GitHub.
- Implement supervision strategies for AI agents in coding tasks.
- Use sandboxing and permission controls for safeguarding agent actions.
- Create a Living Spec (AGENTS.md) to guide an agent.
- Extend the functionality of the script to convert it into a structured research codebase.

:::::::::::::::::::::::::::::::::::::::::::

## Introduction

Helen has turned a growing script into multiple files with a test suite, but it still lives on her
laptop. Her team wants a shareable codebase with documentation, licensing, and collaboration
workflows. She now works on a remote Linux server with only a terminal, so she uses a CLI agent and
Git to scale the work safely.

This episode focuses on agentic workflows: define a spec, approve a plan, execute in small branches,
and review changes before they land on `main`.

:::::::::::::::::::::::::::::::: callout

## A safe default for agentic work

Start with the smallest possible permissions, a clear spec, and a plan you approve. Make changes in
branches, not directly on `main`.

:::::::::::::::::::::::::::::::::::::::::::

## The agentic workflow

An agent is most useful when you give it a clear target and enforce a review gate:

1. **Spec:** Capture the goals, constraints, and data sensitivity in a Living Spec.
2. **Plan:** Ask the agent for a plan and edit it before work begins.
3. **Branches:** Each task is done in a small branch.
4. **Review:** Open a pull request (PR), review changes, and merge only when checks pass.

## Create a Living Spec (AGENTS.md)

A Living Spec is a short file that tells the agent what it can and cannot do. It should include
purpose, scope, data constraints, and what counts as "done."

Example outline:

```
# Living Spec
- Purpose: Describe the research question and expected outputs.
- Scope: List the modules/files the agent may change.
- Data sensitivity: Explain any sensitive datasets and access rules.
- Quality checks: Tests to run or outputs to verify.
- Collaboration rules: Branch + PR workflow, no direct commits to main.
```

:::::::::::::::::::::::::::::::: challenge

## Challenge 1: Draft a Living Spec

Create a short Living Spec for this project. Include at least: purpose, scope, data handling rules,
and a review rule (e.g., "all changes must go through PRs").

:::::::::::::::::::: solution

## Solution

A good spec is brief and explicit: it names the project goals, lists the files the agent may change,
explains how to handle sensitive data, and sets a review gate (branch + PR).

::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::

## Plan before executing

Before you let the agent make changes, ask it to draft a plan and break the work into small tasks.
You should edit the plan to make sure each task is reviewable on its own.

:::::::::::::::::::::::::::::::: challenge

## Challenge 2: Plan and task breakdown

Ask the agent for a plan to add a README, CONTRIBUTING guide, LICENSE, and requirements file. Edit
the plan so each item is a separate task that could be reviewed in a single PR.

:::::::::::::::::::: solution

## Solution

A clean plan typically splits into 3-5 tasks: README, LICENSE, CONTRIBUTING, environment or
requirements, and a short tutorial or example. Each task maps to a branch and PR.

::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::

## Branching and PR-based supervision

Git is your supervision tool. You can keep the agent productive while still controlling quality by
requiring small branches and reviewable PRs.

Suggested branching pattern:

- `docs/readme`
- `docs/contributing`
- `chore/license`
- `build/requirements`
- `docs/tutorial`

:::::::::::::::::::::::::::::::: challenge

## Challenge 3: Build a PR checklist

Write a short PR checklist you will use to review agent changes. Include at least: scope alignment,
tests or checks, and documentation quality.

:::::::::::::::::::: solution

## Solution

A minimal checklist includes: the PR matches the spec, tests (if any) pass, and the new docs are
clear and consistent with the rest of the repo.

::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::

## Safeguards: permissions, sandboxing, secrets hygiene

Agentic tools are powerful because they can read and change files. Keep risk low by using the
smallest possible scope:

- **Permissions:** start read-only and expand only if needed.
- **Sandboxing:** keep sensitive data inside the workspace.
- **Secrets hygiene:** never provide tokens or credentials to the agent.
- **Audit trail:** use branches + PRs so every change is visible.

:::::::::::::::::::::::::::::::: challenge

## Challenge 4: Add a safeguard

Identify one risky agent action in your workflow and add a safeguard that prevents it.

:::::::::::::::::::: solution

## Solution

For example, if the agent might edit files outside the project, restrict the scope to specific
folders and require PR reviews before merging.

::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::: keypoints

- Agentic workflows are safest with a spec, a plan, and PR-based review gates.
- Living Specs clarify goals, limits, and data constraints for the agent.
- Permission scoping, sandboxing, and secrets hygiene reduce risk without blocking progress.

:::::::::::::::::::::::::::::::::::::::::::
