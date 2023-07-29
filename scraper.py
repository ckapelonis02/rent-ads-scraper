import pickle
from bs4 import BeautifulSoup
import requests

xaniwtika_nea = 'https://www.haniotika-nea.gr/aggelies/?aggcat=en_katik_categ#'
filtered_ads_file = 'filtered_ads.pkl'
aggelies_path = 'xaniwtika_nea.html'

try:
	# Send a GET request to fetch the website's HTML content
	response = requests.get(xaniwtika_nea)

	# Raise an exception if the response status code is not 200 (OK)
	response.raise_for_status()

	# Save the HTML content to a file
	with open(aggelies_path, 'w', encoding='utf-8') as file:
		file.write(response.text)

	print(f"Successfully saved the HTML content of {xaniwtika_nea} to {aggelies_path}")

except requests.exceptions.RequestException as e:
	print(f"Error fetching the website: {e}")
except IOError as e:
	print(f"Error writing the file: {e}")

# Load the filtered ads from the pickle file
try:
	with open(filtered_ads_file, 'rb') as file:
		aggelies_old = pickle.load(file)
except FileNotFoundError as e:
	aggelies_old = []

# Read the HTML file
with open(aggelies_path, 'r', encoding='utf-8') as file:
	html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the <li> tags and extract their content
list_items = soup.find_all('li')

aggelies = []
search_word = 'Πληρ.'

# Filter and store the content inside each <li> tag containing the search word
for item in list_items:
	if search_word in item.get_text():
		aggelies.append(item.get_text(strip=False))

# Save the filtered ads using pickle
with open(filtered_ads_file, 'wb') as output_file:
	pickle.dump(aggelies, output_file)

print("Filtered ads have been saved to", filtered_ads_file)

new_ads = [ad for ad in aggelies if ad not in aggelies_old]
print("New aggelies:")
for ad in new_ads:
	print(ad)
