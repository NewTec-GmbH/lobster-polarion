# lobster-polarion <!-- omit in toc -->

[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://choosealicense.com/licenses/gpl-3.0/) [![Repo Status](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

- [Overview](#overview)
- [Installation](#installation)
- [SW Documentation](#sw-documentation)
- [Used Libraries](#used-libraries)
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

The tool is developed according to the V-model. The current development status is tracked via
[GitHub issues](https://github.com/NewTec-GmbH/lobster-polarion/issues).

The requirements, architecture and tests will be written in [TRLC](https://github.com/bmw-software-engineering/trlc) and
located in the `trlc` folder.

The software architecture is described in the [documentation](./doc/README.md) subpage.

## Used Libraries

Used 3rd party libraries which are not part of the standard Python package:

| Library                                                            | Description                                        | License  |
| ------------------------------------------------------------------ | -------------------------------------------------- | -------- |
| [toml](https://github.com/uiri/toml)                               | Parsing [TOML](https://en.wikipedia.org/wiki/TOML) | MIT      |
| [bmw-lobster](https://github.com/bmw-software-engineering/lobster) | LOBSTER common interchange format and tooling      | AGPL-3.0 |

---

## Issues, Ideas And Bugs

If you have further ideas or you found some bugs, great! Create an [issue](https://github.com/NewTec-GmbH/lobster-polarion/issues) or if you are able and willing to fix it by yourself, clone the repository and create a pull request.

## License

The whole source code is published under [GNU General Public License Version 3](https://github.com/NewTec-GmbH/lobster-polarion/blob/main/LICENSE).
Consider the different licenses of the used third party libraries too!

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you, shall be licensed as above, without any additional terms or conditions.
