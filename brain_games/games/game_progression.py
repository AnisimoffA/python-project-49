from random import randint
import brain_games.game_logic as game_logic
import prompt

    
def progression_game():
    name = game_logic.name
    one_step = randint(1,10)
    len_of_range = randint(5,10)
    first_number = randint(1,50)
    our_range = [str(first_number)]

    for x in range(1,len_of_range+1):
        our_range.append(str(int(our_range[-1])+one_step))

    hide_number = randint(0,len(our_range)-1)
    n = -1

    for x in range(1,len(our_range)+1):
        n += 1
        if n == hide_number:
            right_answer = our_range[hide_number]
            our_range[hide_number] = ".."

    list_string = (" ".join(our_range))

    print(f"What number is missing in the progression?\nQuestion: {list_string}")
    answer = prompt.string("Your answer: ")

    return str(answer), str(right_answer)