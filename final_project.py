import os
import random

os.makedirs('setOfFlashcards', exist_ok=True)


def loadFlashcards(filename):
    path = os.path.join('setOfFlashcards', filename)
    if not os.path.exists(path):
        return []
    flashcards = []
    with open(path, 'r') as readfile:
        lines = readfile.readlines()
        for line in lines:
            parts = line.strip().split(', ')
            if len(parts) == 3:
                question = parts[0]
                answer = parts[1]
                correct_num = int(parts[2])
                flashcards.append({'question': question, 'answer': answer, 'count': correct_num})
    return flashcards


def saveFlashcards(filename, flashcards):
    path = os.path.join('setOfFlashcards', filename)
    with open(path, 'w') as writefile:
        for f in flashcards:
            writefile.write(f"{f['question']}, {f['answer']}, {f['count']}\n")


def status():
    if not os.path.exists('status.txt'):
        print('No recorded')
        return None

    with open('status.txt', 'r') as readfile:
        lines = readfile.readlines()
        tq = 0
        tc = 0
        for line in lines:
            l = line.strip()
            parts = l.split(',')
            total = int(parts[0])
            correct = int(parts[1])
            tq += total
            tc += correct
        print('Quizzes taken:', len(lines))
        print(f'Total correct: {tc}/{tq}')
        if tq > 0:
            percentage = (tc / tq) * 100
            print(f'Accuracy: {percentage:.1f}')
        else:
            print('There is no quiz data')


def menu(sn, flashcards):
    while True:
        print(f'\nCurrent Set: {sn}')
        print('1. Add flashcard')
        print('2. Start quiz')
        print('3. Edit flashcard')
        print('4. Delete flashcard')
        print('5. Back to main menu')

        c = input('Choose an option (1-5): ')
        if c == '1':
            question = input('Enter question: ')
            answer = input('Enter answer: ')
            flashcards.append({'question': question, 'answer': answer, 'count': 0})
            saveFlashcards(sn, flashcards)

        elif c == '2':
            if not flashcards:
                print('There is no flashcards in the set')
                continue
            total = 0
            correct = 0
            random.shuffle(flashcards)
            for card in flashcards:
                print(f'Q: {card['question']}')
                ans = input('Your answer: ')
                total += 1
                if ans.strip().lower() == card['answer'].strip().lower():
                    print('Correct!')
                    correct += 1
                    card['count'] += 1
                else:
                    print(f'Wrong!  Correct answer is: {card['answer']}')
                    with open('wrong.txt', 'a') as appendfile:
                        appendfile.write(f'{card['question']}, {card['answer']}\n')
            print(f'\nQuiz complete: {correct}/{total} correct.')
            with open('status.txt', 'a') as appendfile:
                appendfile.write(f'{total}, {correct}\n')
            saveFlashcards(sn, flashcards)

        elif c == '3':
            i = 0
            for card in flashcards:
                print(str(i + 1) + '. ' + card['question'])
                i += 1
            num = int(input('Enter number to edit: ')) - 1
            if 0 <= num < len(flashcards):
                nq = input('New question: ')
                na = input('New answer: ')

                flashcards[num]['question'] = nq
                flashcards[num]['answer'] = na
                flashcards[num]['count'] = 0
                saveFlashcards(sn, flashcards)

        elif c == '4':
            i = 0
            for card in flashcards:
                print(str(i + 1) + '. ' + card['question'])
                i += 1
            num = int(input('Enter the number to delete: ')) - 1
            if 0 <= num < len(flashcards):
                flashcards.pop(num)
                saveFlashcards(sn, flashcards)

        elif c == '5':
            break


        else:
            print('Invalid choice. You should enter the number 1-5.')


# for test
if __name__ == '__main__':
    status()

