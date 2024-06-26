import requests
import csv
import os

#######
#pulls all records a fields from the SJ API, for analysis in a csv
######




api_url = "YOUR API URL"
api_key = "YOUR API KEY"
per_page = 100  # Change per_page to your desired value
#these are all our fields in DBC
fields = "record_id, internal_identifier, title, description, display_collection, category, creator, display_date, publisher, subject, language, rights, partner, notes, statement_of_harm, locations, preview_image_url, full_image_url, thumbnail_url, source_url, landing_url, status, datetime"


output_csv = "OUTPUT PATH"  # Replace with the actual full path

# Specify the categories you want to retrieve. [] for all or categories = ["Image", "Newspaper"]
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
        fieldnames = ['record_id', 'internal_identifier', 'title', 'description', 'display_collection', 'category', 'creator', 'display_date', 'publisher', 'subject', 'language', 'rights', 'partner', 'notes', 'statement_of_harm', 'locations', 'preview_image_url', 'full_image_url', 'thumbnail_url', 'source_url', 'landing_url', 'status', 'datetime']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if os.path.getsize(output_csv) == 0:  # Check if the file is empty before writing header
            writer.writeheader()

        for record in records:
            writer.writerow({
            'record_id': record.get('record_id', ''), 
            'internal_identifier': record.get('internal_identifier', ''), 
            'title': record.get('title', ''), 
            'description': record.get('description', ''), 
            'display_collection': record.get('display_collection', ''), 
            'category': record.get('category', ''), 
            'creator': record.get('creator', ''), 
            'display_date': record.get('dsiplay_date', ''), 
            'publisher': record.get('publisher', ''), 
            'subject': record.get('subject', ''), 
            'language': record.get('language', ''), 
            'rights': record.get('rights', ''), 
            'partner': record.get('partner', ''), 
            'notes': record.get('notes', ''), 
            'statement_of_harm': record.get('statement_of_harm', ''), 
            'locations': record.get('locations', ''), 
            'preview_image_url': record.get('preview_image_url', ''), 
            'full_image_url': record.get('full_image_url', ''), 
            'thumbnail_url': record.get('thumbnail_url', ''), 
            'source_url': record.get('source_url', ''), 
            'landing_url': record.get('landing_url', ''), 
            'status': record.get('status', ''), 
            'datetime': record.get('datetime', '')
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
