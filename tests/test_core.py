import unittest
from textforge import normalize, wrap
class Tests(unittest.TestCase):
 def test_normalize(self): self.assertEqual(normalize(" a  b\n c "),"a b c")
 def test_wrap(self): self.assertEqual(wrap("one two three",7),["one two","three"])
if __name__=="__main__": unittest.main()
