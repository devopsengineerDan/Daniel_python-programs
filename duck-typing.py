#Duck Typing
#Easier to Ask for Forgiveness than Permission (EAFP)


person = {'name': 'Dancun', 'profession': 'software engineer', 'majors': 'Cybersecurity and Artificial Intelligence', 'genius': 'grit to see through complex solutions'}

#EAFP (Pythonic)
try:
    print("I am {name}. I am a {profession}. I major in the fields of {majors}. I have the {genius}.".format(**person))
except KeyError as error:
    print("Missing {} key".format(error))    