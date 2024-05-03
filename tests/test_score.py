from src.property import Property

def test_property_has_score():
    test_prop = Property(1)
    assert type(test_prop.calculate_score()) is int

def test_standalone_property_score_equals_1():
    test_prop = Property(1)
    test_prop.connectivity = "Standalone"
    assert test_prop.calculate_score() == 1
