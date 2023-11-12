from src.utils import load_operations

def test_load_operations(path):
    path2operations = "operations.json"
    assert load_operstions(path2operations)
