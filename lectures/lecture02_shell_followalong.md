# Lecture 2: Shell Commands Follow-Along

This tutorial walks through the shell commands we'll cover in class. You can follow along during lecture and use this as a reference later.

**Prerequisites:** You should have completed the setup guide and have VS Code installed with access to a terminal.

---

## Getting Started

1. Open VS Code
2. Open the `ling250-materials` folder (File → Open Folder)
3. Open this file (`lectures/lecture02_shell_followalong.md`) from the file explorer
4. Open markdown preview side-by-side:
   - **Mac:** Cmd + K, then V
   - **Windows/Linux:** Ctrl + K, then V

   You should now see the formatted version of this document next to the raw text.

5. Open the integrated terminal (Ctrl+` on Windows/Linux, Cmd+` on Mac)

You should see a command prompt. The exact appearance varies, but it will end with `$` (Mac/Linux) or `>` (Windows).

**Tip:** You can drag the terminal panel to resize it, or drag it to the side to have the preview and terminal visible at the same time.

---

## Part 1: Where Am I?

### Print working directory

```bash
pwd
```

This shows your current location in the filesystem. You should see the path to your `ling250-materials` folder.

### List contents

```bash
ls
```

You should see the folders and files in this repository: `README.md`, `data/`, `lectures/`, etc.

### List with details

```bash
ls -l
```

The `-l` flag gives you a "long" listing with more information:
- Permissions (who can read/write/execute)
- Owner
- File size
- Last modified date
- Filename

### Show hidden files

```bash
ls -a
```

Files starting with `.` are hidden by default. You should now see `.git/` and `.gitignore`.

### Combine flags

```bash
ls -la
```

Long listing including hidden files. This is a very common combination.

---

## Part 2: Navigation

### The home directory

```bash
echo ~
```

The `~` symbol represents your home directory. On Mac, this is typically `/Users/yourusername`.

```bash
cd ~
pwd
```

Now you're in your home directory.

### Go back to where we were

```bash
cd -
pwd
```

The `-` takes you back to your previous directory. Very useful!

### Navigate to a subdirectory

```bash
cd data
pwd
ls
```

You're now inside the `data/` folder.

### Go up one level

```bash
cd ..
pwd
```

The `..` means "parent directory." You should be back in `ling250-materials`.

### Tab completion (important!)

Try typing this, but **don't press Enter yet**:

```bash
cd lec
```

Now press **Tab**. The shell should auto-complete to `lectures/`.

**This is one of the most useful shell features.** If there are multiple matches, press Tab twice to see them all.

---

## Part 3: Creating and Organizing

Let's create a workspace for this lecture.

### Create a directory

```bash
mkdir scratch
ls
```

You should now see a `scratch/` folder. (It's in `.gitignore`, so it won't be tracked by git.)

### Create nested directories

```bash
mkdir -p scratch/lecture02/examples
ls scratch/lecture02
```

The `-p` flag creates parent directories as needed.

### Navigate to our workspace

```bash
cd scratch/lecture02
pwd
```

### Create an empty file

```bash
touch notes.txt
ls
```

`touch` creates an empty file (or updates the timestamp if it already exists).

### Create a file with content

```bash
echo "This is a test file." > test.txt
ls
```

The `>` redirects output to a file. **Warning:** This overwrites the file if it exists!

### Append to a file

```bash
echo "This is another line." >> test.txt
```

The `>>` appends instead of overwriting.

### Copy a file

```bash
cp test.txt test_backup.txt
ls
```

### Rename/move a file

```bash
mv test_backup.txt backup.txt
ls
```

`mv` is used both to move files and to rename them.

### Move a file to a different directory

```bash
mv backup.txt examples/
ls examples/
```

### Copy a directory

```bash
cp -r examples examples_copy
ls
```

The `-r` flag means "recursive" — copy the directory and everything inside it.

### Remove a file

```bash
rm notes.txt
ls
```

**Warning:** There is no trash can! The file is gone.

### Remove a directory

```bash
rm -r examples_copy
ls
```

The `-r` flag is required to remove directories.

⚠️ **Be very careful with `rm -rf`** — it will delete everything without asking. Double-check your command before pressing Enter!

---

## Part 4: Viewing File Contents

Let's work with the Night Vale transcript. First, make sure you've downloaded it:

```bash
ls ../../data/
```

You should see `Night_Vale.txt` (if not, follow the instructions in `data/README.md`).

