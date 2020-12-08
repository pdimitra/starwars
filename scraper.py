"""
Title     : StarWarsScraper
Author    : Dimitra Paraskevopoulou
Created   : 06 December 2020
"""

import logging
from typing import Tuple
import settings

import requests


class StarWarsScraper:
    """
    This class holds all the required methods for retrieving and parsing data from the starwars API
    and methods for implementing the exercise relevant steps
    """

    def __init__(self, results_to_output: int = 0) -> None:
        self.__results_to_output = results_to_output if results_to_output != 0 else \
            settings.TOP_HEIGHT_NUMBER
        self.people_uri = f"{settings.STARWARS_API_URI}/people/"

    @staticmethod
    def __get_api_data(uri: str) -> dict:
        """
        Method to fetch the data from the starwars api
        :param uri: string uri from which to fetch the data
        :return: json api response parsed in a python dict
        """
        try:
            r = requests.get(uri)
            r.raise_for_status()
            r = r.json()
            return r
        except Exception as e:
            logging.error(
                f"[{type(e).__name__}] exception occurred with arguments: {e.args!r}.")
            raise e

    def get_people(self, uri: str, characters: list = [],
                   top_appearances: list = []) -> Tuple[list, list]:
        """
        Method to fetch all people (characters) from the https://swapi.dev/api/people/
        This is a recursive method since the data includes pagination, while there is a next
        page, the method is getting called again until all results are fetched
        :param uri: string uri from which to fetch the data
        :param characters: the list where the dictionaries with the fetched data are accumulated
         (max size 10 dictionaries in the specific implementation)
        :param top_appearances: a list of size 10, which holds the number of appearances in films
        of each character in the characters list. This list is used for implementing an algorithm
        for a more optimal and performant solution, than having to sort a big list of dictionaries
        of potential unknown size (in the specific api it would have been a list with 82
        dictionaries)
        :return: 2 lists, the characters and the top_appearances
        """

        try:
            api_response = self.__get_api_data(uri=uri)

            characters, top_appearances = self.__parse_people(api_response, characters,
                                                              top_appearances)

            while api_response["next"] is not None:
                characters, top_appearances = self.get_people(uri=api_response["next"],
                                                              characters=characters,
                                                              top_appearances=top_appearances)
                return characters, top_appearances

            return characters, top_appearances
        except Exception as e:
            logging.error(
                f"[{type(e).__name__}] exception occurred with arguments: {e.args!r}.")
            raise e

    def __parse_people(self, api_response: dict, characters: list, top_appearances: list) -> Tuple[
        list, list]:
        """
        This method implements an algorithm for making sure the output will consist of only the 10
        characters with the most appearances in films. In addition when 2 characters with the same
        number of appearances are competing of which will be in the list, I decided to use the
        'height' as a decision factor and to insert the one with the highest height. The indexes of
        both characters and top_appearances lists are in sync, so that they addressing mapped
        entries in both. The reason I decided to implement such an algorithm is for memory
        optimization (no reason to store 82 dicts in a list) and for making the sorting on a small
        list on the next steps much more efficient.
        The algorithm works as follows:
        1. In the first iteration that both characters and top_appearances are empty, they are
            getting filled with the first 10 results return from the first page of results
        2. In the next iterations both characters and top_appearances are always having 10 elements
            As we want only the characters with most appearances in our list, I am checking if the
            number of the films the current character has played is greater than the minimum
            number in the list top_appearances.
            If the number is smaller, the current character is skipped from further processing
            if the number of films is equal to the minimum, then the height of the corresponding
            character is compared with the height of the current character
                if the height of the current character is higher, then the current character
                replaces the one with the equal number or appearances in both lists
                if the height of the current character is less or equal then the current character
                is skipped from further processing
            if the number of films is greater, he current character
                replaces the one with the minimum number or appearances in both lists
        :param api_response: dictionary response of the starwars /people/ endpoint
        :param characters: the list where the dictionaries with the fetched data are accumulated
         (max size 10 dictionaries in the specific implementation)
        :param top_appearances: a list of size 10, which holds the number of appearances in films
        of each character in the characters list. This list is used for implementing an algorithm
        for a more optimal and performant solution, than having to sort a big list of dictionaries
        of potential unknown size (in the specific api it would have been a list with 82
        dictionaries)
        :return: 2 lists, the characters and the top_appearances
        """
        try:
            for people in api_response["results"]:

                num_of_films = len(people["films"])
                if len(top_appearances) == self.__results_to_output:

                    min_appearances = min(top_appearances)

                    if num_of_films < min_appearances:
                        continue
                    elif num_of_films == min_appearances:
                        min_appearances_index = top_appearances.index(min_appearances)
                        if int(characters[min_appearances_index]["height"]) >= int(
                                people["height"]):
                            continue
                        else:
                            top_appearances[min_appearances_index] = num_of_films
                            characters[min_appearances_index] = {"name": people["name"],
                                                                 "species": people["species"],
                                                                 "height": people["height"],
                                                                 "appearances": num_of_films}
                            continue
                    else:
                        min_appearances_index = top_appearances.index(min_appearances)
                        top_appearances[min_appearances_index] = num_of_films
                        characters[min_appearances_index] = {"name": people["name"],
                                                             "species": people["species"],
                                                             "height": people["height"],
                                                             "appearances": num_of_films}
                        continue

                characters.append({"name": people["name"], "species": people["species"],
                                   "height": people["height"], "appearances": num_of_films})
                top_appearances.append(num_of_films)
            return characters, top_appearances
        except Exception as e:
            logging.error(
                f"[{type(e).__name__}] exception occurred with arguments: {e.args!r}.")
            raise e

    def get_species(self, characters: list) -> list:
        """
        Method to fetch the species name for each character
        By analyzing the data from the API the species value is always of list type. Even though
        I didn't find any occurrence of more than one value in the list, I decided to implement
        a for loop just for being sure that also a case of multiple values would be covered.
        In case of multiple values I decided to concatenate the names of species returned with a
        space in between for making it possible to be on the same column of the scv file.
        :param characters: list of 10 dicts with the 10 characters appear in the most films
        :return: the characters list
        """
        try:
            for people in characters:
                name = ""
                if people["species"]:
                    for species_uri in people["species"]:
                        name = " ".join([self.__get_api_data(species_uri)["name"], name])
                    name = name.strip()
                people["species"] = name
            return characters
        except Exception as e:
            logging.error(
                f"[{type(e).__name__}] exception occurred with arguments: {e.args!r}.")
            raise e
