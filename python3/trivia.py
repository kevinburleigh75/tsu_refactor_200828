#!/usr/bin/env python3

class Game:
    def __init__(self):
        self.players        = []
        self.places         = []
        self.purses         = []
        self.in_penalty_box = []

        self.pop_questions     = []
        self.science_questions = []
        self.sports_questions  = []
        self.rock_questions    = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places.append(0)
        self.purses.append(0)
        self.in_penalty_box.append(False)

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.places[self.current_player] = (self.places[self.current_player] + roll) % 12

                print(self.players[self.current_player] + \
                            '\'s new location is ' + \
                            str(self.places[self.current_player]))
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = (self.places[self.current_player] + roll) % 12

            print(self.players[self.current_player] + \
                        '\'s new location is ' + \
                        str(self.places[self.current_player]))
            print("The category is %s" % self._current_category)
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop':     print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports':  print(self.sports_questions.pop(0))
        if self._current_category == 'Rock':    print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.places[self.current_player] == 0:  return 'Pop'
        if self.places[self.current_player] == 1:  return 'Science'
        if self.places[self.current_player] == 2:  return 'Sports'
        if self.places[self.current_player] == 3:  return 'Rock'
        if self.places[self.current_player] == 4:  return 'Pop'
        if self.places[self.current_player] == 5:  return 'Science'
        if self.places[self.current_player] == 6:  return 'Sports'
        if self.places[self.current_player] == 7:  return 'Rock'
        if self.places[self.current_player] == 8:  return 'Pop'
        if self.places[self.current_player] == 9:  return 'Science'
        if self.places[self.current_player] == 10: return 'Sports'
        if self.places[self.current_player] == 11: return 'Rock'

    def _advance_to_next_player(self):
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + \
                    ' now has ' + \
                    str(self.purses[self.current_player]) + \
                    ' Gold Coins.')

                game_should_continue = not self._did_player_win()
                self._advance_to_next_player()
                return game_should_continue
            else:
                game_should_continue = True
                self._advance_to_next_player()
                return game_should_continue
        else:
            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                ' now has ' + \
                str(self.purses[self.current_player]) + \
                ' Gold Coins.')

            game_should_continue = not self._did_player_win()
            self._advance_to_next_player()
            return game_should_continue

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self._advance_to_next_player()
        return True

    def _did_player_win(self):
        return self.purses[self.current_player] == 6

from random import randrange

if __name__ == '__main__':
    ####################################
    ## Isolate random number generator.
    import sys
    from random import seed
    if len(sys.argv) == 2:
        seed(int(sys.argv[1]))
    ####################################

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    should_continue = True
    while should_continue:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            should_continue = game.wrong_answer()
        else:
            should_continue = game.was_correctly_answered()
