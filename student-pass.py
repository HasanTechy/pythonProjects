def calculate_score():
    while True:
        try:
            mid1 = float(input("1st midterm result: "))
            mid2 = float(input("2nd midterm result: "))
            final = float(input("Final exam's result: "))

            if 0 <= mid1 <= 100 and 0 <= mid2 <= 100 and 0 <= final <= 100:
                final_score = mid1 * 0.3 + mid2 * 0.3 + final * 0.4
                print("Student's final score is:", final_score)

                if 100 >= final_score >= 91:
                    print("Student got A")
                elif 90 >= final_score >= 81:
                    print("Student got B")
                elif 80 >= final_score >= 71:
                    print("Student got C")
                elif 70 >= final_score >= 61:
                    print("Student got D")
                else:
                    print("Student failed the exam")
                break
            else:
                print("Invalid score! Scores must be in the range of 0 to 100.")
        except ValueError:
            print("Invalid input! Please enter numeric values.")


def needed_score_for_final():
    while True:
        try:
            mid1 = float(input("1st midterm result: "))
            mid2 = float(input("2nd midterm result: "))

            if 0 <= mid1 <= 100 and 0 <= mid2 <= 100:
                midterms = (mid1 * 0.3 + mid2 * 0.3)
                if midterms >= 61.0:
                    print("You've already passed the exam")
                else:
                    print("you need to score ", 61 - midterms, "points in final to pass the exam")
                break
            else:
                print("Invalid score! Scores must be in the range of 0 to 100.")
        except ValueError:
            print("Invalid input! Please enter numeric values.")


choice = input("Enter '1' to calculate final score or '2' to calculate points needed to pass in final: ")

if choice == '1':
    calculate_score()
elif choice == '2':
    needed_score_for_final()
else:
    print("Invalid choice!")
