from random import randint
import time
import pathlib
from breakingbaccarat.simngen.CardHelper import CardHelper

class Rando:

    def __init__(self, name='Rando', commission=False):
        self.name = name
        self.commission = commission
        self.card_helper = CardHelper()
        self.history = []
        print('{}: Ready to work.'.format(self.name))

    def prepare_cards(self):
        self.playbox = self.card_helper.get_playbox()
        # remove headout cards
        first_card = self.playbox.pop(0)
        self.headout = first_card.point
        if (self.headout == 0):
            self.headout = 10
        for i in range(self.headout):
            self.playbox.pop(0)
        self.tailoff = randint(12, 20)
        print('{}: Preparing cards.'.format(self.name))

    def prepare_stuffs(self):
        self.res_string = ''
        self.profit = 0
        self.basebet = 1
        self.winner = None
        self.mlevel = 0
        print('{}: Preparing other stuffs.'.format(self.name))

    def setup_bet(self):
        self.bet_value = 0
        self.bet_option = 'B'
        num = randint(1, 1000)
        if num % 2 == 0:
            self.bet_option = 'P'
        self.bet_value = self.basebet


    def work(self):
        print('{}: Start dealing.'.format(self.name))
        self.counter = 0
        while(len(self.playbox) >= self.tailoff):
            self.setup_bet()
            c1 = None
            c2 = None
            c3 = None
            c4 = None
            c5 = None
            c6 = None
            shoe_string = '{},{},{},'.format(self.counter, self.bet_option, self.bet_value)

            c1 = self.playbox.pop(0)
            c2 = self.playbox.pop(0)
            c3 = self.playbox.pop(0)
            c4 = self.playbox.pop(0)

            if (c1 != None and c2 != None and c3 != None and c4 != None):

                player_score = (c1.point + c3.point) % 10
                banker_score = (c2.point + c4.point) % 10

                player_cards = c1.name + c1.group + "-" + c3.name + c3.group
                banker_cards = c2.name + c2.group + "-" + c4.name + c4.group

                if (player_score < 6 and banker_score < 8):
                    c5 = self.playbox.pop(0)  # card for player

                if (c5 == None and player_score < 8):
                    if (banker_score <= 5):
                        c6 = self.playbox.pop(0)  # card for banker

                if (c5 != None and player_score < 8):

                    if (banker_score < 3):
                        c6 = self.playbox.pop(0)
                    if (banker_score == 3):
                        if (c5.point != 8):
                            c6 = self.playbox.pop(0)
                    if (banker_score == 4):
                        if (c5.point >= 2 and c5.point <= 7):
                            c6 = self.playbox.pop(0)
                    if (banker_score == 5):
                        if (c5.point >= 4 and c5.point <= 7):
                            c6 = self.playbox.pop(0)
                    if (banker_score == 6):
                        if (c5.point == 6 or c5.point == 7):
                            c6 = self.playbox.pop(0)
                            # --------------------------------------------------------------------
                if (c5 == None):
                    player_cards = c1.name + c1.group + "-" + c3.name + c3.group
                    player_score = (c1.point + c3.point) % 10
                elif (c5 != None):
                    player_cards = c1.name + c1.group + "-" + c3.name + c3.group + "-" + c5.name + c5.group
                    player_score = (c1.point + c3.point + c5.point) % 10
                if (c6 == None):
                    banker_cards = c2.name + c2.group + "-" + c4.name + c4.group
                    banker_score = (c2.point + c4.point) % 10
                elif (c6 != None):
                    banker_cards = c2.name + c2.group + "-" + c4.name + c4.group + "-" + c6.name + c6.group
                    banker_score = (c2.point + c4.point + c6.point) % 10
                # --------------------------------------------------------------------

                # tie
                if (player_score == banker_score):
                    self.winner = 'T'
                else:
                    # player wins
                    if (player_score > banker_score):
                        self.winner = 'P'
                        if(self.bet_option == 'P'):
                            self.profit += self.bet_value
                        if(self.bet_option == 'B'):
                            self.profit -= self.bet_value
                    # banker wins
                    if (player_score < banker_score):
                        self.winner = 'B'
                        if(self.bet_option == 'B'):
                            if(self.commission==False):
                                if(banker_score == 6):
                                    self.profit += self.bet_value/2
                            if(self.commission==True):
                                self.profit += self.bet_value * 0.95
                        if(self.bet_option == 'P'):
                            self.profit -= self.bet_value
                # ----------------------------------------------------------------------
                shoe_string += '{},{},{},{},{},{:.2f}'.format(player_cards, banker_cards, player_score, banker_score, self.winner, self.profit)
                self.history.append(shoe_string)
                self.playbox.pop(0)
                # ----------------------------------------------------------------------
            self.counter += 1
        print('{}: Finished.'.format(self.name))

    def export_shoes(self):
        export_file = '{}.csv'.format(round(time.time() * 1000))
        export_dir = 'datasets/{}'.format(self.name)
        pathlib.Path(export_dir).mkdir(parents=True, exist_ok=True)
        export_path = 'datasets/{}/{}'.format(self.name, export_file)
        with open(export_path, 'w') as f:
            f.write('COUNTER,BET_OPTION,BET_VALUE,PLAYER_CARDS,BANKER_CARDS,PLAYER_SCORE,BANKER_SCORE,WINNER,PROFIT\n')
            f.write('\n'.join(str(shoe) for shoe in self.history))
        f.close()
        time.sleep(0.01)
        print('{}: Shoes had exported to {}.'.format(self.name, export_path))
