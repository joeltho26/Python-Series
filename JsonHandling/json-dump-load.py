import json

with open("./JsonHandling/input.json","r") as ip_file:
    output = json.load(ip_file)
ip_file.close()
print(output)
output.update({'nationality':'India', 'isAdult': True})
print(output)
with open("./JsonHandling/output.json","a") as op_file:
    final_output = json.dump(output,op_file,indent=2,sort_keys=True)
    #separators=(",","=")
op_file.close()