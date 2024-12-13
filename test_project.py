import pytest

from datetime import datetime

import os
import api.parcer as parcer
import src.core as core
import src.tranzactions as tr

def test_pars():
    first = core.par_output("99999")
    second = core.par_output("99999")

    assert first == second

def test_read_users():
    user_info1 = tr.read_users(0)
    user_info2 = tr.read_users(0)

    assert str(user_info1['group']) == str(user_info2['group'])

def test_read_message():
    msg1 = tr.read_messages()[0]
    msg2 = tr.read_messages()[0]

    assert msg1 == msg2

def test_get_info():
    par = parcer.parcer()
    out = par.get_info("TEST", datetime.now())

    assert out == -1

def test_log_write():
    tr.log_write("test.log", "Test log writing!")
    log = open("test.log", "r")
    test = log.read()

    os.remove("test.log")
    assert test == "Test log writing!\n"
