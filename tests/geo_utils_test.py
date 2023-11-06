from pandas import Series

from geo_utils import find_closest_pharmacies, find_pharmacy_with_most_coffee_bars

from tests.constants import test_pharmacies_gdf, test_coffee_bars_gdf


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
