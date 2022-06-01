class Student:
    def __init__(self, name, age, tracks, score):
        self.student_name = name
        self.student_age = age
        self.student_tracks = tracks
        self.student_score = score

    def change_name(self, new_name):
        self.student_name = new_name

    def change_age(self, new_age):
        self.student_age = int(new_age)

    def add_track(self, new_track):
        self.student_tracks.append(new_track) 
        
    def get_score(self):
        return self.student_score

#test with the codes below

Bob = Student("Bob",26, ["FE","BE"], 20.90)
print(Bob.student_tracks)
Bob.add_track('WE')
print(Bob.student_tracks)
#Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
