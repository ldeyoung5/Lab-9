#Lily and Serenity

#until space
index = 0
s = "Mind the gap!"
while index < len(s) and s[index] != " ":
    index += 1
print (s[:index])



def until_dot (s):
    index = 0
    while index < len (s) and s[index] != ".":
        index += 1
    print (s[:index])

until_dot("This is a sentence. This is another.")


