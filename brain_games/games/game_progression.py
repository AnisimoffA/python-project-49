from random import randint
import prompt


def progression_game():
    one_step = randint(1, 10)
    len_of_range = randint(5, 10)
    first_number = randint(1, 50)
    our_range = [str(first_number)]

    for _ in range(1, len_of_range + 1):
        our_range.append(str(int(our_range[-1]) + one_step))

    hide_number = randint(0, len(our_range) - 1)
    n = -1

    for _ in range(1, len(our_range) + 1):
        n += 1
        if n == hide_number:
            right_answer = our_range[hide_number]
            our_range[hide_number] = ".."

    list_string = (" ".join(our_range))

    print("What number is missing in the progression?")
    print(f"Question: {list_string}")
    answer = prompt.string("Your answer: ")

    return str(answer), str(right_answer)
