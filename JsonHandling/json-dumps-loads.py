import json
string_ip = '{"name": "John", "sex": "Male", "age": 25, "isAdult": false}'

output_dict = json.loads(string_ip)
print(output_dict)
output_json = json.dumps(string_ip, sort_keys=True, indent=2, separators=(":","="))
print(output_json)