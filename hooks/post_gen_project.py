import os
import shutil
import string


TERMINAL = {
    "TERMINATOR": "\x1b[0m",
    "WARNING": "\x1b[1;33m [WARNING]: ",
    "ERROR": "\x1b[0;31m [ERROR]: ",
    "INFO": "\x1b[1;33m [INFO]: ",
    "HINT": "\x1b[3;33m",
    "SUCCESS": "\x1b[1;32m [SUCCESS]: "
}

def remove_open_source_files():
    file_names = ["CONTRIBUTORS.txt", "LICENSE"]
    for file_name in file_names:
        os.remove(file_name)

def remove_gplv3_files():
    file_names = ["COPYING"]
    for file_name in file_names:
        os.remove(file_name)

def remove_docker_files():
    shutil.rmtree("compose")

    file_names = ["Dockerfile", ".dockerignore", "docker-compose.yml"]
    for file_name in file_names:
        os.remove(file_name)

def remove_aws():
    file_names = [f".envs/.{_path}/.aws" for _path in ("production", "local")]
    for file_name in file_names:
        os.remove(file_name)

def remove_postgres():
    file_names = [f".envs/.{_path}/.postgres" for _path in ("production", "local")]
    for file_name in file_names:
        os.remove(file_name)

def main():
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_open_source_files()
    if "{{ cookiecutter.open_source_license}}" != "GPLv3":
        remove_gplv3_files()

    if "{{ cookiecutter.use_docker }}".lower() == "no":
        remove_docker_files()

    if "{{ cookiecutter.cloud_provider}}" == "None":
        print(f"{TERMINAL['WARNING']}You chose not to use a cloud provider, ")
        print(f"media files won't be served in production.{TERMINAL['TERMINATOR']}")
        remove_aws()

    if "{{ cookiecutter.database }}".lower() == "none":
        remove_postgres()

if __name__ == "__main__":
    main()
