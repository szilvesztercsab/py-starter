# py-starter

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Coverage](https://img.shields.io/static/v1?label=🐍+pytest-cov&message=100%&color=2ea44f)](https://pypi.org/project/pytest-cov/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Actions status](https://github.com/szilvesztercsab/py-starter/actions/workflows/ci.yaml/badge.svg)](https://github.com/szilvesztercsab/py-starter/actions)

An opinionated python starter project with:

- [uv](https://docs.astral.sh/uv)
- [poe](https://poethepoet.natn.io)
- [pyest](https://pytest.org)
- [pre-commit](https://pre-commit.com)
- [ruff](https://docs.astral.sh/ruff)
- Visual Studio Code [workspace settings](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings)
  and [recommended extensions](https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions)
- [GitHub Actions Workflow](https://docs.github.com/en/actions)
  for linting and testing

## Usage

Requirements:

- `git clone` this repository
- [install `uv`](https://docs.astral.sh/uv/getting-started/installation/)
- `uv run poe i` to install the project, commit hooks and all requirements

Then you can run the provided hello_world script via:

<!-- markdownlint-disable line-length -->
```console
foo@bar:~$ uv run hello
2025-01-11 16:49:26,284 INFO [/Users/csaba/Code/py-starter/apps/hello_world/hello_world/hello.py:15] Hello, world!
2025-01-11 16:49:26,284 WARNING [/Users/csaba/Code/py-starter/apps/hello_world/hello_world/hello.py:16] Bye, world!
```
<!-- markdownlint-enable line-length -->

Run the linters and tests via:

```sh
uv run poe l  # runs ruff
uv run poe t  # runs pytest
```

<!-- TODO: add more documentation on usage, customization, etc. -->
<!-- TODO: add documentation generation -->
<!-- TODO: add templating support -->
<!-- TODO: add dockerfile -->
<!-- TODO: add ... -->
