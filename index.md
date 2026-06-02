---
site: sandpaper::sandpaper_site
---

# Introduction

Welcome to this lesson on the use of generative AI for developing research software.

Software is critical to research - the Software Sustainability Institute's UK Research Software Survey found that more than 92% of academics use research software, and 56% write their own code.
A study also conducted by the Institute also found an exponential increase in the prevalence of software-related terms in publications between 2000-2017.

![Percentage of research publications with software-related terms 2000-2017, S.J.Hettrick](fig/software-terms-publications.png)

As a specific institutional example, when researchers were asked "how important is research software to your work?" in a software study conducted at the University of Southampton, 73% of respondents indicated that it was "Vital".

For many researchers, writing code for data analysis or software development can be boring, frustrating, or intimidating. 
Most researchers would rather be thinking about and researching their subject matter rather than spending lots of time learning a programming language and writing code.
Therefore, with easy access to AI tools, it can be very tempting to ask AI to write your research code for you.

![Artwork by @allison_horst, CC-BY](fig/i_would_rather_not_behold.png){alt='Cartoon of an instructor gesturing enthusiastically to a screen full of R documentation saying "BEHOLD! An amazing function!" A skeptical looking student looks on, saying "I would rather not behold...'}

For illustrating these concepts in a tangible manner, we introduce here the story of Helen. She is a researcher who just started working with a new research group, she inherits some data and code from a colleague who just left the group. Her task is to now integrate a new qualitative dataset (interviews or personal information) to the quantitative analysis.

However, she soon realises that the code that the previous colleague did is a messy state. It is not readable, documented, tested, or commented.

Given this additional challenge, Helen knows that additional effort is required to bring this code up to good standard in order to build on top of it and do her job.

## Overview

Researchers will develop practical skills to enhance productivity, improve code quality, and apply AI responsibly in real-world research projects.

Building on foundational knowledge of large language models (LLMs) and AI coding assistants, this course focuses on the responsible and effective use of these tools for developing research software. The tools in this workshop include AI chatbots, integrated development environments (IDEs), and agentic workflows.

By the end of this lesson, learners will be able to assess which tool or if any tool is needed for their purposes, use these tools, and evaluate their outputs.

This lesson is divided into five content episodes which focus on the skills that are needed to produce high quality research software and that are upskilled by integrating generative AI tools. In addition, we include two episodes that allow you to gain and share experience from the use with these tools (episode 6 - Reflecting and contributing) and discover your next steps (episode 7 - Resources and next steps).


## Generative AI tools for research software

| Episode | Main tool | Examples |
| --- | --- | --- |
| Prompting effectively |  Chatbot | ChatGPT, Claude, duck.ai, Ollama  |
| Explain and clean scripts | Chatbot | ChatGPT, Claude, duck.ai, Ollama |
| Writing and validating scripts | IDE | Visual Studio Code, Cursor, Windsurf, Zed |
| Testing and refactoring scripts | IDE | Visual Studio Code, Cursor, Windsurf, Zed |
| Guiding agents from script to codebase | AI Agent | Copilot, Codex, Claude Code, OpenCode |


::::::::::::::::::::::::::::::::::::: callout

## Which tools are most commonly used by researchers?

In a study of 868 scientists who code as part of their research, ChatGPT was by far the most common tool used to assist with research coding, used by 64% of participants, followed by GitHub Copilot, used by 12% of participants. 

*(O'Brien, G., Parker, A., Eisty, N., & Carver, J. (2025). More code, less validation: Risk factors for over-reliance on AI coding tools among scientists. arXiv preprint arXiv:2512.19644.)*

::::::::::::::::::::::::::::::::::::::::::::::::


## Credits

These training materials were partially adapted from the materials developed by

- Southampton Research Software Group. The development of their [course](https://southampton-rsg-training.github.io/research-software-ai-tools/) was funded through the EPSRC Doctoral Landscape Award EP/Z534894/1 2025 additional skills funding underpinning the pipeline for AI skills.
- Tim Dennis - UCLA Library Data Science Center. Course: [Agentic Research Workflows: AI and Validation](https://www.tim-dennis.com/vibe-coding-lesson/)
- The course [Responsible Use of Generative AI in Assisted Coding](https://coderefinery.github.io/coding-with-ai/) from the CodeRefinery training activities. The initial draft of that lesson came from the workshop “AI and Research Work” (Glerean & Silva, 2024). The materials were originally written by Enrico Glerean, and further expanded and discussed by Bjørn Lindi, Ina Pöhner, Jarno Rantaharju, Simon Christ, Ashwin V. Mohanan, Michele Mesiti, Frankie Robertson.

The data is based on free material from GAPMINDER.ORG, CC-BY LICENSE.
