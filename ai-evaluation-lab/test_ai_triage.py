
from deepeval.metrics import ExactMatchMetric
from deepeval.test_case import LLMTestCase

test_cases = [
    {
        "name": "TC01 - Correct classification",
        "actual": "critical",
        "expected": "critical",
    },
    {
        "name": "TC02 - Incorrect classification",
        "actual": "low",
        "expected": "critical",
    },
]

for tc in test_cases:
    test_case = LLMTestCase(
        input="All payments are failing for all customers.",
        actual_output=tc["actual"],
        expected_output=tc["expected"]
    )

    metric = ExactMatchMetric()
    metric.measure(test_case)

    print(f"\n{tc['name']}")
    print(f"Score: {metric.score}")
    print(f"Result: {'PASS' if metric.is_successful() else 'FAIL'}")
