import allure
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            try:
                screenshot = page.screenshot(full_page=True)
                allure.attach(
                    screenshot,
                    name="Failure screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:
                print(f"Could not take screenshot: {e}")
