import json
import importlib
from fixture.application import Application

import pytest
import os.path



fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']

    if fixture is None or not fixture.is_valid():
            fixture = Application(browser=browser, baseUrl=web_config["baseUrl"])

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
    #parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc): #получить инфо о тест функции
    for fixture in metafunc.fixturenames: #пробегаем по всем параметрам
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata #после импорта взять из модуля тестдата

def load_from_json(file, jsonpickle=None):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data/%s.json" % file)) as f_out:
        return jsonpickle.decode(f_out.read())