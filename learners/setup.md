---
title: Setup
---

## Skills Prerequisites

The following are necessary to be able to participate in this course:

- You have a basic knowledge of programming in Python (using variables, lists, conditional statements, functions and importing external libraries)
- You have previously written Python scripts or iPython/Jupyter notebooks to accomplish tasks in your domain of work

It is also helpful but not necessary to have some basic knowledge of Git version control (cloning repositories, making commits, pushing to a remote repository).

## Software Setup

To participate in this course we recommend having the following software installed on your machine:

- Bash shell (Linux, Mac) or Git Bash for Windows
- Git version control (available from the Bash shell or Git Bash for Windows)
- Python version 3.8 or above
- Microsoft Visual Studio Code version 1.98 or above

If you do not have these installed, see below for installation instructions.
Please open the tab for your operating system and follow the setup instructions.
Then, look below the tab and follow the 'Additional Git Setup' instructions too.

:::::::::::::::: spoiler

### Windows

#### Bash Shell

We’ll be using Git Bash. If you’ve already installed Git Bash then go to the next section. Otherwise, go to [git for windows](https://gitforwindows.org/) and click Download, then install it. Most of the options can be left on default, but be sure you check these:

- **Choosing the default editor used by Git**: Make sure **Nano** is selected from the drop-down. If you’re comfortable with other editors, feel free to change it, but we recommend Nano - we use it as it’s present on Windows, Mac and Linux. If you change it, you might not quite match what we’re doing on-screen.
- **Adjusting your PATH environment**: Make sure **Git from the command line and also from 3rd-party software** is selected.
- **Choosing HTTPS transport backend**: Make sure **Use the native Windows Secure Channel Library** is selected.
- **Configuring the terminal emulator to use with Git Bash**: Make sure **Use Windows’ default console window** is selected.

#### Git Setup

We’ll be using Git Bash for both git and a shell to run it in.

#### Python

The “Anaconda3” package provides everything Python-related you will need for the workshop. To install Anaconda, follow the instructions below.

Download the latest Anaconda Windows installer from [Anaconda](https://www.anaconda.com/download), you may need click 'Get Started' and register first. 

Double-click the installer and follow the instructions. **When asked “Add Anaconda to my PATH environment variable”, answer “yes”. It will warn you not to, but it’s required for it to be found by git bash**. After it’s finished, close and reopen any open terminals to reload the updated PATH and allow the installed Python to be found.

Once the Anaconda installation is finished you will be asked if you want the installer to initialize Anaconda3 by running conda init? You should select yes. Alternatively/additionally you will need to run the following command in Git Bash

```bash
conda init bash
```
Then close and reopen GitBash.

Please test the python install open GitBash (or your favorite terminal) and run the following command to verify that the installation was successful.

```bash
cd ~
python
```
You can then type the following to exit:

```bash
quit()
```

**Git Bash might hang on this command and not launch the Python interpreter.** 
**In this case close and reopen git bash and issue the following commands:**

```bash
cd ~
echo 'alias python="winpty python.exe"' >> ~/.bash_profile
source .bash_profile
python
```

Note: for older versions of git bash you will need to use .bashrc rather than .bash_profile

::::::::::::::::::::::::

:::::::::::::::: spoiler

### MacOS

#### Bash Shell

You can open a terminal by opening the “Terminal” application, which can be found in the “Utilities” folder which is in your “Applications” folder.
Z shell is the default shell on Mac, but you can run a Bash shell from the terminal by typing `bash` and pressing enter.

#### Git Setup

To use Git you must install the Apple Command Line Tools, this may take a few minutes.

You can obtain these [from Apple](https://idmsa.apple.com/IDMSWebAuth/signin.html?path=%2Fdownload%2Fall%2F%3Fname%3Dcommand%2520line%2520tools%2520for%2520xcode%252012&appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&rv=0) (requires your Apple ID)

-   Select **Command Line Tools for Xcode 12 (or higher)** and click the link to download the dmg archive.
-   If prompted, choose to allow downloads from developer.apple.com
-   Open the downloaded dmg archive from the Downloads folder
-   Double-click the Command Line Tools.pkg icon to install

Alternatively, you can install the tools from the command line:

```bash
xcode-select --install
```
#### Python

Download the latest Anaconda Mac OS X installer from [Anaconda](https://www.anaconda.com/download).
Double-click the .pkg file and follow the instructions.

::::::::::::::::::::::::


:::::::::::::::: spoiler

### Linux

#### Bash Shell

This will depend on the Linux distribution you are running, but you should be able to find a “Terminal” application in your desktop’s application menu that gives you access to Bash.

#### Git Setup

Git comes pre-installed on most Linux distributions. You can test if it’s installed by running `git --version`. If it’s not installed, you can install it by running `sudo apt-get install git` or `sudo yum install git`, depending on your distribution.

#### Python

Download the latest Anaconda Linux Installer from [Anaconda](https://www.anaconda.com/download).

Install via the terminal like this (you will need to change the version number to the latest version):

First move to the folder where you downloaded the installer, this is likely to be the Downloads folder e.g.

```bash
cd ~/Downloads
```

```bash
bash Anaconda3-2025.12-2-Linux-x86_64.sh
```

Answer ‘yes’ to allow the installer to initialize Anaconda3 in your .bashrc.
::::::::::::::::::::::::

### Additional Git Setup

#### Setting up Git

The first time we use Git on a new machine, we need to configure it. We’re going to set some global options, so when Git starts tracking changes to files it records who made them and how to contact them.

(Please use your own name and the email address you used to sign up to GitHub!)

```bash
git config --global user.name "Firstname Surname"
git config --global user.email "fsurname@university.ac.uk"

```

We’re going to set Nano, a simple, minimal command-line text editor to be the default for when you need to edit messages.  If you’re already comfortable with another command-line editor, feel free to select that!

```bash
git config --global core.editor "nano -w"`
```

The three commands above only need to be run once: the flag `--global` tells Git to use the settings for every project on this machine.

You can check your settings at any time:

```bash
 git config --list
```

#### GitHub

We’ll be using the website [GitHub](https://github.com/) to host, back up, and distribute our code. You’ll need to create an account there. As your GitHub username will appear in the URLs of your projects there, it’s best to use a short, clear version of your name if you can.

#### SSH Key Setup (Optional/Advanced)

An optional step that isn't required for the course but is a useful and established practice,
is to set up SSH access to GitHub from your computer.
This is a more secure alternative method to access GitHub than using a password.
To set up SSH access, we generate a pair of keys - one public, one private. We want to add the public key to GitHub, whilst the private one stays on our computer.

We can run a simple command to generate a new SSH key. It’ll ask you for some settings, but you should just hit enter to use the defaults for everything:

```bash
ssh-keygen -t ed25519
```

```output
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/smangham/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in id_ed25519
Your public key has been saved in id_ed25519.pub
The key fingerprint is:
SHA256:tm2lRVXqWdkwiu+fvOF8WxRaf6peAqZHKSaWDO8jjjs user-name@computer-name
The key's randomart image is:
+--[ED25519 256]--+
|              +..|
|           . o +o|
|    .     . o .+o|
|     + .   + .ooo|
|      * S = +.o +|
|     o + B *   o.|
|    . o o = o + .|
|  Eo . . o   O oo|
|  oo.      .o B+.|
+----[SHA256]-----+
```

Now we’ve generated a key, we can add this to [GitHub](https://github.com) and register the key there.
First, visit GitHub, and make sure you’ve signed in to your account.
Once you’re signed in, go to [GitHub > Settings > SSH and GPG keys > Add new](https://github.com/settings/ssh/new), and you should see this:

![](../episodes/fig/add-ssh-key.png)

We need to fill in the details. Give the key a title like “Laptop SSH key”, and then paste your public key into the key box - we can find it in our ~/.ssh folder:

```bash
ls ~/.ssh
```

```output
id_ed25519  id_ed25519.pub  known_hosts
```

You want to copy the contents of the .pub file, which you can display with:

```bash
cat ~/.ssh/id_ed25519.pub
```

```output
ssh-ed25519 <SNIPPED FOR SECURITY> user-name@computer-name
```

**Make sure you copy the .pub file and not the private key!** Your private key lives on your machine and is never shared with anyone else. Then click Add key, and you’re done!

### Microsoft Visual Studio Code

The hands-on part of this topic will be conducted using Visual Studio Code (VS Code), a widely used IDE.
Please [download the appropriate version of Visual Studio Code][https://code.visualstudio.com/] for your operating system (Windows, macOS, or Linux)
and system architecture (e.g., 64-bit, ARM).

## Introduction to GitHub Copilot

GitHub Copilot integrates directly into Visual Studio Code as an extension installable from within the IDE,
providing access to:

- **On-request explanations** - allowing you to obtain responses to questions in a chat interface
- **Real-time assistance as you continue to develop your code** - where Copilot continuously analyzes the code you write, as well as comments and surrounding context, to offer intelligent suggestions which require approval.
- **On-request direct code modification** - by requesting specific changes, your code is modified directly by Copilot (again, requiring specific approval before it integrates the suggested changes)

All of this is integrated into the VSCode editor, so you do not need to leave your development environment.

### The Lifecycle of a Copilot Prompt

So how does Copilot integrate with VSCode, and how does it handle data?
Let's look at how it creates a code suggestion as an example:

![Lifecycle of a Copilot prompt](fig/copilot-prompt-lifecycle.png)

At a high level, the following steps are followed:

Within the Copilot-enabled IDE:

1. Developer enters text into code editor, such as VSCode, gathering context from a number of sources (code before and after cursor, file name and type, other open editor tabs)
2. The prompt is constructed from the amassed context and sent to the Copilot proxy

Within the Copilot proxy (within the "Cloud"):

3. Filters the requests, terminating those involving toxic language, unrelated code requests, and perceived hacking attempts.
The prompt is sent to the GitHub Copilot LLM

The Copilot LLM (also in the "Cloud"):

4. Receives the request and formulates a code suggestion which is sent back to the proxy

Back within the Copilot proxy:

5. Receives the response, and tests code suggestions for code vulnerabilities, truncating responses that contain unique identifiers (such as email addresses, GitHub URLs, IP addresses, etc.), and filters out those matching known public code. The processed response is fed back to the Copilot client within the IDE

Back within the Copilot-enabled IDE:

6. The Copilot extension receives the code suggestion which is presented to the user to accept or reject

GitHub provides further detailed information about [how GitHub Copilot handles data](https://resources.github.com/learn/pathways/copilot/essentials/how-github-copilot-handles-data/).

### Different Models

GitHub Copilot's free tier provides access to multiple large language models, each with different strengths and tradeoffs.
The following table summarizes the models currently available at time of writing:

| **Model** | **Provider** | **Specialization** | **Speed** | **Best for** |
|-----------|--------------|--------------------|-----------|--------------|
| **Claude Haiku** | Anthropic | Balanced, efficient reasoning | Fast | Quick code completions, lightweight tasks, local development |
| **GPT-4.1** | OpenAI | Complex reasoning and analysis | Moderate | Detailed code reviews, architectural decisions, complex refactoring |
| **GPT-5 Mini** | OpenAI | Lightweight version of GPT-5 | Faster | Balance of capability and speed, most general-purpose tasks |

Each model can be selected based on your specific task requirements.
For routine coding tasks, lighter models like Claude Haiku or GPT-5 Mini may be sufficient and faster, while more complex problems may benefit from the deeper reasoning of GPT-4.1.

There are many [other models available](https://docs.github.com/en/copilot/get-started/plans#models) for use within various priced priced tiers,
including other models from OpenAI and Anthropic, as well as models from Google (i.e. Gemini).
Some of these e.g. GPT-5-Codex have been further optimised for writing code and other software engineering tasks.
You can also find a [comparison of these models](https://docs.github.com/en/copilot/reference/ai-models/model-comparison).

### Limitations of the Copilot Free Tier

There are two key quotas which are reset per month to be aware of (which we'll look into during the practical elements of the course):

- **Inline suggestions** - 2000 completions per month, essentially where Copilot provides suggestions as you type
- **Premium requests** - 50 per month, where you use more advanced AI features, such as Copilot chat requests or advanced reasonsing models
