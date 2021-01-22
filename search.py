

def search(string, list_value, size):
    '''
    The function takes a list of strings and finds the position of a given string within the list
    If the given string cannot be found within the list the function returns -1

    >>> a = ["hello fred", "come here", "let's go"]
    >>> print(search("hello", a, 3))
    >>> The location of the given string in the list is 0
    
    >>> a = ["hello fred", "come here", "let's go"]
    >>> print(search("hell", a, 3))
    >>> -1
    '''
    search_result = -1
    for i in range(size):
        # converting each element in the main string into a sub-list
        record = 0
        inner_list = list_value[i].upper().split(" ")

        for value in inner_list:
            # for each of the elements in the sub-list is the required string present?
            if string.upper() == value:
                # if YES then the location of the required string is stored in the variable "search_result"
                record += i
                search_result = "The location of the given string in the list is {}".format(record)
            
    return search_result   


# for quick run uncomment the lines below and run program
#print(search("come", ["hello fred", "come here", "let's go"], 3))
#print(search("here", ["hello fred", "come here", "let's go"], 3))
#print(search("coem", ["hello fred", "come here", "let's go"], 3))





    
