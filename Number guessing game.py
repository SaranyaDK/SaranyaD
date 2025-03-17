import random
def number_guessing():
    secret_number = random.randint(1,20)
    attempts = 1
    print('Guess number between 1 to 20: ')
    fixed_attempts = 2

    while True:
        try:
            guess = int(input('Enter your guess: '))
            if guess < secret_number and attempts < fixed_attempts:
                print('Too low! try again, you have ',fixed_attempts-attempts, 'attempts')
                attempts += 1
            elif guess > secret_number and attempts < fixed_attempts:
                print('Too high! try again, you have ',fixed_attempts-attempts, 'attempts')
                attempts += 1
            elif attempts >= fixed_attempts:
                print('Sorry attempts ended')
                print('The number is: ', secret_number)
                break
            else:
                print('Congratulations! you guessed the correct number..', secret_number)
                break
        except ValueError:
            print('Invalid input. Please enter a valid number')

if __name__ == '__main__':
    number_guessing()


        

