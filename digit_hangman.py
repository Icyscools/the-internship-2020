"""
Digit Hangman
Author: Woramat Ngamkham
"""


class Hangman:
    def __init__(self):
        self.real_answer = list(map(int, input().split()))
        self.guesses = []
        self.current_round = 0
        self.show_guess()  # Show empty guess
        self.next_round()  # Start first round

    def next_round(self):
        if self.current_round < 5:
            self.guesses.append(int(input()))
            self.show_guess()
            self.current_round += 1
            self.next_round()
        else:
            self.end_game()

    def show_guess(self):
        for ans in self.real_answer:
            if ans in self.guesses:
                print(ans, end=' ')
            else:
                print("_", end=' ')

        for guess in filter(lambda x: x not in self.real_answer, self.guesses):
            print(guess, end=' ')
        print()

    def end_game(self):
        print(sum(map(lambda x: x in self.guesses, self.real_answer)))


if __name__ == "__main__":
    Hangman()
