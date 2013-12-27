# In Django 1.6, the old test runner was deprecated, and
# {setup,teardown}_databases was moved out from the test runner class
try:
    from django.test.runner import setup_databases, teardown_databases
except ImportError:
    from django.test.simple import DjangoTestSuiteRunner

    _runner = DjangoTestSuiteRunner(interactive=False)
    setup_databases = _runner.setup_databases
    teardown_databases = _runner.teardown_databases


# OperationalError was introduced in Django 1.6
# Use the less generic DatabaseError for older Django versions
try:
    from django.db.utils import OperationalError
except ImportError:
    from django.db.utils import DatabaseError as OperationalError
    OperationalError  # silence pyflakes
