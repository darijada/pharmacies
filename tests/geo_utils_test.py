from pandas import Series
from geopandas import GeoDataFrame

from geo_utils import (
    find_closest_pharmacies,
    find_pharmacy_with_most_coffee_bars,
    remove_duplicates,
)

from tests.constants import (
    test_pharmacies_gdf,
    test_duplicate_pharmacies_gdf,
    test_coffee_bars_gdf,
)


def test_find_closest_pharmacies():
    closest_pharmacies, min_distance = find_closest_pharmacies(test_pharmacies_gdf)

    assert isinstance(closest_pharmacies, list)
    assert all(isinstance(pharmacy, Series) for pharmacy in closest_pharmacies)
    assert isinstance(min_distance, float)


def test_find_pharmacy_with_most_coffee_bars():
    (
        pharmacy_with_most_coffee_bars,
        max_coffee_bars_no,
    ) = find_pharmacy_with_most_coffee_bars(test_pharmacies_gdf, test_coffee_bars_gdf)

    assert isinstance(pharmacy_with_most_coffee_bars, list)
    assert all(
        isinstance(pharmacy, Series) for pharmacy in pharmacy_with_most_coffee_bars
    )
    assert isinstance(max_coffee_bars_no, int)


def test_remove_duplicates():
    result = remove_duplicates(test_duplicate_pharmacies_gdf)

    assert isinstance(result, GeoDataFrame)

    assert len(result) == 4  # expected result after removing duplicates
