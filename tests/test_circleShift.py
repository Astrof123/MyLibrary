import pytest
from CircleShift.main import circleShift
def test_circle():
   assert circleShift("abcabc", "abc") == 4
   assert circleShift("abcabc", "acb") == 0
   assert circleShift("aaaaaaa", "aa") == 6
   assert circleShift("aAaa8aaAa", "aAa") == 4