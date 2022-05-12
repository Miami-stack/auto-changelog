import pytest

from auto_changelog.repository import GitRepository


@pytest.mark.parametrize(
    "message, expected",
    [
        ("feat(scope): description\n\nbody\n\nFooter #1", ("feat", "scope", "description", "body", "Footer #1")),
    ],
)
def test_parse_conventional_commit_with_parentheses(message, expected):
    assert expected == GitRepository._parse_conventional_commit(message)


@pytest.mark.parametrize(
    "message, expected",
    [
        ("feat!: description\n\nbody\n\nFooter #1", ("feat", "", "description", "body", "Footer #1")),
    ],
)
def test_parse_conventional_commit_without_parentheses(message, expected):
    assert expected != GitRepository._parse_conventional_commit(message)
