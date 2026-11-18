
import os

from google import genai
from deepeval.metrics import ExactMatchMetric
from deepeval.test_case import LLMTestCase

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

incident = "All payments are failing for all customers."

prompt = f"""
Classify the severity of this incident.

Rules:
- low: single failure followed by successful retry
- medium: failure without confirmed recovery,
  but no evidence of a global outage
- critical: all payments fail for all customers

Incident: {incident}

Reply using exactly one word:
low, medium, or critical.
Do not add explanations or punctuation.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

actual_output = response.text or ""

test_case = LLMTestCase(
    input=incident,
    actual_output=actual_output,
    expected_output="critical"
)

metric = ExactMatchMetric()
metric.measure(test_case)

print(f"Gemini response: {actual_output!r}")
print(f"Score: {metric.score}")
print(f"Result: {'PASS' if metric.is_successful() else 'FAIL'}")
