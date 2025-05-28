Your goal is to generate AWS infrastructure as code using AWS CDK for Python following repository conventions and AWS best practices.

Ask for missing details if not provided, such as stack name, environment (account/region), and resource specifications.

Requirements:

* Use Python 3.9+ and AWS CDK v2 (`aws_cdk_lib`, `constructs`).
* Organize code with `app.py`, `stacks/`, `constructs/`, and `tests/`.
* Implement reusable `Construct` classes for related resources.
* Parameterize environment-specific values via `cdk.json` context or `CfnParameter`; avoid hardcoding account/region.
* Apply the principle of least privilege for IAM roles; use managed policies when possible.
* Store sensitive data in AWS Secrets Manager or Parameter Store.
* Tag all resources with `project`, `environment`, and `owner`.
* Right-size resources and enable auto-scaling where appropriate.
* Write unit tests using `pytest` and `aws_cdk_lib.assertions`.
* Validate changes with `cdk synth` and `cdk diff` before deployment.
* Include clear import statements and inline comments for non-obvious logic.
* Integrate CDK CLI commands (`synth`, `deploy --require-approval never`) in CI workflows.

Do not include explanations unless asked. Provide only code templates that adhere to these instructions.
