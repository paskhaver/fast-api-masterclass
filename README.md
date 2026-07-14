# FastAPI Masterclass

Welcome to FastAPI Masterclass! This repository contains the course materials for the video course including all projects and slide decks.

## Downloading the Course Materials

### Option A: Clone repository with Git

In Terminal/PowerShell, navigate to the directory where you'd like to download the `fast-api-masterclass` course materials.

Execute `git clone git@github.com:paskhaver/fast-api-masterclass.git` to clone the repository to your computer.

### Option B: Download repository

On this GitHub page, click the green `Code` button, then select "Download ZIP". Unpack the zip and move the `fast-api-masterclass` directory to wherever you'd like.

## Course Prerequisites

- Basic/intermediate knowledge of Python (functions, classes/objects, data structures like list/dictionaries, etc.)
- Basic knowledge of Terminal (navigation)
- Basic experience with coding text editor

This course assumes no previous experience with backend development. Although we cover FastAPI from scratch, I do recommend completing a Python course before starting on this one.

This course uses the [(VSCode)](https://code.visualstudio.com/) editor and multiple VSCode extensions. You are welcome to utilize another editor (i.e. PyCharm) if you prefer. The code will remain the same, but you'll have to figure out how to achieve similar editor actions like debugging in your editor.

## Browser Setup

FastAPI uses the JSON text format to send and receive data.

I recommend installing the Chrome `JSONVue` extension (or a similar tool) to format your JSON. See this page:

https://chromewebstore.google.com/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc?hl=en

Without the extension, the browser will render raw JSON like this:

```text
{"id":1,"name":"Alice"}
```

With the extension, the browser will render the JSON with indentation, color-coding, and collapsible sections.

```json
{
  "id": 1,
  "name": "Alice"
}
```

## Working Through the Course

Every top-level folder in this repo contains a separate project.

Each project has a list of dependencies which you can find within `pyproject.toml`. A dependency is a library (a bundle of developer code) that the project depends in order to be able to run. Dependencies need to be downloaded to your computer.

The video course proceeds through the projects in the following order:

- [`rent-a-room/`](rent-a-room) — FastAPI project inspired by AirBnB (Sections 1-10)
- [`database-management/`](database-management) — Database migrations with Alembic (Section 11)
- [`authentication/`](authentication) — Authentication and authorization (Sections 12-13)

### Install uv

I recommend installing `uv`, a command-line tool for managing Python projects, virtual environments, and dependencies. `uv` has a simple `uv sync` command that installs Python and downloads all dependencies for any project with a `pyproject.toml` file.

If you are familiar with the Python ecosystem and prefer to use an alternate Python manager (`pip`, `poetry`, etc), you are welcome to do so. See each project's `pyproject.toml` file for a list of dependencies.

You can fidn the `uv` setup instructions below. The course videos can also walk you through setting up `uv` step-by-step.

#### macOS uv Setup

Execute the following commands in Terminal to install `uv` and enable command auto-completion. The final two commands (auto-completion) are optional but recommended.

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh

echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc

echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
```

Verify installation with `uv --version`. You should see a version number like:

```sh
uv --version
uv 0.11.26 (396ef7ce4 2026-06-30 aarch64-pc-windows-msvc)
```

See https://docs.astral.sh/uv/getting-started/installation/ for the `uv` installation documentation.

#### Windows uv Setup

Execute the following commands in PowerShell to install `uv` and enable command auto-completion. The final two commands (auto-completion) are optional but recommended.

```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

if (!(Test-Path -Path $PROFILE)) {
  New-Item -ItemType File -Path $PROFILE -Force
}
Add-Content -Path $PROFILE -Value '(& uv generate-shell-completion powershell) | Out-String | Invoke-Expression'

if (!(Test-Path -Path $PROFILE)) {
  New-Item -ItemType File -Path $PROFILE -Force
}
Add-Content -Path $PROFILE -Value '(& uvx --generate-shell-completion powershell) | Out-String | Invoke-Expression'
```

Verify installation with `uv --version`. You should see a version number like:

```shell
uv --version
uv 0.11.26 (396ef7ce4 2026-06-30 aarch64-apple-darwin)
```

See https://docs.astral.sh/uv/getting-started/installation/ for the `uv` installation documentation.

### Work on a course project

1. Navigate into a sample project from the Terminal.

```sh
cd rent-a-room
```

2. Execute `uv sync` to setup a virtual environment with the project's version of Python and all of the project's dependencies/libraries. `uv` will automatically download any dependencies that are not locally available on the computer.

```sh
uv sync

Using CPython 3.14.6
Creating virtual environment at: .venv
Resolved 53 packages in 14ms
Prepared 51 packages in 2.80s
Installed 51 packages in 63ms
 + aiosqlite==0.22.1
 + alembic==1.18.5
#...
```

3. Open the project in VSCode with `code .`. Alternatively, you can open the project's folder in VSCode by clicking `File > Open Folder`. Make sure to open a specific project to ensure VSCode picks up that project's virtual environment automatically. If you open the top-level `fast-api-masterclass` folder, VSCode will NOT be able to correctly identify the virtual environment.

4. A project has a `.vscode/extensions.json` file with recommended VSCode extensions to install. If you do not have the extensions, a pop-up will appear when you first open the project. Click the button to download all recommended VSCode extensions.

## Project Dependencies

Each project's `pyproject.toml` file lists its dependencies under `[project.dependencies]`. FastAPI needs these dependencies for the project to run.

Here's a complete list of libraries we use throughout the course:

- **fastapi** — a Python micro-framework for building APIs/web servers
- **pydantic** — a library for data validation and transformation
- **sqlalchemy** - an ORM (object-relational mapper) for using Python to communicate with databases
- **sqlmodel** — a new ORM from the developers of FastAPI that combines Pydantic and SQLAlchemy for database models and queries
- **alembic** — a tool for generating and running database migrations (updates to the database schema)
- **pydantic-settings** — a Pydantic expansion that loads environment variables from a `.env` file
- **pydantic-extra-types** — a Pydantic expansion that adds validation for extra field types like phone numbers
- **pwdlib** — a password hashing algorithm that converts a plain-text password into a hash
- **pyjwt** — a library for encoding and decoding JSON Web Tokens (JWTs)
- **aiosqlite** — an async SQLite driver to add support for async database calls
- **greenlet** — a dependency that SQLAlchemy/SQLModel needs to add support for async database calls

## Developer Dependencies

`Ruff` is a developer dependency in every project. A developer dependency is a library that exists for the benefit of the developer rather than the end user. A FastAPI project does not need developer dependencies to run correctly.

Ruff is a formatter that formats code in a consistent, aesthetically pleasing standard. It is made by the same team as `uv`.

You can find developer dependencies in `pyproject.toml` in a dedicated section.

I configured VSCode settings to run Ruff automatically on save. See any project's `.vscode/settings.json` for the setup.

### Before/After Example

Before Ruff formatting:

```python
import sys
import os
from fastapi import FastAPI

app=FastAPI()
@app.get('/users')
def get_users():
    return{"name":"Alice"}
```

After Ruff formatting:

```python
import os
import sys

from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def get_users():
    return {"name": "Alice"}
```

Ruff grouped and sorted the imports (standard library first, then third-party), added the missing spacing around `=` and after `return`, switched single quotes to double quotes, and inserted the blank lines Python convention expects around a function definition.
