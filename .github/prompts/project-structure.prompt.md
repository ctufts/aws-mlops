```markdown
Your goal is to generate an ideal file and directory structure for an AWS CDK–based MLOps/LLMOps API platform project, written in **Python**, following AWS CDK Python best practices and using **uv** for package and environment management.

Project context & best practices:
- AWS CDK v2 with Python, structured as a Python package under `src/my_project`.
- Manage dependencies and virtual environments via **uv**:
  - Define project metadata and dependencies in `pyproject.toml`, including the uv plugin.
  - Use `uv.lock` for a reproducible lock file.
  - Keep the isolated environment in `.venv/` (listed in `.gitignore`).
  - CI/CD should run `uv install --lock` and `uv sync`.
- Organize CDK into logical stacks: `network`, `api`, `inference`, `rag`, `async`.
- Build reusable L2 constructs in `constructs/`.
- Include a self-mutating CDK Pipeline under `pipelines/` (CodePipeline + CodeBuild → synth & deploy).
- Parameterize account/region via `cdk.json` context; write environment-agnostic code.
- Apply cost‐allocation tags in each stack.
- Write unit tests with pytest and CDK assertions in `tests/`, mirroring `src/my_project`.
- Add pre‐commit hooks (`.pre-commit-config.yaml`) for linting (flake8, isort) and formatting (black).

Directory requirements:
```

src/my\_project/
├── app.py                    # CDK App entrypoint
├── stacks/
│   ├── network\_stack.py
│   ├── api\_stack.py
│   ├── inference\_stack.py
│   ├── rag\_stack.py
│   └── async\_stack.py
├── constructs/               # reusable construct modules
│   └── example\_construct.py
└── pipelines/
└── pipeline\_stack.py     # CDK Pipeline definition

tests/
└── unit/
├── test\_network\_stack.py
└── test\_api\_stack.py

config/
├── dev.yml
├── staging.yml
└── prod.yml

scripts/
├── bootstrap.sh
├── deploy.sh
└── local\_test.sh

docs/
├── architecture.md
└── design\_decisions.md

.github/workflows/
├── ci.yml
└── deploy.yml

```

Root files:
```

README.md
pyproject.toml
uv.lock
cdk.json
cdk.context.json
.pre-commit-config.yaml
.gitignore

```

When you generate the structure, output an ASCII tree (using hyphens and indentation) showing directories and files.