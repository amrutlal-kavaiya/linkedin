import pandas as pd
import re

# Read the CSV file
df = pd.read_csv('5dgai-introductions_page_1.csv')

# Function to extract LinkedIn URLs
def extract_linkedin_url(content):
    if isinstance(content, str):
        match = re.search(r'(https?://www\.linkedin\.com/in/[^\s]+)', content)
        return match.group(0) if match else None
    return None

# Extract names and LinkedIn URLs
df['linkedin_url'] = df['content'].apply(extract_linkedin_url)
df_filtered = df[['author.global_name', 'linkedin_url']].dropna()

# Remove duplicates
df_filtered = df_filtered.drop_duplicates()

# Print the results
print(df_filtered)

# Optionally, save the results to a new CSV file
df_filtered.to_csv('extracted_names_and_linkedin_urls.csv', index=False)