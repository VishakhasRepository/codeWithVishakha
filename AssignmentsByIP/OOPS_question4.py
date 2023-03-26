# Q4. Create a simple Card game in which there are 8 cards which are randomly chosen from a
# deck. The first card is shown face up. The game asks the player to predict whether the next card
# in the selection will have a higher or lower value than the currently showing card.
# For example, say the card that’s shown is a 3. The player chooses “higher,” and the next card is
# shown. If that card has a higher value, the player is correct. In this example, if the player had
# chosen “lower,” they would have been incorrect. If the player guesses correctly, they get 20
# points. If they choose incorrectly, they lose 15 points. If the next card to be turned over has the
# same value as the previous card, the player is incorrect.


class Card_Game:
    def __init__(self, list_of_cards):
        self.list_of_cards = list_of_cards

    def game(self):
        points = int(0)
        print("Your first card is ", self.list_of_cards[0])
        for i in range(0, 7):
            print("THIS IS THE CARD VALUE - ", self.list_of_cards[i])
            res = input("Will the next card is higher or lower value?")
            if res == "higher":
                if self.list_of_cards[i] < self.list_of_cards[i + 1]:
                    points = points + 20
                    print("Congrats! you won 20 points and its added.", points)
                elif self.list_of_cards[i] == self.list_of_cards[i + 1]:
                    print("You are incorrect!! The value is same as of the previous card")
                else:
                    points = points - 15
                    print("You are incorrect value is lower than the previous card, 15 points deducted", points)
            elif res == "lower":
                if self.list_of_cards[i] > self.list_of_cards[i + 1]:
                    points = points + 20
                    print("Congrats! you won 20 points and its added.", points)
                elif self.list_of_cards[i] == self.list_of_cards[i + 1]:
                    print("You are incorrect!! The value is same as of the previous card, no points deducted")
                else:
                    points = points - 15
                    print("You are incorrect value is higher than the previous card, 15 points deducted", points)

        print("CONGRATS!!, your total points are - ", points)


cardgame = Card_Game([1, 2, 1, 4, 7, 6, 7, 7])
cardgame.game()
