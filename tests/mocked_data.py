"""
Title     : Mocked Data
Author    : Dimitra Paraskevopoulou
Created   : 06 December 2020
"""


class MockedData:
    def __init__(self):
        self.characters = [
            {'name': 'Luke Skywalker', 'species': [], 'height': '172', 'appearances': 4},
            {'name': 'C-3PO', 'species': ['http://swapi.dev/api/species/2/'],
             'height': '167', 'appearances': 6},
            {'name': 'R2-D2', 'species': ['http://swapi.dev/api/species/2/'],
             'height': '96', 'appearances': 6},
            {'name': 'Darth Vader', 'species': [], 'height': '202', 'appearances': 4},
            {'name': 'Leia Organa', 'species': [], 'height': '150', 'appearances': 4},
            {'name': 'Yoda', 'species': ['http://swapi.dev/api/species/6/'],
             'height': '66', 'appearances': 5},
            {'name': 'Palpatine', 'species': [], 'height': '170', 'appearances': 5},
            {'name': 'Ki-Adi-Mundi', 'species': ['http://swapi.dev/api/species/20/'],
             'height': '198', 'appearances': 3},
            {'name': 'Chewbacca', 'species': ['http://swapi.dev/api/species/3/'],
             'height': '228', 'appearances': 4},
            {'name': 'Obi-Wan Kenobi', 'species': [], 'height': '182', 'appearances': 6}]

        self.characters_after_species = [
            {'name': 'Luke Skywalker', 'species': '', 'height': '172', 'appearances': 4},
            {'name': 'C-3PO', 'species': 'Droid', 'height': '167', 'appearances': 6},
            {'name': 'R2-D2', 'species': 'Droid', 'height': '96', 'appearances': 6},
            {'name': 'Darth Vader', 'species': '', 'height': '202', 'appearances': 4},
            {'name': 'Leia Organa', 'species': '', 'height': '150', 'appearances': 4},
            {'name': 'Yoda', 'species': "Yoda's species", 'height': '66',
             'appearances': 5},
            {'name': 'Palpatine', 'species': '', 'height': '170', 'appearances': 5},
            {'name': 'Ki-Adi-Mundi', 'species': 'Cerean', 'height': '198',
             'appearances': 3},
            {'name': 'Chewbacca', 'species': 'Wookie', 'height': '228',
             'appearances': 4},
            {'name': 'Obi-Wan Kenobi', 'species': '', 'height': '182', 'appearances': 6}]

        self.characters_without_height = [
            {'name': 'Luke Skywalker', 'species': '', 'appearances': 4},
            {'name': 'C-3PO', 'species': 'Droid', 'appearances': 6},
            {'name': 'R2-D2', 'species': 'Droid', 'appearances': 6}]

        self.characters_after_sorting = [
            {'name': 'Chewbacca', 'species': 'Wookie', 'height': '228', 'appearances': 4},
            {'name': 'Darth Vader', 'species': '', 'height': '202', 'appearances': 4},
            {'name': 'Ki-Adi-Mundi', 'species': 'Cerean', 'height': '198', 'appearances': 3},
            {'name': 'Obi-Wan Kenobi', 'species': '', 'height': '182', 'appearances': 6},
            {'name': 'Luke Skywalker', 'species': '', 'height': '172', 'appearances': 4},
            {'name': 'Palpatine', 'species': '', 'height': '170', 'appearances': 5},
            {'name': 'C-3PO', 'species': 'Droid', 'height': '167', 'appearances': 6},
            {'name': 'Leia Organa', 'species': '', 'height': '150', 'appearances': 4},
            {'name': 'R2-D2', 'species': 'Droid', 'height': '96', 'appearances': 6},
            {'name': 'Yoda', 'species': "Yoda's species", 'height': '66', 'appearances': 5}]

        self.expected_characters = [
            {'appearances': 4, 'height': '172', 'name': 'Luke Skywalker', 'species': []},
            {'appearances': 6,
             'height': '167',
             'name': 'C-3PO',
             'species': ['http://swapi.dev/api/species/2/']},
            {'appearances': 6,
             'height': '96',
             'name': 'R2-D2',
             'species': ['http://swapi.dev/api/species/2/']},
            {'appearances': 4, 'height': '202', 'name': 'Darth Vader', 'species': []},
            {'appearances': 4, 'height': '150', 'name': 'Leia Organa', 'species': []},
            {'appearances': 5,
             'height': '66',
             'name': 'Yoda',
             'species': ['http://swapi.dev/api/species/6/']},
            {'appearances': 5, 'height': '170', 'name': 'Palpatine', 'species': []},
            {'appearances': 3,
             'height': '188',
             'name': 'Anakin Skywalker',
             'species': []},
            {'appearances': 4,
             'height': '228',
             'name': 'Chewbacca',
             'species': ['http://swapi.dev/api/species/3/']},
            {'appearances': 6, 'height': '182', 'name': 'Obi-Wan Kenobi', 'species': []}]

        self.expected_top_appearances = [4, 6, 6, 4, 4, 5, 5, 3, 4, 6]

        self.expected_characters_8_results = [
            {'appearances': 4, 'height': '172', 'name': 'Luke Skywalker', 'species': []},
            {'appearances': 6,
             'height': '167',
             'name': 'C-3PO',
             'species': ['http://swapi.dev/api/species/2/']},
            {'appearances': 6,
             'height': '96',
             'name': 'R2-D2',
             'species': ['http://swapi.dev/api/species/2/']},
            {'appearances': 4, 'height': '202', 'name': 'Darth Vader', 'species': []},
            {'appearances': 4, 'height': '150', 'name': 'Leia Organa', 'species': []},
            {'appearances': 3, 'height': '178', 'name': 'Owen Lars', 'species': []},
            {'appearances': 3,
             'height': '165',
             'name': 'Beru Whitesun lars',
             'species': []},
            {'appearances': 1,
             'height': '97',
             'name': 'R5-D4',
             'species': ['http://swapi.dev/api/species/2/']}]

        self.expected_top_appearances_8_results = [4, 6, 6, 4, 4, 3, 3, 1]

    @staticmethod
    def people_page1():
        return """{
            "count": 82,
            "next": "http://swapi.dev/api/people/?page=2",
            "previous": null,
            "results": [
                {
                    "name": "Luke Skywalker",
                    "height": "172",
                    "mass": "77",
                    "hair_color": "blond",
                    "skin_color": "fair",
                    "eye_color": "blue",
                    "birth_year": "19BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/14/",
                        "http://swapi.dev/api/vehicles/30/"
                    ],
                    "starships": [
                        "http://swapi.dev/api/starships/12/",
                        "http://swapi.dev/api/starships/22/"
                    ],
                    "created": "2014-12-09T13:50:51.644000Z",
                    "edited": "2014-12-20T21:17:56.891000Z",
                    "url": "http://swapi.dev/api/people/1/"
                },
                {
                    "name": "C-3PO",
                    "height": "167",
                    "mass": "75",
                    "hair_color": "n/a",
                    "skin_color": "gold",
                    "eye_color": "yellow",
                    "birth_year": "112BBY",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:10:51.357000Z",
                    "edited": "2014-12-20T21:17:50.309000Z",
                    "url": "http://swapi.dev/api/people/2/"
                },
                {
                    "name": "R2-D2",
                    "height": "96",
                    "mass": "32",
                    "hair_color": "n/a",
                    "skin_color": "white, blue",
                    "eye_color": "red",
                    "birth_year": "33BBY",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/8/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:11:50.376000Z",
                    "edited": "2014-12-20T21:17:50.311000Z",
                    "url": "http://swapi.dev/api/people/3/"
                },
                {
                    "name": "Darth Vader",
                    "height": "202",
                    "mass": "136",
                    "hair_color": "none",
                    "skin_color": "white",
                    "eye_color": "yellow",
                    "birth_year": "41.9BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/13/"
                    ],
                    "created": "2014-12-10T15:18:20.704000Z",
                    "edited": "2014-12-20T21:17:50.313000Z",
                    "url": "http://swapi.dev/api/people/4/"
                },
                {
                    "name": "Leia Organa",
                    "height": "150",
                    "mass": "49",
                    "hair_color": "brown",
                    "skin_color": "light",
                    "eye_color": "brown",
                    "birth_year": "19BBY",
                    "gender": "female",
                    "homeworld": "http://swapi.dev/api/planets/2/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/30/"
                    ],
                    "starships": [],
                    "created": "2014-12-10T15:20:09.791000Z",
                    "edited": "2014-12-20T21:17:50.315000Z",
                    "url": "http://swapi.dev/api/people/5/"
                },
                {
                    "name": "Owen Lars",
                    "height": "178",
                    "mass": "120",
                    "hair_color": "brown, grey",
                    "skin_color": "light",
                    "eye_color": "blue",
                    "birth_year": "52BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:52:14.024000Z",
                    "edited": "2014-12-20T21:17:50.317000Z",
                    "url": "http://swapi.dev/api/people/6/"
                },
                {
                    "name": "Beru Whitesun lars",
                    "height": "165",
                    "mass": "75",
                    "hair_color": "brown",
                    "skin_color": "light",
                    "eye_color": "blue",
                    "birth_year": "47BBY",
                    "gender": "female",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:53:41.121000Z",
                    "edited": "2014-12-20T21:17:50.319000Z",
                    "url": "http://swapi.dev/api/people/7/"
                },
                {
                    "name": "R5-D4",
                    "height": "97",
                    "mass": "32",
                    "hair_color": "n/a",
                    "skin_color": "white, red",
                    "eye_color": "red",
                    "birth_year": "unknown",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:57:50.959000Z",
                    "edited": "2014-12-20T21:17:50.321000Z",
                    "url": "http://swapi.dev/api/people/8/"
                },
                {
                    "name": "Biggs Darklighter",
                    "height": "183",
                    "mass": "84",
                    "hair_color": "black",
                    "skin_color": "light",
                    "eye_color": "brown",
                    "birth_year": "24BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/12/"
                    ],
                    "created": "2014-12-10T15:59:50.509000Z",
                    "edited": "2014-12-20T21:17:50.323000Z",
                    "url": "http://swapi.dev/api/people/9/"
                },
                {
                    "name": "Obi-Wan Kenobi",
                    "height": "182",
                    "mass": "77",
                    "hair_color": "auburn, white",
                    "skin_color": "fair",
                    "eye_color": "blue-gray",
                    "birth_year": "57BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/20/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/38/"
                    ],
                    "starships": [
                        "http://swapi.dev/api/starships/48/",
                        "http://swapi.dev/api/starships/59/",
                        "http://swapi.dev/api/starships/64/",
                        "http://swapi.dev/api/starships/65/",
                        "http://swapi.dev/api/starships/74/"
                    ],
                    "created": "2014-12-10T16:16:29.192000Z",
                    "edited": "2014-12-20T21:17:50.325000Z",
                    "url": "http://swapi.dev/api/people/10/"
                }
            ]
        }"""

    @staticmethod
    def people_page2():
        return """{
            "count": 82,
            "next": "http://swapi.dev/api/people/?page=3",
            "previous": "http://swapi.dev/api/people/?page=1",
            "results": [
                {
                    "name": "Anakin Skywalker",
                    "height": "188",
                    "mass": "84",
                    "hair_color": "blond",
                    "skin_color": "fair",
                    "eye_color": "blue",
                    "birth_year": "41.9BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/44/",
                        "http://swapi.dev/api/vehicles/46/"
                    ],
                    "starships": [
                        "http://swapi.dev/api/starships/39/",
                        "http://swapi.dev/api/starships/59/",
                        "http://swapi.dev/api/starships/65/"
                    ],
                    "created": "2014-12-10T16:20:44.310000Z",
                    "edited": "2014-12-20T21:17:50.327000Z",
                    "url": "http://swapi.dev/api/people/11/"
                },
                {
                    "name": "Wilhuff Tarkin",
                    "height": "180",
                    "mass": "unknown",
                    "hair_color": "auburn, grey",
                    "skin_color": "fair",
                    "eye_color": "blue",
                    "birth_year": "64BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/21/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T16:26:56.138000Z",
                    "edited": "2014-12-20T21:17:50.330000Z",
                    "url": "http://swapi.dev/api/people/12/"
                },
                {
                    "name": "Chewbacca",
                    "height": "228",
                    "mass": "112",
                    "hair_color": "brown",
                    "skin_color": "unknown",
                    "eye_color": "blue",
                    "birth_year": "200BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/14/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/3/"
                    ],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/19/"
                    ],
                    "starships": [
                        "http://swapi.dev/api/starships/10/",
                        "http://swapi.dev/api/starships/22/"
                    ],
                    "created": "2014-12-10T16:42:45.066000Z",
                    "edited": "2014-12-20T21:17:50.332000Z",
                    "url": "http://swapi.dev/api/people/13/"
                },
                {
                    "name": "Han Solo",
                    "height": "180",
                    "mass": "80",
                    "hair_color": "brown",
                    "skin_color": "fair",
                    "eye_color": "brown",
                    "birth_year": "29BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/22/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/10/",
                        "http://swapi.dev/api/starships/22/"
                    ],
                    "created": "2014-12-10T16:49:14.582000Z",
                    "edited": "2014-12-20T21:17:50.334000Z",
                    "url": "http://swapi.dev/api/people/14/"
                },
                {
                    "name": "Greedo",
                    "height": "173",
                    "mass": "74",
                    "hair_color": "n/a",
                    "skin_color": "green",
                    "eye_color": "black",
                    "birth_year": "44BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/23/",
                    "films": [
                        "http://swapi.dev/api/films/1/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/4/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T17:03:30.334000Z",
                    "edited": "2014-12-20T21:17:50.336000Z",
                    "url": "http://swapi.dev/api/people/15/"
                },
                {
                    "name": "Jabba Desilijic Tiure",
                    "height": "175",
                    "mass": "1,358",
                    "hair_color": "n/a",
                    "skin_color": "green-tan, brown",
                    "eye_color": "orange",
                    "birth_year": "600BBY",
                    "gender": "hermaphrodite",
                    "homeworld": "http://swapi.dev/api/planets/24/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/5/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T17:11:31.638000Z",
                    "edited": "2014-12-20T21:17:50.338000Z",
                    "url": "http://swapi.dev/api/people/16/"
                },
                {
                    "name": "Wedge Antilles",
                    "height": "170",
                    "mass": "77",
                    "hair_color": "brown",
                    "skin_color": "fair",
                    "eye_color": "hazel",
                    "birth_year": "21BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/22/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/14/"
                    ],
                    "starships": [
                        "http://swapi.dev/api/starships/12/"
                    ],
                    "created": "2014-12-12T11:08:06.469000Z",
                    "edited": "2014-12-20T21:17:50.341000Z",
                    "url": "http://swapi.dev/api/people/18/"
                },
                {
                    "name": "Jek Tono Porkins",
                    "height": "180",
                    "mass": "110",
                    "hair_color": "brown",
                    "skin_color": "fair",
                    "eye_color": "blue",
                    "birth_year": "unknown",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/26/",
                    "films": [
                        "http://swapi.dev/api/films/1/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/12/"
                    ],
                    "created": "2014-12-12T11:16:56.569000Z",
                    "edited": "2014-12-20T21:17:50.343000Z",
                    "url": "http://swapi.dev/api/people/19/"
                },
                {
                    "name": "Yoda",
                    "height": "66",
                    "mass": "17",
                    "hair_color": "white",
                    "skin_color": "green",
                    "eye_color": "brown",
                    "birth_year": "896BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/28/",
                    "films": [
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/6/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-15T12:26:01.042000Z",
                    "edited": "2014-12-20T21:17:50.345000Z",
                    "url": "http://swapi.dev/api/people/20/"
                },
                {
                    "name": "Palpatine",
                    "height": "170",
                    "mass": "75",
                    "hair_color": "grey",
                    "skin_color": "pale",
                    "eye_color": "yellow",
                    "birth_year": "82BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/8/",
                    "films": [
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-15T12:48:05.971000Z",
                    "edited": "2014-12-20T21:17:50.347000Z",
                    "url": "http://swapi.dev/api/people/21/"
                }
            ]
        }"""

    @staticmethod
    def people_page3():
        return """{
            "count": 82,
            "next": null,
            "previous": "http://swapi.dev/api/people/?page=2",
            "results": [
                {
                    "name": "Boba Fett",
                    "height": "183",
                    "mass": "78.2",
                    "hair_color": "black",
                    "skin_color": "fair",
                    "eye_color": "brown",
                    "birth_year": "31.5BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/10/",
                    "films": [
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/5/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/21/"
                    ],
                    "created": "2014-12-15T12:49:32.457000Z",
                    "edited": "2014-12-20T21:17:50.349000Z",
                    "url": "http://swapi.dev/api/people/22/"
                },
                {
                    "name": "IG-88",
                    "height": "200",
                    "mass": "140",
                    "hair_color": "none",
                    "skin_color": "metal",
                    "eye_color": "red",
                    "birth_year": "15BBY",
                    "gender": "none",
                    "homeworld": "http://swapi.dev/api/planets/28/",
                    "films": [
                        "http://swapi.dev/api/films/2/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-15T12:51:10.076000Z",
                    "edited": "2014-12-20T21:17:50.351000Z",
                    "url": "http://swapi.dev/api/people/23/"
                },
                {
                    "name": "Bossk",
                    "height": "190",
                    "mass": "113",
                    "hair_color": "none",
                    "skin_color": "green",
                    "eye_color": "red",
                    "birth_year": "53BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/29/",
                    "films": [
                        "http://swapi.dev/api/films/2/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/7/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-15T12:53:49.297000Z",
                    "edited": "2014-12-20T21:17:50.355000Z",
                    "url": "http://swapi.dev/api/people/24/"
                },
                {
                    "name": "Lando Calrissian",
                    "height": "177",
                    "mass": "79",
                    "hair_color": "black",
                    "skin_color": "dark",
                    "eye_color": "brown",
                    "birth_year": "31BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/30/",
                    "films": [
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/10/"
                    ],
                    "created": "2014-12-15T12:56:32.683000Z",
                    "edited": "2014-12-20T21:17:50.357000Z",
                    "url": "http://swapi.dev/api/people/25/"
                },
                {
                    "name": "Lobot",
                    "height": "175",
                    "mass": "79",
                    "hair_color": "none",
                    "skin_color": "light",
                    "eye_color": "blue",
                    "birth_year": "37BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/6/",
                    "films": [
                        "http://swapi.dev/api/films/2/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-15T13:01:57.178000Z",
                    "edited": "2014-12-20T21:17:50.359000Z",
                    "url": "http://swapi.dev/api/people/26/"
                },
                {
                    "name": "Ackbar",
                    "height": "180",
                    "mass": "83",
                    "hair_color": "none",
                    "skin_color": "brown mottle",
                    "eye_color": "orange",
                    "birth_year": "41BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/31/",
                    "films": [
                        "http://swapi.dev/api/films/3/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/8/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-18T11:07:50.584000Z",
                    "edited": "2014-12-20T21:17:50.362000Z",
                    "url": "http://swapi.dev/api/people/27/"
                },
                {
                    "name": "Mon Mothma",
                    "height": "150",
                    "mass": "unknown",
                    "hair_color": "auburn",
                    "skin_color": "fair",
                    "eye_color": "blue",
                    "birth_year": "48BBY",
                    "gender": "female",
                    "homeworld": "http://swapi.dev/api/planets/32/",
                    "films": [
                        "http://swapi.dev/api/films/3/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-18T11:12:38.895000Z",
                    "edited": "2014-12-20T21:17:50.364000Z",
                    "url": "http://swapi.dev/api/people/28/"
                },
                {
                    "name": "Arvel Crynyd",
                    "height": "unknown",
                    "mass": "unknown",
                    "hair_color": "brown",
                    "skin_color": "fair",
                    "eye_color": "brown",
                    "birth_year": "unknown",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/28/",
                    "films": [
                        "http://swapi.dev/api/films/3/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/28/"
                    ],
                    "created": "2014-12-18T11:16:33.020000Z",
                    "edited": "2014-12-20T21:17:50.367000Z",
                    "url": "http://swapi.dev/api/people/29/"
                },
                {
                    "name": "Wicket Systri Warrick",
                    "height": "88",
                    "mass": "20",
                    "hair_color": "brown",
                    "skin_color": "brown",
                    "eye_color": "brown",
                    "birth_year": "8BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/7/",
                    "films": [
                        "http://swapi.dev/api/films/3/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/9/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-18T11:21:58.954000Z",
                    "edited": "2014-12-20T21:17:50.369000Z",
                    "url": "http://swapi.dev/api/people/30/"
                },
                {
                    "name": "Nien Nunb",
                    "height": "160",
                    "mass": "68",
                    "hair_color": "none",
                    "skin_color": "grey",
                    "eye_color": "black",
                    "birth_year": "unknown",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/33/",
                    "films": [
                        "http://swapi.dev/api/films/3/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/10/"
                    ],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/10/"
                    ],
                    "created": "2014-12-18T11:26:18.541000Z",
                    "edited": "2014-12-20T21:17:50.371000Z",
                    "url": "http://swapi.dev/api/people/31/"
                }
            ]
        }"""

    @staticmethod
    def people_page1_no_next_key():
        return """{
            "count": 82,
            "previous": null,
            "results": [
                {
                    "name": "Luke Skywalker",
                    "height": "172",
                    "mass": "77",
                    "hair_color": "blond",
                    "skin_color": "fair",
                    "eye_color": "blue",
                    "birth_year": "19BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/14/",
                        "http://swapi.dev/api/vehicles/30/"
                    ],
                    "starships": [
                        "http://swapi.dev/api/starships/12/",
                        "http://swapi.dev/api/starships/22/"
                    ],
                    "created": "2014-12-09T13:50:51.644000Z",
                    "edited": "2014-12-20T21:17:56.891000Z",
                    "url": "http://swapi.dev/api/people/1/"
                },
                {
                    "name": "C-3PO",
                    "height": "167",
                    "mass": "75",
                    "hair_color": "n/a",
                    "skin_color": "gold",
                    "eye_color": "yellow",
                    "birth_year": "112BBY",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:10:51.357000Z",
                    "edited": "2014-12-20T21:17:50.309000Z",
                    "url": "http://swapi.dev/api/people/2/"
                },
                {
                    "name": "R2-D2",
                    "height": "96",
                    "mass": "32",
                    "hair_color": "n/a",
                    "skin_color": "white, blue",
                    "eye_color": "red",
                    "birth_year": "33BBY",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/8/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:11:50.376000Z",
                    "edited": "2014-12-20T21:17:50.311000Z",
                    "url": "http://swapi.dev/api/people/3/"
                },
                {
                    "name": "Darth Vader",
                    "height": "202",
                    "mass": "136",
                    "hair_color": "none",
                    "skin_color": "white",
                    "eye_color": "yellow",
                    "birth_year": "41.9BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/13/"
                    ],
                    "created": "2014-12-10T15:18:20.704000Z",
                    "edited": "2014-12-20T21:17:50.313000Z",
                    "url": "http://swapi.dev/api/people/4/"
                },
                {
                    "name": "Leia Organa",
                    "height": "150",
                    "mass": "49",
                    "hair_color": "brown",
                    "skin_color": "light",
                    "eye_color": "brown",
                    "birth_year": "19BBY",
                    "gender": "female",
                    "homeworld": "http://swapi.dev/api/planets/2/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/30/"
                    ],
                    "starships": [],
                    "created": "2014-12-10T15:20:09.791000Z",
                    "edited": "2014-12-20T21:17:50.315000Z",
                    "url": "http://swapi.dev/api/people/5/"
                },
                {
                    "name": "Owen Lars",
                    "height": "178",
                    "mass": "120",
                    "hair_color": "brown, grey",
                    "skin_color": "light",
                    "eye_color": "blue",
                    "birth_year": "52BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:52:14.024000Z",
                    "edited": "2014-12-20T21:17:50.317000Z",
                    "url": "http://swapi.dev/api/people/6/"
                },
                {
                    "name": "Beru Whitesun lars",
                    "height": "165",
                    "mass": "75",
                    "hair_color": "brown",
                    "skin_color": "light",
                    "eye_color": "blue",
                    "birth_year": "47BBY",
                    "gender": "female",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:53:41.121000Z",
                    "edited": "2014-12-20T21:17:50.319000Z",
                    "url": "http://swapi.dev/api/people/7/"
                },
                {
                    "name": "R5-D4",
                    "height": "97",
                    "mass": "32",
                    "hair_color": "n/a",
                    "skin_color": "white, red",
                    "eye_color": "red",
                    "birth_year": "unknown",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:57:50.959000Z",
                    "edited": "2014-12-20T21:17:50.321000Z",
                    "url": "http://swapi.dev/api/people/8/"
                },
                {
                    "name": "Biggs Darklighter",
                    "height": "183",
                    "mass": "84",
                    "hair_color": "black",
                    "skin_color": "light",
                    "eye_color": "brown",
                    "birth_year": "24BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/12/"
                    ],
                    "created": "2014-12-10T15:59:50.509000Z",
                    "edited": "2014-12-20T21:17:50.323000Z",
                    "url": "http://swapi.dev/api/people/9/"
                },
                {
                    "name": "Obi-Wan Kenobi",
                    "height": "182",
                    "mass": "77",
                    "hair_color": "auburn, white",
                    "skin_color": "fair",
                    "eye_color": "blue-gray",
                    "birth_year": "57BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/20/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/38/"
                    ],
                    "starships": [
                        "http://swapi.dev/api/starships/48/",
                        "http://swapi.dev/api/starships/59/",
                        "http://swapi.dev/api/starships/64/",
                        "http://swapi.dev/api/starships/65/",
                        "http://swapi.dev/api/starships/74/"
                    ],
                    "created": "2014-12-10T16:16:29.192000Z",
                    "edited": "2014-12-20T21:17:50.325000Z",
                    "url": "http://swapi.dev/api/people/10/"
                }
            ]
        }"""

    @staticmethod
    def people_page1_no_height_key():
        return """{
            "count": 82,
            "next": "http://swapi.dev/api/people/?page=2",
            "previous": null,
            "results": [
                {
                    "name": "Luke Skywalker",
                    "mass": "77",
                    "hair_color": "blond",
                    "skin_color": "fair",
                    "eye_color": "blue",
                    "birth_year": "19BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/14/",
                        "http://swapi.dev/api/vehicles/30/"
                    ],
                    "starships": [
                        "http://swapi.dev/api/starships/12/",
                        "http://swapi.dev/api/starships/22/"
                    ],
                    "created": "2014-12-09T13:50:51.644000Z",
                    "edited": "2014-12-20T21:17:56.891000Z",
                    "url": "http://swapi.dev/api/people/1/"
                },
                {
                    "name": "C-3PO",
                    "mass": "75",
                    "hair_color": "n/a",
                    "skin_color": "gold",
                    "eye_color": "yellow",
                    "birth_year": "112BBY",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:10:51.357000Z",
                    "edited": "2014-12-20T21:17:50.309000Z",
                    "url": "http://swapi.dev/api/people/2/"
                },
                {
                    "name": "R2-D2",
                    "mass": "32",
                    "hair_color": "n/a",
                    "skin_color": "white, blue",
                    "eye_color": "red",
                    "birth_year": "33BBY",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/8/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:11:50.376000Z",
                    "edited": "2014-12-20T21:17:50.311000Z",
                    "url": "http://swapi.dev/api/people/3/"
                },
                {
                    "name": "Darth Vader",
                    "mass": "136",
                    "hair_color": "none",
                    "skin_color": "white",
                    "eye_color": "yellow",
                    "birth_year": "41.9BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/13/"
                    ],
                    "created": "2014-12-10T15:18:20.704000Z",
                    "edited": "2014-12-20T21:17:50.313000Z",
                    "url": "http://swapi.dev/api/people/4/"
                },
                {
                    "name": "Leia Organa",
                    "mass": "49",
                    "hair_color": "brown",
                    "skin_color": "light",
                    "eye_color": "brown",
                    "birth_year": "19BBY",
                    "gender": "female",
                    "homeworld": "http://swapi.dev/api/planets/2/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/30/"
                    ],
                    "starships": [],
                    "created": "2014-12-10T15:20:09.791000Z",
                    "edited": "2014-12-20T21:17:50.315000Z",
                    "url": "http://swapi.dev/api/people/5/"
                },
                {
                    "name": "Owen Lars",
                    "mass": "120",
                    "hair_color": "brown, grey",
                    "skin_color": "light",
                    "eye_color": "blue",
                    "birth_year": "52BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:52:14.024000Z",
                    "edited": "2014-12-20T21:17:50.317000Z",
                    "url": "http://swapi.dev/api/people/6/"
                },
                {
                    "name": "Beru Whitesun lars",
                    "mass": "75",
                    "hair_color": "brown",
                    "skin_color": "light",
                    "eye_color": "blue",
                    "birth_year": "47BBY",
                    "gender": "female",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:53:41.121000Z",
                    "edited": "2014-12-20T21:17:50.319000Z",
                    "url": "http://swapi.dev/api/people/7/"
                },
                {
                    "name": "R5-D4",
                    "mass": "32",
                    "hair_color": "n/a",
                    "skin_color": "white, red",
                    "eye_color": "red",
                    "birth_year": "unknown",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:57:50.959000Z",
                    "edited": "2014-12-20T21:17:50.321000Z",
                    "url": "http://swapi.dev/api/people/8/"
                },
                {
                    "name": "Biggs Darklighter",
                    "mass": "84",
                    "hair_color": "black",
                    "skin_color": "light",
                    "eye_color": "brown",
                    "birth_year": "24BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/12/"
                    ],
                    "created": "2014-12-10T15:59:50.509000Z",
                    "edited": "2014-12-20T21:17:50.323000Z",
                    "url": "http://swapi.dev/api/people/9/"
                },
                {
                    "name": "Obi-Wan Kenobi",
                    "mass": "77",
                    "hair_color": "auburn, white",
                    "skin_color": "fair",
                    "eye_color": "blue-gray",
                    "birth_year": "57BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/20/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/38/"
                    ],
                    "starships": [
                        "http://swapi.dev/api/starships/48/",
                        "http://swapi.dev/api/starships/59/",
                        "http://swapi.dev/api/starships/64/",
                        "http://swapi.dev/api/starships/65/",
                        "http://swapi.dev/api/starships/74/"
                    ],
                    "created": "2014-12-10T16:16:29.192000Z",
                    "edited": "2014-12-20T21:17:50.325000Z",
                    "url": "http://swapi.dev/api/people/10/"
                }
            ]
        }"""

    @staticmethod
    def people_page1_8_results():
        return """{
            "count": 8,
            "next": null,
            "previous": null,
            "results": [
                {
                    "name": "Luke Skywalker",
                    "height": "172",
                    "mass": "77",
                    "hair_color": "blond",
                    "skin_color": "fair",
                    "eye_color": "blue",
                    "birth_year": "19BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/14/",
                        "http://swapi.dev/api/vehicles/30/"
                    ],
                    "starships": [
                        "http://swapi.dev/api/starships/12/",
                        "http://swapi.dev/api/starships/22/"
                    ],
                    "created": "2014-12-09T13:50:51.644000Z",
                    "edited": "2014-12-20T21:17:56.891000Z",
                    "url": "http://swapi.dev/api/people/1/"
                },
                {
                    "name": "C-3PO",
                    "height": "167",
                    "mass": "75",
                    "hair_color": "n/a",
                    "skin_color": "gold",
                    "eye_color": "yellow",
                    "birth_year": "112BBY",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:10:51.357000Z",
                    "edited": "2014-12-20T21:17:50.309000Z",
                    "url": "http://swapi.dev/api/people/2/"
                },
                {
                    "name": "R2-D2",
                    "height": "96",
                    "mass": "32",
                    "hair_color": "n/a",
                    "skin_color": "white, blue",
                    "eye_color": "red",
                    "birth_year": "33BBY",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/8/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/4/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:11:50.376000Z",
                    "edited": "2014-12-20T21:17:50.311000Z",
                    "url": "http://swapi.dev/api/people/3/"
                },
                {
                    "name": "Darth Vader",
                    "height": "202",
                    "mass": "136",
                    "hair_color": "none",
                    "skin_color": "white",
                    "eye_color": "yellow",
                    "birth_year": "41.9BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [
                        "http://swapi.dev/api/starships/13/"
                    ],
                    "created": "2014-12-10T15:18:20.704000Z",
                    "edited": "2014-12-20T21:17:50.313000Z",
                    "url": "http://swapi.dev/api/people/4/"
                },
                {
                    "name": "Leia Organa",
                    "height": "150",
                    "mass": "49",
                    "hair_color": "brown",
                    "skin_color": "light",
                    "eye_color": "brown",
                    "birth_year": "19BBY",
                    "gender": "female",
                    "homeworld": "http://swapi.dev/api/planets/2/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/2/",
                        "http://swapi.dev/api/films/3/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [
                        "http://swapi.dev/api/vehicles/30/"
                    ],
                    "starships": [],
                    "created": "2014-12-10T15:20:09.791000Z",
                    "edited": "2014-12-20T21:17:50.315000Z",
                    "url": "http://swapi.dev/api/people/5/"
                },
                {
                    "name": "Owen Lars",
                    "height": "178",
                    "mass": "120",
                    "hair_color": "brown, grey",
                    "skin_color": "light",
                    "eye_color": "blue",
                    "birth_year": "52BBY",
                    "gender": "male",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:52:14.024000Z",
                    "edited": "2014-12-20T21:17:50.317000Z",
                    "url": "http://swapi.dev/api/people/6/"
                },
                {
                    "name": "Beru Whitesun lars",
                    "height": "165",
                    "mass": "75",
                    "hair_color": "brown",
                    "skin_color": "light",
                    "eye_color": "blue",
                    "birth_year": "47BBY",
                    "gender": "female",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/",
                        "http://swapi.dev/api/films/5/",
                        "http://swapi.dev/api/films/6/"
                    ],
                    "species": [],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:53:41.121000Z",
                    "edited": "2014-12-20T21:17:50.319000Z",
                    "url": "http://swapi.dev/api/people/7/"
                },
                {
                    "name": "R5-D4",
                    "height": "97",
                    "mass": "32",
                    "hair_color": "n/a",
                    "skin_color": "white, red",
                    "eye_color": "red",
                    "birth_year": "unknown",
                    "gender": "n/a",
                    "homeworld": "http://swapi.dev/api/planets/1/",
                    "films": [
                        "http://swapi.dev/api/films/1/"
                    ],
                    "species": [
                        "http://swapi.dev/api/species/2/"
                    ],
                    "vehicles": [],
                    "starships": [],
                    "created": "2014-12-10T15:57:50.959000Z",
                    "edited": "2014-12-20T21:17:50.321000Z",
                    "url": "http://swapi.dev/api/people/8/"
                }
            ]
        }"""

    @staticmethod
    def species_2():
        return """{
            "name": "Droid",
            "classification": "artificial",
            "designation": "sentient",
            "average_height": "n/a",
            "skin_colors": "n/a",
            "hair_colors": "n/a",
            "eye_colors": "n/a",
            "average_lifespan": "indefinite",
            "homeworld": null,
            "language": "n/a",
            "people": [
                "http://swapi.dev/api/people/2/",
                "http://swapi.dev/api/people/3/",
                "http://swapi.dev/api/people/8/",
                "http://swapi.dev/api/people/23/"
            ],
            "films": [
                "http://swapi.dev/api/films/1/",
                "http://swapi.dev/api/films/2/",
                "http://swapi.dev/api/films/3/",
                "http://swapi.dev/api/films/4/",
                "http://swapi.dev/api/films/5/",
                "http://swapi.dev/api/films/6/"
            ],
            "created": "2014-12-10T15:16:16.259000Z",
            "edited": "2014-12-20T21:36:42.139000Z",
            "url": "http://swapi.dev/api/species/2/"
        }"""

    @staticmethod
    def species_3():
        return """{
            "name": "Wookie",
            "classification": "mammal",
            "designation": "sentient",
            "average_height": "210",
            "skin_colors": "gray",
            "hair_colors": "black, brown",
            "eye_colors": "blue, green, yellow, brown, golden, red",
            "average_lifespan": "400",
            "homeworld": "http://swapi.dev/api/planets/14/",
            "language": "Shyriiwook",
            "people": [
                "http://swapi.dev/api/people/13/",
                "http://swapi.dev/api/people/80/"
            ],
            "films": [
                "http://swapi.dev/api/films/1/",
                "http://swapi.dev/api/films/2/",
                "http://swapi.dev/api/films/3/",
                "http://swapi.dev/api/films/6/"
            ],
            "created": "2014-12-10T16:44:31.486000Z",
            "edited": "2014-12-20T21:36:42.142000Z",
            "url": "http://swapi.dev/api/species/3/"
        }"""

    @staticmethod
    def species_6():
        return """{
            "name": "Yoda's species",
            "classification": "mammal",
            "designation": "sentient",
            "average_height": "66",
            "skin_colors": "green, yellow",
            "hair_colors": "brown, white",
            "eye_colors": "brown, green, yellow",
            "average_lifespan": "900",
            "homeworld": "http://swapi.dev/api/planets/28/",
            "language": "Galactic basic",
            "people": [
                "http://swapi.dev/api/people/20/"
            ],
            "films": [
                "http://swapi.dev/api/films/2/",
                "http://swapi.dev/api/films/3/",
                "http://swapi.dev/api/films/4/",
                "http://swapi.dev/api/films/5/",
                "http://swapi.dev/api/films/6/"
            ],
            "created": "2014-12-15T12:27:22.877000Z",
            "edited": "2014-12-20T21:36:42.148000Z",
            "url": "http://swapi.dev/api/species/6/"
        }"""

    @staticmethod
    def species_20():
        return """{
            "name": "Cerean",
            "classification": "mammal",
            "designation": "sentient",
            "average_height": "200",
            "skin_colors": "pale pink",
            "hair_colors": "red, blond, black, white",
            "eye_colors": "hazel",
            "average_lifespan": "unknown",
            "homeworld": "http://swapi.dev/api/planets/43/",
            "language": "Cerean",
            "people": [
                "http://swapi.dev/api/people/52/"
            ],
            "films": [
                "http://swapi.dev/api/films/4/",
                "http://swapi.dev/api/films/6/"
            ],
            "created": "2014-12-20T10:15:33.765000Z",
            "edited": "2014-12-20T21:36:42.179000Z",
            "url": "http://swapi.dev/api/species/20/"
        }"""
