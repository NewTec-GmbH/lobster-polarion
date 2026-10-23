# lobster-polarion <!-- omit in toc -->

[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://choosealicense.com/licenses/gpl-3.0/) [![Repo Status](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

- [Overview](#overview)
- [Development Status](#development-status)
- [Installation](#installation)
- [SW Documentation](#sw-documentation)
- [Issues, Ideas And Bugs](#issues-ideas-and-bugs)
- [License](#license)
- [Contribution](#contribution)

## Overview

lobster-polarion shall be a python commandline tool to provide work items (e.g. requirements) from
[Polarion ALM](https://polarion.plm.automation.siemens.com/) in the
[LOBSTER common interchange format](https://github.com/bmw-software-engineering/lobster/blob/main/documentation/schemas.md).
This allows to use Polarion work items in a LOBSTER tracing report. The concept follows
[lobster-codebeamer](https://github.com/bmw-software-engineering/lobster/tree/main/packages/lobster-tool-codebeamer),
which closes the same gap for Codebeamer.

> [!NOTE]
> lobster-polarion is not a standalone solution, but a component extending the
> [BMW LOBSTER tooling](https://github.com/bmw-software-engineering/lobster). Understanding of the LOBSTER tool purpose and usage
> is required to benefit from lobster-polarion.

## Development Status

The tool is developed according to the V-model. The current phase is the requirements engineering:

| Artefact                  | Location                                            | Status      |
| ------------------------- | --------------------------------------------------- | ----------- |
| Stakeholder requirements  | [trlc/stk-req](./trlc/stk-req)                      | In review   |
| SW requirements           | `trlc/swe-req`                                      | Open        |
| SW architecture           | `trlc/swe-arch`, `doc/architecture`                 | Open        |
| Implementation            | `src/lobster_polarion`                              | Open        |
| SW tests                  | `trlc/swe-test`, `tests`                            | Open        |

## Installation

- `git clone https://github.com/NewTec-GmbH/lobster-polarion.git` to clone repository.
- `cd lobster-polarion` to go to root directory.
- It is recommended to use a virtual environment:
  - In VS-Code: `Ctrl+Shift+P` type **Python: Create Environment**: select `Venv`.
    - When asked, select the Python version you want to work with, based on the versions installed in your machine.
    - When asked, select `dev` to be installed. This will set-up the development environment, including all the tools used in this template.
    - In the background, VS Code will install all the dependencies. This may take some time.
    - To activate the virtual environment, close all terminal panels inside of VS-Code.
      You can double check if the virtual environment is active, e.g. by `pip -V` the displayed path should point to your virtual environment.
  - In PowerShell:
    - `python -m venv .venv` to create the virtual environment.
    - `.venv\Scripts\Activate.ps1` to activate it.
    - `pip install -e .[dev]` to install the packages for development.
  - Under Linux / MacOS:
    - `python -m venv .venv` to create the virtual environment.
    - `source .venv/bin/activate` to activate it.
    - `pip install -e .[dev]` to install the packages for development.
  For more details about handling Venv, see [Python venv: How To Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv#Python_venv_activation)

## SW Documentation

The requirements, architecture and tests are written in [TRLC](https://github.com/bmw-software-engineering/trlc) and
located in [trlc](./trlc). The model (`trlc/model`) defines two requirement levels:

- Stakeholder requirements (`StkReq`, `StkConstraint`) — the needs of the tool user.
- SW requirements (`SwReq`, `SwReqNonFunc`, `SwConstraint`) — derived from the stakeholder requirements via `derived_from`.

Run `trlc --verify trlc/model trlc/stk-req` to check the requirements. The documentation build incl. tracing report will be
added together with the further V-model levels.

---

## Issues, Ideas And Bugs

If you have further ideas or you found some bugs, great! Create an [issue](https://github.com/NewTec-GmbH/lobster-polarion/issues) or if you are able and willing to fix it by yourself, clone the repository and create a pull request.

## License

The whole source code is published under [GNU General Public License Version 3](https://github.com/NewTec-GmbH/lobster-polarion/blob/main/LICENSE).
Consider the different licenses of the used third party libraries too!

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you, shall be licensed as above, without any additional terms or conditions.
