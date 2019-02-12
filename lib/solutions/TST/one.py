
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


