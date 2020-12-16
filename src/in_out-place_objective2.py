def triple_list_in_place(int_list):
    for i in range(len(int_list)):
        int_list[i] *= 3

# no return statement because we've modified the original list in place.
# There is no need to return another reference to the same list.

# There are no side effects with out-of-place. Create a new list and return the new list
def triple_list_out_of_place(int_list): # Use out-of-place. usually always better
    # Allocate a new list with enough room for all of the elements
    tripled_list = [None] * len(int_list)

    for i in range(len(int_list)):
        tripled_list[i] = int_list[i] * 3
    return tripled_list

num_list = [1,2,3,4,5]
print(num_list)