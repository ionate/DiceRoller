import random


class DiceStruct:
    toprow = " -----  "
    topstruct = "|     | "
    numrow = "|     | "
    botstruct = "|     | "
    botrow = " -----  "

    def __init__(self, numlist) -> None:
        self.numlist = numlist
        self.resrow = None
    
    def _buildresultsrow(self):
        rc = False
        strlist = []
        for num in self.numlist:
            resstr = "|  {}  |".format(num)
            strlist.append(resstr)
        self.resrow = ' '.join([element for element in strlist])
        #print(self.resrow)
        return True

    def printme(self):
        rc = self._buildresultsrow()
        if not rc:
            print(f'Problem building results row, Returning False.')
            return False
        
        numdice = len(self.numlist)
        print(ds.toprow * numdice)
        print(ds.topstruct *numdice)
        print(self.resrow)
        print(ds.botstruct *numdice)
        print(ds.botrow *numdice)
        return True

results = [1,2,4,6,3,1,1,4]
# hmmm... got me to thinking. would work for letters! So I could use as the title as well?
# (testing...)
results = ['N','A','T','H','A','N']
ds = DiceStruct(results)
ds.printme()

# (testing...WORKED! So let's replace with title...)
results = ['F','o','R','t','U','n','E',' ','T','e','L','l','E','r','!']
ds = DiceStruct(results)
ds.printme()

class DiceRoller:
    def __init__(self):
        self.num_dice = 1
        self.total_score = 0

    def set_num_dice(self, num_dice):
        self.num_dice = num_dice

    def roll_dice(self):
        return [random.randint(1, 6) for _ in range(self.num_dice)]

    def check_guess(self, user_guess, rolled_numbers):
        correct_guesses = set(rolled_numbers) & set(user_guess)
        return len(correct_guesses)

    def print_round_result(self, rolled_numbers, user_guess):
        print(f"Results: {rolled_numbers}")
        print(f"Your Guess: {user_guess}") 

def main():
    print("Welcome to FortuneTeller!")

    fortune_teller = DiceRoller()

    while True:
        print("\nMenu:")
        print("1. Start new Round")
        print("2. Show Score")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                num_dice = int(input("How many dice do I roll at once? "))
                if 1 <= num_dice <= 10:
                    fortune_teller.set_num_dice(num_dice)

                    user_guess = list(map(int, input("Enter your guess for the results (comma-separated numbers): ").split(',')))
                    if len(user_guess) != fortune_teller.num_dice:
                        print(f"Invalid input. Please enter {fortune_teller.num_dice} numbers.")
                        continue

                    rolled_numbers = fortune_teller.roll_dice()
                    ds = DiceStruct(rolled_numbers)
                    if ds:
                        ds.printme()
                    fortune_teller.print_round_result(rolled_numbers, user_guess)

                    score = fortune_teller.check_guess(user_guess, rolled_numbers)
                    print(f"Your score for this round: {score}")
                    fortune_teller.total_score += score
                    print(f"Your total score: {fortune_teller.total_score}")

                else:
                    print("Invalid input. Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "2":
            print(f"Your total score: {fortune_teller.total_score}")

        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
