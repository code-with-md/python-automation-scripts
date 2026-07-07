"""
Web Scraper - FIXED for quotes.toscrape.com
- Scrapes quotes and authors
- Saves to CSV
"""

import requests
from bs4 import BeautifulSoup
import csv
import sys

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.data = []
    
    def fetch_page(self, url):
        """Fetch a web page"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"❌ Error fetching {url}: {e}")
            return None
    
    def scrape(self):
        """Scrape quotes from the website"""
        print(f"🌐 Scraping from: {self.base_url}")
        
        html = self.fetch_page(self.base_url)
        if not html:
            return
        
        soup = BeautifulSoup(html, 'html.parser')
        
        print(f"⏳ Extracting data...\n")
        
        # Find all divs with class "quote" (correct for this website)
        quotes = soup.find_all('div', class_='quote')
        
        if not quotes:
            print("❌ No quotes found!")
            return
        
        for quote in quotes:
            try:
                # Extract quote text
                quote_text = quote.find('span', class_='text')
                author = quote.find('small', class_='author')
                
                if quote_text and author:
                    text = quote_text.get_text(strip=True)
                    author_name = author.get_text(strip=True)
                    
                    self.data.append({
                        'Quote': text,
                        'Author': author_name
                    })
                    print(f"✅ Extracted: {text[:60]}...")
            
            except Exception as e:
                print(f"⚠️  Error: {e}")
                continue
        
        print(f"\n📊 Total quotes extracted: {len(self.data)}")
    
    def save_to_csv(self, filename='scraped_quotes.csv'):
        """Save to CSV"""
        if not self.data:
            print("❌ No data to save!")
            return False
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['Quote', 'Author'])
                writer.writeheader()
                writer.writerows(self.data)
            
            print(f"✅ Saved to: {filename}")
            return True
        
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python web_scraper.py <url> [output_file]")
        print("Example: python web_scraper.py https://quotes.toscrape.com scraped_quotes.csv")
        return
    
    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'scraped_quotes.csv'
    
    print("=" * 50)
    print("WEB SCRAPER")
    print("=" * 50 + "\n")
    
    scraper = WebScraper(url)
    scraper.scrape()
    scraper.save_to_csv(output_file)

if __name__ == "__main__":
    main()