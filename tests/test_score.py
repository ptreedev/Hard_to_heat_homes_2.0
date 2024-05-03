from src.property import Property

# todo test when age range is unknown/null 
# todo look into when material is mixed brick and also concrete

test_prop = Property(1)

def test_property_has_score():
    assert type(test_prop.calculate_score()) is int

def test_standalone_property_score_equals_1():
    test_prop.connectivity = "Standalone"
    assert test_prop.calculate_score() == 1

def test_property_not_brick_score_adds_1():
    test_prop.material = "Wood"
    assert test_prop.calculate_score() == 2

def test_property_epc_rating_below_c_adds_point():
    test_prop.epc_rating = "D"
    assert test_prop.calculate_score() == 3

def test_property_age_before_1960_adds_point():
    test_prop.age = 1950
    assert test_prop.calculate_score() == 4

def test_property_age_range_before_1960_adds_point():
    test_prop_2 = Property(1)
    test_prop_2.age = "1940-1950"

    assert test_prop_2.calculate_score() == 1