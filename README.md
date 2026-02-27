# Excel Analyzer

This is a simple Python/Streamlit application designed to process Excel
files with the same structure as the provided sample (`تقرير 1-2026 من اكسل ابو سليمان.xls`).

## Features

* Upload `.xls` or `.xlsx` files via a modern web interface
* Display basic dataframe information and a sample of the data
* Show descriptive statistics and value counts for common categorical columns
* Compute totals and averages for recharge amount columns

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501` by default.

## Usage

Upload any Excel file that matches the expected column layout and the
application will automatically compute and display the analysis results.

Feel free to extend the code with additional plots or export options.