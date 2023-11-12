import json

def task(file_path) -> float:
    with open(file_path, 'r') as f:
        data = json.load(f)

    total = sum(item['score'] * item['weight'] for item in data)
    return round(total, 3)

file_path = 'input.json'

result = task(file_path)
print(result)
