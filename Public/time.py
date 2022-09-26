import doctest
import xmlrunner

def twice(n):
    """
    >>> twice(5)
    10
    """
    return 2 * n

class Multiplicator(object):
    def threetimes(self, n):
        """
        >>> Multiplicator().threetimes(5)
        15
        """
        return 3 * n

if __name__ == "__main__":
    suite = doctest.DocTestSuite()
    xmlrunner.XMLTestRunner().run(suite)