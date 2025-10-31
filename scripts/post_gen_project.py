#!/usr/bin/env -S uv run --script --quiet

#
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "rich>=14.2.0",
# ]
# ///

"""
Post-generation script for Copier template.
"""

import contextlib
import glob
import os
import random
import shutil
import subprocess
import sys
from pathlib import Path

from rich import print


PROJECT_DIRECTORY = Path.cwd()
print(f"Project directory: {PROJECT_DIRECTORY}")


@contextlib.contextmanager
def cd(path):
    """Context manager for changing directory."""
    cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(cwd)


def system(*args, **kwargs):
    """Run system command."""
    env = kwargs.pop("env", None)
    return subprocess.call(list(args), env=env)


class Project:
    """Project management utilities."""

    def mkdir(self, directory: str) -> None:
        """Create directory."""
        system(
            "mkdir",
            "-p",
            os.path.join(PROJECT_DIRECTORY, directory),
        )

    def rmdir(self, path: str) -> None:
        """Remove directory."""
        path = os.path.join(PROJECT_DIRECTORY, path)
        if os.path.exists(path):
            shutil.rmtree(path)

    def add(self, *, pkg: str, group: str = "") -> None:
        """Add package with uv."""
        if group:
            system("uv", "add", "--group", group, pkg)
        else:
            system("uv", "add", pkg)

    def sync(self):
        """Sync dependencies with uv."""
        system("uv", "sync")

    def collectstatic(self):
        """Run Django collectstatic."""
        system(
            "uv",
            "run",
            "python",
            os.path.join(PROJECT_DIRECTORY, "manage.py"),
            "collectstatic",
            "--noinput",
        )


def get_random_string(
    length=50, allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)"
):
    """
    Generate a securely random string.
    """
    return "".join(random.choice(allowed_chars) for i in range(length))


def set_secret_key(setting_file_location):
    """Set SECRET_KEY in settings file."""
    # Read file
    with open(setting_file_location) as f:
        file_content = f.read()

    # Generate SECRET_KEY
    SECRET_KEY = get_random_string()

    # Replace placeholder
    file_content = file_content.replace("<%SECRET_KEY%>", SECRET_KEY, 1)

    # Write back
    with open(setting_file_location, "w") as f:
        f.write(file_content)


def uv_add(project: Project, group: str = "") -> None:
    """Install packages from requirements file using uv add."""
    filename = f"requirements.{group}.in" if group else "requirements.in"
    path = os.path.join(PROJECT_DIRECTORY, "_requirements", filename)

    if not os.path.exists(path):
        print(f"Skipping {filename} (not found)")
        return

    print(f"Installing from {path}")
    with open(path) as f:
        for line in f.readlines():
            line = line.replace("\n", "").strip()
            if line and not line.startswith("#"):
                print(f"  Adding: {line}")
                project.add(pkg=line, group=group)


def main():
    """Main post-generation logic."""
    project = Project()

    # Install dependencies using uv
    print("\n=== Installing dependencies ===")
    uv_add(project)
    uv_add(project, "dev")
    uv_add(project, "ci")
    uv_add(project, "upgrade")

    # Clean up requirements directory
    print("\n=== Cleaning up ===")
    project.rmdir("_requirements")

    print("\n=== Post-generation complete! ===")


if __name__ == "__main__":
    main()

