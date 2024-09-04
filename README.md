# python-scripts

A collection of Python scripts for various tasks.

## Contents

- [Blog Crawler](#blog-crawler)

## Blog Crawler

This script fetches and extracts text content from a list of blog URLs. It handles rate limiting and retries for failed requests.

### Features

- Fetches blog content from a list of URLs.
- Handles rate limiting by waiting and retrying requests.
- Extracts and saves blog titles and text content.
- Saves the extracted data to a JSON file.

### Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

### Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:

   ```sh
   pip install requests beautifulsoup4
   ```

### Usage

1. Add the blog URLs to the `urls` list in the `blog_crawler.py` script.
2. Run the script:

   ```sh
   python blog_crawler.py
   ```

3. The script will save the extracted data to a `blog_data.json` file in the same directory.

### Script Details

#### `fetch_text_content(url, blog_id, retries=5)`

- Fetches the text content from the given URL.
- Retries the request up to `retries` times if it fails or is rate-limited.
- Returns a dictionary with the blog ID, title, content, and source URL.

#### `main(urls)`

- Iterates over the list of URLs and fetches their content.
- Saves the fetched data to a `blog_data.json` file.

## License

This project is licensed under the MIT License.
