#Lily and Serenity
def count_character (string, target):
    count = 0
    for ch in string:
        if ch == target:
            count = count + 1
    print (count)

count_character ("bonobos", "o")
count_character ("alacazam", "a")
