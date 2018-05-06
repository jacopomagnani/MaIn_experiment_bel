from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class MyWaitPage1(WaitPage):

    def after_all_players_arrive(self):
        self.subsession.initialize_round()


class Page1(Page):

    timeout_seconds = 60

    form_model = 'player'
    form_fields = ['choice']

    def before_next_page(self):
        if self.timeout_happened:
            self.player.late = 1
            flip = random.randint(0,1)
            if flip ==0:
                self.player.choice = False
            else:
                self.player.choice = True


class MyWaitPage2(WaitPage):

    def after_all_players_arrive(self):
        self.subsession.get_outcome()


class Page2(Page):

    timeout_seconds = 10


class FinalPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    MyWaitPage1,
    Page1,
    MyWaitPage2,
    Page2,
    FinalPage
]