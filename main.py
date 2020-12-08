"""
Title     : main
Author    : Dimitra Paraskevopoulou
Created   : 06 December 2020
"""
from scraper import StarWarsScraper
from utils import Utils
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    scraper = StarWarsScraper()
    utils = Utils()

    # Get the 10 characters which appear in the most films
    characters, top_appearances = scraper.get_people(scraper.people_uri)

    # Get each character species
    characters = scraper.get_species(characters)

    # Sort the list with the characters per height
    characters = utils.sort_by_height(characters)

    # Output the list of characters to a csv file
    utils.output_results(characters)

    # Send CSV file to httpbin.org
    utils.send_csv()

    logging.info("Exercise was successfully executed!")