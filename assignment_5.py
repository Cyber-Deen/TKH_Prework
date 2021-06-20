names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]

def get_big_name(names):
    longest_name = ""
    for name in names_list:
        if len(name) > len(longest_name):
            longest_name = name
    return longest_name
        

big_name = get_big_name(names_list)
print("Big name is " + big_name)




