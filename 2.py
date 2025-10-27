x="7"

print(int(x)*x)

#output: 7777777
#Explanation: The string x contains the character '7'.
# When we convert x to an integer using int(x), it becomes the number 7.
# Multiplying 7 (integer) by '7' (string) results in the string '7777777'.
# This is because multiplying a string by an integer n in Python
# repeats the string n times. Hence, '7' repeated 7 times gives '7777777'.