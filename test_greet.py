from greet import *

def test_1():
    assert greet("Bob") == "Hello, Bob."

def test_2():
    assert greet(None) == "Hello, my friend."

def test_3():
    assert greet("JERRY") == "HELLO, JERRY."

def test_4():
    assert greet(["Jill", "Jane"]) == "Hello, Jill and Jane."

def test_5():
    assert greet(["Amy", "Brian", "Charlotte"]) == "Hello, Amy, Brian, and Charlotte."

def test_6():
    assert greet(["Amy", "BRIAN", "Charlotte"]) == "Hello, Amy and Charlotte. AND HELLO BRIAN!"

def test_7():
    assert greet(["Bob", "Charlie, Dianne"]) == "Hello, Bob, Charlie, and Dianne."

def test_8():
    assert greet(["Bob", "\"Charlie, Dianne\""]) == "Hello, Bob and Charlie, Dianne."
