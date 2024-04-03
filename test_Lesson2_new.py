from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture
def browser_config():
    browser.config.window_width = 1600
    browser.config.window_height = 1080
    yield
    browser.quit()

def test_google_find_selene(browser_config):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_find_something(browser_config):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ывбаоывзадлтоыьвжабытосахыва').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))
