# core/reader.py

def read_exercises(file_path):
    exercises = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            try:
                name, muscle = line.strip().split(",")
                exercises.append({"name": name, "muscle": muscle})
            except ValueError:
                continue

    return exercises
