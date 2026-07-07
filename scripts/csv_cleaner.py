"""
CSV Data Cleaner
- Removes duplicate rows
- Removes empty rows
- Cleans whitespace
- Removes empty columns
- Outputs cleaned CSV
"""

import pandas as pd
import sys

def clean_csv(input_file, output_file='cleaned.csv'):
    """
    Clean a CSV file by removing duplicates and empty rows
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to save cleaned CSV
    """
    
    print(f"📂 Reading file: {input_file}")
    
    # Read CSV
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found!")
        return
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return
    
    print(f"📊 Original rows: {len(df)}")
    
    # Strip whitespace from all columns
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # Remove completely empty rows
    df = df.dropna(how='all')
    
    # Remove duplicate rows
    initial_rows = len(df)
    df = df.drop_duplicates()
    duplicates_removed = initial_rows - len(df)
    
    # Remove completely empty columns
    df = df.dropna(axis=1, how='all')
    
    # Save cleaned file
    try:
        df.to_csv(output_file, index=False)
        print(f"✅ Cleaned! Saved to: {output_file}")
        print(f"📈 Final rows: {len(df)}")
        print(f"🗑️  Duplicates removed: {duplicates_removed}")
        print(f"📋 Columns: {len(df.columns)}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

def main():
    """Main entry point"""
    
    # Check if file provided
    if len(sys.argv) < 2:
        print("Usage: python csv_cleaner.py <input_file.csv>")
        print("\nExample: python csv_cleaner.py data.csv")
        print("\nThis will create 'cleaned.csv'")
        return
    
    input_file = sys.argv[1]
    output_file = input_file.replace('.csv', '_cleaned.csv')
    
    clean_csv(input_file, output_file)

if __name__ == "__main__":
    main()