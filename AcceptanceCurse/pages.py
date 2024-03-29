from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class MyWaitPage1(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.initialize_group()


class Page1Active(Page):

    form_model = 'player'
    form_fields = ['choice']

    def choice_error_message(self, value):
        print('value is', value)
        if value is None:
            return 'Please select one of the options.'

    def vars_for_template(self):
        return {'prob': Constants.prob_Haccept[self.subsession.game]}

    def is_displayed(self):
        return self.player.status == 0

    def before_next_page(self):
        if self.timeout_happened:
            self.player.late = 1
            flip = random.randint(0,1)
            if flip ==0:
                self.player.choice = False
            else:
                self.player.choice = True


class Page1Passive(Page):

    def vars_for_template(self):
        return {'prob': Constants.prob_Haccept[self.subsession.game]}

    def is_displayed(self):
        return self.player.status == 1


class MyWaitPage2(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.get_outcome()


class Page2(Page):
    pass


class FinalPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'part1_payoff': self.participant.vars['part1_payoff'],
            'paying_round': self.session.vars['paying_round']
        }


page_sequence = [
    Intro,
    MyWaitPage1,
    Page1Active,
    Page1Passive,
    MyWaitPage2,
    Page2,
    FinalPage
]
