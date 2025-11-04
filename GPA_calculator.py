# GPA Calculator 
# This program calculates the GPA based on user-inputted grades and credit hours.
# It supports both numeric grades (0-100) and letter grades (A, B+, C-, etc.).

# Here we define a function to convert numeric grades to GPA points:-

def get_gpa_points (grade):
    if 90<= grade <=100:
        print("A")
        return 4.0
    elif 85<= grade <=90:
        print("A-")
        return 3.7
    elif 80<= grade <=85:
        print("B+")
        return 3.3
    elif 75<= grade <=80:
        print("B")
        return 3.0
    elif 70<= grade <=75:
        print("B-")
        return 2.7
    elif 65<= grade <=70:
        print("C+")
        return 2.3
    elif 60<= grade <=65:
        print("C")
        return 2.0
    elif 55<= grade <=60:
        print("C-")
        return 1.7 
    elif 50<= grade <=55:
        print("D+")
        return 1.3
    elif 45<= grade <=50:
        print("D")
        return 1.0
    else:
        print("F")
        return 0.0
   
# Here we define a function to convert letter grades to GPA points:-

def get_gpa_points_from_letter(letter):
    """Convert letter grade to GPA points"""
    letter = letter.upper()
    gpa_scale = {
        "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0
    }
    return gpa_scale.get(letter, -1) 

def calculate_gpa():
    num_courses = int(input("Enter the number of courses: "))
    total_points = 0
    total_credits = 0

    for i in range(num_courses):
        print(f"\nCourse {i+1}:")
        choice = input("Do you want to enter the grade as (N)number or (L)letter? ").strip().lower()

        if choice == "n":
            grade = float(input("Enter the grade (0-100): "))
            points = get_gpa_points(grade)
        elif choice == "l":
            letter = input("Enter the letter grade (A, B+, C-, etc.): ").strip()
            points = get_gpa_points_from_letter(letter)
            if points == -1:
                print("Invalid letter grade entered. Please try again.")
                return
        else:
            print("Invalid choice! Please enter 'N' for number or 'L' for letter.")
            return

        credits = float(input("Enter the credit hours: "))
        total_points += points * credits
        total_credits += credits

    if total_credits == 0:
        print("No credit hours entered, can't calculate your GPA.")
        return

    gpa = total_points / total_credits
    print(f"\nYour GPA: {round(gpa, 2)}")

calculate_gpa()