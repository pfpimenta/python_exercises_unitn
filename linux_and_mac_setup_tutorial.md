
# Python Environment Setup Tutorial (Linux & macOS)

Follow these steps to set up a working Python environment for our lab.

⚠️ Please use the terminal inside **VS Code** to ensure everything works as expected!

⚠️ This tutorial is for **Linux** and **macOS** only.

## Setup

### 0. Create a project working folder
If you have not done this yet, then create a dedicated folder for the lab exercises:
```bash
mkdir python_exercises_unitn; cd python_exercises_unitn
```

### 1. Install the 'uv' Package Manager
Downloads and installs uv, a high-performance tool for managing Python versions and packages without the complexity of standard installers.
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Initialize the Project
Creates a new UV project structure, including a `pyproject.toml` file that will keep track of which packages your code needs to run.
```bash
uv init
```

### 3. Create a Virtual Environment
Creates a dedicated .venv folder. This acts as a "container" so that the packages you install here don't mess up other projects on your computer.
```bash
uv venv
```

### 4. Activate the Environment
Activates the created environment. Now, the Python packages we install will be saved there, instead of in the global space of your OS. After activated, you should see something like this on your terminal: `(venv)`.
```bash
source .venv/bin/activate
```

### 5. Install Python Packages

```bash
uv add pandas seaborn
```

### 6. Test Installation
If you run this command and see "Setup Successful!", you are ready to go.
```bash
python3 -c "import pandas; import seaborn; print('Setup Successful')"
```

## Usage

Now, every time you want to run your Python scripts of this project, you just have to activate the virtual environment first.
```bash
source .venv/bin/activate
```

## Adding new packages
Ensure your virtual environment is activated, then use `uv add`. For example:
```bash
uv add matplotlib
```

---

### ⚠️ Common Troubleshooting (Linux/macOS)

**1. "Command not found: uv"**
If `uv` isn't recognized after step 1, your shell doesn't know where it is yet. Try closing the VS Code terminal and opening a new one.

**2. Python vs Python3**
On some Linux/macOS systems, the command is `python3` instead of `python`. If the test in Step 7 fails, try replacing `python` with `python3`.

**3. macOS "Developer Tools" Prompt**
If macOS asks you to install "Command Line Developer Tools" during any of these steps, click **Install**. It is required for Python packages to compile correctly.