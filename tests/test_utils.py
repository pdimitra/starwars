"""
Title     : TestUtils
Author    : Dimitra Paraskevopoulou
Created   : 06 December 2020
"""

import unittest
import filecmp
import requests_mock
from utils import Utils
from tests.mocked_data import MockedData
import os


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.utils = Utils(file_path='tests/characters.csv')
        self.mocked_data = MockedData()

    def test_sort_by_height(self):
        sorted_characters = self.utils.sort_by_height(self.mocked_data.characters_after_species)
        for i, character in enumerate(sorted_characters[1:]):
            self.assertTrue(int(character["height"]) <= int(sorted_characters[i]["height"]))

    def test_sort_by_height_key_error_exception(self):
        with self.assertRaises(Exception):
            sorted_characters = self.utils.sort_by_height(
                self.mocked_data.characters_without_height)

    def test_output_results(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.utils.output_results(self.mocked_data.characters_after_sorting)
        self.assertTrue(filecmp.cmp(os.path.join(dir_path, 'characters.csv'),
                                    os.path.join(dir_path, 'expected_characters.csv'),
                                    shallow=False))

    def test_output_results_exception(self):
        with self.assertRaises(Exception):
            self.utils.output_results(self.mocked_data.characters[0]["name"])

    @requests_mock.Mocker()
    def test_send_csv(self, m):
        m.post(self.utils.csv_upload_uri, json={}, status_code=200)
        self.utils.send_csv()
        self.assertTrue(m._adapter.called_once)

    @requests_mock.Mocker()
    def test_send_csv_status_raises(self, m):
        m.post(self.utils.csv_upload_uri, json={}, status_code=500)
        with self.assertRaises(Exception):
            self.utils.send_csv()
