# printing acronyms

user_input = input("Enter a phrase: ")


#by replace() method get rid of preposition 'of' and then split into individual words by method split():
phrase = (user_input.replace('of', '')).split()

# Initializing an empty string to append the acronym named a:
a = ""

# use for loop to append acronym and convert into  the uppercase:
for word in phrase:
    a = a + word[0].upper()

print(f'Acronym of {user_input} is {a}')

