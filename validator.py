import json
from jsonschema import validate, ValidationError

with open("catalogue.schema.json") as schema_file:
    schema = json.load(schema_file)

with open("valid.json") as data_file:
    data1 = json.load(data_file)

try:
    validate(instance=data1, schema=schema)
    print("Success: Data matches the schema!")
except ValidationError as e:
    print(f"Validation Error: {e.message}")


with open("invalid.json") as data_file:
    data = json.load(data_file)

try:
    validate(instance=data, schema=schema)
    print("Success: Data matches the schema!")
except ValidationError as e:
    print(f"Validation Error: {e.message}")
