import unittest


class PlaintextBaselineTests(unittest.TestCase):
    def test_sample_average(self):
        values = [82_000.0, 91_500.0, 76_250.0, 104_000.0]
        self.assertAlmostEqual(sum(values) / len(values), 88437.5)

    def test_empty_input_is_rejected_by_demo_validation(self):
        values = []
        with self.assertRaises(ValueError):
            if not values:
                raise ValueError("At least one value is required.")


if __name__ == "__main__":
    unittest.main()
