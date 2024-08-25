import time
from playwright.sync_api import expect




def test_chat_message(login_set_up_for_chat):
    page, page2 = login_set_up_for_chat
    page.locator("#container_friends").get_by_role("img").first.click()
    page.locator("#container_friends div").filter(has_text="MehulAnju").nth(2).click()
    page.locator("#container_friends").get_by_role("img").first.click()
    page.locator("#avcontent").get_by_text("Action").click()
    page.locator("#glob_actions").get_by_text("Private").click()
    page.locator("#message_content").click()
    page.locator("#message_content").fill("hi, how are you")
    page.locator("#message_content").press("Enter")

    page.locator("#get_private i").click()
    page.get_by_text("AnjuMehul").click()
    msg = page.get_by_text("hi, how are you")
    expect(msg).to_be_visible()

