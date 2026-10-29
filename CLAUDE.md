# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Process (V-model) — mandatory

The tool is developed strictly according to the V-model and every work result is reviewed (code review via PR).

- **Never skip ahead.** Only produce the artefacts of the current phase. Do not write architecture, code or tests before the
  requirements they are based on exist and were reviewed. Ask if unsure which phase is active (see the GitHub issues).
- Left side: stakeholder requirements → SW requirements → SW architecture → implementation.
  Right side: SW tests (verify SW requirements) → tool qualification tests (verify stakeholder requirements).
- One PR per feature; the PR contains the artefacts of the feature in the order of the V-model.
- Open questions are recorded in the `note` attribute with the prefix `Open issue:` and must be resolved in the review.
  Rejected requirements are kept with `valid_status = AbstractRequirements.VALID_STATUS.rejected`.

### Traceability

| Level                   | TRLC                        | Traces to (field)                                 |
| ----------------------- | --------------------------- | ------------------------------------------------- |
| Stakeholder requirement | `trlc/stk-req` (`StkReq`)   | -                                                 |
| Stakeholder constraint  | `trlc/stk-req` (`StkConstraint`) | -                                            |
| SW requirement          | `trlc/swe-req` (`SwReq`)    | `derived_from` → `StkReq` (mandatory)             |
| SW constraint           | `trlc/swe-req` (`SwConstraint`) | `derived_from` → `StkConstraint` (optional)   |
| SW architecture         | `trlc/swe-arch` (`SwArchSpec`) | `satisfies` → SW requirements                  |
| SW test case            | `trlc/swe-test` (`SwTestCase`) | `verifies` → `SwReq`                           |
| Code                    | `src/lobster_polarion`      | `# lobster-trace: SwRequirements.<id>`            |
| Test code               | `tests`                     | `# lobster-trace: SwTests.<id>` + `record_property("lobster-trace", "SwTests.<id>")` |

The tracing policy will be defined in `tools/traceReport/lobster-report-sw-req.conf` (not yet present, added together with
the SW requirements). Do not remove trace comments when modifying traced functions. Do not annotate a class *and* its methods — lobster-python ignores the method traces then.

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate          # Linux/macOS
# .venv\Scripts\activate.ps1       # Windows PowerShell

pip install -e .[dev]
```

## Common Commands

```bash
# Check TRLC model and requirements (once the trlc folder exists)
trlc --verify trlc

# Lint (must be clean — score 10.00/10, no warnings or errors tolerated)
pylint --rcfile=.pylintrc src/lobster_polarion tests

# Run all tests / a single test
pytest tests
pytest tests/test_cli.py::test_tc_help
```

The documentation build (`tools/`, TRLC -> RST, test report, LOBSTER tracing report, Sphinx) and the CI workflows
(`.github/workflows`) are not yet part of the repository. They are added once the further levels (swe-req, swe-arch,
swe-test, src, tests) exist.

## Concept Reference

The tool concept shall be similar to lobster-codebeamer
(https://github.com/bmw-software-engineering/lobster/tree/main/packages/lobster-tool-codebeamer): YAML configuration file,
selection by query / tagged items / baseline, `refs` from item links, selectable LOBSTER schema. The repository structure and
Python code shall be similar to lobster-doxygen (https://github.com/NewTec-GmbH/lobster-doxygen).

## Coding Standards

- Follow `coding-guidelines/README.md`: PEP8, Google-style docstrings, max line length 120, autopep8 formatting.
- Review against `coding-guidelines/code-review-checklist.md`.
- Every function/method must have exactly one `return` statement.
- Every module, class, function, and method must have a docstring with all parameters and return value.
- Every Python file starts with a module docstring (incl. `Author:`), followed by the GPL v3 license header, then the section
  separator comments (`# Imports ***`, `# Variables ***`, `# Classes ***`, `# Functions ***`, `# Main ***`).
  Use the `template_lobster_polarion` VS Code snippet.
- Use the `logging` module — never `print()`.
- When releasing, update the version in `pyproject.toml`.

See the `/python-coding-standard` skill for the full workflow and file template.

## TRLC Language

TRLC (Treat Requirements Like Code) is the DSL used for requirement definitions (`.rsl`) and instances (`.trlc`).
Type definitions live in `trlc/model/`; requirement objects live in the further `trlc/` sub-folders.

See the `/trlc` skill for the full language reference and syntax rules.

## Commits

Commit messages follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format.
See the `/conventional-commit` skill.
