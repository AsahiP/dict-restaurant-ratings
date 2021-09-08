"""Restaurant rating lister.

Your job is to write a program named ratings.py that:
Reads the ratings in from the file
Stores them in a dictionary
And finally, spits out the ratings in alphabetical order by restaurant
Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.
Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.

PSEUDOCODE
import txt document (for loop, iterating lines)
splice lines into lists
extract scores & restaurant name from lists
sort restaurant names
store restaurant names (key) & scores (value) into dictionary
print restaurant names & scores

The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
"""
scores_file = open("scores.txt")


def restaurant_info(file):
    """Getting info of restaurants/scores from txt file"""
    for line in file: #iterating through each line 
        line_str = line.strip() #stripping white space
        # print(line_str)
        line_list = line_str.split("\n") #breaking at each end of line
    print(line_list)
    return line_list
    
restaurant_info(scores_file)
        
# lst_to_sort = restaurant_info(scores_file)


# def sort_restaurant_info():
#     "Alphabetizing information by restaurant name"
#     # restaurant_lst = restaurant_info(file)
#     # print(restaurant_lst)
#     for line in lst_to_sort:
#         alpha_line_list = lst_to_sort.sort()
#         print(alpha_line_list)


# sort_restaurant_info()