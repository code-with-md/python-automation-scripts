# Python Automation Scripts Bundle

> Save Hours of Work with These 5 Ready-to-Use Python Scripts

## What's Inside?

A collection of 5 powerful automation scripts that handle the tasks you do every day. No coding required—just copy, paste, and run.

### 🔧 The 5 Scripts

#### 1. **CSV Data Cleaner** 🧹
- Remove duplicate rows
- Fix formatting issues
- Remove empty cells and columns
- Perfect for messy data files

**Use case:** You have a spreadsheet with duplicate entries and missing data. Run this script, get a clean file in seconds.

#### 2. **Email Bulk Sender** 📧
- Send 100s of personalized emails at once
- Read from Excel/CSV file
- Automatic logging of sent emails
- Works with Gmail (free setup)

**Use case:** You need to email 50 clients with personalized messages. Load them in a CSV, run this script, done.

#### 3. **File Organizer** 📁
- Automatically sort files by type (images, documents, videos, etc)
- Creates folders automatically
- Moves files instantly
- Logs all actions

**Use case:** Your Downloads folder is a mess. Run this once, everything is organized into folders by type.

#### 4. **PDF Merger** 📄
- Combine multiple PDFs into one
- Keeps them in order
- Simple and reliable
- One command

**Use case:** You have 10 PDF files that need to be one document. Run this script, get merged PDF in seconds.

#### 5. **Web Scraper** 🕷️
- Extract data from websites
- Save to CSV automatically
- Template provided (modify for any site)
- Handles errors gracefully

**Use case:** You need data from a website. Point it at the URL, get a CSV file with all the data.

---

## ⚡ Quick Start (30 seconds)

```bash
# 1. Download and extract the files
unzip python-automation-scripts.zip
cd python-automation-scripts

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run any script
python scripts/csv_cleaner.py your_file.csv
python scripts/email_sender.py emails.csv
python scripts/file_organizer.py ~/Downloads
python scripts/pdf_merger.py ./pdf_folder
python scripts/web_scraper.py https://example.com
```

See detailed instructions for each script below.

---

## 📖 Installation & Setup

