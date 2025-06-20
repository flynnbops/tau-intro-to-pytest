import pytest

from playwright.sync_api import Page, expect

pytestmark = [pytest.mark.ui, pytest.mark.restfulbooker]


def test_submit_booking_enquiry(page: Page):
    #  Locators
    message_header = page.get_by_role("heading", name='Send Us a Message')
    name = page.get_by_test_id('ContactName')
    email = page.get_by_test_id('ContactEmail')
    phone = page.get_by_test_id('ContactPhone')
    subject = page.get_by_test_id('ContactSubject')
    message = page.get_by_test_id('ContactDescription')
    submit_button = page.get_by_role("button", name="Submit")
    submitted_message = page.get_by_role("heading", name='Thanks for getting in touch') 

    # Arrange
    page.goto('https://automationintesting.online/#contact')
    expect(message_header).to_be_visible()

    # Act
    name.fill('Aaron')
    email.fill('a123@bcdef.com')
    phone.fill('1234562312321131')
    subject.fill('Roomz plz')
    message.fill('10000 rooms10000 rooms10000 rooms')
    submit_button.click()

    # Assert
    expect(submitted_message).to_be_visible()
