# Pharmacies

This project provides a solution for finding the closest two pharmacies and identifying the pharmacy with the most 
coffee bars within a specified radius.

## Prerequisites

* [Python 3.x](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/)

## Setup and installation

To get the project up and running, following steps are required:
  * Clone the repository
  * Create a virtual environment:
    
          Linux/macOS:   python3 -m venv .pharmacies_env
          Windows:       py -m venv .pharmacies_env

  * Activate virtual environment

          Linux/macOS:   source .pharmacies_env/bin/activate
          Windows:       .\.pharmacies_env\Scripts\activate

  * Install dependencies using `pip install -r requirements.txt`
  * Run using `python3 main.py`

## Usage

Running the `main.py` script, `export.geojson` GeoJSON data file is loaded and next two functionalities are executed:

### 1. Finding two closest pharmacies

The `find_closest_pharmacies` function calculates the closest pair of pharmacies. It takes a GeoDataFrame (pandas.DataFrame 
that has a column with geometry) with filtered pharmacies data and returns pair of closest pharmacies and their distance.

### 2. Finding Pharmacy with Most Coffee Bars

The `find_pharmacy_with_most_coffee_bars` function calculates the pharmacy with the most coffee bars within a given 
radius (250 meters as default). It takes two GeoDataFrame-s, one with filtered pharmacies data and one with filtered 
coffee bars data, and returns the pharmacy with the most coffee bars and the number of coffee bars within the specified 
radius.

## Automated tests

Tests are implemented using `pytest`. To execute all the tests, use the following command: `python3 -m pytest`.

## Documentation references

- [CRF](https://epsg.io/32633)
- [GeoPandas](https://geopandas.org/en/latest/docs.html)
