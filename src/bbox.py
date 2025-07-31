import geopandas as gpd
import json

with open("data/councils_bbox_data.json") as bbox_json:
        bbox_data = json.load(bbox_json)

def _create_bbox_data():
    gdf = gpd.read_file("data/bdline_gpkg_gb/Data/bdline_gb.gpkg", layer = "district_borough_unitary")

    #convert coordinates to correct format
    gdf = gdf.to_crs("EPSG:4326")

    bbox_data = []
    for _, row in gdf.iterrows():
          
        name = row["Name"]
        census_code = row["Census_Code"]
        bounds = row.geometry.bounds
        bbox = {
                "minx": bounds[0],
                "miny": bounds[1],
                "maxx": bounds[2],
                "maxy": bounds[3]
        }

        bbox_data.append({
            "name": name,
            "census_code": census_code,
            "bbox": bbox
        })
    
    with open("data/bdline_gpkg_gb/councils_bbox_data.json", "w") as f:
        json.dump(bbox_data, f, indent=2)

def get_bbox_for_council_code(council_code):
    match = next ((entry for entry in bbox_data if entry["census_code"] == council_code),None)
    if match:
        bbox_dict = match["bbox"]
        bbox_string = f"{bbox_dict['minx']},{bbox_dict['miny']},{bbox_dict['maxx']},{bbox_dict['maxy']}"
        print(bbox_string)
        return bbox_string
    else:
        return False
