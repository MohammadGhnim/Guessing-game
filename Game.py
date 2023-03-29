
'''

Game:

     - welcome message to user.
     - show games.
     - user can play : game number
     - option to exit.
     - ask play again.

     Games:
     - sentence no duplicate.
     -names ---> list[count]
     - x, y: 1 ---> 100

'''

class Game:
    def __init__(self):
        print(''' Welcome to our Game:
    1- Sentence No Duplicate.
    2- Names List Count.
    3- Divided By.
    4- to exit.
''')
        user_choice = int(input('Enter Game Number: '))
        if user_choice == 1:
            sentence = input('Enter Sentence: ')
            self.no_duplicate(sentence)

        elif user_choice == 2:
            names = eval(input('Enter Names : '))
            self.names_count(names)

        elif user_choice == 3:
            first_number = int(input('Enter First Number: '))
            second_number = int(input('Enter Second Number: '))
            self.divided_by(first_number, second_number)

        elif user_choice == 4:
            print('Goodbey ...')
            return
            
        else:
            print('please enter numbers between 1:3')
        
    def no_duplicate(self, sentence):
        words = sentence.split(' ')
        new_words = []
        for w in words:
            if w in new_words:
                continue
            else:
                new_words.append(w)
                
        new_sentence = ' '.join(new_words)
        print(new_sentence)


    def names_count(self, names):
        count = []
        for n in names:
            count.append(len(n))
        print(count)
    
    def divided_by(self, x, y):
        result = []
        for n in range(1, 101):
            if n%x == 0 and n%y == 0:
                result.append(n)  
        print(result)

g1 = Game()

    
    






#no_duplicate('my name is is is alex')

#names_count(['alex', 'anna', 'emma'])
        
#divided_by(5,6)




