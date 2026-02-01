import pytest

from src.os.env import Env

# Helper methods that can be reused in the tests.
# Chris Joakim, 3Cloud/Cognizant, 2026


def set_testing_envvars(monkeypatch):
    monkeypatch.setenv("USER", "chris")
    monkeypatch.setenv("USERNAME", "joakim")
