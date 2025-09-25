# DriftAnalyzer

The **DriftAnalyzer** is a Python-based utility designed to streamline and automate parametric drift analysis over multiple test readpoints. By reducing manual data wrangling and spreadsheet setup, this tool lets engineers focus on interpreting results and identifying meaningful trends in test data.

---

## Table of Contents

- [Features](#features)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Usage](#usage)  
  - [Beginner-Friendly Setup Guide](#beginner-friendly-setup-guide)  
  - [Troubleshooting](#troubleshooting)  
- [Project Structure](#project-structure)  
- [Example Workflow](#example-workflow)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact / Support](#contact--support)  

---

## Features

- Processes raw readpoint/test data across multiple files  
- Performs parametric drift analysis automatically  
- Generates plots and visualizations  
- Exports results and summaries to Excel  
- Minimal manual pre-formatting required  

---

## Getting Started

### Prerequisites

- Python 3.7+  
- The following Python libraries (install via pip):  

```
pip install numpy pandas matplotlib seaborn openpyxl
pip install git+https://github.com/galenmarchetti/pystdf.git
```

*(Or simply use requirements.txt if provided.)*

### Installation

1. Clone this repository:  

```
git clone https://github.com/adrianpar1/Parametric-Drift-Analysis-Tool.git
cd Parametric-Drift-Analysis-Tool
```

2. (Optional) Create and activate a virtual environment:  

```
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:  

```
pip install -r requirements.txt
```

### Usage

Run the tool via GUI or command line.

- **GUI mode**:  

```
python gui.py
```

- **Command line mode**:  

```
python data_processing.py path/to/input_folder path/to/output_folder
```

---

### Beginner-Friendly Setup Guide

If you’re new to Python or virtual environments, follow this step-by-step:

1. **Install Python**  
   - Download from [python.org](https://www.python.org/downloads/).  
   - On Windows, check **“Add Python to PATH.”**

2. **Open a Terminal/Command Prompt**  
   - macOS: use **Terminal**.  
   - Windows: use **Command Prompt** or **PowerShell**.

3. **Go into the Project Folder**  
   ```
   cd Parametric-Drift-Analysis-Tool
   ```

4. **Make a Virtual Environment**  
   ```
   python -m venv venv
   ```

5. **Activate It**  
   - On macOS/Linux:  
     ```
     source venv/bin/activate
     ```
   - On Windows:  
     ```
     venv\Scripts\activate
     ```
   You’ll know it worked if you see `(venv)` in your prompt.

6. **Install the Packages**  
   ```
   pip install -r requirements.txt
   ```

7. **Check Tkinter Works (GUI needs this)**  
   ```
   python -m tkinter
   ```
   If a blank window pops up, you’re good.

8. **Run the Program**  
   ```
   python gui.py
   ```

---

### Troubleshooting

- **Error: No module named _tkinter**  
  → Install Python from [python.org](https://www.python.org/downloads/macos/) instead of Homebrew. Recreate your virtual environment with the Python.org version.  

- **Error: ModuleNotFoundError (e.g., seaborn, openpyxl)**  
  → Run `pip install -r requirements.txt` again to ensure all dependencies are installed.  

- **GUI does not appear**  
  → Run `python -m tkinter` to confirm Tkinter is working. If no window appears, reinstall Python using the official installer.  

---

## Project Structure

```
Parametric-Drift-Analysis-Tool/
├── data_processing.py     # Handles parsing and cleaning input data
├── excel_export.py        # Exports results to Excel format
├── gui.py                 # Graphical interface implementation
├── plotting.py            # Functions for generating visualizations
├── requirements.txt       # List of Python dependencies
└── README.md              # This file
```

---

## Example Workflow

1. Place your raw test data files in an input folder (STDF files). 
2. Run the tool (GUI or CLI).  
3. The tool processes data, computes drift metrics, creates plots, and exports Excel summaries.  
4. Review generated output files for drift plots, numeric summaries, and trend tables.  

You can customize settings by editing `plotting.py` or `excel_export.py`.

---

## Contributing

Contributions are welcome! You can:  
- Submit pull requests with fixes or enhancements  
- Open issues for bugs or feature requests  
- Add tests to improve coverage  
- Improve documentation or sample datasets  

Please follow the code style and include tests where possible.

---

## License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## Contact / Support

For questions or feature requests, open a GitHub Issue or reach out via GitHub.  
