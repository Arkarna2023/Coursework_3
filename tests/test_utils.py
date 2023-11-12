from src.utils import load_operations

def test_load_operations():
    path2operations = "operations.json"
    result = load_operations(path2operations)
    print(result)
