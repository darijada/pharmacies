import geopandas as gpd

from geo_utils import (
    SEARCH_RADIUS,
    GEOJSON_FILE,
    TARGET_CRS,
    PHARMACY_AMENITIES,
    COFFEE_BAR_AMENITIES,
    find_closest_pharmacies,
    find_pharmacy_with_most_coffee_bars,
)


features_gdf = gpd.read_file(GEOJSON_FILE)
features_gdf = features_gdf.to_crs(TARGET_CRS)
pharmacies_gdf = features_gdf[features_gdf["amenity"].isin(PHARMACY_AMENITIES)]
coffee_bars_gdf = features_gdf[features_gdf["amenity"].isin(COFFEE_BAR_AMENITIES)]


if __name__ == "__main__":
    closest_pharmacies, distance = find_closest_pharmacies(pharmacies_gdf)

    print(
        f"Ids of two closest pharmacies are {closest_pharmacies[0]['id']} and {closest_pharmacies[1]['id']}."
    )
    print(f"Their distance is {distance:.2f} meters.")

    (
        pharmacy_with_most_coffee_bars,
        coffee_bars_no,
    ) = find_pharmacy_with_most_coffee_bars(pharmacies_gdf, coffee_bars_gdf)

    if len(pharmacy_with_most_coffee_bars) > 1:
        print(
            f"Ids of pharmacies with most coffe bars within {SEARCH_RADIUS} meters radius are: {' '.join(pharmacy['id'] for pharmacy in pharmacy_with_most_coffee_bars)}."
        )
    else:
        print(
            f"Pharmacy id with most coffe bars within {SEARCH_RADIUS} meters radius is {pharmacy_with_most_coffee_bars[0]['id']}."
        )
    print(f"Number of coffee bars is {coffee_bars_no}.")
