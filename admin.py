# Name:  Asahi Smith
# Student Number:  10655230


# Import the necessary module(s).
import json


# This function repeatedly prompts for input until an integer between 1 and max_value is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt, max_value):
    while True:
        try: 
            number = int(input(prompt))
            if number == 0:
                break
            if number == -1:
                break
            elif number >= 1 and number <= max_value:
                break
            elif number < 1 or number > max_value:
                print("Invalid input. Please enter a number in the accepted range. ")
        except:
            print("Invalid input. Please enter a number.")
    return number


# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    while True:
        something = str(input(prompt))
        if something.strip() == "":
            print("Invalid input, please enter a character. ")
            continue
        elif something.strip() != "":
            break
    return something.lower()


# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data):
    with open("data.txt", "w") as file:
        print("File Saved")
        json.dump(data, file, indent = 4)


# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

try:
    with open("data.txt", "r") as file:
        data = json.load(file)
except:
    data = []




# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() 


    if choice == 'a':
        # Add a new question.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        answerList = []
        correctNo = 0
        incorrectNo = 0
        questions = input_something("Enter a question: ")
        while True:
            answer = input_something("Enter a valid answer (enter 'q' when done): ")
            if answer != 'q':
                answerList.append(answer)
            if answer == 'q':
                break

        difficultyLevel = input_int("Enter the question difficulty (1-3): ", 3)
        
        #add question to dictionary
        dictionary = {"question": f"{questions}", "answer": f"{answerList}", "difficulty": f"{difficultyLevel}", "correct": f"{correctNo}", "incorrect": f"{incorrectNo}"}
        data.append(dictionary)
        print("Question added!")
        save_data(data)


    elif choice == 'l':
        # List the current questions.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        try:
            if data == [] or data == ["[]"]:
                print("No questions saved. ")
                continue
            print("Current questions: ")
            count = 1
            for dict in data:
                print(f"{count})", dict["question"])
                count += 1
        except:
            print("No questions saved.")


    elif choice == 's':
        # Search the current questions.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        if data == []:
            print("No questions saved. ")
            continue
        count3 = 0
        search = input_something("Enter a search term: ")
        for dict in data:
            for key in dict:
                value = dict[key]
                if search in value:
                    questionno = data.index(dict)
                    print(f"{questionno + 1}) {value}")
                    count3 += 1
        if count3 == 0:   
            print("Your search returned no results. ")  


    elif choice == 'v':
        # View a question.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        if data == [] or data == ["[]"]:
            print("No questions saved. ")
            continue
        view = input_int("Question number to view (enter '0' to quit): ", len(data))
        if view == 0:
            continue
        
        print("Question:", data[view - 1]["question"])  
        

    elif choice == 'd':
        # Delete a question.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        if data == [] or data == ["[]"]:
            print("No questions saved. ")
            continue
        delete = input_int("Question number to delete (enter '0' to quit, enter '-1' to delete all): ", len(data))

        if delete == 0:
            continue
        
        if delete == -1:
            clear_confirm = input_something("Are you sure you want to delete all questions? ['Y'/'N']")
            if clear_confirm.lower() == 'y':
                data.clear()
                print("All questions have been deleted.")
                save_data(data)
                continue
            if clear_confirm.lower() == "n":
                continue

        confirm = input_something(f"Are you sure you want to delete the question: '{data[delete - 1]['question']}'? ['Y'/'N']")
        if confirm.lower() == 'y':
            del data[delete - 1]
            print(f"Question number {delete} has been deleted. ")
            if data == ["[]"]:
                data.clear()
            save_data(data)
        if confirm.lower() == 'n':
            continue


    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print("Goodbye!")
        break


    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice. Please enter either an 'a', 'l', 's', 'v', 'd', or 'q'.")







# If you have been paid to write this program, please delete this comment.
