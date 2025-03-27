# Name:  Asahi Smith
# Student Number:  10655230

# This file is provided to you as a starting point for the "quiz.py" program of the Project
# of Programming Principles in Semester 1, 2024.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis of your work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the necessary module(s).
import tkinter, tkinter.messagebox, random, json


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of quiz.py" section of the assignment brief.
        try:
            with open("data.txt", "r") as file:
                self.data = json.load(file)
        except:
            main = tkinter.Tk()
            main.withdraw()
            tkinter.messagebox.showerror("Error", "Missing/Invalid file")
            return

        #If less than 5 questions give error
        if len(self.data) < 5:
            main = tkinter.Tk()
            main.withdraw()
            tkinter.messagebox.showerror("Error", "Insufficient number of questions. Program needs at least 5 questions to run. ")
            return
            


        self.questions = random.sample(self.data, 5)
        self.current_question_index = 0
        self.correct = 0
        self.incorrect = 0
        
        self.main = tkinter.Tk()
        self.main.title("Quiz")

        # Create the widgets
        self.question_frame = tkinter.Frame(self.main)
        self.question_frame.pack(pady=20)
        
        self.progress_label = tkinter.Label(self.question_frame, text="Question 1 of 5")
        self.progress_label.pack()
        
        self.question_label = tkinter.Label(self.question_frame, text="", wraplength=400)
        self.question_label.pack(pady=10)

        self.difficulty_label = tkinter.Label(self.question_frame, text = "")
        self.difficulty_label.pack(pady=5)
        
        self.answer_entry = tkinter.Entry(self.question_frame, width=50)
        self.answer_entry.focus_set()
        self.answer_entry.pack(pady=10, padx = 50)
        
        self.submit_button = tkinter.Button(self.question_frame, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=5)


        #Run main program
        self.show_question()
        tkinter.mainloop()
        



    def show_question(self):
        # This method is responsible for displaying the current question and some other messages in the GUI.
        # See Point 1 of the "Methods in the GUI class of quiz.py" section of the assignment brief.
        question = self.questions[self.current_question_index]
        self.question_label.configure(text = question["question"])
        self.progress_label.configure(text = f"Question {self.current_question_index + 1} of 5")

        difficulty = int(question.get("difficulty", 1))

        #Set correct difficulty text
        if difficulty == 1:
            difficulty_text = "Easy"
        elif difficulty == 2:
            difficulty_text = "Medium"
        elif difficulty == 3:
            difficulty_text = "Hard"
            
        self.difficulty_label.configure(text=f"Difficulty: {difficulty_text}")
        self.answer_entry.delete(0, tkinter.END)

        

    def check_answer(self):   
        # This method is responsible for checking if the user's answer is correct and recording that information in "data.txt".
        # See Point 2 of the "Methods in the GUI class of quiz.py" section of the assignment brief.
        
        self.user_answer = self.answer_entry.get().lower().strip()
        
        correct_answers = [self.questions[self.current_question_index]['answer']]

        #Check user's answer in answer list
        if any(self.user_answer in ans for ans in correct_answers):
            self.correct += 1
            tkinter.messagebox.showinfo("Correct!", "You are correct!" )
            self.questions[self.current_question_index]['correct'] = int(self.questions[self.current_question_index]['correct']) + 1
            
        else:
            self.incorrect += 1
            tkinter.messagebox.showerror("Incorrect!", "Sorry, that was incorrect.")
            self.questions[self.current_question_index]['incorrect'] = int(self.questions[self.current_question_index]['incorrect']) + 1
        
        self.current_question_index += 1

        with open("data.txt", "w") as file:
            json.dump(self.data, file, indent = 4)

        if self.current_question_index < len(self.questions):
            self.show_question()
            
        #End program
        else:
            self.question_frame.pack_forget()
            result_message = f"Quiz Over! \n Correct Answers: {self.correct} \n Incorrect Answers: {self.incorrect}"
            tkinter.messagebox.showinfo("Quiz Result", result_message)
            self.main.destroy()



# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()

# If you have been paid to write this program, please delete this comment.