### Print entire file (careful!)

```bash
cat ../../data/Night_Vale.txt
```

This prints the whole file. Press Ctrl+C if it's taking too long!

### First few lines

```bash
head ../../data/Night_Vale.txt
```

By default, `head` shows the first 10 lines.

### Specify number of lines

```bash
head -n 20 ../../data/Night_Vale.txt
```

### Last few lines

```bash
tail -n 20 ../../data/Night_Vale.txt
```

### Paginated viewing

```bash
less ../../data/Night_Vale.txt
```

Navigation in `less`:
- **Space** or **Page Down**: next page
- **b** or **Page Up**: previous page
- **/** then type a word: search for that word
- **n**: next search result
- **q**: quit

### Count lines, words, characters

```bash
wc ../../data/Night_Vale.txt
```

Output is: lines, words, characters (bytes).

```bash
wc -l ../../data/Night_Vale.txt
```

Just the line count.

---

## Part 5: Searching

### Find lines containing a word

```bash
grep "Night" ../../data/Night_Vale.txt
```

This prints every line containing "Night".

### Case-insensitive search

```bash
grep -i "night" ../../data/Night_Vale.txt
```

### Count matches

```bash
grep -c "Night" ../../data/Night_Vale.txt
```

### Save results to a file

```bash
grep -i "sheriff" ../../data/Night_Vale.txt > sheriff_lines.txt
wc -l sheriff_lines.txt
```

---

## Part 6: Pipes

Pipes (`|`) let you chain commands together. The output of one command becomes the input to the next.

### Example: paginate a long output

```bash
grep -i "night" ../../data/Night_Vale.txt | less
```

Press `q` to quit.

### Example: count results

```bash
grep -i "night" ../../data/Night_Vale.txt | wc -l
```

This counts lines containing "night" (case-insensitive).

### Example: get the first few matches

```bash
grep -i "cecil" ../../data/Night_Vale.txt | head -n 5
```

---

## Part 7: Useful Shortcuts

Try these out:

| Shortcut | What it does |
|----------|--------------|
| **Tab** | Auto-complete file/directory names |
| **Up arrow** | Previous command |
| **Ctrl + R** | Search command history (type to search, Enter to run) |
| **Ctrl + C** | Cancel current command |
| **Ctrl + A** | Jump to beginning of line |
| **Ctrl + E** | Jump to end of line |
| **Ctrl + L** | Clear screen (same as `clear`) |

### View command history

```bash
history
```

### Wildcards

```bash
ls ../../demos/data_formats/*.json
```

The `*` matches anything. This lists all `.json` files.

```bash
ls ../../audio/sine_*.wav
```

All sine wave files.

---

## Challenge

Using what you've learned, try this:

> Find all lines in Night_Vale.txt that contain the word "police" (case-insensitive), and save them to a file called `police_lines.txt`. Then count how many lines you found.

<details>
<summary>Solution</summary>

```bash
grep -i "police" ../../data/Night_Vale.txt > police_lines.txt
wc -l police_lines.txt
```

</details>

---

## Cleanup

When you're done experimenting:

```bash
cd ../..
rm -r scratch/lecture02
```

Or keep it around for reference — it's in `.gitignore` so it won't affect the repository.

---

## Quick Reference

| Command | What it does |
|---------|--------------|
| `pwd` | Print working directory |
| `ls` | List directory contents |
| `ls -la` | List with details and hidden files |
| `cd dir` | Change to directory |
| `cd ..` | Go up one level |
| `cd ~` | Go to home directory |
| `cd -` | Go to previous directory |
| `mkdir dir` | Create directory |
| `mkdir -p a/b/c` | Create nested directories |
| `touch file` | Create empty file |
| `cp src dst` | Copy file |
| `cp -r src dst` | Copy directory |
| `mv src dst` | Move or rename |
| `rm file` | Remove file |
| `rm -r dir` | Remove directory |
| `cat file` | Print entire file |
| `head -n N file` | First N lines |
| `tail -n N file` | Last N lines |
| `less file` | Paginated viewing |
| `wc file` | Count lines/words/chars |
| `wc -l file` | Count lines only |
| `grep pattern file` | Search for pattern |
| `grep -i pattern file` | Case-insensitive search |
| `cmd1 \| cmd2` | Pipe output to next command |
| `cmd > file` | Redirect output to file (overwrite) |
| `cmd >> file` | Redirect output to file (append) |
