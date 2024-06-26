import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import random

#checks thumbs using urls pulled from SJ API via api2csv-c.py (or elsewhere)
#save to file every 100 records (set wit sleep below)
#run with a vpn


# Function to check if an image is present based on URL
def check_image_presence(url):
    try:
        # Send a GET request to retrieve the content
        response = requests.get(url)

        # Check if the status code is 200
        if response.status_code == 200:
            # Check the transfer size.  (UBC ~2 * 1024)
            if len(response.content) > 9 * 1024:  
                return "Image is present."
            else:
                return "Image is not present. Transfer size is less than 10 KB."
        else:
            return f"Image is not present. Status Code: {response.status_code}"

    except requests.RequestException as e:
        return f"Error: {e}"

input_csv_path = "CSV PATH"
output_csv_path = "CSV PATH"


# Set a user agent string to mimic a browser visit
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"


# Read the CSV into a DataFrame
df = pd.read_csv(input_csv_path)

# Add a new column for check messages
df['Check Message'] = ""

# Iterate over the rows and check each URL
for index, row in df.iterrows():
    url = row['Thumbnail_URL']
    print(f"Checking URL {index + 1}/{len(df)}: {url}")
    check_message = check_image_presence(url)
    df.at[index, 'Check Message'] = check_message
    print(f"Check Result: {check_message}")

    # Introduce a sleep after each check
    
    #time.sleep(5)
    time.sleep(random.uniform(2, 5)) # a random sleep between 2-5 secs . . . 


    # Check if 100 records have been processed and introduce a random sleep
    if (index + 1) % 100 == 0:
        random_sleep = random.uniform(5, 15)
        print(f"Sleeping for {random_sleep:.2f} seconds after processing 100 records.")
        time.sleep(random_sleep)

    # Save the DataFrame with check messages to a new CSV file after each iteration
    df.to_csv(output_csv_path, index=False)

# Save the final DataFrame with check messages to a new CSV file
df.to_csv(output_csv_path, index=False)

print(f"Check messages have been written to {output_csv_path}")

