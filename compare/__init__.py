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
    QV_RULES = models.StringField(label="", choices=["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"], widget=widgets.RadioSelectHorizontal)
    MV_RULES = models.StringField(label="", choices=["Strongly Agree", "Somewhat Agree", "Neutral", "Somewhat Disagree", "Strongly Disagree"], widget=widgets.RadioSelectHorizontal)

# PAGES
class VOTE(Page):
    form_model = "player"
    form_fields = ["QV_RULES", "MV_RULES"]


class ResultsWaitPage(WaitPage):
    pass

class lang(Page):
    form_model = "player"
    form_fields = ["language"]


class Results(Page):
    pass


page_sequence = [lang, VOTE]
