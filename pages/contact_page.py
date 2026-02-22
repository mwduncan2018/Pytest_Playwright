from typing import List
from .base_page import BasePage

class ContactPage(BasePage):
    _SECRET_MESSAGE = "#secretMessage"
    _GITHUB_LINK = "#github a"
    _SKILL_LIST = "#skillList li"

    def get_github_href(self) -> str:
        return self.page.get_attribute(self._GITHUB_LINK, "href")

    def get_footer_text(self) -> str:
        return self.page.inner_text(self._SECRET_MESSAGE)

    def get_all_skills(self) -> List[str]:
        return [skill.strip() for skill in self.page.locator(self._SKILL_LIST).all_inner_texts()]