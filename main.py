from sys import path

path.append('..\\Scraping')
path.append('..\\DbInterface')

from Scraping.bleauinfo import *
from DbInterface.seed import * 

bleauinfo_url = "https://bleau.info/areas_by_region"

def main():
    # Run scraping module
    all_sites_links = scrape_sectors(bleauinfo_url)
    all_sites_url = create_sites_url(all_sites_links) 
    result = scrape_sites(all_sites_url) # return all_routes_types, sites_name, all_data
    print(result)

    # Run the insertion into db module
    executeInsertions(result[1], result[0], result[3])
 




if __name__ == "__main__":
    main()