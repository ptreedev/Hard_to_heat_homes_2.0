from src.property import Property

test_prop = Property(1)

def test_property_has_score():
    assert type(test_prop.calculate_score()) is int

def test_standalone_property_score_equals_1():
    test_prop.connectivity = "Standalone"
    assert test_prop.calculate_score() == 1

def test_property_not_brick_score_adds_1():
    test_prop.material = "Wood"
    assert test_prop.calculate_score() == 2