import requests
from bs4 import BeautifulSoup
from collections import Counter

bleauinfo_url = "https://bleau.info/areas_by_region"

# Final data : 
all_routes_types = set()
sites_name = []
all_data = {}

# Function to get all sites link 
def scrape_sectors(url):
    sites_links = []
    # Send the HTTP GET request to bleau.info
    response = requests.get(url)
    if response.status_code == 200:
            # Parse the html content of the page
            soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8") # ISO-8859-1
            # soup_result = soup.prettify().encode('ISO-8859-1')
            # print(soup_result)
            divs = soup.find_all("div", class_=False)
            for div in divs:
                 # Find all direct/first child <a> elements of each div
                 sites_links.extend(div.find_all('a', recursive=False))
               #   print(sites_links)
                 
            create_sites_url(sites_links)
            
    else:
            print('Failed to fetch bleau.info webstite :', response.status_code)
            return None

# Function to construct url link of each sites     
def create_sites_url(links):
      sites_url = []
      # Retrieve all the href 
      for link in links:
        href = link.get("href")
        if href:
              site_url = "https://bleau.info" + href
              sites_url.append(site_url)
     #  print(sites_url)
     # Iterate over each url link and scrap it 
      for sites in sites_url:
           scrape_site(sites)
      print("ALL ROUTE TYPES :", all_routes_types)
      print("FINAL ALL DATA : ", all_data)


# Function to scrape each sites and retrieve its types
def scrape_site(url):
    routes_types = []
    response = requests.get(url)
    if response.status_code == 200:
         soup = BeautifulSoup(response.content, "html.parser", from_encoding="ISO-8859-1")
         site = soup.h3 # Find the first h3 element
         name = site.text.strip() # Extract the inner text of this h3 element 
         sites_name.append(name) # Store the site name inside global array for later
         types = soup.find_all("span", class_="btype")
         for t in types:
              routes_types.extend(t.text.split(', '))
          #     print(routes_types)

         # Adding the array of all the routes types of a site to a global array for later 
         all_routes_types.update(routes_types)

         # Getting each type and its count for a single site 
         counted_routes_types = count_types(routes_types)

         # Add the site name and its corresponding route type and counts to the dictionary
         all_data[name] = counted_routes_types
         print(all_data)


    else:
        print('Failed to fetch bleau.info webstite :', response.status_code)
        return None 

# Function to get the count of each route type in a site
def count_types(array):
     type_counts = Counter(array)
     top_type = type_counts.most_common()
     # print(top_type)
     return top_type


# scrape_sites('https://bleau.info/cuvier')
scrape_sectors(bleauinfo_url)

# Where am i : 
# I have a script that scrap over all sites references in bleau.info and 
# returns a dictionary where keys are sites names and values are each routes types you can find there and its counted occurrence. 

