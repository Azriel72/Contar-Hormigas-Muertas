import pytest
from dead_ants import count_dead_ants

def test_count_dead_ants():
    assert count_dead_ants("...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t") == 3
