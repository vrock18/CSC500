# 3 dictionaries with the key using the Course Number
# Step 1: Data Specifications (Dictionaries)
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}


meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "10:00 a.m.",
    "CSC103": "01:00 p.m.",
    "NET110": "3:00 a.m.",
    "COM241": "5:00 p.m.",
}


# Step 2: Program Logic
# present is a False and changes to True if a correct course is entered (worked well in last weeks assignment)
present = False

# Loop keeps asking until a correct course number is entered
while present == False:
    # prompt for the course number
    # .strip and .upper will remove any accidental spaces and change letters to uppercase to make sure they match the keys exactly
    course = input("Enter a Course Number (e.g., CSC101): ").strip().upper()

    # Retrieval and Output
    if course in room_numbers:
        print(f"\nCourse:        {course}")
        print(f"Room Number:   {room_numbers[course]}")
        print(f"Instructor:    {instructors[course]}")
        print(f"Meeting Time:  {meeting_times[course]}")
        present = True
    else:
        print(f"\nSorry, can't find '{course}'. Please make sure you're entering the correct course number and try again (for example, CSC101).\n")