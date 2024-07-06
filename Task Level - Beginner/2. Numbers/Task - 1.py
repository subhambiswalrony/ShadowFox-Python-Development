'''
Write a function that takes two arguments, 145 and 'o', and
 uses the `format` function to return a formatted string. Print the
 result. Try to identify the representation used.
'''


def format_number(number, formatSpecifier):
    return format(number, formatSpecifier)


result = format_number(145, 'o')
print(result)
