from src.property import Property

def test_property_has_occupied_status():
    test_prop = Property(1)
    assert test_prop.void == False
    