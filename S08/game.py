import random


# def check(number, secret):
#     if number > secret:
#         return 1
#     if number < secret:
#         return -1
#     return 0
def check(n, m):
    return 0 if n == m else 1 if n > m else -1


def show_message(check_result):
    messages = {
        0: "\033[32;7m  BINGO \033[0m",
        1: "\033[31;1m  greater \033[0m",
        -1: "\033[34;1m  lesser \033[0m"
    }
    print(messages[check_result])


secret = random.randint(1, 100)

while True:
    guess = int(input("\033[32m guess the secret number \033[0m"))
    compare_result = check(guess, secret)
    show_message(compare_result)
    if compare_result == 0:
        break
