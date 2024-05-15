"""
The purpose of this script is to reverse geocode the latitude and longitude of
meteorite landings to get the country

This can be useful for data analysis and visualization

Libraries used:
- reverse_geocode
- csv
"""

import reverse_geocode
import csv

meteor_data = []
with open('Meteorite_Landings.csv', 'r') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        if row[-3] == '' or row[-2] == '':
            continue

        lat = float(row[-3])
        lon = float(row[-2])

        coordinates = (lat, lon),
        print(coordinates)
        countryData = (reverse_geocode.search(coordinates))[0]
        country = countryData['country']
        country_code = countryData['country_code']

        meteor_data.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], country, country_code])
        print("Finished Row:", i)

# Write this data as a JSON for easier data manipulation
import json

with open('meteorite-landings.json', 'w') as file:
    data = []
    for row in meteor_data:
        data.append({
            "name": row[0],
            "id": row[1],
            "nametype": row[2],
            "recclass": row[3],
            "mass": row[4],
            "fall": row[5],
            "year": row[6],
            "reclat": row[7],
            "reclong": row[8],
            "country": row[9],
            "country_code": row[10]
        })

    json.dump(data, file, indent=4)

print("Finished writing JSON file")