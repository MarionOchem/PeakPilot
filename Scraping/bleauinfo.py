import requests
from bs4 import BeautifulSoup
from collections import Counter

bleauinfo_url = "https://bleau.info/areas_by_region"

# Function to get all sites link 
def scrape_sectors(url):
    sites_links = []
    # Send the HTTP GET request to bleau.info
    response = requests.get(url)
    if response.status_code == 200:
            # Parse the html content of the page
            soup = BeautifulSoup(response.content, "html.parser")
            soup_result = soup.prettify().encode('ISO-8859-1')
            # print(soup_result)
            divs = soup.find_all("div", class_=False)
            for div in divs:
                 # Find all direct child <a> elements of each div
                 sites_links.extend(div.find_all('a', recursive=False))
                 
            create_sites_url(sites_links)
            
    else:
            print('Failed to fetch bleau.info webstite :', response.status_code)
            return None

# Function to get all sites data     
def create_sites_url(links):
      sites_url = []
      # Retrieve all the href 
      for link in links:
        href = link.get("href")
        if href:
              site_url = "https://bleau.info" + href
              sites_url.append(site_url)
     #  print(sites_url)
      for sites in sites_url:
           scrape_sites(sites)

def scrape_sites(url):
    all_types = []
    response = requests.get(url)
    if response.status_code == 200:
         soup = BeautifulSoup(response.content, "html.parser", from_encoding="ISO-8859-1")
         types = soup.find_all("span", class_="btype")
     #     print(types)
         for t in types:
              all_types.append(t.text)
     #     print(all_types)
         top_types(all_types)
    else:
        print('Failed to fetch bleau.info webstite :', response.status_code)
        return None 

# Function to get the top 3 of route type in the site
def top_types(array):
     type_counts = Counter(array)
     top_type = type_counts.most_common(3)
     print(top_type)


# scrape_sites('https://bleau.info/cuvier')
scrape_sectors(bleauinfo_url)

# Where am i : 
# I have a script that scrap over all sites references in bleau.info and 
# returns the top 3 type of routes for each site. 

