def construct_exam_schedule(students_courses):
    schedule = {}
    
    for student, courses in students_courses.items():
        for course in courses:
            if course not in schedule:
                schedule[course] = []
            schedule[course].append(student)
            
    exam_schedule = {}
    
    for course, students in schedule.items():
        exam_schedule[course] = students
        
    return exam_schedule

# Example input: Dictionary of students and their courses
students_courses = {
    "Alice": ["Math", "Physics"],
    "Bob": ["Math", "Chemistry"],
    "Charlie": ["Physics", "Chemistry"],
    "David": ["Biology"],
    "Eve": ["History", "Biology"]
}

exam_schedule = construct_exam_schedule(students_courses)
for course, students in exam_schedule.items():
    print(course, ":", students)
