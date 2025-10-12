import streamlit as st

def Quizz():
    st.write(" Welcome to the Quiz Zone:---------")
    questions = ("1. Which of the following is a pet...?",  # used tuple to create a question list for quiz you can use list also.
                 "2. First alphabet is..?",
                 "3. Biggest mamel in the world...?",
                 "4. Nearest Planet to SUN..?",
                 "5. Biggest planet in the solar System..?")
    options = (("A. Tiger", "B. Dog", "C. Bear", "D. Giraf"),  # Options list also n tuple you can use list also.
               ("A. A", "B. C", "C. T", "D. I"),
               ("A. Monkey", "B. Whale", "C. Dolphin", "D. Donkey"),
               ("A. Earth", "B. Venus", "C. Mercury", "D. Mars"),
               ("A. Earth", "B. Mars", "C. Saturn", "D. Uranus"))
    answers = ("B", "A", "B", "C", "B")      # created to compare the guesses of the user to calculate the score.
    guesses = []                               # created to store the guesses of the user for answers.
    score = 0                                #created to calculate the score of individual
    ques_num = 0                             # Created to provide the index 0 to select the whole answer options from tuple.
   
    st.sidebar.markdown("Quiz Menu...")
    choice = st.sidebar.button("RESET THE QUIZ")

    if choice == 0:
        for question in questions:
            st.write("----------------------------------------------------------------------")
            st.write(question)                        # print all questions from question tuple.

            for option in options[ques_num]:
                st.write(option)                        # print all the options from option tuple.
            ans = st.text_input('Enter your answer', key=question, placeholder='Enter your answer here').upper()
            guesses.append(ans)
            if (guesses[ques_num] == answers[ques_num]):
                score += 1                                   # Calculate the score of user.
            else:
                score=score
            ques_num += 1
        else:
            if score == 5:
                st.write("Wow! You have won the Quiz....with 1st Position")
                st.balloons()
            else:
                st.write("You have scored good  may be beeter score next time.......")
    else:
        print(guesses)
        guesses.clear()                                # To clear the guesses of user to Refresh/Restart the game.
        score = 0
        print('-----------------------cc-------------------')
Quizz()
