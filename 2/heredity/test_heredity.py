import pytest

import heredity


def main():
    test_joint_probability()


def test_joint_probability():
    people = {
        'Harry': {'name': 'Harry', 'mother': 'Lily', 'father': 'James', 'trait': None},
        'James': {'name': 'James', 'mother': None, 'father': None, 'trait': True},
        'Lily': {'name': 'Lily', 'mother': None, 'father': None, 'trait': False}
    }
    assert heredity.joint_probability(people, {"Harry"}, {"James"}, {"James"}) == 0.0026643247488 # pytest.approx(0.0026643247488, 0.0001)


if __name__ == "main":
    main()