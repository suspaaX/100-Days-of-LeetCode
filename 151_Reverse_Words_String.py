

s = "the sky is blue"
Output =  "blue is sky the"

# s = "  hello world  "
# Output =  "world hello"

# s = "a good   example"
# Output = "example good a"

def reverseWords(s):
    str1= ''
    x = s.split()
    x.reverse()
    for i in x:
        str1= str1+i+str(' ')

    return str1[0:len(str1)-1]

print(reverseWords(s))