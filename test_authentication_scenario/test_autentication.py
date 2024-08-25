import time


def test_orangehrm_one(page_creation) -> None:
    page = page_creation
    page.get_by_role("link", name="Admin").click()
    time.sleep(5)


def test_orangehrm_two(page_creation) -> None:
    page = page_creation
    page.get_by_role("link", name="PIM").click()
    time.sleep(5)




