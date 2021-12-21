# file = open('list.txt', 'r') 

# file.close()


# with open('./list.txt', 'r') as rf:
#     lines = rf.readlines()
#     users = []
#     for line in lines:
#         list = line.strip().split(';')
#         user = {
#             'fullname': list[0],
#             'birthDate': list[1],
#             'age': list[2],
#             'sex': list[3]
#         }
#         users.append(user)
#     print(users)


# .strip убирает новые пустые строки
# old way 
# rf = open('/list.txt', 'r')
# rf.close()




# print(isinstance('23', str))
# print(isinstance(True, str))
# print(isinstance('Hello', str))

# print(isinstance('23', int))
# print(isinstance('Hello', int))
# print(isinstance(True, int))


# print(type(True) == bool)
# print(type(1) == int)

