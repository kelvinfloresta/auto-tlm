import time
import pyautogui
from selector import selector

def click_selector(selector):
    print('Searching for selector "{}"'.format(selector))
    element = pyautogui.locateCenterOnScreen(selector, confidence=0.5)
    not_found = element == None
    if (not_found):
        print('Selector "{}" NOT found!'.format(selector))
        return False

    print('Clicking on Selector "{}"'.format(selector))
    pyautogui.click(x=element.x, y=element.y)
    pyautogui.click(x=element.x, y=element.y)
    time.sleep(1)
    return True

def wait_for_selector(selector):
    print('Waiting for selector "{}"'.format(selector))
    element = pyautogui.locateOnScreen(selector, confidence=0.4)
    while element is None:
        print('Selector "{}" NOT found!'.format(selector))
        time.sleep(1)
        element = pyautogui.locateOnScreen(selector, confidence=0.4)

    print('Found selector "{}"'.format(selector))
    return element

def retry_click(selector, delayInSeconds):
    success = click_selector(selector)
    while success is False:
        print('Retrying in "{}" seconds'.format(delayInSeconds))
        time.sleep(delayInSeconds)
        success = click_selector(selector)


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
    time.sleep(5)
    retry_click(selector.get("transaction_request"), 1)
    pyautogui.scroll(-1000)
    time.sleep(5)
    retry_click(selector.get("approve_transaction"), 1)
    retry_click(selector.get("home"), 1)

def main():
    mine()
    claim()
    main()

if __name__ == "__main__":
    main()