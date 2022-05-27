import os


def pytest_addoption(parser):
    """A list of additional command line arguments"""
    parser.addoption('--env', action='store', default='qa', help='Select the environment your test will run against')


def pytest_configure(config):
    """Sets the command line arguments to configuration options"""
    os.environ['env'] = config.getoption('env')


def get_api_url():
    return f'https://reqres.in/api/'


def get_env():
    return os.environ["env"].upper()



