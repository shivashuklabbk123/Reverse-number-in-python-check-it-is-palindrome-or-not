n = int(input("Enter the number::"))
temp = n
rev = 0
while(n>0):
    dig= n%10
    rev = rev*10 + dig
    n = n//10
print("The reverse number of given number is::", rev)
if(temp == rev):
    print("It is palindrome number")
else:
    print("It is not palindrome number")