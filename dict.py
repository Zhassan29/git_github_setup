# what is a Dictionary
# how to manage dictionaries - how to manage the data using dict
# it works as key value pair key = value
# syntax { "key": "value"     }

# store students data - name, course name, progress, completed lessons

student_1 = {
    "keys": "values",
    "name": "zakarie",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lessons_names": ["lists", "tuples", "strings"]
}
#print(student_1)
#print(type(student_1))
#print(student_1["stream"]) # this will display the value saved inside stream

# print/ display completed_lessons_names
# print/ display completed_lessons_names_index 0 means lists

#print(student_1["completed_lessons_names"])
#print(student_1["completed_lessons_names"][0])

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

# delete an item from the list of completed_lesson_names
student_1["completed_lessons_names"].remove("strings")
print(student_1["completed_lessons_names"])

# dict builtin methods
# display keys only or values
# keys() values()
print(student_1.keys())

# display values only from student_1
print(student_1.values())





