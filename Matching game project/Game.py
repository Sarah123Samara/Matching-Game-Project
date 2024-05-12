import random


class Card:
    def __init__(self, word, number):
        self.word = word
        self.matched = False
        self.number = number

    def __str__(self):
        return self.word


class Game:
    def __init__(self):
        self.size = 4
        self.card_options = ["egg", "cat", "dog", "mat", "pan", "bat", "pet", "hut"]
        self.cards = []
        self.playing = True
        self.attempts = 0
        self.high_score = None

    def set_cards(self):
        if len(self.card_options) % 2 != 0:
            raise ValueError("There must be an even number of card options.")

        card_numbers = list(range(1, len(self.card_options) * 2 + 1))
        random.shuffle(card_numbers)

        self.cards = [
            Card(word, number)
            for word, number in zip(self.card_options * 2, card_numbers)
        ]

    def create_grid(self):
        for row in range(1, self.size + 1):
            for col in range(1, self.size + 1):
                num = (row - 1) * self.size + col
                card = self.get_card_by_number(num)
                if card is not None and card.matched:
                    print(f"| {card.word.center(3)} ", end="")
                else:
                    print(f"| {str(num).center(3)} ", end="")
            print("|")
            print()

    def get_card_by_number(self, number):
        for card in self.cards:
            if card.number == number:
                return card
        return None

    def check_match(self, num1, num2):
        card1 = self.get_card_by_number(num1)
        card2 = self.get_card_by_number(num2)

        if (
            card1 is not None
            and card2 is not None
            and card1 != card2
            and card1.word == card2.word
        ):
            return True
        return False

    def check_win(self):
        return all(card.matched for card in self.cards)

    def check_location(self):
        while True:
            location = (
                input("Enter a location from (1-16), Enter 'Quit' to leave the game: ")
                .strip()
                .lower()
            )

            if location == "quit":
                self.playing = False
                return None
            try:
                num = int(location)
                if 1 <= num <= 16 and not self.get_card_by_number(num).matched:
                    return num
                else:
                    print()
                    print("Invalid input. Please enter unmatched numbers from 1 to 16.")
                    print()
            except ValueError:
                print()
                print("Invalid input. Please enter unmatched numbers from 1 to 16.")
                print()

    def play(self):
        print()
        print("-" * 28)
        print("Welcome to the Matching Game")
        print("-" * 28)
        print()
        while self.playing:
            if self.high_score is not None:
                print(f"Your high score is {self.high_score}.")
                print()
            self.set_cards()
            self.attempts = 0  # Reset the number of attempts for each game

            while not self.check_win():
                self.create_grid()
                num1 = self.check_location()
                if num1 is None:
                    break
                num2 = self.check_location()
                if num2 is None:
                    break

                self.attempts += 1  # Increment the number of attempts

                if self.check_match(num1, num2):
                    card1 = self.get_card_by_number(num1)
                    card2 = self.get_card_by_number(num2)
                    card1.matched = True
                    card2.matched = True
                    print()
                    print(f"Well done! You got a match with the word {card1.word}.")
                    print()
                else:
                    print()
                    print("Sorry, but the cards did not match")
                    print()

            if self.playing:
                self.create_grid()
                print()
                print(
                    f"Well Done! You have matched all the words in {self.attempts} attempts."
                )
                print()
                while True:
                    play_again = (
                        input("Do you want to play again? (Yes/No): ").strip().lower()
                    )
                    print()
                    if play_again == "no":
                        self.playing = False
                        if self.high_score is None or self.attempts < self.high_score:
                            self.high_score = self.attempts
                            print("Thank you for playing. Have a nice day! ")
                            print()
                        break
                    elif play_again == "yes":
                        if self.high_score is None or self.attempts < self.high_score:
                            self.high_score = self.attempts
                        break
                    else:
                        print("Invalid input. Please enter Yes or No.")
                        print()
            else:
                print()
                print("Thank you for playing. Have a nice day! ")
                print()


if __name__ == "__main__":
    game = Game()
    game.play()
