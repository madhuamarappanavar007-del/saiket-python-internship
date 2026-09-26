import requests
from bs4 import BeautifulSoup


URL = "https://news.ycombinator.com/"
TIMEOUT = 10
MAX_HEADLINES = 10


def fetch_page(url):
    """Retrieve and return the HTML from a public webpage."""
    try:
        response = requests.get(
            url,
            timeout=TIMEOUT,
            headers={"User-Agent": "Mozilla/5.0 (Educational Web Scraper)"},
        )
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as error:
        print(f"Unable to retrieve the webpage: {error}")
        return None


def extract_headlines(html):
    """Parse HTML and extract headline text."""
    soup = BeautifulSoup(html, "html.parser")

    # Try a few common headline structures in order.
    selectors = [
        ".titleline > a",
        "article h2 a",
        "article h3 a",
        "main h2 a",
        "main h3 a",
    ]

    for selector in selectors:
        elements = soup.select(selector)
        headlines = []

        for element in elements:
            headline = element.get_text(" ", strip=True)
            if headline and headline not in headlines:
                headlines.append(headline)

        if headlines:
            return headlines[:MAX_HEADLINES]

    return []


def main():
    print("===== BASIC WEB SCRAPER =====")
    print(f"Source: {URL}\n")

    html = fetch_page(URL)
    if html is None:
        return

    headlines = extract_headlines(html)

    if not headlines:
        print("No headlines were found on the webpage.")
        return

    print("Headlines:")
    for number, headline in enumerate(headlines, start=1):
        print(f"{number}. {headline}")


if __name__ == "__main__":
    main()
