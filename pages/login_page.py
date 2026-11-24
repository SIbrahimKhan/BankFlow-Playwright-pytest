from playwright.sync_api import Page
from utils.config import BASE_URL

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        #locators
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.get_by_role("button", name="LOG IN")

    #navigate to login page
    def open(self):
        self.page.goto(BASE_URL)

    #Execute
    def login(self, username:str, password:str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
