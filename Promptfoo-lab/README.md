#Promptfoo Lab

A practical workspace for evaluating AI-powered applications with
[Promptfoo](https://www.promptfoo.dev/).

Promptfoo is an evaluation framework for testing prompts, comparing models,
and checking AI-generated responses against defined requirements.

This lab explores how to:
- Translate requirements into test cases and acceptance criteria.
- Validate responses using deterministic assertions and model-based grading.
- Compare prompt versions and model configurations.
- Investigate incorrect answers and distinguish them from API errors.
- Detect regressions after changes.
- Assess response quality alongside latency and token usage.

Evaluations are learning projects developed incrementally.
Coverage, findings, and limitations are documented within each project.

## Projects
### 1. Northstar Store - Shop chatbot evaluation
**Status:** In progress

Evaluation of a customer support chatbot that answers questions using
a fictional online store policy.

The project focuses on whether the chatbot correctly interprets business
rules, handles missing information, and respects its capability limits.

**Planned test coverage:**

| Area | What We Evaluate |
|---|---|
| Policy accuracy | Answers reflect the rules in the provided policy |
| Return deadlines | Request deadlines are distinguished from return shipping deadlines |
| Boundary conditions | Rules are applied correctly at time and price thresholds |
| Exceptions | Defect claims are distinguished from change-of-mind returns |
| Missing information | The chatbot acknowledges gaps instead of inventing answers |
| Clarification | Missing customer details trigger appropriate questions |
| Capability limits | The chatbot does not claim to access orders or perform actions |
| Prompt injection | Customer instructions do not override store rules |

**Evaluation approach:**

- A versioned, synthetic store policy provides the reference requirements.
- Customer questions represent specific scenarios and risks.
- Deterministic assertions check objective conditions.
- Model-based rubrics evaluate semantic correctness.
- Responses and grading explanations are reviewed manually.

The current approach supplies the policy directly to the model.
It does not test a deployed user interface or a document retrieval pipeline.

## Interpreting Results

- **PASS:** The response satisfied the configured assertions.
- **FAIL:** At least one assertion was not satisfied.
- **ERROR:** An execution or integration issue prevented normal evaluation.

Passing results apply only to the tested cases and criteria.
Model-based graders can make mistakes and require calibration.

## References

- [Promptfoo Configuration Guide](https://www.promptfoo.dev/docs/configuration/guide/)
- [Promptfoo Providers](https://www.promptfoo.dev/docs/providers/)
- [Promptfoo Assertions and Metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/)

---

Part of the [AI Testing portfolio](../README.md).
