import requests
from bs4 import BeautifulSoup
import time
#html parsing

target_url = "https://atilsamancioglu.com"
foundLinks = []
screenshots = []
def make_request(url):
    response = requests.get(url)
    links1 = BeautifulSoup(response.text, "html.parser")
    #html.parser is the identification that we're using this code for html
    return links1

def crawl(url):
    links = make_request(url)
    for link in links.find_all("a"):
        found_link = link.get("href")
        if found_link:
            if "#" in found_link:
                found_link = found_link.split("#")[0]
            if "Screenshot" in found_link:
                screenshots.append(found_link)
            elif "Screen-Shot" in found_link:
                screenshots.append(found_link)
            elif ".png" in found_link:
                screenshots.append(found_link)
            elif "jpeg." in found_link:
                screenshots.append(found_link)
            else:
                if target_url in found_link and found_link not in foundLinks:
                    foundLinks.append(found_link)
                    print(found_link)
                    crawl(found_link) #recursive func.
st = time.time()
crawl(target_url)
print(foundLinks)
print(screenshots)
et = time.time()
Execution_time = et - st
print(f"Execution Time: {Execution_time} seconds")


