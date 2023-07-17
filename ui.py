from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"
class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window = Tk()

        self.window.title('Quiz')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score=0
        self.score_label=Label(text=f'Score : {self.score}',font=('Arial',20,'normal'),bg=THEME_COLOR , fg='white')
        self.score_label.grid(row=0,column=1)
        self.canvas=Canvas(height=250,width=300)
        self.question_text=self.canvas.create_text(150,110,text="Title",font=('Arial',20,'italic'),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.img_true=PhotoImage(file='images/true.png')
        self.img_false=PhotoImage(file='images/false.png')

        self.t_button=Button(image=self.img_true,highlightthickness=0,command=self.true_p)
        self.w_button=Button(image=self.img_false,highlightthickness=0,command=self.false_p)
        self.t_button.grid(row=2,column=0)
        self.w_button.grid(row=2, column=1)

        self.get_next()
        self.window.mainloop()
    def get_next(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()

            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="Quiz Finished")
            self.t_button.config(state='disabled')
            self.w_button.config(state='disabled')

    def true_p(self):
        self.feedback(self.quiz.check_answer('True'))
    def false_p(self):
        self.feedback(self.quiz.check_answer('false'))
    # def check(self):
    #     ans = self.quiz.check_answer()
    #     if ans==userans:
    #         self.score+=1
    #         self.score_label.config(text=f'Score : {self.score}')
    def feedback(self,is_correct):
        if is_correct == 0:
            self.canvas.config(bg="red")
        else:
            self.canvas.config(bg="green")
        self.window.after(1000,self.get_next)





