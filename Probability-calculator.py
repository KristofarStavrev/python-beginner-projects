import math


def main():

    while True:
        try:
            question_num = int(input("Number of questions: "))
            break

        except ValueError:
            print("Invalid input. Try again: ")

    while True:
        try:
            answer_num = int(input("Number of answers per question: "))
            break

        except ValueError:
            print("Invalid input. Try again: ")

    while True:
        try:
            correct_answer_num = int(input("Number of correct "
                                           "answers per question: "))
            break

        except ValueError:
            print("Invalid input. Try again: ")

    while True:
        try:
            correct_answers_needed = int(input("Number of correct "
                                               "answers needed: "))
            break

        except ValueError:
            print("Invalid input. Try again: ")

    answer_variable_correct = correct_answer_num / answer_num
    answer_variable_wrong = (answer_num - correct_answer_num) / answer_num
    final_answer = 0
    end = False

    while end is False:

        if correct_answers_needed > question_num:
            end = True
            break

        temp_answer = (math.factorial(question_num) /
                       (math.factorial(correct_answers_needed) *
                        math.factorial(question_num -
                        correct_answers_needed))) * \
                      ((answer_variable_correct ** (correct_answers_needed)) *
                       (answer_variable_wrong ** (question_num -
                        correct_answers_needed)))

        final_answer = final_answer + temp_answer
        correct_answers_needed += 1

    final_result = round(final_answer * 100, 2)
    print("{0} % chance to pass the test".format(final_result))


if __name__ == "__main__":
    main()
