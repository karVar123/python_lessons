def request_question():
    answer = input("what you min ? ")
    return answer


def answer_of_bot(user_answer):
    if user_answer == "hi":
        return "hi"
    elif user_answer == "how are you":
        return "fine , how are you"
    elif user_answer == "how ord are you ?":
        return "I am a robot , i have not a age"
    elif user_answer == "break":
        pass
    else:
        print("some answer")


def main_logic_of_bot():
    while True:
        question = request_question()
        print(answer_of_bot(question))
        if question == "break":
            print("breaking while loop")
            break


print(main_logic_of_bot)


