# OK just gonna scrape through the titles

import requests
from bs4 import BeautifulSoup

# Set the base URL of the Austin data catalog
base_url = "https://data.austintexas.gov/browse"

# Set the number of pages to scroll through
num_pages = 146

# Create an empty list to store the names of the datasets
dataset_names = []

# Iterate through the pages
for page in range(1, num_pages + 1):
    # Send a request to the URL and get the HTML content
    url = f"{base_url}?limitTo=datasets&page={page}"
    html_content = requests.get(url).text

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all elements with the class "browse2-result-name"
    name_tags = soup.find_all(class_="browse2-result-name")

    # Iterate through the name tags and extract the text from each one
    for tag in name_tags:
        dataset_names.append(tag.text)

# Print the list of dataset names
print(dataset_names)

