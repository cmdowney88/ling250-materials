# Lecture 3: Python Modes & Environment Management

This tutorial covers different ways to run Python and how to manage environments with Conda.

**Prerequisites:** Anaconda installed (from setup guide), VS Code, terminal access.

---

## Part 1: Three Ways to Run Python

### The REPL (Interactive Python)

Open your terminal and type:

```bash
python
```

You should see something like:

```
Python 3.10.x | packaged by conda-forge | ...
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is the Python prompt. Try some commands:

```python
>>> 2 + 2
4
>>> x = "hello"
>>> x
'hello'
>>> type(x)
<class 'str'>
>>> len(x)
5
```

To exit the REPL:

```python
>>> exit()
```

**When to use:** Quick calculations, testing small snippets, checking how something works.

**When NOT to use:** Anything you want to save or share.

---

### Scripts (.py files)

A script is Python code saved in a file. You run the whole file at once.

1. In VS Code, create a new file called `hello.py` in your `ling250-materials` folder
2. Add this code:

```python
message = "Hello from a script!"
print(message)

for i in range(3):
    print(f"Count: {i}")
```

3. Run it from the terminal:

```bash
python hello.py
```

You should see:

```
Hello from a script!
Count: 0
Count: 1
Count: 2
```

**When to use:** Code you want to save, share, or run repeatedly. This is the standard for "real" programs.

---

### Notebooks (.ipynb files)

Notebooks mix code, output, and text in one document. We'll use them later in the course for some demos.

#### Setting up notebooks in VS Code

1. **Install the Python extension** (if you haven't already):
   - Open the Extensions panel (Ctrl+Shift+X / Cmd+Shift+X)
   - Search for "Python"
   - Install the extension by Microsoft
   - This includes Jupyter notebook support

2. **Create a new notebook:**
   - Open the Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
   - Type "Jupyter: Create New Blank Notebook"
   - Or: Create a new file with the `.ipynb` extension

3. **Select a kernel:**
   - Click "Select Kernel" in the top right (or you'll be prompted when you try to run a cell)
   - Choose "Python Environments..."
   - Select your `ling250` environment (or `base` if you haven't created it yet)

4. **Write and run code:**
   - Type code in a cell
   - Press **Shift+Enter** to run the cell and move to the next one
   - Or press **Ctrl+Enter** to run without moving
   - Click the `+ Code` or `+ Markdown` buttons to add cells

5. **Try it:**
   - Create a cell with: `print("Hello from a notebook!")`
   - Run it with Shift+Enter
   - Create another cell with: `x = 5; x ** 2`
   - Run it — you should see `25` as output

#### Alternative: Browser interface

You can still use the traditional browser interface if you prefer:

```bash
jupyter notebook
```

This opens in your browser. Press `Ctrl+C` in the terminal to stop the server when done.

**When to use notebooks:** Data exploration, teaching, mixing explanation with code.

**When NOT to use:** Code you want to maintain long-term or version control cleanly.

---

## Part 2: Why Environments?

Imagine this scenario:
- Project A needs `numpy` version 1.20
- Project B needs `numpy` version 2.0
- You can only have one version installed at a time...

**Environments solve this.** Each project gets its own isolated set of packages.

Other benefits:
- **Reproducibility:** Share your environment, others get the exact same setup
- **Safety:** Experiment without breaking your main setup
- **Collaboration:** Everyone on a team uses the same versions

---

## Part 3: Conda Basics

### Check your installation

```bash
conda --version
```

You should see something like `conda 23.x.x`. If you get "command not found," revisit the setup guide.

### See your environments

```bash
conda env list
```

Output:

```
# conda environments:
#
base                  *  /Users/yourname/anaconda3
```

The `*` shows which environment is active. `base` is the default.

### Create a new environment

Let's make a test environment:

```bash
conda create --name test-env python=3.10
```

- `--name test-env`: the environment's name
- `python=3.10`: install Python 3.10 in this environment

Type `y` when asked to proceed.

### Activate the environment

```bash
conda activate test-env
```

Notice your prompt changes to show `(test-env)` at the beginning.

Verify you're using the environment's Python:

```bash
which python
```

On Mac/Linux, this should show a path containing `test-env`. On Windows, use `where python`.

### Install packages

```bash
conda install numpy
```

Type `y` to confirm. You can install multiple packages at once:

```bash
conda install matplotlib pandas
```

### See what's installed

```bash
conda list
```

This shows all packages in the current environment.

### Deactivate

```bash
conda deactivate
```

Your prompt goes back to `(base)` or no prefix.

### Remove the test environment

```bash
conda env remove --name test-env
```

Verify it's gone:

```bash
conda env list
```

---

## Part 4: Environment Files

Typing install commands is tedious and error-prone. Environment files let you specify everything in one place.

### Anatomy of an environment.yaml

Look at the `environment.yaml` in the course repository:

```yaml
name: ling250
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - nltk
  - numpy
  - matplotlib
  - pandas
  - jupyter
