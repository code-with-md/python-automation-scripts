"""
Email Bulk Sender
- Reads email list from CSV
- Sends personalized emails
- Logs results
- Uses Gmail SMTP
"""

import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
from time import sleep

class EmailSender:
    def __init__(self, sender_email, sender_password):
        """
        Initialize email sender
        
        Args:
            sender_email (str): Gmail address
            sender_password (str): Gmail app password (NOT regular password)
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.sent_count = 0
        self.failed_count = 0
        
    def load_emails(self, file_path):
        """Load email list from CSV"""
        try:
            df = pd.read_csv(file_path)
            print(f"✅ Loaded {len(df)} emails from {file_path}")
            return df
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
            return None
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            return None
    
    def send_email(self, recipient, subject, body):
        """Send individual email"""
        try:
            # Create message
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = recipient
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))
            
            # Connect to Gmail
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(self.sender_email, self.sender_password)
            
            # Send email
            server.send_message(message)
            server.quit()
            
            print(f"✅ Email sent to {recipient}")
            self.sent_count += 1
            
        except Exception as e:
            print(f"❌ Failed to send to {recipient}: {e}")
            self.failed_count += 1
    
    def send_bulk(self, csv_file, delay=1):
        """
        Send emails to bulk list
        
        Args:
            csv_file (str): Path to CSV with columns: email, subject, message
            delay (int): Delay between emails in seconds (avoid spam filter)
        """
        
        df = self.load_emails(csv_file)
        if df is None:
            return
        
        # Validate columns
        required_columns = ['email', 'subject', 'message']
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            print(f"❌ Missing columns: {missing}")
            print(f"Your CSV must have: {required_columns}")
            return
        
        print(f"\n📧 Starting to send {len(df)} emails...\n")
        
        # Send each email
        for index, row in df.iterrows():
            recipient = row['email'].strip()
            subject = str(row['subject']).strip()
            body = str(row['message']).strip()
            
            self.send_email(recipient, subject, body)
            
            # Delay to avoid spam filter
            if index < len(df) - 1:  # Don't sleep after last email
                sleep(delay)
        
        print(f"\n✅ Done!")
        print(f"📊 Sent: {self.sent_count}")
        print(f"❌ Failed: {self.failed_count}")

def main():
    """Main entry point"""
    
    if len(sys.argv) < 2:
        print("Usage: python email_sender.py <csv_file>")
        print("\nYour CSV must have these columns:")
        print("  - email (recipient email)")
        print("  - subject (email subject)")
        print("  - message (email body)")
        print("\nExample CSV:")
        print("  email,subject,message")
        print("  john@example.com,Hello,Hi John\\nThis is a test")
        print("\nBEFORE RUNNING:")
        print("1. Enable 2-factor auth on Gmail")
        print("2. Create app password: https://myaccount.google.com/apppasswords")
        print("3. Run: python email_sender.py your_file.csv")
        return
    
    csv_file = sys.argv[1]
    
    print("=" * 50)
    print("EMAIL BULK SENDER")
    print("=" * 50)
    
    # Get credentials
    sender_email = input("\nEnter your Gmail address: ").strip()
    sender_password = input("Enter your Gmail app password: ").strip()
    
    # Create sender
    sender = EmailSender(sender_email, sender_password)
    
    # Send emails
    sender.send_bulk(csv_file)

if __name__ == "__main__":
    main()