import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

base_url = "http://apod.nasa.gov/apod/archivepix.html"
download_directory = "apod_pictures"

to_visit = set ((base_url,))
visited = set()
page_counter = 0

while to_visit:
    #pick a link to visit
    #Visit the link
    current_page = to_visit.pop()
    print("visiting:", current_page)
    visited.add(current_page)
    content = urllib.request.urlopen(current_page).read()
    if page_counter == 10:
        break
    page_counter +=1

    #Extract any new links from the page
    for link in BeautifulSoup(content, "lxml").findAll("a"):
        absolute_link = urljoin(current_page, link["href"])
        if absolute_link not in visited:
            to_visit.add(absolute_link)
        else:
            print("Already Visited:", absolute_link)

    #Download an impages on the page
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(current_page, img["src"])
        print("Downloading image: ", img_href)
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))