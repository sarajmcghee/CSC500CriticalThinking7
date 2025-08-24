
#Create Data Dictionaries for Courses

course_room_numbers = {
    "CSC101" : "3004",
    "CSC102" : "4501",
    "CSC103" : "6755",
    "NET110" : "1244",
    "COM241" : "1411"
}

course_instructors_name ={
    "CSC101" : "Haynes",
    "CSC102" : "Alvarado",
    "CSC103" : "Rich",
    "NET110" : "Burke",
    "COM241" : "Lee"
}

course_time ={
    "CSC101" : "8:00 a.m.",
    "CSC102" : "9:00 a.m.",
    "CSC103" : "10:00 a.m.",
    "NET110" : "11:00 a.m.",
    "COM241" : "1:00 p.m.",
}

valid_courses = set(course_room_numbers.keys())

def display_course_information(course_number):
    print(f"\nCourse: {course_number}")
    print(f"Room Number: {course_room_numbers[course_number]}")
    print(f"Instructor: {course_instructors_name[course_number]}")
    print(f"Class Start Time: {course_time[course_number]}")
while True :
    course_number = input(f"Enter a Valid Course Number {list(valid_courses)} : ").strip().upper()
    if course_number in valid_courses:
        display_course_information (course_number)
        break
    else:
        print(f"Please enter a valid course number. One provided from the list {list(valid_courses)}")

