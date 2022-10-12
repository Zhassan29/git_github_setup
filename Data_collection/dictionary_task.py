story1 = {
    "start": "devops130 starts at 9am and finishes at 6pm.",
    "middle": "lunch is from 12:30 to 1:30",
    "end": "finish of the day with an exercise"
}
print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1["start"])
print(story1["middle"])
print(story1["end"])

story1["hero"] = "superman"
print(story1)