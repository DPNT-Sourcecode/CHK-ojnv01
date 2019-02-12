from iwoca.accelerate_runner.lib.solutions.SUM.sum_solution import compute


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

