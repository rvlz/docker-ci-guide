"""Flask manager"""
import sys

import pytest
from flask.cli import FlaskGroup

from app import create_app

cli = FlaskGroup(create_app=create_app)


@cli.command("test")
def run_tests():
    result = pytest.main(["-x", "app/test"])
    if result == pytest.ExitCode.OK:
        return 0
    sys.exit(result.value)


if __name__ == "__main__":
    cli()
