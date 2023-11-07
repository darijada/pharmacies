import pathlib

import geopandas as gpd

from geo_utils import TARGET_CRS, PHARMACY_AMENITIES, COFFEE_BAR_AMENITIES


TEST_DATA_DIR = pathlib.Path(__file__).parent / "test_data"
TEST_GEOJSON_FEATURES = str(TEST_DATA_DIR / "features.geojson")
TEST_GEOJSON_DUPLICATE_PHARMACY_FEATURES = str(
    TEST_DATA_DIR / "duplicate_features.geojson"
)

test_features_gdf = gpd.read_file(TEST_GEOJSON_FEATURES)
test_features_gdf = test_features_gdf.to_crs(TARGET_CRS)
test_pharmacies_gdf = test_features_gdf[
    test_features_gdf["amenity"].isin(PHARMACY_AMENITIES)
]
test_duplicate_pharmacies_gdf = gpd.read_file(TEST_GEOJSON_DUPLICATE_PHARMACY_FEATURES)
test_coffee_bars_gdf = test_features_gdf[
    test_features_gdf["amenity"].isin(COFFEE_BAR_AMENITIES)
]
