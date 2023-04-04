# ---------open-in-file----------------------
file_1 = open("08.txt", "r")

STACK_first_player = list(map(int, file_1.readline().split()))
STACK_second_player = list(map(int, file_1.readline().split()))

del file_1
# ---------close-in-file----------------------

if STACK_first_player != 0 and STACK_second_player != 0:

    step_counter = 0

    while len(STACK_first_player) != 0 and len(STACK_second_player) != 0:

        first_player_card = STACK_first_player[0]
        second_player_card = STACK_second_player[0]

        if first_player_card == 0 and second_player_card == 9:
            STACK_first_player.append(first_player_card)  #
            STACK_first_player.append(second_player_card)
            del STACK_first_player[0]
            del STACK_second_player[0]

            step_counter += 1
            continue

        elif second_player_card == 0 and first_player_card == 9:
            STACK_second_player.append(first_player_card)
            STACK_second_player.append(second_player_card)
            del STACK_first_player[0]
            del STACK_second_player[0]
            step_counter += 1
            continue

        elif first_player_card > second_player_card:
            STACK_first_player.append(first_player_card)  #
            STACK_first_player.append(second_player_card)
            del STACK_first_player[0]
            del STACK_second_player[0]

        elif second_player_card > first_player_card:
            STACK_second_player.append(first_player_card)
            STACK_second_player.append(second_player_card)
            del STACK_first_player[0]
            del STACK_second_player[0]

        step_counter += 1
        if step_counter >= 10**6: break

if len(STACK_second_player) == 0: print(f'first {step_counter}', end='')
elif len(STACK_first_player) == 0: print(f'second {step_counter}', end='')
elif len(STACK_first_player) != 0 and len(STACK_second_player) != 0: print(f'botva', end='')