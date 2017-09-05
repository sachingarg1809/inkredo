import numpy as np

class Session:
    def __init__(self, sess_id, clicked = False, n_results=0, group=None, time=None):
        self.session_id = sess_id
        self.clicked = clicked
        self.n_results = n_results
        self.group = group
        self.time = time

def getSessions(data):
    sessions = {} # key = session id, value = Session
    for log in data:
        if not log[2] in sessions:
            sessions[log[2]] = Session(log[2], group=log[3])
        if log[4]=='visitPage':
            sessions[log[2]].clicked = True
        if log[4]=='searchResultPage':
            sessions[log[2]].n_results = int(log[7])
            try:
                sessions[log[2]].time = int(log[1][8:10])
            except(ValueError):
                sessions[log[2]].time = 0
    return sessions

def getXY(data):
    sessions = getSessions(data)
    X = []
    Y = []
    for key in sessions.keys():
        if sessions[key].group=='a':
            group = 1
        elif sessions[key].group=='b':
            group = 2
        X.append([sessions[key].n_results, group, sessions[key].time])
        Y.append(sessions[key].clicked)
    return np.array(X),np.array(Y)
