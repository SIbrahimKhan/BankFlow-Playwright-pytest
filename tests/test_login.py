import pytest
from playwright.sync_api import Page, expect
from test_data.login_data import login_test_date

@pytest.mark.parametrize(
        "username, password, is_valid, expected_message", login_test_date
)

def test_login_scenario(login_page, page: Page, username, password, is_valid, expected_message):
    login_page.open()

    login_page.login(username, password)

    if is_valid:
        expect(
            page.get_by_role("heading", name="Accounts Overview")
        ).to_be_visible()

    else:
        expect(
            page.get_by_text(expected_message)
        ).to_be_visible()

    