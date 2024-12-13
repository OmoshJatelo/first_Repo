import json
student_info='{"name":"JAtelo","couse":"Bsc","Year":"1.1"}'
json_data=json.loads(student_info)


for info in json_data:
    print(info)


#converting python objects into json strings and writing the string  to a file
import json
my_dictionary={
    "student":[
        {"name":"Omosh Jatelo","age":"18","Rsidence":"Qwetu","Profession":"software Developer"},
        {"name":"Zuckerberg Jatelo","age":"19","Rsidence":"Qejani","Profession":"Cyber Security Analist"}

        ],
        "is A garduate":"false",
    "worker":[{"name":"john","age":"24"}]    


}

json_string=json.dumps(my_dictionary)
print(json_string)

with open("my_json_file","w") as my_json_file:       #json.dumps(): Converts Python objects into a JSON strin 
    my_json_file.write(json_string)                  #json.dump(): Writes the JSON string directly to a file

  
with open("my_json_file","r") as my_json_file:
    for detail in my_json_file:
        print(detail)
