import random
COLUMN1 = []
COLUMN2 = []
COLUMN3 = []
def create_list():
    number_list = []
    i = 0
    while i < 21:
        random_number = random.randint(10,99)
        if random_number not in number_list:
            number_list.append(random_number)
        else:
            continue
        i = i + 1
    return number_list

def print_add_numbers(number_list):
    for i in range (7):
        COLUMN1.append(number_list[3*i])
        COLUMN2.append(number_list[3*i + 1])
        COLUMN3.append(number_list[3*i + 2])
        print(str(number_list[3*i]) + '\t' + str(number_list[3*i + 1]) + '\t' + str(number_list[3*i + 2]))

def new_list_maker(first,middle,last):
    number_list = []
    for first_item in first:
        number_list.append(first_item)
    for middle_item in middle:
        number_list.append(middle_item)
    for last_item in last:
        number_list.append(last_item)
    return number_list
def main():
    number_list = create_list()
    print_add_numbers(number_list)
    print("Which column is your number in?  1, 2, 3")
    column_select = int(input())
    number_list2 = []
    if column_select == 1:
        number_list2 = new_list_maker(COLUMN2,COLUMN1,COLUMN3)
    elif column_select == 2:
        number_list2 = new_list_maker(COLUMN3, COLUMN2, COLUMN1)
    elif column_select == 3:
        number_list2 = new_list_maker(COLUMN1,COLUMN3,COLUMN2)

    COLUMN1.clear()
    COLUMN2.clear()
    COLUMN3.clear()

    print_add_numbers(number_list2)
    print("Which column is your number in?  1, 2, 3")
    column_select = int(input())
    number_list3 = []
    if column_select == 1:
        number_list3 = new_list_maker(COLUMN2,COLUMN1,COLUMN3)
    elif column_select == 2:
        number_list3 = new_list_maker(COLUMN3, COLUMN2, COLUMN1)
    elif column_select == 3:
        number_list3 = new_list_maker(COLUMN1,COLUMN3,COLUMN2)

    COLUMN1.clear()
    COLUMN2.clear()
    COLUMN3.clear()

    print_add_numbers(number_list3)
    print("Which column is your number in?  1, 2, 3")
    column_select = int(input())
    print("Your number is:")
    if column_select == 1:
        print(COLUMN1[3])
    elif column_select == 2:
        print(COLUMN2[3])
    elif column_select == 3:
        print(COLUMN3[3])



main()