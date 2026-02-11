# Lecture 7: Git & GitHub Follow-Along

This tutorial walks through the core Git concepts and commands you'll use throughout this course (and beyond). You can follow along during lecture and use this as a reference later.

**Prerequisites:** You should have a GitHub account and Git installed. Check with:

```bash
git --version
```

---

## What is Git?

Git is a **version control system**. It tracks changes to your files over time, so you can:
- See what changed, when, and by whom
- Go back to a previous version if something breaks
- Collaborate with others without overwriting each other's work

**Git** is the tool that runs on your computer. **GitHub** is a website that hosts Git repositories online, making it easy to share and collaborate.

You've already been using Git without thinking about it — when you ran `git clone` and `git pull` for the `ling250-materials` repo, those are Git commands.

---

## Part 1: Setup

Before making commits, Git needs to know who you are. This information is attached to every commit you make.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Check your settings:

```bash
git config --list
```

You should see your name and email in the output.

---

## Part 2: Creating a Repository

There are two ways to start working with Git:

### Option A: Create a new repository from scratch

```bash
mkdir my-project
cd my-project
git init
```

This creates a hidden `.git/` folder that stores all of Git's tracking information. The directory is now a Git repository.

```bash
ls -a
```

You should see `.git/` in the listing.

### Option B: Clone an existing repository

```bash
git clone https://github.com/username/repo-name.git
```

This downloads the entire repository (with its full history) to your computer. You've already done this with `ling250-materials`.

**For this tutorial**, let's create a practice repo:

```bash
mkdir ~/git-practice
cd ~/git-practice
git init
```

---

## Part 3: The Basic Workflow

This is the core of using Git. Almost everything you do follows this cycle:

```
Edit files → Stage changes → Commit
```

### Checking status

`git status` is your best friend. Run it early and often.

```bash
git status
```

Right now you should see something like:

```
On branch main
No commits yet
nothing to commit
```

### Create some files to work with

```bash
echo "# My Practice Repo" > README.md
echo "print('hello world')" > hello.py
```

Now check the status:

```bash
git status
```

You should see both files listed as **Untracked files** in red. Git sees them, but isn't tracking them yet.

### Staging changes with `git add`

Before you can commit, you need to **stage** the changes you want to include. Think of it as putting items in a box before shipping it.

```bash
git add README.md
```

Check the status again:

```bash
git status
```

Now `README.md` appears in green under "Changes to be committed," and `hello.py` is still red under "Untracked files."

**Stage the second file:**

```bash
git add hello.py
```

**Tip:** Add files by name rather than using `git add .` (which stages *everything*). This gives you control over exactly what goes into each commit.

### Committing with `git commit`

A **commit** is a snapshot of your staged changes, saved permanently in the repository's history.

```bash
git commit -m "Add README and hello script"
```

The `-m` flag lets you write a message describing what the commit does. Good commit messages are short and describe the *purpose* of the change.

Check the status:

```bash
git status
```

You should see "nothing to commit, working tree clean."

### Viewing history with `git log`

```bash
git log
```

You'll see your commit with:
- A long hexadecimal **hash** (unique ID for the commit)
- Author name and email
- Date
- Your commit message

For a more compact view:

```bash
git log --oneline
```

This shows just the short hash and message — much easier to scan.

### The full cycle again

Let's make another change:

```bash
echo "print('goodbye world')" > goodbye.py
echo "# My Practice Repo" > README.md
echo "" >> README.md
echo "A repository for learning Git." >> README.md
```

```bash
git status
```

You should see one untracked file (`goodbye.py`) and one modified file (`README.md`).

### Viewing changes with `git diff`

Before staging, you can see exactly what changed:

```bash
git diff
```

This shows line-by-line changes to tracked files that haven't been staged yet. Added lines are shown with `+`, removed lines with `-`.

Now stage and commit:

```bash
git add goodbye.py README.md
git commit -m "Add goodbye script and update README"
```

```bash
git log --oneline
```

You should now see two commits.

---

## Part 4: Working with Remotes

So far everything has been local. To share your work (or back it up), you connect your local repository to a **remote** — usually on GitHub.

### How `ling250-materials` works

When you cloned `ling250-materials`, Git automatically set up a remote called `origin` pointing to the GitHub URL. You can see this:

```bash
cd ~/ling250-materials
git remote -v
```

You should see the GitHub URL listed for both "fetch" and "push."

### Pulling updates

When the instructor pushes new materials, you get them with:

```bash
git pull
```

This downloads new commits from the remote and updates your local files. You've been doing this already.

### Pushing your work

For your own repositories (homework, projects), you push your commits to GitHub:

```bash
git push
```

This sends your local commits to the remote. If you just created a local repo and haven't connected it to GitHub yet, you'll need to:

1. Create a new repository on GitHub (through the website)
2. Connect your local repo to it:

```bash
git remote add origin https://github.com/yourusername/your-repo.git
```

3. Push for the first time:

```bash
git push -u origin main
```

The `-u` flag sets up the tracking relationship so future pushes only need `git push`.

### The `pull` before `push` habit

If you're working across multiple computers (or with collaborators), always pull before you push:

```bash
git pull
git push
```

This avoids conflicts where your local history diverges from the remote.

---

## Part 5: Branches

Branches let you work on separate things without affecting the main codebase. Think of them as parallel timelines.

### Why branches?

- Try out an idea without risking your working code
- Work on a feature while keeping `main` stable
- Collaborate without stepping on each other's toes

### Viewing branches

```bash
git branch
```

The `*` marks the branch you're currently on. Right now there's probably just `main`.

### Creating and switching branches

```bash
git branch experiment
git switch experiment
```

Or do both at once:

