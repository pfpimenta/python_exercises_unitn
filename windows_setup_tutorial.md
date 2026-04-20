# Python Environment Setup Tutorial (Windows)

Follow these steps to set up a working Python environment for our lab.

⚠️ Please use the **PowerShell** terminal inside VSCode be sure everything works as expected!

⚠️ Tutorial for **Windows** only! For Mac and Linux, use the other tutorial.

## Setup

### 0. Create a project working folder
If you have not done this yet, then create a dedicated folder for the lab exercises:
```powershell
mkdir python_exercises_unitn; cd python_exercises_unitn
```

### 1. Install the 'uv' Package Manager
Downloads and installs uv, a high-performance tool for managing Python versions and packages without the complexity of standard installers.
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Update the System Path
Tells your computer exactly where the uv program was just installed so you can run it by simply typing its name.
```powershell
$env:Path += ";$env:USERPROFILE\.local\bin;$env:USERPROFILE\.cargo\bin"
```

### 3. Initialize the Project
Creates a new UV project structure, including a `pyproject.toml` file that will keep track of which packages your code needs to run.
```powershell
uv init
```

### 4. Create a Virtual Environment
Creates a dedicated .venv folder. This acts as a "container" so that the packages you install here don't mess up other projects on your computer.
```powershell
uv venv
```

### 5. Adjust PowerShell Security Settings
Changes your computer's security settings to allow the execution of local scripts, which is required to "activate" your virtual environment.
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 6. Activate the Environment
Activates the created environment. Now, the Python packages we install will be saved there, instead of in the global space of your OS. After activated, you should see something like this on your terminal: `(venv)`.
```powershell
.\.venv\Scripts\activate
```

### 7. Install Python Packages

```powershell
uv add pandas seaborn
```

### 8. Test Installation
If you run this command and see "Setup Successful!", you are ready to go.
```powershell
python -c "import pandas; import seaborn; print('Setup Successful')"
```

---

## Usage

Now, every time you want to run your Python scripts of this project, you just have to activate the virtual environment first.

---

## Adding new packages
Ensure your virtual environment is activated, then use `uv add`. For example:
```powershell
uv add matplotlib
```

---

### ⚠️ Common Error: "DLL load failed" when importing torch
This means your Windows is missing the C++ Redistributable.

1. **Download:** Open `https://aka.ms/vs/17/release/vc_redist.x64.exe` in your browser.
2. **Install:** Run the downloaded `.exe` file and follow the prompts.
3. **Restart:** Close and reopen the VS Code terminal.
4. **Test:** Run `python -c "import torch; print('Success!')"`