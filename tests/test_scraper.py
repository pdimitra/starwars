"""
Title     : TestStarWarsScraper
Author    : Dimitra Paraskevopoulou
Created   : 06 December 2020
"""

import unittest
import requests_mock
import settings
from scraper import StarWarsScraper
from tests.mocked_data import MockedData


class TestStarWarsScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = StarWarsScraper()
        self.mocked_data = MockedData()

    @requests_mock.Mocker()
    def test_get_people(self, m):
        m.get(f"{settings.STARWARS_API_URI}/people/", text=self.mocked_data.people_page1(),
              status_code=200)
        m.get(f"{settings.STARWARS_API_URI}/people/?page=2", text=self.mocked_data.people_page2(),
              status_code=200)
        m.get(f"{settings.STARWARS_API_URI}/people/?page=3", text=self.mocked_data.people_page3(),
              status_code=200)
        characters, top_appearances = self.scraper.get_people(self.scraper.people_uri, [], [])
        self.assertEqual(self.mocked_data.expected_characters, characters)
        self.assertEqual(self.mocked_data.expected_top_appearances, top_appearances)

    @requests_mock.Mocker()
    def test_get_people_api_count_8(self, m8):
        m8.get(f"{settings.STARWARS_API_URI}/people/",
               text=self.mocked_data.people_page1_8_results(), status_code=200)
        characters, top_appearances = self.scraper.get_people(self.scraper.people_uri, [], [])
        self.assertEqual(self.mocked_data.expected_characters_8_results, characters)
        self.assertEqual(self.mocked_data.expected_top_appearances_8_results, top_appearances)

    @requests_mock.Mocker()
    def test_get_people_exception_bad_status_code(self, m):
        m.get(f"{settings.STARWARS_API_URI}/people/", text=self.mocked_data.people_page1(),
              status_code=500)
        with self.assertRaises(Exception):
            characters, top_appearances = self.scraper.get_people(self.scraper.people_uri)

    @requests_mock.Mocker()
    def test_get_people_exception_on_missing_next_keyword(self, m):
        m.get(f"{settings.STARWARS_API_URI}/people/",
              text=self.mocked_data.people_page1_no_next_key(),
              status_code=200)
        with self.assertRaises(Exception):
            characters, top_appearances = self.scraper.get_people(self.scraper.people_uri)

    @requests_mock.Mocker()
    def test_get_people_exception_on_missing_height_keyword(self, m):
        m.get(f"{settings.STARWARS_API_URI}/people/",
              text=self.mocked_data.people_page1_no_height_key(),
              status_code=200)
        with self.assertRaises(Exception):
            characters, top_appearances = self.scraper.get_people(self.scraper.people_uri)

    @requests_mock.Mocker()
    def test_get_species(self, m):
        m.get(f"{settings.STARWARS_API_URI}/species/2/", text=self.mocked_data.species_2(),
              status_code=200)
        m.get(f"{settings.STARWARS_API_URI}/species/3/", text=self.mocked_data.species_3(),
              status_code=200)
        m.get(f"{settings.STARWARS_API_URI}/species/6/", text=self.mocked_data.species_6(),
              status_code=200)
        m.get(f"{settings.STARWARS_API_URI}/species/20/", text=self.mocked_data.species_20(),
              status_code=200)

        characters = self.scraper.get_species(self.mocked_data.characters)
        self.assertEqual(characters, self.mocked_data.characters_after_species)

    @requests_mock.Mocker()
    def test_get_species_exception_bad_status_code(self, m):
        m.get(f"{settings.STARWARS_API_URI}/species/2/", text=self.mocked_data.species_2(),
              status_code=403)
        with self.assertRaises(Exception):
            characters = self.scraper.get_species(self.mocked_data.characters)

    @requests_mock.Mocker()
    def test_get_species_exception_response_data_no_name(self, m):
        m.get(f"{settings.STARWARS_API_URI}/species/2/", text="""{"fake data":"test"}""",
              status_code=200)
        with self.assertRaises(Exception):
            characters = self.scraper.get_species(self.mocked_data.characters)