```

**What each part means:**

| Field | Purpose |
|-------|---------|
| `name` | What the environment will be called |
| `channels` | Where to download packages from (order matters!) |
| `dependencies` | The packages to install |

### Creating an environment from a file

```bash
conda env create -f environment.yaml
```

Note: It's `env create` (with `env`), not just `create`, when using a file.

### Activating the course environment

```bash
conda activate ling250
```

Verify the packages are there:

```bash
conda list
```

You should see nltk, numpy, matplotlib, etc.

### Updating an environment

If the environment.yaml changes (e.g., we add a new package), update your environment:

```bash
conda env update -f environment.yaml
```

---

## Part 5: Version Pinning

You can specify versions in the environment file:

```yaml
dependencies:
  - python=3.10          # exact minor version
  - numpy>=1.20          # at least this version
  - pandas>=1.0,<2.0     # range (at least 1.0, below 2.0)
  - matplotlib           # any version (most flexible)
```

**When to pin versions:**
- Always pin Python version
- Pin major versions when breaking changes are known
- Pin exactly only if you've hit a specific bug

**When NOT to pin:**
- Don't pin everything exactly (makes it fragile and platform-specific)
- Don't pin dependencies of dependencies (let conda figure those out)

For this course, minimal pinning is fine.

---

## Part 6: Channels and pip

### Channels

Conda packages come from "channels." The main ones are:
- `defaults`: Anaconda's official channel
- `conda-forge`: Community-maintained, often more up-to-date

Channel order matters — packages are searched in order.

### pip packages

Some packages aren't on conda. You can include pip packages in your environment file:

```yaml
dependencies:
  - python=3.10
  - pip
  - pip:
    - some-package-only-on-pip
```

Always include `pip` in the conda dependencies if you have a `pip:` section.

---

## Quick Reference

| Command | What it does |
|---------|--------------|
| `conda --version` | Check conda is installed |
| `conda env list` | List all environments |
| `conda create --name NAME python=3.10` | Create new environment |
| `conda activate NAME` | Switch to an environment |
| `conda deactivate` | Leave current environment |
| `conda install PACKAGE` | Install a package |
| `conda list` | List packages in current environment |
| `conda env create -f FILE` | Create environment from file |
| `conda env update -f FILE` | Update environment from file |
| `conda env remove --name NAME` | Delete an environment |

---

## Challenge

Create your own environment file called `my-environment.yaml` with:
- Python 3.10
- The `requests` package (for making web requests)
- The `beautifulsoup4` package (for parsing HTML)

Then create the environment and verify the packages are installed.

<details>
<summary>Solution</summary>

Create `my-environment.yaml`:

```yaml
name: my-env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - requests
  - beautifulsoup4
```

Then run:

```bash
conda env create -f my-environment.yaml
conda activate my-env
conda list
```

You should see `requests` and `beautifulsoup4` in the list.

Clean up when done:

```bash
conda deactivate
conda env remove --name my-env
```

</details>

---

## Next Steps

For the rest of this course, use the `ling250` environment:

```bash
conda activate ling250
```

If you haven't created it yet:

```bash
cd ling250-materials
conda env create -f environment.yaml
conda activate ling250
```

All the packages we'll use are specified in that file. If we add new ones during the semester, you'll just run `conda env update -f environment.yaml`.
