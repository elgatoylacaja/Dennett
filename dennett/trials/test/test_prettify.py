import requests
from conftest import session, URL_PREFIX


TRIAL_LEGACY_FORMAT = {"test_subject": "Federico", "experiment_log": "{\"Confidence_Answer\":-1,\"Operator\":\"+\",\"Session_Correct\":1,\"Max_Time\":14000,\"Corr_in_a_Row\":1,\"Effort_Answer\":-1,\"Initial_Confidence\":-1,\"Correct\":1,\"Entered_Answer\":15,\"Response_Vector\":[1,5,20],\"Game_Type\":\"Arcade\",\"Response_Times\":[8536,9127,10217],\"Score\":1000,\"Total_Time\":10217,\"Operand_2\":7,\"Session_Trial\":1,\"Hint_Shown\":0,\"Operand_1\":8,\"Operation_Type\":\"1d+1d\",\"End_Date\":[2016,12,27,14,50,0],\"PersonalData\":{\"Name\":\"Jorge Berrueta\",\"Hand\":\"Diestro\",\"Birthdate\":[1987,1,27],\"Studies\":\"Terciario en curso\",\"AUID\":\"95e85ed03e1c34e7\",\"Email\":\"jorgeaber@gmail.com\",\"Gender\":\"Masculino\"},\"Hide_Question\":0,\"Initial_Effort\":-1,\"Correct_Result\":15,\"Erase\":0,\"Start_Date\":[2016,12,27,14,49,50],\"Time_Exceeded\":0,\"Level\":1,\"Hints_Available\":3}", "experiment_name": "MoravecData_v02"}


TRIAL_NEW_FORMAT = {
    'user': {
        'auid': '95e85ed03e1c34e7',
        'name': 'Jorge Berrueta',
        'gender': 'Masculino',
        'hand': 'Diestro',
        'studies': 'Terciario en curso',
        'birthdate': [1987,1,27]
    },
    'operation': {
        'level': 1,
        'operand_1': 8,
        'operand_2': 7,
        'operator': '+',
        'type': '1d+1d',
        'result': 15
    },
    'answer': {
        'result': 15,
        'correct': 1,
        'score': 1000,
        'confidence': -1,
        'effort': -1
    },
    'time': {
        'max': 14000,
        'exceeded': 0,
        'total': 10217,
        'start': [2016,12,27,14,49,50],
        'end': [2016,12,27,14,50,0]
    },
    'hints': {
        'shown': 0,
        'available': 3
    },
    'session': {
        'correct': 1,
        'trial': 1
    },
    'initial': {
        'confidence': -1,
        'effort': -1
    },
    'response': {
        'vector': [1,5,20],
        'times': [8536,9127,10217],
        'correctInARow': 1
    }
}


def test_pretty_format(session):
    requests.post(URL_PREFIX + 'v1/trials', json=TRIAL_LEGACY_FORMAT)
    data = requests.get(URL_PREFIX + 'v1/trials?format=pretty').json()
    assert data[0] == TRIAL_NEW_FORMAT 
