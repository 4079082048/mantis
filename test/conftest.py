from fixture.application import Application
import pytest
import json
import os.path
import importlib
import ftputil



fixture = None
target = None

#def load_config(file):
    #global target
    #if target is None:
        #config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        #config_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(file))), "target.json")
        #with open(config_file) as f:
            #target = json.load(f)
    #return target
def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(file)), file)
        #config_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(file))), "target.json")
        with (open(config_file) as f):
            target = json.load(f)
    return target

@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture(scope="session", autouse=True)
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, config=config)
    return fixture



@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

@pytest.fixture(scope="session", autouse=True)
def configure_server(request, config):
    install_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    def fin():
        restore_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    request.addfinalizer(fin)

def install_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            remote.remove("config_inc.php.bak")
        if remote.path.isfile("config_inc.php"):
            remote.rename("config_inc.php", "config_inc.php.bak")
        #remote.upload(os.path.join(os.path.dirname(__file__), "resources/config_inc.php"), "config_inc.php")
        # Путь к файлу config_inc.php
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources/config_inc.php")
        # Загрузка файла на сервер
        remote.upload(file_path, "config_inc.php")

def restore_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.bak"):
            if remote.path.isfile("config_inc.php"):
                remote.remove("config_inc.php")
            remote.rename("config_inc.php.bak", "config_inc.php")


