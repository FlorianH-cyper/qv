from otree.api import *
import random
import time
import math

c = Currency

doc = """
Your app description
"""



class Constants(BaseConstants):
    name_in_url = 'QV_final_version'
    players_per_group = None
    num_rounds = 1
    endowment = 100
    max_number_votes_on_one_issue = int(math.sqrt(endowment))
    Q1_text = "Increase the minimum wage from 9,50 Euros to 12 Euros"
    Q2_text = "Abolish the dual system (private and public insurance) and replace it with one general insurance system"
    Q3_text = "Introduce a wealth tax of 2% with a tax allowance of 1Million Euros (2% tax only applies to every Euro of property above 1Million)"
    Q4_text = "There should be a general rent cover (adjusted to city and district)"
    Q5_text = "The 2% goal for defense spending should be fulfilled within the next election period"
    Q6_text = "Arms exports from Germany should be completely forbidden"
    Q7_text = "Reestablish the compulsory military service (first year after graduation with option for civil service instead)"
    Q8_text = "Establish a mandatory women’s quota (40%) in management of big companies"
    Q9_text = "Lower legal voting age to 16 years"
    Q10_text = "The full-face veil (german: Vollverschleierung, e.g. Burka) should be forbidden in the public space"
    Q11_text = "There should be a general speed-limit on the German Autobahn"
    Q12_text = "An annual upper limit is to apply to the admission of new asylum seekers"
    Q13_text = "Make vaccination against infectious diseases mandatory for children"
    Q14_text = "The controlled sale of Cannabis should be legal for people above the age of 21"
    Q15_text = "Inner-country flights should generally be forbidden"
    Q16_text = "Increase petrol prices in Germany by 16ct (like proposed by green candidate)"
    Q17_text = "To reduce dependency on coal: move partially back to nuclear energy production"

    Erfahrung_text_english = "Did you already know the voting mechanism of 'Quadratic Voting' before this experiment?"

    Q1_text_german = "Der Mindestlohn sollte von 9,50 Euro auf 12 Euro erhöht werden"
    Q2_text_german = "Abschaffung des dualen Systems (private und gesetzliche Krankenversicherung) und Ersetzung durch ein allgemeines Krankenversicherungssystem"
    Q3_text_german = "Einführung einer Vermögenssteuer von 2% mit einem Freibetrag von 1 Million Euro (2% Steuer gilt nur für jeden Euro an Vermögen über 1 Million)"
    Q4_text_german = "Es sollte eine allgemeine Mietpreisbremse geben (an Stadt und Landkreis angepasst)"
    Q5_text_german = "Das 2%-Ziel für die Verteidigungsausgaben Deutschlands sollte innerhalb der nächsten Wahlperiode erreicht werden"
    Q6_text_german = "Waffenexporte aus Deutschland sollen komplett verboten werden"
    Q7_text_german = "Wiedereinführung der Wehrpflicht (erstes Jahr nach Schulabschluss mit Option auf Zivildienst)"
    Q8_text_german = "Etablierung einer obligatorischen Frauenquote (40%) im Management großer Unternehmen"
    Q9_text_german = "Gesetzliches Wahlalter auf 16 Jahre senken"
    Q10_text_german = "Die Vollverschleierung (z.B. Burka) sollte im öffentlichen Raum verboten werden"
    Q11_text_german = "Auf deutschen Autobahnen soll es ein generelles Tempolimit geben"
    Q12_text_german = "Für die Aufnahme neuer Asylbewerber soll eine jährliche Obergrenze gelten"
    Q13_text_german = "Es sollte eine Impfpflicht gegen Infektionskrankheiten für Kinder geben"
    Q14_text_german = "Der kontrollierte Erwerb und Konsum von Cannabis sollte für Personen über 21 Jahren legal sein"
    Q15_text_german = "Innerstaatliche Flüge sollen generell verboten werden"
    Q16_text_german = "Benzinpreise in Deutschland sollten um 16ct erhöht werden (wie von der grünen Kanzlerkandidatin vorgeschlagen)"
    Q17_text_german = "Um die Abhängigkeit von Kohle reduzieren: Teilweise Rückkehr zur Kernenergieerzeugung/Atomkraft"

    Erfahrung_text_german = "Haben Sie vor diesem Experiment den Wahlmechanismus 'Quadratic Voting' bereits gekannt?"




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rest = models.IntegerField(initial=Constants.endowment)
    rest_to_hide = models.IntegerField(initial=Constants.endowment)
    gender = models.StringField(label="your gender:", choices=["female", "divers", "male", "prefer not to say"], widget=widgets.RadioSelectHorizontal)
    age = models.IntegerField(label="your age:", min=0, max=100)
    language = models.StringField(label="Please choose your preferred language ", choices=["english", "deutsch"], widget=widgets.RadioSelectHorizontal)
    Erfahrung = models.StringField(label="", choices=["Yes", "No"], widgets=widgets.RadioSelectHorizontal)
    Welche_besser = models.StringField(label="", choices=["Quadratic Voting", "indifferent", "Majority Voting"], widgets=widgets.RadioSelectHorizontal)
    nr_of_errors = models.IntegerField(initial=0)

    #1
    Q1_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral",  widget=widgets.RadioSelectHorizontal)
    Q1_QV = models.IntegerField(initial=0, min=0, max=10)
    Q1_QV_costs = models.IntegerField(initial=0, min=0, max=100)

    #2
    Q2_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral",  widget=widgets.RadioSelectHorizontal)
    Q2_QV = models.IntegerField(initial=0, min=0, max=10)
    Q2_QV_costs = models.IntegerField(initial=0, min=0, max=100)

    #3
    Q3_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral",  widget=widgets.RadioSelectHorizontal)
    Q3_QV = models.IntegerField(initial=0, min=0, max=10)
    Q3_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #4
    Q4_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral",  widget=widgets.RadioSelectHorizontal)
    Q4_QV = models.IntegerField(initial=0, min=0, max=10)
    Q4_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #5
    Q5_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral",  widget=widgets.RadioSelectHorizontal)
    Q5_QV = models.IntegerField(initial=0, min=0, max=10)
    Q5_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #6
    Q6_MV = models.StringField(label="", choices=["Yes", "neutral", "no"],  initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q6_QV = models.IntegerField(initial=0, min=0, max=10)
    Q6_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #7
    Q7_MV = models.StringField(label="", choices=["Yes", "neutral", "no"],  initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q7_QV = models.IntegerField(initial=0, min=0, max=10)
    Q7_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #8
    Q8_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q8_QV = models.IntegerField(initial=0, min=0, max=10)
    Q8_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #9
    Q9_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q9_QV = models.IntegerField(initial=0, min=0, max=10)
    Q9_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #10
    Q10_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q10_QV = models.IntegerField(initial=0, min=0, max=10)
    Q10_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #11
    Q11_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q11_QV = models.IntegerField(initial=0, min=0, max=10)
    Q11_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #12
    Q12_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q12_QV = models.IntegerField(initial=0, min=0, max=10)
    Q12_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #13
    Q13_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q13_QV = models.IntegerField(initial=0, min=0, max=10)
    Q13_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #14
    Q14_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q14_QV = models.IntegerField(initial=0, min=0, max=10)
    Q14_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #15
    Q15_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q15_QV = models.IntegerField(initial=0, min=0, max=10)
    Q15_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #16
    Q16_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q16_QV = models.IntegerField(initial=0, min=0, max=10)
    Q16_QV_costs = models.IntegerField(initial=0, min=0, max=100)
    #17
    Q17_MV = models.StringField(label="", choices=["Yes", "neutral", "no"], initial="neutral", widget=widgets.RadioSelectHorizontal)
    Q17_QV = models.IntegerField(initial=0, min=0, max=10)
    Q17_QV_costs = models.IntegerField(initial=0, min=0, max=100)

#functions

def live_method(player: Player, data):
    news = None
    if data:
        try:
            if "Q1_anserver" in data:
                player.Q1_QV = int(data["Q1_anserver"])
                player.Q1_QV_costs = player.Q1_QV ** 2
            if "Q2_anserver" in data:
                player.Q2_QV = int(data["Q2_anserver"])
                player.Q2_QV_costs = player.Q2_QV ** 2
            if "Q3_anserver" in data:
                player.Q3_QV = int(data["Q3_anserver"])
                player.Q3_QV_costs = player.Q3_QV ** 2
            if "Q4_anserver" in data:
                player.Q4_QV = int(data["Q4_anserver"])
                player.Q4_QV_costs = player.Q4_QV ** 2
            if "Q5_anserver" in data:
                player.Q5_QV = int(data["Q5_anserver"])
                player.Q5_QV_costs = player.Q5_QV ** 2
            if "Q6_anserver" in data:
                player.Q6_QV = int(data["Q6_anserver"])
                player.Q6_QV_costs = player.Q6_QV ** 2
            if "Q7_anserver" in data:
                player.Q7_QV = int(data["Q7_anserver"])
                player.Q7_QV_costs = player.Q7_QV ** 2
            if "Q8_anserver" in data:
                player.Q8_QV = int(data["Q8_anserver"])
                player.Q8_QV_costs = player.Q8_QV ** 2
            if "Q9_anserver" in data:
                player.Q9_QV = int(data["Q9_anserver"])
                player.Q9_QV_costs = player.Q9_QV ** 2
            if "Q10_anserver" in data:
                player.Q10_QV = int(data["Q10_anserver"])
                player.Q10_QV_costs = player.Q10_QV ** 2
            if "Q11_anserver" in data:
                player.Q11_QV = int(data["Q11_anserver"])
                player.Q11_QV_costs = player.Q11_QV ** 2
            if "Q12_anserver" in data:
                player.Q12_QV = int(data["Q12_anserver"])
                player.Q12_QV_costs = player.Q12_QV ** 2
            if "Q13_anserver" in data:
                player.Q13_QV = int(data["Q13_anserver"])
                player.Q13_QV_costs = player.Q13_QV ** 2
            if "Q14_anserver" in data:
                player.Q14_QV = int(data["Q14_anserver"])
                player.Q14_QV_costs = player.Q14_QV ** 2
            if "Q15_anserver" in data:
                player.Q15_QV = int(data["Q15_anserver"])
                player.Q15_QV_costs = player.Q15_QV ** 2
            if "Q16_anserver" in data:
                player.Q16_QV = int(data["Q16_anserver"])
                player.Q16_QV_costs = player.Q16_QV ** 2
            if "Q17_anserver" in data:
                player.Q17_QV = int(data["Q17_anserver"])
                player.Q17_QV_costs = player.Q17_QV ** 2

            player.rest = Constants.endowment - player.Q1_QV_costs - player.Q2_QV_costs - player.Q3_QV_costs - player.Q4_QV_costs - player.Q5_QV_costs - player.Q6_QV_costs - player.Q7_QV_costs - player.Q8_QV_costs - player.Q9_QV_costs - player.Q10_QV_costs - player.Q11_QV_costs - player.Q12_QV_costs - player.Q13_QV_costs - player.Q14_QV_costs - player.Q15_QV_costs - player.Q16_QV_costs - player.Q17_QV_costs
            player.rest_to_hide = Constants.endowment - player.Q1_QV_costs - player.Q2_QV_costs - player.Q3_QV_costs - player.Q4_QV_costs - player.Q5_QV_costs - player.Q6_QV_costs - player.Q7_QV_costs - player.Q8_QV_costs - player.Q9_QV_costs - player.Q10_QV_costs - player.Q11_QV_costs - player.Q12_QV_costs - player.Q13_QV_costs - player.Q14_QV_costs - player.Q15_QV_costs - player.Q16_QV_costs - player.Q17_QV_costs




        except Exception:
            print('invalid message received:', data)
            return
    return {
        player.id_in_group: dict(
            Q1_back=player.Q1_QV,
            Q1_credits=player.Q1_QV_costs,
            Q2_back=player.Q2_QV,
            Q2_credits=player.Q2_QV_costs,
            Q3_back = player.Q3_QV,
            Q3_credits = player.Q3_QV_costs,
            Q4_back = player.Q4_QV,
            Q4_credits = player.Q4_QV_costs,
            Q5_back=player.Q5_QV,
            Q5_credits=player.Q5_QV_costs,
            Q6_back=player.Q6_QV,
            Q6_credits=player.Q6_QV_costs,
            Q7_back=player.Q7_QV,
            Q7_credits=player.Q7_QV_costs,
            Q8_back=player.Q8_QV,
            Q8_credits=player.Q8_QV_costs,
            Q9_back=player.Q9_QV,
            Q9_credits=player.Q9_QV_costs,
            Q10_back=player.Q10_QV,
            Q10_credits=player.Q10_QV_costs,
            Q11_back=player.Q11_QV,
            Q11_credits=player.Q11_QV_costs,
            Q12_back=player.Q12_QV,
            Q12_credits=player.Q12_QV_costs,
            Q13_back=player.Q13_QV,
            Q13_credits=player.Q13_QV_costs,
            Q14_back=player.Q14_QV,
            Q14_credits=player.Q14_QV_costs,
            Q15_back=player.Q15_QV,
            Q15_credits=player.Q15_QV_costs,
            Q16_back=player.Q16_QV,
            Q16_credits=player.Q16_QV_costs,
            Q17_back=player.Q17_QV,
            Q17_credits=player.Q17_QV_costs,


            rest=player.rest

        )}

# PAGES
class MyPage(Page):
    pass

class choose_language(Page):
    form_model = "player"
    form_fields = ["language"]


class Introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.language == "english"


class Introduction_german(Page):

    @staticmethod
    def is_displayed(player):
        return player.language == "deutsch"




class MV(Page):
    form_model = "player"
    form_fields = ["Q1_MV", "Q2_MV","Q3_MV", "Q4_MV", "Q5_MV", "Q6_MV", "Q7_MV", "Q8_MV", "Q9_MV", "Q10_MV", "Q11_MV", "Q12_MV", "Q13_MV", "Q14_MV", "Q15_MV", "Q16_MV", "Q17_MV"]
    @staticmethod
    def is_displayed(player):
        return player.language == "english"

class MV_german(Page):
    form_model = "player"
    form_fields = ["Q1_MV", "Q2_MV","Q3_MV", "Q4_MV", "Q5_MV", "Q6_MV", "Q7_MV", "Q8_MV", "Q9_MV", "Q10_MV", "Q11_MV", "Q12_MV", "Q13_MV", "Q14_MV", "Q15_MV", "Q16_MV", "Q17_MV"]
    @staticmethod
    def is_displayed(player):
        return player.language == "deutsch"

class QV_before(Page):
    @staticmethod
    def is_displayed(player):
        return player.language == "english"

class QV_before_german(Page):
    @staticmethod
    def is_displayed(player):
        return player.language == "deutsch"



class QV(Page):
    @staticmethod
    def is_displayed(player):
        return player.language == "english"

    live_method = live_method
    form_model = "player"
    form_fields = ["rest_to_hide"]

    @staticmethod
    def error_message(player, values):
        if player.rest_to_hide < 0:
            player.nr_of_errors += 1
            return "You have spend too many credits!"
        if player.rest_to_hide == 100:
            player.nr_of_errors += 1
            return "You have not submitted any votes. Please do not forget to click the 'vote' buttons."


class QV_german(Page):
    @staticmethod
    def is_displayed(player):
        return player.language == "deutsch"

    live_method = live_method
    form_model = "player"
    form_fields = ["rest_to_hide"]


    @staticmethod
    def error_message(player, values):
        if player.rest_to_hide < 0:
            player.nr_of_errors += 1
            return "Sie haben zu viele Credits ausgegeben!!"
        if player.rest_to_hide == 100:
            player.nr_of_errors += 1
            return "Sie haben keinerlei Stimmen eingereicht. Bitte vergessen Sie nicht die 'wählen' buttons zu drücken."


class Thank_you(Page):
    @staticmethod
    def is_displayed(player):
        return player.language == "english"

class Thank_you_german(Page):
    @staticmethod
    def is_displayed(player):
        return player.language == "deutsch"


class personal_data(Page):
    @staticmethod
    def is_displayed(player):
        return player.language == "english"

    form_model = "player"
    form_fields = ["gender", "age", "Erfahrung", "Welche_besser"]

class personal_data_german(Page):
    @staticmethod
    def is_displayed(player):
        return player.language == "deutsch"

    form_model = "player"
    form_fields = ["gender", "age", "Erfahrung", "Welche_besser"]

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


#page_sequence = [MV, QV]

page_sequence = [choose_language, Introduction, Introduction_german, MV, MV_german, QV_before, QV_before_german, QV, QV_german, personal_data, personal_data_german, Thank_you, Thank_you_german]