name = input('enter your name: ')

text_file = open('usernames.txt', 'a+') # 'r': read / 'w': write/ 'a': append, added information/ 'a+': append+create file if it doesn't exist
text_file.write(name + '\n')
text_file.close()



