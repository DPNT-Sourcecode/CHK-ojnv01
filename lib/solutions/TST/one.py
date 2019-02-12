
def get(items):
    """
    expecting a string

    in theory can have any letter but only have data for A - D so won't accept anything else at the moment

    i'm going to allow upper or lower case to be entered, and convert to upper case for checking

    """
    if type(items) != str:
        return -1

    valid_letters = ['A', 'B', 'C', 'D']

    # we need to convert the string to a list

    item_list = []
    for i in items:
        item_list.append(i.upper())


    # now lets check that all the letters are valid. not all of the valid letters have to be in the string

    if len(set(items) - set(valid_letters)) > 0:
        return -1

    A = 0
    B = 0
    C = 0
    D = 0

    for item in item_list:
        if item == 'A':
            A = A + 1
        elif item == 'B':
            B = B + 1
        elif item == 'C':
            C = C + 1
        else:
            D = D + 1

    # for A there is a special offer 3 for 130

    # find out how many of the offers there are, and then how many extra

    offers = A / 3
    left = A % 3

    total = (offers * 130) + (left * 50)

    # for B there is also an offer, 2 for 45

    offers = B / 2
    left = B % 2

    total = total + (offers * 45) + (left * 30)

    total = total + (C * 20)
    total = total + (D * 15)

    return total


