import ast


def prettify(legacy_trial):
    trial = ast.literal_eval(legacy_trial['experiment_log'])
    return {
        'user': {
            'auid': trial['PersonalData']['AUID'],
            'name': trial['PersonalData']['Name'],
            'gender': trial['PersonalData']['Gender'],
            'hand': trial['PersonalData']['Hand'],
            'studies': trial['PersonalData']['Studies'],
            'birthdate': trial['PersonalData']['Birthdate']
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
            'start': trial['Start_Date'],
            'end': trial['End_Date']
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
