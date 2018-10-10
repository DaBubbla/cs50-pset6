from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    linesA = []
    linesB = []

    linesA = set(a.split('\n'))
    linesB = set(b.split('\n'))

    return linesA & linesB


def sentences(a, b):
    """Return sentences in both a and b"""
    sentenceA = set(sent_tokenize(a))
    sentenceB = set(sent_tokenize(b))

    return sentenceA & sentenceB


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    def tokenize(str, n):
        """Helper function to tokenize a and b"""
        substrings = []

        for i in range(len(str) - n + 1):
            substrings.append(str[i:i + n])
        return substrings

    substringsA = set(tokenize(a, n))
    substringsB = set(tokenize(b, n))

    return substringsA & substringsB
