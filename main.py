import time
import pyautogui

selector = {
    "mine": "mine_btn.png",
    "mine2": "mine_btn_2.png",
    "claim": "claim_btn.png",
    "home": "home_btn.png",
    "mining_not_exhaust": "mining_not_exhaust.png",
}

def click_selector(selector):
    print('Searching for selector "{}"'.format(selector))
    element = pyautogui.locateOnScreen(selector)
    not_found = element == None
    if (not_found):
        print('Selector "{}" NOT found!'.format(selector))
        return False

    print('Clicking on Selector "{}"'.format(selector))
    pyautogui.click(selector)
    time.sleep(1)
    return True

def wait_for_selector(selector):
    print('Waiting for selector "{}"'.format(selector))
    element = pyautogui.locateOnScreen(selector)
    not_found = element == None
    if (not_found):
        print('Selector "{}" NOT found!'.format(selector))
        time.sleep(1)
        return wait_for_selector(selector)

    print('Found selector "{}"'.format(selector))
    return element

def retry_click(selector, delayInSeconds):
    success = click_selector(selector)
    if (success):
        return

    print('Retrying in "{}" seconds'.format(delayInSeconds))
    time.sleep(delayInSeconds)
    return retry_click(selector, delayInSeconds)

def check_mine_exhaust():
    print("Checking mine exhaust")
    wait_for_selector(selector.get("mining_not_exhaust"))
    print("Recovered from exhaust!")

def mine():
    check_mine_exhaust()
    print("Starting mining!")
    retry_click(selector.get("mine"), 1)
    retry_click(selector.get("mine2"), 1)

def claim():
    print("Claiming!")
    retry_click(selector.get("claim"), 1)
    retry_click(selector.get("home"), 1)

def main():
    mine()
    claim()
    main()

main()