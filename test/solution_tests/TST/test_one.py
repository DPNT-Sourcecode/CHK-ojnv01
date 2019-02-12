from solutions.TST import one


class TestSum():
    def test_sum(self):
        assert one.get() == 1
        assert one.checkout("") == -1
