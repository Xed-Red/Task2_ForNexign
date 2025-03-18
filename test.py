import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Firefox()
    browser.get("https://nexign.com/ru")
    yield browser
    browser.quit()


def test_counting_in_page(browser):
    page_text = browser.page_source
    elements_count = page_text.lower().count("nexign")
    print("Количество упоминаний слова 'Nexign', без учета регистра: ", elements_count)
    assert elements_count > 0, "Nexign отсутствует на странице"
