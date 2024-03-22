import requests
from bs4 import BeautifulSoup
from collections import Counter
from unidecode import unidecode
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# TODO: try except catch instead of if/else
# TODO: handle encoding exception for character "É" and others
# TODO: fichier test : bleauinfo_test.py import bleauinfo.py function and test it 


# Function to get all sites link 
def scrape_sectors(url):
    logger.info('Starting scrape_sectors -- scraping href')
    sites_links = []
    # Send the HTTP GET request to bleau.info
    response = requests.get(url)
    if response.status_code == 200:
            # Parse the html content of the page
            soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8") # ISO-8859-1
            # Get all div that don't have any CSS class 
            divs = soup.find_all("div", class_=False)
            for div in divs:
                 # Find all direct/first child <a> elements of each div found
                 sites_links.extend(div.find_all('a', recursive=False))
            return sites_links
            
    else:
            logger.error('Failed to fetch bleau.info webstite :', response.status_code)
            return None

# Function to construct url link of each sites     
def create_sites_url(links):
      logger.info('Starting create_sites_url -- creating urls')
      sites_url = []
      # Retrieve all the href 
      for link in links:
        href = link.get("href")
        if href:
              site_url = "https://bleau.info" + href
              sites_url.append(site_url)

      return sites_url


# Function to scrape each sites and retrieve its types
def scrape_sites(urls):
    logger.info('Starting scrape_sites -- main scrap')
    all_routes_types = set()
    sites_name = []
    all_data = {}

    for url in urls:
        routes_types = []
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
            site = soup.h3  # Find the first h3 element
            name = site.text.strip()  # Extract the inner text of this h3 element
            encodedName = unidecode(name) # encode string to avoid encoding exception
            sites_name.append(encodedName)  # Store the site name inside global array for later
            
            types = soup.find_all("span", class_="btype")
            for t in types:
                split_types = t.text.split(', ')
                for st in split_types:
                    routes_types.append(unidecode(st))  # encode string to avoid encoding exception

            # Adding the array of all the routes types of a site to a global array for later 
            all_routes_types.update(routes_types)

            # Getting each type and its count for a single site 
            counted_routes_types = count_types(routes_types)

            # Add the site name and its corresponding route type and counts to the dictionary
            all_data[encodedName] = counted_routes_types

        else:
            logger.error('Failed to fetch bleau.info webstite :', response.status_code)
            return None 
        
    return all_routes_types, sites_name, all_data


# Function to get the count of each route type in a site
def count_types(array):
     return Counter(array).most_common()

