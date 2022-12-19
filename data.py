# Trying to get names of all datasets using Discovery API
# Janky af

import requests

# Set the base URL for the Socrata API
base_url = "https://data.austintexas.gov/api/discover/v1"
params = {
    "q": "real estate",
    "limit": 100
}
response = requests.get(base_url + "/find-by-id", params=params)


# Check the status code of the response
if response.status_code == 200:
    # If the request is successful, parse the JSON response
    data = response.json()

    # Iterate through the results and download each dataset
    for result in data["results"]:
        # Get the URL for the dataset
        dataset_url = result["data_url"]

        # Send a request to download the dataset
        dataset_response = requests.get(dataset_url)

        # If the request is successful, save the dataset to a file
        if dataset_response.status_code == 200:
            with open(f"{result['title']}.csv", "w") as f:
                f.write(dataset_response.text)
        else:
            print(f"Error downloading dataset: {result['title']}")
else:
    print("Error searching for datasets")
