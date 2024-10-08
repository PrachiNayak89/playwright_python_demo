import pytest
import re
from playwright.sync_api import Page, expect
import playwright_python_demo.data as data


@pytest.mark.register
def test_register_new_user(page: Page):
    # Go to AUT page
    page.goto('/')
    # Verify the application launch page success
    expect(page).to_have_title(re.compile("frontend"))
    # Click on the register button
    page.get_by_role("main").get_by_role("button", name="Register").click()
    # Click on the email field
    page.get_by_label("Email").click()
    # Fill the email field
    user_email = data.generate_random_email(data.generate_random_name())
    page.get_by_label("Email").fill(user_email)
    # Click on the pw field
    page.get_by_label("Password").click()
    # Fill the pw field
    pw = data.generate_random_password()
    page.get_by_label("Password").fill(pw)
    # Click on the register button
    page.get_by_role("main").get_by_role("button", name="Register").click()
    page.get_by_role("main").get_by_role("button", name="Register").click()
    # Verify the success message
    # expect(page.locator("div").filter(has_text=re.compile(r"^Login$"))).to_be_visible()
    expect(page.get_by_text("Registration successful!")).to_be_visible()


@pytest.mark.login
def test_login_new_user(page: Page):
    # Go to AUT page
    page.goto('/')
    # Verify the application launch page success
    expect(page).to_have_title(re.compile("frontend"))
    # Click on the register button
    page.get_by_role("main").get_by_role("button", name="Register").click()
    # Click on the email field
    page.get_by_label("Email").click()
    # Fill the email field
    user_email = data.generate_random_email(data.generate_random_name())
    page.get_by_label("Email").fill(user_email)
    # Click on the pw field
    page.get_by_label("Password").click()
    # Fill the pw field
    pw = data.generate_random_password()
    page.get_by_label("Password").fill(pw)
    # Click on the register button
    page.get_by_role("main").get_by_role("button", name="Register").click()
    # Verify the success message
    expect(page.get_by_text("Registration successful!")).to_be_visible()
    # Now login with newly created user
    page.goto('/login')
    # Fill email details
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill(user_email)
    # Fill pw details
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(pw)
    # Click on login button
    page.get_by_role("main").get_by_role("button", name="Login").click()
    # Verify login success and landed on the User Dashboard
    expect(page.get_by_role("heading", name="User Dashboard")).to_be_visible()


@pytest.mark.ticket
def test_create_new_ticket(page: Page):
    # Go to AUT page
    page.goto('/')
    # Verify the application launch page success
    expect(page).to_have_title(re.compile("frontend"))
    # Click on the register button
    page.get_by_role("main").get_by_role("button", name="Register").click()
    # Click on the email field
    page.get_by_label("Email").click()
    # Fill the email field
    user_email = data.generate_random_email(data.generate_random_name())
    page.get_by_label("Email").fill(user_email)
    # Click on the pw field
    page.get_by_label("Password").click()
    # Fill the pw field
    pw = data.generate_random_password()
    page.get_by_label("Password").fill(pw)
    # Click on the register button
    page.get_by_role("main").get_by_role("button", name="Register").click()
    # Verify the success message
    expect(page.get_by_text("Registration successful!")).to_be_visible()
    # Now login with newly created user
    page.goto('/login')
    # Fill email details
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill(user_email)
    # Fill pw details
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(pw)
    # Click on login button
    page.get_by_role("main").get_by_role("button", name="Login").click()
    # Verify login success and landed on the User Dashboard
    expect(page.get_by_role("heading", name="User Dashboard")).to_be_visible()
    # Create a new ticket
    page.goto('/dashboard')
    page.get_by_role("button", name="Create Support Ticket").click()
    # Enter the title of the ticket
    ticket_title = data.generate_random_title()
    page.get_by_label("Title").click()
    page.get_by_label("Title").fill(ticket_title)
    # Enter the description of the ticket
    ticket_description = data.generate_random_description()
    page.get_by_label("Description").click()
    page.get_by_label("Description").fill(ticket_description)
    # Click on Submit ticket
    page.get_by_role("button", name="Submit Ticket").click()
    # Verify ticket creation success
    expect(page.get_by_role("heading", name="User Dashboard")).to_be_visible()


@pytest.mark.case
def test_create_new_case(page: Page):
    # Go to AUT page
    page.goto('/')
    # Verify the application launch page success
    expect(page).to_have_title(re.compile("frontend"))
    # Click on the register button
    page.get_by_role("main").get_by_role("button", name="Register").click()
    # Click on the email field
    page.get_by_label("Email").click()
    # Fill the email field
    user_email = data.generate_random_email(data.generate_random_name())
    page.get_by_label("Email").fill(user_email)
    # Click on the pw field
    page.get_by_label("Password").click()
    # Fill the pw field
    pw = data.generate_random_password()
    page.get_by_label("Password").fill(pw)
    # Click on the register button
    page.get_by_role("main").get_by_role("button", name="Register").click()
    # Verify the success message
    expect(page.get_by_text("Registration successful!")).to_be_visible()
    # Now login with newly created user
    page.goto('/login')
    # Fill email details
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill(user_email)
    # Fill pw details
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(pw)
    # Click on login button
    page.get_by_role("main").get_by_role("button", name="Login").click()
    # Verify login success and landed on the User Dashboard
    expect(page.get_by_role("heading", name="User Dashboard")).to_be_visible()
    # Create a new ticket
    page.goto('/dashboard')
    page.get_by_role("button", name="Create Case").click()
    # Enter the case name
    case_name = data.generate_random_name() + '_case_'
    page.get_by_label("Case Name").click()
    page.get_by_label("Case Name").fill(case_name)
    # Select the case type
    page.get_by_role("combobox").locator("div").filter(has_text="Select ItemSelect Item").locator("div").click()
    page.get_by_role("option").first.click()
    # Click on Submit case
    page.get_by_role("button", name="Submit Case").click()
    # Verify case creation success
    expect(page.get_by_role("heading", name="User Dashboard")).to_be_visible()
