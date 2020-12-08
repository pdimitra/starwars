"""
Title     : Utils
Author    : Dimitra Paraskevopoulou
Created   : 06 December 2020
"""

import csv
import logging
import requests
import settings
import os
from pprint import pformat


class Utils:
    """
    This class holds some helper methods
    """

    def __init__(self, file_path: str = ''):
        self.csv_upload_uri = settings.CSV_UPLOAD_URI
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = file_path if file_path != '' else settings.CSV_FILE
        self.__cvc_file_path = os.path.join(dir_path, file_path)

    @staticmethod
    def sort_by_height(characters: list) -> list:
        """
        Method to sort a list of dictionaries by the value of a specific key in the dictionaries
        in descending order
        :param characters: list of dictionaries
        :return: sorted list of dictionaries by height value
        """
        try:
            return sorted(characters, key=lambda k: int(k['height']), reverse=True)
        except Exception as e:
            logging.error(
                f"[{type(e).__name__}] exception occurred with arguments: {e.args!r}.")
            raise e

    def output_results(self, characters: list) -> None:
        """
        Method to dump input data into a csv file
        :param characters: list of dictionaries
        """
        try:
            csvfile = None
            with open(self.__cvc_file_path, 'w', newline='') as csvfile:
                fieldnames = ['name', 'species', 'height', 'appearances']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for row in characters:
                    writer.writerow(row)
        except Exception as e:
            if csvfile is not None:
                csvfile.close()
            logging.error(
                f"[{type(e).__name__}] exception occurred with arguments: {e.args!r}.")
            raise e

    def send_csv(self):
        """
        Upload the csv file to httpbin.org
        :return:
        """
        try:
            with open(self.__cvc_file_path, 'rb') as csvfile:
                r = requests.post(self.csv_upload_uri, files={'file': csvfile})

            r.raise_for_status()

            # The following log is just for visualization of the final step
            logging.info(pformat(r.json()))
        except Exception as e:
            logging.error(
                f"[{type(e).__name__}] exception occurred with arguments: {e.args!r}.")
            raise e
