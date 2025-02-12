# this function is a personalized input modification

# this function can be used to acquire user Yes or No answer
# function requires an input of question string
# function will request user input as Y or N
# if user input anything other than Y(y) or N(n), function will print tips
# function does not distinguish capital letters, both are acceptible
# function will not quit until user input Y/N correct
# function will return Y or N, only capital letter
# Y/N input with input validation ↓
def Y_N_input(customized_suggestion):    
    while True:
        y_n_input = input(f"{customized_suggestion}\nY/N?\n").upper()
        if y_n_input == "Y" or y_n_input == "N":
            break
        else:
            print("Please enter a valid response!")
            continue
    return y_n_input
# Y/N input with input validation ↑


# print in one line for a list
def print_in_line(message_list):
    items = ""
    for item in message_list:
        items += f"{item}  "
    print(items)
# test run
# test_list = ["one","two","three"]
# print_in_line(test_list)