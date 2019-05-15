def show_people(s):
    s = s.replace('><', r'\/').replace('>', ' ').replace('<', ' ')
    print(s)


people = "<><>><>>>>><>><>>>>><><>"


sum_moves = 0
while True:
    show_people(people)
    moves = people.count("><")
    sum_moves += moves
    people = people.replace("><", "<>")
    if moves == 0:
        break


print(sum_moves)
