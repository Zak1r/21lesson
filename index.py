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


# with open('./list.txt', 'r') as rf:
#     lines = rf.readlines()
#     numbers = []
#     for line in lines:
#         list = line.strip().strip(';')
#         if len(list) == 1:
#             numbers.append(list[0])
    
#     print(numbers)



with open('./list.txt', 'r') as rf:
    numbers = []
    for line in rf:
        line = line.strip()
        if line.isdigit():
            numbers.append(int(line))
    print(numbers)


    