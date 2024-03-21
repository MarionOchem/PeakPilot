from sys import path

path.append('..\\Scraping')

from Scraping.bleauinfo import *

bleauinfo_url = "https://bleau.info/areas_by_region"

def main():
    # Run scraping 
    # Run db connexion and injection of scrapped data
    
    all_sites_links = scrape_sectors(bleauinfo_url)
    all_sites_url = create_sites_url(all_sites_links)
    result = scrape_sites(all_sites_url)
    print(result)

 







if __name__ == "__main__":
    main()