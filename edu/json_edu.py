import json

# json-строка
people_string = """{
    "people": [
        {
            "name": "John Smith",
            "phone": "666-555-444",
            "emails": [
                "johnsmith@home.com",
                "john.smith@work.com"
            ],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "111-222-333",
            "emails": null,
            "has_license": true
        }
    ]
}"""

data = '{"name": "John Smith", "age": 30, "city": "New York"}'
print(data)  # >>> {"name": "John Smith", "age": 30, "city": "New York"}
print(type(data))  # >>> <class 'str'>

py_data = json.loads(data)  # loads - загрузить данные из json-строки в python
print(py_data)  # >>> {'name': 'John Smith', 'age': 30, 'city': 'New York'}
print(type(py_data))  # >>> <class 'dict'>

json_data = json.dumps(py_data)  # dumps - толкнуть из python в json-строку
print(json_data)  # >>> {"name": "John Smith", "age": 30, "city": "New York"}
print(type(json_data))  # >>> <class 'str'>

if data == json_data:
    print("OK")

print(type(people_string))

py_people_string = json.loads(people_string)
print(type(py_people_string))

json_people_string = json.dumps(py_people_string, indent=4)
print(type(json_people_string))

if people_string == json_people_string:
    print("OK")


print(type(json.loads("true")))  # >>> <class 'bool'>
print(type(json.loads("[1, 2, 3]")))  # >>> <class 'list'>
