import re

class DataExtractor:
    def __init__(self):
        # Email pattern: matches user@example.com, firstname.lastname@company.co.uk
        self.email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        
        # URL pattern: matches https://www.example.com, https://subdomain.example.org/page
        self.url = r'https?://(?:www\.)?[A-Za-z0-9.-]+(?:\.[A-Za-z]{2,})+(?:/[A-Za-z0-9._~:/?#[\]@!$&\'()*+,;=%-]*)?'
        # Credit card pattern
        self.credit_card = r'\b(?:\d[ -]*?){13,16}\b'

        # HTML tag pattern
        self.html_tag = r'<[^>]+>'
        
        # Currency pattern
        self.currency = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    
    def extract_emails(self, text):
        return re.findall(self.email, text)
    
    def extract_urls(self, text):
        return re.findall(self.url, text)

    def extract_credit_cards(self, text):
        return re.findall(self.credit_card, text)
    
    def extract_html_tags(self, text):
        return re.findall(self.html_tag, text)
    
    def extract_hashtags(self, text):
        return re.findall(self.hashtag, text)
    
    def extract_currencies(self, text):
        return re.findall(self.currency, text)
    
    def extract_all(self, text):
        return {
            'emails': self.extract_emails(text),
            'urls': self.extract_urls(text),
            'credit_cards': self.extract_credit_cards(text),
            'html_tags': self.extract_html_tags(text),
            'currencies': self.extract_currencies(text)
        }

def main():
    extractor = DataExtractor()
    
    # Sample text with the data you provided
    text = """
    Email addresses:
    user@example.com
    firstname.lastname@company.co.uk
    
    URLs:
    https://www.example.com
    https://subdomain.example.org/page
    
    Credit card numbers:
    1234 5678 9012 3456
    1234-5678-9012-3456
    
    HTML tags:
    <p>
    <div class="example">
    <img src="image.jpg" alt="description">
    
    Currency amounts:
    $19.99
    $1,234.56
    """
    
    results = extractor.extract_all(text)
    
    print(" Extracted Data")
    print("=" * 50)
    
    print("\n Emails:")
    for email in results['emails']:
        print(f"  - {email}")
    
    print("\n URLs:")
    for url in results['urls']:
        print(f"  - {url}")
    
    print("\n Credit Cards:")
    for card in results['credit_cards']:
        print(f"  - {card}")
    
    print("\n HTML Tags:")
    for tag in results['html_tags']:
        print(f"  - {tag}")
    
    print("\n Currency Amounts:")
    for currency in results['currencies']:
        print(f"  - {currency}")

if __name__ == "__main__":
    main()