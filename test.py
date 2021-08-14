import json

json_string = '''
{
  "students": [
    {
      "name": "Millie Brown",
      "active": true,
      "rollno": 11
    },
    {
      "name": "Sadie Sink",
      "active": true,
      "rollno": 10
    }
  ]
}
'''
print(json_string)
print("The type of object is: ", type(json_string))
stud_obj = json.loads(json_string)
print(stud_obj)