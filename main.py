import requests


def fetch_site_content(url: str) -> str:
    """Fetch content from a website."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    url = "https://example.com"
    content = fetch_site_content(url)
    print(content)
