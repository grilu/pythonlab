import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to retrieve the webpage: HTTP {response.status_code}")
        return None

def extract_headlines(soup):
    # Find all div elements with the class 'ui-story-headline'
    headlines = soup.find_all('div', class_='ui-story-headline')
    for headline in headlines:
        # Get the text and href attribute from the anchor tag within the div
        link = headline.find('a')
        if link:
            print("Headline:", link.text.strip())
            print("URL:", 'https://news.sky.com' + link['href'])
            print()  # Print a newline for better readability between entries

def main():
    url = 'https://news.sky.com'
    soup = fetch_and_parse(url)
    if soup:
        extract_headlines(soup)

if __name__ == "__main__":
    main()
