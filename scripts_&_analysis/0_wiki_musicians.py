# This script retrieves the 111 musician names from the Wiki page
# for outsider musicians and saves the list to a .csv.
# This is VERY likely to become DEPRECATED.  There is a hard-coded
# number of alphabetical categories (<26) that this script expects to 
# be in the Wikipedia list, which is specific to this point in time
# (Feb 2022).

# imports
print("Importing bs4...")
from bs4 import BeautifulSoup
print("Importing requests...")
import requests

# get Wiki HTML
url = "https://en.wikipedia.org/wiki/Category:Outsider_musicians"
print("Getting results...")
result = requests.get(url)
print("Completed!\n")

# parse Wiki HTML with bs4
outsiderwiki = BeautifulSoup(result.text, "html.parser")

# find all 111 musician names from the list
musicians = []
# this is tailored to the list at this specific point in time
for item in outsiderwiki.find_all("ul")[1:23]:
    for string in item.strings:
        if string != "\n":
            musicians.append(repr(string))

# save uncleaned list to file
file = open("0_wiki_musicians.txt", "w")
for m in musicians:
    file.write(m.strip("''")+"\n")
file.close()

