class Student:
    def __init__(self, name, age, tracks, score):
        self.student_name = name
        self.student_age = age
        self.student_tracks = tracks
        self.student_score = score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
