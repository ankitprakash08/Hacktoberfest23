def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
input_string = "A man a plan a canal Panama"

if is_palindrome(input_string):
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")
