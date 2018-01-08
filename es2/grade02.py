

from testlib import runtests
from simulatore import nogui
import sys

def test_anello():
    pista = 'anello'
    players = 'program02'
    logfile = pista + '.log'
    return nogui.callback(pista, logfile, players)

def test_monza():
    pista = 'monza'
    players = 'program02'
    logfile = pista + '.log'
    return nogui.callback(pista, logfile, players)

def test_roma():
    pista = 'roma'
    players = 'program02'
    logfile = pista + '.log'
    return nogui.callback(pista, logfile, players)


tests = [ 
        test_anello,
        test_monza,
        test_roma,
        ]

if __name__ == '__main__':
    #runtests(tests)
    runtests(tests,logfile='grade02.csv')

