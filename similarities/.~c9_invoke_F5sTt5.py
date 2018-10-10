from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    # Refer to: https://docs.python.org/3/library/stdtypes.html#string-methods

    linesA = []
    linesB = []

    linesA = set(a.split('\n'))
    linesB = set(b.split('\n'))


    return linesA & linesB


def sentences(a, b):
    """Return sentences in both a and b"""
    sentA = []
    sentB = []

    sentA = a.sent_tokenize
    sentB = b.sent_tokenize
    return sentA and sentB


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    return []