### Prerequisites
- Python 3.7+ (download from [python.org](https://www.python.org/downloads/))
- A terminal/command prompt

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `pandas` - For CSV handling
- `requests` - For web scraping
- `beautifulsoup4` - For HTML parsing
- `PyPDF2` - For PDF merging

### Step 2: Test Your Installation

```bash
# Test CSV Cleaner
python scripts/csv_cleaner.py examples/sample_data.csv

# You should see:
# ✅ Cleaned! Saved to: sample_data_cleaned.csv
```

If you see errors, see **Troubleshooting** section below.

---

## 🔍 Detailed Usage Guide

### Script #1: CSV Data Cleaner

**Purpose:** Clean messy CSV files

**How to use:**
```bash
python scripts/csv_cleaner.py your_file.csv
```

**What it does:**
- Removes duplicate rows (keeps first occurrence)
- Removes completely empty rows
- Removes extra whitespace
- Removes empty columns
- Saves as `your_file_cleaned.csv`

**Example:**
```bash
python scripts/csv_cleaner.py messy_data.csv
# Creates: messy_data_cleaned.csv
```

BEFORE:
name,email,age
John,john@email.com,25
Jane,jane@email.com,30
John,john@email.com,25    ← Duplicate
,,                        ← Empty row
Bob,bob@email.com,35

AFTER:
name,email,age
John,john@email.com,25
Jane,jane@email.com,30
Bob,bob@email.com,35

---

### Script #3: File Organizer

**Purpose:** Auto-sort files in a folder by type

**How to use:**
```bash
python scripts/file_organizer.py /path/to/folder
```

**Example:**
```bash
python scripts/file_organizer.py ~/Downloads
```

**What it creates:**
- `Images/` - .jpg, .png, .gif, .bmp, etc
- `Documents/` - .pdf, .doc, .xlsx, .txt, etc
- `Videos/` - .mp4, .avi, .mkv, etc
- `Audio/` - .mp3, .wav, .flac, etc
- `Archives/` - .zip, .rar, .7z, etc
- `Code/` - .py, .js, .html, etc
- `Other/` - Everything else

**Before:**
Downloads/
├── document.pdf
├── photo.jpg
├── song.mp3
├── script.py
├── archive.zip
└── video.mp4

**After:**
Downloads/
├── Documents/
│   └── document.pdf
├── Images/
│   └── photo.jpg
├── Audio/
│   └── song.mp3
├── Code/
│   └── script.py
├── Archives/
│   └── archive.zip
└── Videos/
└── video.mp4

---

### Script #4: PDF Merger

**Purpose:** Combine multiple PDFs into one

**How to use:**
```bash
python scripts/pdf_merger.py /path/to/pdf/folder output_name.pdf
```

**Example:**
```bash
python scripts/pdf_merger.py ./my_pdfs merged.pdf
```

**Requirements:**
- All PDFs must be in one folder
- Script merges them in alphabetical order

**Example:**
my_pdfs/
├── 01_introduction.pdf
├── 02_chapter1.pdf
├── 03_chapter2.pdf
└── 04_conclusion.pdf

After running:
merged.pdf  ← Combined 4 PDFs in order

---

### Script #5: Web Scraper

**Purpose:** Extract data from websites

**How to use:**
```bash
python scripts/web_scraper.py https://website.com output.csv
```

**Example:**
```bash
python scripts/web_scraper.py https://quotes.toscrape.com quotes.csv
```

**What you get:**
```csv
Quote,Author
"The way to get started is to quit talking and begin doing.",Walt Disney
"Your time is limited so don't waste it living someone else's life.",Steve Jobs
```

**Important Notes:**
- Different websites have different HTML structures
- You may need to modify the script for your specific website
- Check website's `robots.txt` file
- Be respectful with scraping (don't overload their servers)
- Some sites block scraping—check their Terms of Service

---

## 📂 File Structure
python-automation-scripts/
├── README.md                          ← You are here
├── QUICK_START.md                     ← Copy-paste instructions
├── requirements.txt                   ← Dependencies
├── scripts/
│   ├── csv_cleaner.py
│   ├── email_sender.py
│   ├── file_organizer.py
│   ├── pdf_merger.py
│   └── web_scraper.py
└── examples/
├── sample_data.csv
├── sample_emails.csv
└── scraped_quotes.csv

---

## ⚠️ Troubleshooting

### Error: "ModuleNotFoundError: No module named 'pandas'"

**Solution:**
```bash
pip install pandas
```

### Error: "Gmail authentication failed"

**Solution:**
- You must use **App Password**, not your regular Gmail password
- Go to: https://myaccount.google.com/apppasswords
- Make sure 2-factor auth is enabled first

### Error: "File not found"

**Solution:**
- Check the file path is correct
- Use absolute paths: `/Users/yourname/Documents/file.csv`
- Or use relative paths: `./files/data.csv`

### Web Scraper extracts wrong data

**Solution:**
- Different websites have different HTML structures
- Right-click website → Inspect → Find the correct selectors
- Modify the script's `scrape()` function with correct CSS selectors

---

## 💡 Common Use Cases

**I have 100 duplicate rows in my data**
→ Use CSV Cleaner

**I need to send emails to 50 people with personalized messages**
→ Use Email Bulk Sender

**My Downloads folder is a mess**
→ Use File Organizer

**I have 10 PDFs that need to be one file**
→ Use PDF Merger

**I need data from a website**
→ Use Web Scraper

---

## 🤝 Support & Questions

If you hit any issues:
1. Check the Troubleshooting section above
2. Ensure all dependencies are installed: `pip install -r requirements.txt`
3. Try the example files first to confirm setup works

---

## 📄 License & Usage

These scripts are provided as-is for personal and business use.

---

## 🚀 Next Steps

1. Install dependencies: `pip install -r requirements.txt`
2. Read QUICK_START.md for fastest setup
3. Try running a script on your own files
4. Customize for your specific needs

---

**Made with ❤️ by Maninder singh**

Happy automating! 🎉
