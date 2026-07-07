"""
File Organizer
- Scans a directory
- Groups files by type (images, documents, videos, etc)
- Creates folders automatically
- Moves files to appropriate folders
- Logs all actions
"""

import os
import shutil
from pathlib import Path
import sys
from datetime import datetime

class FileOrganizer:
    def __init__(self, directory):
        """
        Initialize file organizer
        
        Args:
            directory (str): Path to directory to organize
        """
        self.directory = Path(directory)
        self.moved_count = 0
        self.skipped_count = 0
        
        # File categories and extensions
        self.categories = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv'],
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.m4a', '.wma'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php'],
            'Other': []
        }
    
    def get_category(self, file_extension):
        """Determine file category based on extension"""
        file_extension = file_extension.lower()
        
        for category, extensions in self.categories.items():
            if file_extension in extensions:
                return category
        
        return 'Other'
    
    def organize(self):
        """Organize files in directory"""
        
        if not self.directory.exists():
            print(f"❌ Directory not found: {self.directory}")
            return
        
        print(f"📂 Scanning directory: {self.directory}")
        print(f"⏳ This may take a moment...\n")
        
        # Get all files in directory (not subdirectories)
        files = [f for f in self.directory.iterdir() if f.is_file()]
        
        if not files:
            print("❌ No files found in directory!")
            return
        
        print(f"📊 Found {len(files)} files\n")
        
        # Process each file
        for file in files:
            # Skip hidden files and system files
            if file.name.startswith('.'):
                self.skipped_count += 1
                continue
            
            # Get file extension
            file_extension = file.suffix
            
            # Determine category
            category = self.get_category(file_extension)
            
            # Create category folder if it doesn't exist
            category_folder = self.directory / category
            if not category_folder.exists():
                category_folder.mkdir()
                print(f"📁 Created folder: {category}")
            
            # Move file
            try:
                destination = category_folder / file.name
                shutil.move(str(file), str(destination))
                print(f"✅ {file.name} → {category}/")
                self.moved_count += 1
            except Exception as e:
                print(f"❌ Failed to move {file.name}: {e}")
                self.skipped_count += 1
        
        # Print summary
        print(f"\n" + "=" * 50)
        print(f"✅ DONE!")
        print(f"=" * 50)
        print(f"📊 Moved: {self.moved_count}")
        print(f"⏭️  Skipped: {self.skipped_count}")
        print(f"📁 Total folders created: {len([f for f in self.directory.iterdir() if f.is_dir()])}")

def main():
    """Main entry point"""
    
    if len(sys.argv) < 2:
        print("Usage: python file_organizer.py <directory_path>")
        print("\nExample: python file_organizer.py ~/Downloads")
        print("\nThis will organize all files in the directory into folders by type.")
        print("Files will be moved into: Images/, Documents/, Videos/, etc.")
        return
    
    directory = sys.argv[1]
    
    # Confirm with user
    print("=" * 50)
    print("FILE ORGANIZER")
    print("=" * 50)
    print(f"\n📂 Directory: {directory}")
    print("\nThis will organize files into folders by type:")
    print("  - Images, Documents, Videos, Audio, Archives, Code, Other")
    
    confirm = input("\n⚠️  Continue? (yes/no): ").strip().lower()
    
    if confirm != 'yes':
        print("Cancelled.")
        return
    
    organizer = FileOrganizer(directory)
    organizer.organize()

if __name__ == "__main__":
    main()