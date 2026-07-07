"""
PDF Merger
- Finds all PDF files in a directory
- Merges them in alphabetical order
- Creates single output PDF
- Simple and reliable
"""

import os
import sys
from pathlib import Path

try:
    from PyPDF2 import PdfMerger
except ImportError:
    print("❌ PyPDF2 not installed!")
    print("Install it with: pip install PyPDF2")
    sys.exit(1)

class PDFMerger:
    def __init__(self, input_folder, output_file='merged.pdf'):
        """
        Initialize PDF merger
        
        Args:
            input_folder (str): Folder containing PDF files
            output_file (str): Name of output merged PDF
        """
        self.input_folder = Path(input_folder)
        self.output_file = output_file
        self.merger = PdfMerger()
        self.merged_count = 0
    
    def find_pdfs(self):
        """Find all PDF files in folder"""
        if not self.input_folder.exists():
            print(f"❌ Folder not found: {self.input_folder}")
            return []
        
        pdfs = sorted(self.input_folder.glob('*.pdf'))
        return pdfs
    
    def merge(self):
        """Merge PDFs"""
        
        print(f"📂 Scanning folder: {self.input_folder}")
        
        pdfs = self.find_pdfs()
        
        if not pdfs:
            print("❌ No PDF files found!")
            return False
        
        print(f"📄 Found {len(pdfs)} PDFs:\n")
        
        # Add each PDF to merger
        for pdf_file in pdfs:
            print(f"✅ Adding: {pdf_file.name}")
            try:
                self.merger.append(str(pdf_file))
                self.merged_count += 1
            except Exception as e:
                print(f"❌ Error adding {pdf_file.name}: {e}")
        
        if self.merged_count == 0:
            print("❌ No valid PDFs to merge!")
            return False
        
        # Write output
        try:
            output_path = self.input_folder / self.output_file
            print(f"\n⏳ Merging {self.merged_count} PDFs...")
            
            self.merger.write(str(output_path))
            self.merger.close()
            
            # Get file size
            file_size = output_path.stat().st_size / (1024 * 1024)  # Convert to MB
            
            print(f"\n✅ SUCCESS!")
            print(f"📄 Output file: {output_path}")
            print(f"📊 Size: {file_size:.2f} MB")
            print(f"📈 Combined {self.merged_count} PDFs")
            
            return True
            
        except Exception as e:
            print(f"❌ Error writing output file: {e}")
            return False

def main():
    """Main entry point"""
    
    if len(sys.argv) < 2:
        print("Usage: python pdf_merger.py <pdf_folder> [output_file]")
        print("\nExample: python pdf_merger.py ./my_pdfs merged.pdf")
        print("\nThis will merge all PDFs in the folder into a single PDF.")
        return
    
    input_folder = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'merged.pdf'
    
    print("=" * 50)
    print("PDF MERGER")
    print("=" * 50 + "\n")
    
    merger = PDFMerger(input_folder, output_file)
    merger.merge()

if __name__ == "__main__":
    main()