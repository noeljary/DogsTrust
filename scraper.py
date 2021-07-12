import csv
import requests

from bs4  import BeautifulSoup
from pync import Notifier

# CSV File
csvfile = "tmp_dogs_list.csv"

# Create Empty Dogs List
dogs_list = []

# Fill List from CSV
with open(csvfile, "r") as f:
	read = csv.reader(f)
	dogs_list = list(read)

# DogsTrust URLS
base = "https://www.dogstrust.org.uk"
new  = "https://www.dogstrust.org.uk/rehoming/"

# Get HTML from Page
page = requests.get(new)

# Parse HTML
soup = BeautifulSoup(page.content, "html.parser")

# Get List of Dogs
dogs = soup.find(id="BodyContent_DogList1_dvMainGrid").section.contents[5].find_all("div", "col-xs-12")

# Loop through Dogs
new_dogs_list = []
for dog in reversed(dogs):
	# Get Dog Information
	name = dog.find("h3").text.strip()
	breed = dog.find("span").text.strip()
	location = dog.find("strong").text.strip()
	link = dog.find("a")["href"].strip()

	# Create List Item for Dog
	dog_list = [name, breed, location, link]

	# Add Dog to List to Overwrite CSV File
	new_dogs_list.append(dog_list)

	# Does Dog exist in current list?
	if dog_list not in dogs_list:
		# If not - must be new
		# Send notification
		Notifier.notify("{}\n{}".format(breed, location), title="DogsTrust: {}".format(name), open="{}{}".format(base, link))	

# Save updated dogs list to CSV
with open(csvfile, "w") as f:
	write = csv.writer(f, quoting=csv.QUOTE_ALL)
	for dog in new_dogs_list:
		write.writerow(dog)



