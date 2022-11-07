from random import randint


TASK = "What number is missing in the progression?"


def start_game():
    one_step = randint(1, 10)
    len_of_range = randint(5, 10)
    first_number = randint(1, 50)
    our_range = [str(first_number)]

    for _ in range(len_of_range):
        our_range.append(str(int(our_range[-1]) + one_step))

    hide_number = randint(0, len(our_range) - 1)

    right_answer = our_range[hide_number]
    our_range[hide_number] = ".."

    list_string = (" ".join(our_range))
    input_line = f"Question: {list_string}"

    return input_line, str(right_answer)
