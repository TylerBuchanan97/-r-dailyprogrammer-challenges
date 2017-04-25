input_statements = {"I am elite.", "Da pain!", "Eye need help!",
                    "3Y3 (\)33d j00 t0 g37 d4 d0c70r.", "1 n33d m4 p1llz!"}

l33t_translations = {"A":"4", "B":"6", "E":"3", "I":"1", "L":"1", "M":"(V)",
                     "N":"(\)", "O":"0", "S":"5", "T":"7", "V":"\/", "W":"`//"}

def main():
    for statement in input_statements:
        for value in l33t_translations.values():
            if value in statement:
                to_words(statement)
                break
            if value == "`//":
                to_l33t(statement)
            
            
def to_l33t(statement):
    print(statement, end = " -> ")
    for letter in statement:
        if letter.upper() in l33t_translations:
            statement = statement.replace(letter, l33t_translations[letter.upper()])
                                         
    print(statement)

def to_words(statement):
    print(statement, end = " -> ")
    for key, value in l33t_translations.items():
        if value in statement:
            statement = statement.replace(value, key.lower())

    print(statement)
            
            

main()       
