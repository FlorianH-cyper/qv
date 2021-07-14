from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'compare'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    language = models.StringField(label="please choose your preferred language", choices=["english", "deutsch"], widget=widgets.RadioSelectHorizontal)
    QV_RULES_ENG = models.StringField(label="", choices=["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"], widget=widgets.RadioSelectHorizontal)
    MV_RULES_ENG = models.StringField(label="", choices=["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"], widget=widgets.RadioSelectHorizontal)
    QV_RULES_GER = models.StringField(label="", choices=["Trifft zu", "Trifft eher zu", "teils-teils", "Trifft eher nicht zu", "Trifft eher nicht zu"], widget=widgets.RadioSelectHorizontal)
    MV_RULES_GER = models.StringField(label="", choices=["Trifft zu", "Trifft eher zu", "teils-teils", "Trifft eher nicht zu", "Trifft eher nicht zu"], widget=widgets.RadioSelectHorizontal)
    Comparison_GER = models.StringField(label="", choices=["Ich bevorzuge X stark", "Ich bevorzuge X leicht", "neutral", "Ich bevorzuge Y leicht", "Ich bevorzuge Y stark"], widget=widgets.RadioSelectHorizontal)
    Comparison_ENG = models.StringField(label="", choices=["I strongly prefer X", "I slightly prefer X",
                                                           "No difference", "I slightly prefer Y", "I strongly prefer Y"],widget=widgets.RadioSelectHorizontal)
# PAGES

class Intro_GER(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.language == "deutsch"

class Intro_ENG(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.language == "english"


class VOTE_GERMAN(Page):
    form_model = "player"
    form_fields = ["QV_RULES_GER", "MV_RULES_GER", "Comparison_GER"]
    @staticmethod
    def is_displayed(player: Player):
        return player.language == "deutsch"


class VOTE_ENGLISH(Page):
    form_model = "player"
    form_fields = ["QV_RULES_ENG", "MV_RULES_ENG", "Comparison_ENG"]
    @staticmethod
    def is_displayed(player: Player):
        return player.language == "english"


class THANKS_GERMAN(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.language == "deutsch"

class THANKS_ENGLISH(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.language == "english"


class ResultsWaitPage(WaitPage):
    pass

class lang(Page):
    form_model = "player"
    form_fields = ["language"]


class Results(Page):
    pass


page_sequence = [lang, Intro_ENG, Intro_GER, VOTE_ENGLISH, VOTE_GERMAN, THANKS_ENGLISH, THANKS_GERMAN]
