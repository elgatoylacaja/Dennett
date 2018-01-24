import ast
import datetime


def gender_pretty(gender):
    return gender


def hand_pretty(hand):
    return hand


def studies_pretty(studies):
    return studies


def birthdate_pretty(birthdate):
    return datetime.date(*birthdate).isoformat() if birthdate else ''


def time_pretty(time):
    return datetime.datetime(*time).isoformat() if time else ''


def prettify(legacy_trial):
    trial = ast.literal_eval(legacy_trial['experiment_log'])
    return {
        'user': {
            'auid': trial['PersonalData']['AUID'],
            'name': trial['PersonalData']['Name'],
            'gender': gender_pretty(trial['PersonalData']['Gender']),
            'hand': hand_pretty(trial['PersonalData']['Hand']),
            'studies': hand_pretty(trial['PersonalData']['Studies']),
            'birthdate': birthdate_pretty(trial['PersonalData']['Birthdate'])
        },
        'operation': {
            'level': trial['Level'],
            'operand_1': trial['Operand_1'],
            'operand_2': trial['Operand_2'],
            'operator': trial['Operator'],
            'type': trial['Operation_Type'],
            'result': trial['Correct_Result']
        },
        'answer': {
            'result': trial['Entered_Answer'],
            'correct': trial['Correct'],
            'score': trial['Score'],
            'confidence': trial['Confidence_Answer'],
            'effort': trial['Effort_Answer']
        },
        'time': {
            'max': trial['Max_Time'],
            'exceeded': trial['Time_Exceeded'],
            'total': trial['Total_Time'],
            'start': time_pretty(trial['Start_Date']),
            'end': time_pretty(trial['End_Date'])
        },
        'hints': {
            'shown': trial['Hint_Shown'],
            'available': trial['Hints_Available']
        },
        'session': {
            'correct': trial['Session_Correct'],
            'trial': trial['Session_Trial']
        },
        'initial': {
            'confidence': trial['Initial_Confidence'],
            'effort': trial['Initial_Effort']
        },
        'response': {
            'vector': trial['Response_Vector'],
            'times': trial['Response_Times'],
            'correctInARow': trial['Corr_in_a_Row']
        }

    }