```bash
git switch -c another-experiment
```

The `-c` flag creates the branch and switches to it in one step.

```bash
git branch
```

You should see the `*` next to your new branch.

### Working on a branch

Any commits you make now only exist on this branch. The `main` branch stays exactly as it was.

```bash
echo "print('experimenting!')" > experiment.py
git add experiment.py
git commit -m "Add experimental script"
```

Switch back to main:

```bash
git switch main
ls
```

Notice that `experiment.py` is gone — it only exists on the `another-experiment` branch. Switch back and it reappears:

```bash
git switch another-experiment
ls
```

---

## Part 6: Merging

When you're happy with the work on a branch, you **merge** it back into `main`.

### Basic merge

First, switch to the branch you want to merge *into* (usually `main`):

```bash
git switch main
```

Then merge the other branch:

```bash
git merge another-experiment
```

If there are no conflicting changes, Git will automatically combine the histories. Now `main` has everything from `another-experiment`.

```bash
git log --oneline
ls
```

You should see `experiment.py` is now on `main`.

### Merge conflicts

A **merge conflict** happens when two branches changed the *same lines* of the same file. Git can't automatically decide which version to keep, so it asks you to resolve it manually.

When a conflict happens, Git marks the conflicting sections in the file:

```
<<<<<<< HEAD
your version of the line
=======
the other branch's version
>>>>>>> branch-name
```

To resolve:
1. Open the file and decide which version to keep (or combine them)
2. Remove the `<<<`, `===`, and `>>>` markers
3. Stage and commit the resolved file

Merge conflicts sound scary, but they're a normal part of collaboration. VS Code has nice visual tools for resolving them.

### Cleaning up branches

After merging, you can delete the branch:

```bash
git branch -d another-experiment
git branch -d experiment
```

---

## Part 7: `.gitignore`

A `.gitignore` file tells Git which files to **not track**. This is useful for:
- Large data files that shouldn't be in the repository
- Secret files (API keys, passwords)
- Generated files (compiled code, build artifacts)
- Operating system files (`.DS_Store` on Mac)

### How it works

Create a file called `.gitignore` in your repository root:

```bash
echo "*.pyc" > .gitignore
echo "__pycache__/" >> .gitignore
echo ".DS_Store" >> .gitignore
```

Each line is a pattern. Common patterns:

| Pattern | Matches |
|---------|---------|
| `*.pyc` | All `.pyc` files |
| `__pycache__/` | The `__pycache__` directory |
| `data/` | The entire `data/` directory |
| `secret.txt` | A specific file |
| `*.csv` | All CSV files |

**Important:** `.gitignore` only affects **untracked** files. If a file is already tracked by Git, adding it to `.gitignore` won't stop tracking it. You'd need to remove it from tracking first with `git rm --cached filename`.

The `ling250-materials` repo already has a `.gitignore` — take a look:

```bash
cat ~/ling250-materials/.gitignore
```

---

## Challenge Exercises

### Challenge 1: The full cycle

Create a new file in your practice repo, stage it, and commit it with a descriptive message. Then make a change to an existing file, view the diff, and commit that too.

<details>
<summary>Solution</summary>

```bash
cd ~/git-practice
echo "x = 42" > answer.py
git add answer.py
git commit -m "Add answer script"

echo "print(x)" >> answer.py
git diff
git add answer.py
git commit -m "Print the answer in answer.py"
```

</details>

### Challenge 2: Branch and merge

Create a branch called `feature`, add a new file on that branch, then merge it back into `main`.

<details>
<summary>Solution</summary>

```bash
git switch -c feature
echo "print('new feature')" > feature.py
git add feature.py
git commit -m "Add new feature"
git switch main
git merge feature
git branch -d feature
```

</details>

### Challenge 3: Explore `ling250-materials` history

Use `git log --oneline` in the `ling250-materials` repo to see the commit history. How many commits are there? Can you find the commit where a specific file was added?

<details>
<summary>Hint</summary>

```bash
cd ~/ling250-materials
git log --oneline
git log --oneline -- lectures/lecture02_shell_followalong.md
```

The `--` followed by a path shows only commits that touched that file.

</details>

---

## Cleanup

When you're done practicing, you can delete the practice repository:

```bash
rm -r ~/git-practice
```

Or keep it around to experiment more — it's just a local folder.

---

## Quick Reference

### Setup

| Command | What it does |
|---------|--------------|
| `git config --global user.name "Name"` | Set your name |
| `git config --global user.email "email"` | Set your email |
| `git init` | Create a new repository |
| `git clone URL` | Clone an existing repository |

### The Basic Workflow

| Command | What it does |
|---------|--------------|
| `git status` | See what's changed |
| `git diff` | See line-by-line changes (unstaged) |
| `git add filename` | Stage a file for commit |
| `git commit -m "message"` | Commit staged changes |
| `git log` | View commit history |
| `git log --oneline` | Compact commit history |

### Remotes

| Command | What it does |
|---------|--------------|
| `git remote -v` | See remote connections |
| `git remote add origin URL` | Connect to a remote |
| `git pull` | Download and apply remote changes |
| `git push` | Upload local commits to remote |
| `git push -u origin main` | First push (sets up tracking) |

### Branches

| Command | What it does |
|---------|--------------|
| `git branch` | List branches |
| `git branch name` | Create a branch |
| `git switch name` | Switch to a branch |
| `git switch -c name` | Create and switch in one step |
| `git merge name` | Merge a branch into current branch |
| `git branch -d name` | Delete a branch |

### Other

| Command | What it does |
|---------|--------------|
| `.gitignore` | File listing patterns to not track |
| `git log -- path` | History for a specific file |
| `git diff --staged` | See staged changes (before commit) |
