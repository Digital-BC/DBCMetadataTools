import requests
import csv
import os

#######
#Pulls title and a URL field from the sj API and places in a csv file. Extract only the item types (Categories) you specify
#Verify item presence with a scraper
#Or change to thumbnail_url for image verification scraper

#######




api_url = "SJ API URL"
api_key = "APIKEY
per_page = 100  # Change per_page to your desired value
fields = "title,landing_url"
output_csv = "YOUR LOCAL FOLDER"  # Replace with the actual full path

# Specify the categories you want to retrieve like this - #categories = ["Image", "Newspaper"]
categories = [] 

# Function to retrieve records from the API with specified categories
def fetch_records(page):
    params = {
        'api_key': api_key,
        'per_page': per_page,
        'fields': fields,
        'page': page
    }

    # Add categories to the params if specified
    if categories:
        params['or[category][]'] = categories

    response = requests.get(api_url, params=params)
    data = response.json()

    # Print the entire API response for debugging
    print(data)

    # Adjust this part based on the actual structure of the API response
    if 'search' in data and 'results' in data['search']:
        return data['search']['results']
    else:
        return []

# Function to write records to CSV
def write_to_csv(records):
    with open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Landing_URL'] #swap URL here . . .
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if os.path.getsize(output_csv) == 0:  # Check if the file is empty before writing header
            writer.writeheader()

        for record in records:
            writer.writerow({
                'Title': record.get('title', ''),
                'Landing_URL': record.get('landing_url', '')
            })

# Function to get the total number of results
def get_total_results():
    params = {
        'api_key': api_key,
        'per_page': 1,  # Fetch only one result to get total count
        'fields': fields,
        'page': 1
    }

    # Add categories to the params if specified
    if categories:
        params['or[category][]'] = categories

    response = requests.get(api_url, params=params)
    data = response.json()

    if 'search' in data and 'result_count' in data['search']:
        return data['search']['result_count']
    else:
        return 0

# Fetch records and write to CSV
total_results = get_total_results()
per_page = 100  # Set per_page to the desired value

for page in range(1, (total_results // per_page) + 2):
    records = fetch_records(page)
    write_to_csv(records)

print(f"All records retrieved and stored in {output_csv}")
