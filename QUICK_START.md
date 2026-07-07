# Quick Start Guide

Get started in 2 minutes.

## Step 1: Install (1 minute)

```bash
pip install -r requirements.txt
```

## Step 2: Pick a Script & Run

### CSV Cleaner
```bash
python scripts/csv_cleaner.py your_file.csv
```
Output: `your_file_cleaned.csv`

### Email Sender
```bash
python scripts/email_sender.py emails.csv
```
CSV format:
email,subject,message
name@gmail.com,Hello,Your message here

### File Organizer
```bash
python scripts/file_organizer.py ~/Downloads
```
Organizes by type (Images, Documents, etc)

### PDF Merger
```bash
python scripts/pdf_merger.py ./pdf_folder merged.pdf
```

### Web Scraper
```bash
python scripts/web_scraper.py https://quotes.toscrape.com output.csv
```

---

## Example Output

**CSV Cleaner:** Input 1000 rows → Output 950 cleaned rows ✅

**Email Sender:** Input 50 emails → Sends all with logging ✅

**File Organizer:** Input messy folder → Output organized by type ✅

**PDF Merger:** Input 5 PDFs → Output 1 merged PDF ✅

**Web Scraper:** Input URL → Output CSV with data ✅

---
