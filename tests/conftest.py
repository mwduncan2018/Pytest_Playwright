import allure
import pytest
from pages.pages import Pages


@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:3000"


@pytest.fixture
def pages(page):
    """Provides a typed Page Object Factory to tests."""
    return Pages(page)


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "args": ["--window-position=-1900,595", "--window-size=1750,900"],
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1750, "height": 900},
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call':
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            
            # 1. Attach Screenshot
            screenshot = page.screenshot(full_page=True)
            allure.attach(screenshot, name="Final Screenshot", attachment_type=allure.attachment_type.PNG)
            
            # 2. Attach Video (The safe way)
            # We close the context to ensure the video file is written to disk
            context = page.context
            context.close() 
            
            video = page.video
            if video:
                allure.attach.file(video.path(), name="Execution Video", attachment_type=allure.attachment_type.WEBM)