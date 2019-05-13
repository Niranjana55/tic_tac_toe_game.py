from Question import Question
questions_prompts=["1. The glass lay ________ on the table.\n (a) not touched\n (b) untouched\n (c) untouching\n (d) not touch\n",
           "2. She ________ at a shop.\n (a) works\n (b) work\n (c) working\n (d) be working\n ",
           "3. We urgently need to recruit a counselor ________ the vacant position.\n  (a) on\n (b) for\n (c) at\n (d) in\n",
           "4. The roomboy was asked to clean the vacant rooms first and then go to the ________ rooms.\n  (a) empty\n (b) occupied\n (c) filled\n (d) guest\n ",
           "5. The rival team won the match ________ they foul played.\n  (a) since\n (b) while\n  (c) yet\n (d) because\n "

]


questions = [ 
    Question(questions_prompts[0], "b"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "b"),
    Question(questions_prompts[3], "b"),
    Question(questions_prompts[4], "d"),

]

def run_test(questions):

    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer :
            score+=1
    print ("your score" + str(score) + "/" + str (len(questions)) + "correct" )
run_test(questions)



        