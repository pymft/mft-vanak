

lower_limit = 10
upper_limit = 20

num = 25
#
# cond_1 = num > lower_limit
# cond_2 = num < upper_limit
#
# cond = cond_1 and cond_2

# cond = (num > lower_limit) and (num < upper_limit)

# +--------+#########+--------+-------->
cond_1 = 10 < num < 20
print(cond_1)


# #########+---------+##################
cond_1_rev = not cond_1
print(cond_1_rev)

# +###########################+-------->
cond_2 = 0 < num < 30
print(cond_2)

# using `or` operator
# +########+---------+########+-------->
cond_new = (0 < num < 10) or (20 < num < 30)
print(cond_new)

cond_new = cond_2 and cond_1_rev
print(cond_new)