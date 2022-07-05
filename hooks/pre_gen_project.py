import sys


TERMINAL = {
    "TERMINATOR": "\x1b[0m",
    "WARNING": "\x1b[1;33m [WARNING]: ",
    "ERROR": "\x1b[0;31m [ERROR]: ",
    "INFO": "\x1b[1;33m [INFO]: ",
    "HINT": "\x1b[3;33m",
    "SUCCESS": "\x1b[1;32m [SUCCESS]: "
}

def confirmation(message):
    print(f"{TERMINAL['WARNING']}{message}{TERMINAL['TERMINATOR']}")
    opt = input(f"Do you want to proceed (y/n)?{TERMINAL['TERMINATOR']}").lower()
    while opt not in ("y", "n"):
        opt = input(f"{TERMINAL['HINT']}Do you want to proceed (y/n)?{TERMINAL['TERMINATOR']}").lower()

    if opt == "n":
        print(f"{TERMINAL['INFO']}Generation process stopped as requested.{TERMINAL['TERMINATOR']}")
        sys.exit(1)

project_slug = "{{ cookiecutter.project_slug }}"

try:
    if hasattr(project_slug, "isidentifier"):
        assert (
            project_slug.isidentifier()
        ), ("ERROR", f"'{project_slug}' project slug is not a valid Python identifier.")

    assert (
        project_slug == project_slug.lower()
    ), ("WARNING", f"'{project_slug}' project slug should be all lowercase.")

    if "{{ cookiecutter.ci_tool }}".lower() != "none":
        print(f"{TERMINAL['WARNING']}CI tool not available yet.{TERMINAL['TERMINATOR']}")

    if "{{ cookiecutter.use_docker }}".lower() == "no":
        print(f"{TERMINAL['WARNING']}Specified python version does not apply.{TERMINAL['TERMINATOR']}")

        python_major_version, python_minor_version = sys.version_info[:2]

        if python_major_version == 2:
            assert (
                project_slug == project_slug.lower()
            ), ("ERROR", f"Project requires Python 3.7+")
        else:
            if python_minor_version < 7:
                message = f"You're running cookiecutter with Python 3.{python_minor_version},"
                message += "\nBut the generated project require Python 3.7+"
                confirmation(message)

        if "{{ cookiecutter.database }}".lower() != "none":
            confirmation("For local development with database, it is recommended to use docker")

    if "{{ cookiecutter.cloud_provider }}".lower() == "gcp":
        confirmation("No GCP support yet.")

except AssertionError as ae:
    color, msg = ae.args[0]
    print(f'{TERMINAL[color]}{msg}{TERMINAL["TERMINATOR"]}')
    sys.exit(1)
