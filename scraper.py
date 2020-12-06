import csv
import requests


# TODO add try/catch, types, comments , pylint etc, logs
# MAke 10 a parameter or constant?/ tests

# try/ catch
def get_species(uri):
    r = requests.get(uri)
    r = r.json()
    return r["name"]


def get_people_optimal(uri='https://swapi.dev/api/people/', results=[], appears=[]):
    r = requests.get(uri)
    r = r.json()
    for people in r["results"]:
        if len(appears) == 10:
            min_appearances = min(appears)
            if len(people["films"]) < min_appearances:
                continue
            elif len(people["films"]) == min_appearances:
                min_appearances_index = appears.index(min_appearances)
                if int(results[min_appearances_index]["height"]) >= int(people["height"]):
                    continue
                else:
                    appears[min_appearances_index] = len(people["films"])
                    results[min_appearances_index] = {"name": people["name"],
                                                      "species": people["species"],
                                                      "height": people["height"],
                                                      "appearances": len(people["films"])}
                    continue
            else:
                min_appearances_index = appears.index(min_appearances)
                appears[min_appearances_index] = len(people["films"])
                results[min_appearances_index] = {"name": people["name"],
                                                  "species": people["species"],
                                                  "height": people["height"],
                                                  "appearances": len(people["films"])}
                continue

        results.append({"name": people["name"], "species": people["species"],
                        "height": people["height"], "appearances": len(people["films"])})
        appears.append(len(people["films"]))

    while r["next"] is not None:
        results, appears = get_people_optimal(uri=r["next"], results=results, appears=appears)
        return results, appears

    return results, appears


# people = get_people()

# people, appears = get_people_optimal()


people_mock_optimal = [{'name': 'Luke Skywalker', 'species': [], 'height': '172', 'appearances': 4},
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

print(people_mock_optimal)

# for people in people_mock_optimal:
#     name = ""
#     if people["species"]:
#         for species_uri in people["species"]:
#             name = " ".join([get_species(species_uri), name])
#         name = name.strip()
#     people["species"] = name

print(people_mock_optimal)
people_mock_optimal = [{'name': 'Luke Skywalker', 'species': '', 'height': '172', 'appearances': 4},
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

newlist = sorted(people_mock_optimal, key=lambda k: int(k['height']), reverse=True)

import pprint

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(newlist)

import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'species', 'height', 'appearances']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in newlist:
        writer.writerow(row)
