#!/usr/bin/python3
def no_c(my_string):
    copy_string = ''
    for i in range(len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            continue
        copy_string = copy_string + my_string[i]
    my_string = copy_string
    return my_string

# or you can this method for simplification
#!/usr/bin/python3

def no_c(my_string):
    return my_string.replace('C', '').replace('c', '')

# Example usage:
original_string = "Hello, World! Python is cool."
result = no_c(original_string)
print(result)


