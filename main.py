import final_project
import os
import random

os.makedirs('setOfFlashcards', exist_ok=True)

def main():
    while True:
        print('Flashcard Quiz App')
        print('1. Choose a flashcard set')
        print('2. Create a new set')
        print('3. Review the wrong answers')
        print('4. View the status')
        print('5. Exit')
        ans = input('Select an option (1-5): ')
        if ans == '1':
            sets = os.listdir('setOfFlashcards')
            if not sets:
                print('There is no flashcard sets')
                continue
            i = 0
            for s in sets:
                print(str(i + 1) + '. ' + s)
                i += 1
            i = int(input('Select a set: ')) - 1
            if 0 <= i < len(sets):
                sn = sets[i]
                flashcards = final_project.loadFlashcards(sn)
                final_project.menu(sn, flashcards)
        elif ans == '2':
            sn = input('Enter a new setName (setname .txt): ')
            flashcards = []
            final_project.saveFlashcards(sn, flashcards)
            print(f'Set {sn} created.')
        elif ans == '3':
            if not os.path.exists('wrong.txt'):
                print('There is no WrongAnswer!!!')
                continue
            with open('wrong.txt', 'r') as readfile:
                lines = readfile.readlines()
                if not lines:
                    print('There is no Wrong Answer!!!')
                    continue

                print('Review the wrong answer:')
                for line in lines:
                    qa = line.strip().split(', ')
                    q = qa[0]
                    a = qa[1]
                    print(f'Question: {q}')
                    input('Your answer: ')
                    print(f'Correct Answer: {a}\n')
            if os.path.exists('wrong.txt'):
                os.remove('wrong.txt')
        elif ans == '4':
            final_project.status()
        elif ans == '5':
            print('Seeya!')
            break

if __name__ == "__main__":
    main()
