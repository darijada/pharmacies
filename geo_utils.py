from typing import List, Tuple
from itertools import combinations

from geopandas import GeoDataFrame
from pandas import Series


GEOJSON_FILE = "data/export.geojson"

PHARMACY_AMENITIES = ["pharmacy"]
COFFEE_BAR_AMENITIES = ["bar", "cafe"]

TARGET_CRS = "EPSG:32633"
SEARCH_RADIUS = 250


def find_closest_pharmacies(pharmacies_gdf: GeoDataFrame) -> Tuple[List[Series], float]:
    """
    Find the two closest pharmacies in a GeoDataFrame and their distance.

    :param pharmacies_gdf: A GeoDataFrame containing pharmacy geolocations.
    :return: A tuple containing a list of two GeoDataFrames representing the two closest pharmacies and a float
            representing their distance.
    """
    closest_pharmacies = []
    min_distance = float("inf")

    for i, j in combinations(pharmacies_gdf.index, 2):
        geo_pharmacy_one = pharmacies_gdf.loc[i, "geometry"]
        geo_pharmacy_two = pharmacies_gdf.loc[j, "geometry"]

        distance = geo_pharmacy_one.distance(geo_pharmacy_two)

        if distance < min_distance:
            min_distance = distance
            closest_pharmacies = [i, j]

    closest_pharmacies = [pharmacies_gdf.loc[i] for i in closest_pharmacies]

    return closest_pharmacies, min_distance


def find_pharmacy_with_most_coffee_bars(
    pharmacies_gdf: GeoDataFrame, coffee_bars_gdf: GeoDataFrame
) -> Tuple[List[Series], int]:
    """
    Find the pharmacy with the most coffee bars within a specified radius.
    :param pharmacies_gdf: A GeoDataFrame containing pharmacy geolocations.
    :param coffee_bars_gdf: A GeoDataFrame containing coffee bar geolocations.
    :return: A tuple containing a list of GeoDataFrame(s) representing pharmacies with the most coffee bars and an
            integer representing the count of coffee bars within the specified radius.
    """
    max_coffee_bars_no = 0
    pharmacy_with_most_coffee_bars = []

    for idx, pharmacy_row in pharmacies_gdf.iterrows():
        pharmacy_geom = pharmacy_row["geometry"]
        buffered_pharmacy = pharmacy_geom.buffer(SEARCH_RADIUS)

        coffee_bars_in_radius = coffee_bars_gdf[
            coffee_bars_gdf.intersects(buffered_pharmacy)
        ]
        coffee_bars_count = len(coffee_bars_in_radius)

        if coffee_bars_count > max_coffee_bars_no:
            pharmacy_with_most_coffee_bars = []
            max_coffee_bars_no = coffee_bars_count
            pharmacy_with_most_coffee_bars.append(pharmacy_row)
        elif coffee_bars_count == max_coffee_bars_no:
            pharmacy_with_most_coffee_bars.append(pharmacy_row)

    return pharmacy_with_most_coffee_bars, max_coffee_bars_no
