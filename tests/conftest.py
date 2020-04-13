import os
import sys

import pytest

@pytest.fixture(scope='session', autouse=True)
def scope_session():
    print("setup before session")
    yield
    print("teardown after session")


@pytest.fixture(scope='module', autouse=True)
def scope_module():
    print("    setup before module")
    yield
    print("    teardown after module")


@pytest.fixture(scope='class', autouse=True)
def scope_class():
    print("        setup before class")
    yield
    print("        teardown after class")


@pytest.fixture(scope='function', autouse=True)
def scope_function():
    print("            setup before function")
    yield
    print("            teardown after function")

sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../excel_fill_in_the_blank/"))