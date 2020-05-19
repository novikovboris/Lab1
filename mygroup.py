groupmates = [
  {
    "name": "Иванов Н.",
    "group": "УБАП1901",
    "age": 21,
    "marks": [4, 3, 5, 5, 4]
  },
  {
    "name": "Власов Д.",
    "group": "УБАП1901",
    "age": 22,
    "marks": [3, 2, 3, 4, 3]
  },
  {
    "name": "Мешочков М.",
    "group": "УБАП1901",
    "age": 22,
    "marks": [3, 5, 4, 3, 5]
  },
  {
    "name": "Новиков Б.",
    "group": "УБАП1901",
    "age": 30,
    "marks": [5, 5, 5, 4, 5]
  },
  {
    "name": "Лисин А.",
    "group": "УБАП1901",
    "age": 22,
    "marks": [5, 5, 5, 5, 5]
  }
]

def count_mark(students,mark):
    print ("name".ljust(15), "group".ljust(8), "age".ljust(8), "marks".ljust(20))
    for student in students:
        marks_list = student['marks']
        result =  (sum(marks_list)/len(marks_list))
        if result >= need:
            print(student["name"].ljust(15), student["group"].ljust(8), str(student["age"]).ljust(8), str(student["marks"]).ljust(20))

need = int(input('Input :'))

count_mark(groupmates,need)