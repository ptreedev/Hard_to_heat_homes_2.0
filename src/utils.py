from src.property import Property

def get_props(props):
    result = []
    for prop in props:
        building = Property(prop['uprn'])
        building.epc_rating = prop["current-energy-rating"]
        building.epc_score = prop["current-energy-efficiency"]
        building.address = f'{prop["address"]}, {prop["postcode"]}'
        result.append(building)

    return result

def get_props_from_os(list_of_buildings):
    result = []
    for i in range(len(list_of_buildings)):
        building = list_of_buildings[i]["properties"]
        uprn_array = building["uprnreference"]
        for j in range(len(uprn_array)):
            age = "buildingage_year" if building["buildingage_year"] else "buildingage_period"
            new_prop = Property(uprn_array[j]['uprn'])
            new_prop.connectivity =  building["connectivity"]
            new_prop.age =  building[age]
            new_prop.material =  building["constructionmaterial"]
            result.append(new_prop)
    return result