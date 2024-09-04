import os
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random
import json

urls = []  # [Paste the blogs URL here]


def fetch_text_content(url, blog_id, retries=5):
    initial_wait_time = 1  # Initial wait time in seconds
    for attempt in range(retries):
        try:
            print(f"Fetching {url}, attempt {attempt + 1}")
            response = requests.get(url, timeout=10)
            if response.status_code == 429:
                wait_time = initial_wait_time * (2**attempt)
                wait_time += random.uniform(0.5, 1.5)
                print(f"Rate limited. Waiting {wait_time:.2f} seconds before retrying.")
                time.sleep(wait_time)
                continue  # Retry
            if response.status_code != 200:
                return None  # Skip non-200 responses
            response.raise_for_status()  # Raise an HTTPError for bad responses
            soup = BeautifulSoup(response.text, "html.parser")
            blog_title = soup.title.string if soup.title else "No Title"
            text_content = "\n".join(p.get_text(strip=True) for p in soup.find_all("p"))
            return {
                "blog_id": blog_id,
                "blog_title": blog_title,
                "content": text_content,
                "source": url.split("/")[2],
            }
        except requests.RequestException as e:
            print(f"Request error: {e}")
            if attempt < retries - 1:
                wait_time = random.uniform(1, 3)
                print(f"Waiting {wait_time:.2f} seconds before retrying.")
                time.sleep(wait_time)
            else:
                return None  # Skip after retries


def main(urls):
    blog_data = []
    for blog_id, url in enumerate(urls, start=1):
        data = fetch_text_content(url, blog_id)
        if data:  # Only append if data is not None
            blog_data.append(data)

    # Save the data to a file in the same directory
    file_path = os.path.join(os.path.dirname(__file__), "blog_data.json")
    with open(file_path, "w") as f:
        json.dump(blog_data, f, indent=4)


if __name__ == "__main__":
    main(urls)
