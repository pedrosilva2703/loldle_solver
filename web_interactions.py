from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary

correct_str = "square-good"
partial_str = "square-partial"
wrong_str = "square-bad"

def accept_cookies(wd):
    accept_cookies_button = WebDriverWait(wd, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'fc-button.fc-cta-consent.fc-primary-button'))
    )
    accept_cookies_button.click()

def set_english(wd):
    # Open change language menu
    language_button = WebDriverWait(wd, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'animate__animated.animate__fadeIn.top-button.top-right-game.has-tooltip'))
    )
    language_button.click()

    # Select language combo
    language_combo_button = WebDriverWait(wd, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'vs__dropdown-toggle'))
    )
    language_combo_button.click()


    # Select English language
    english_button = WebDriverWait(wd, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'fi.flag.fi-us.fis '))
    )
    english_button.click()

def input_guess(wd, champion_name):

    guess_box = WebDriverWait(wd, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'guessbox'))
    )
    
    input = WebDriverWait(guess_box, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'input'))
    )
    input.clear()
    input.send_keys(champion_name)

    confirm_button = WebDriverWait(guess_box, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "guess-button"))
    )
    confirm_button.click()


def is_element_present(container, by, value):
    try:
        element = container.find_element(by, value)
        return True
    except NoSuchElementException:
        return False
    
def is_finished(wd):
    end_container = wd.find_element(By.ID, "endId")
    return is_element_present(end_container, By.CLASS_NAME, "finished")

def is_correct(answer_container, square_xpath, square_pos):
    correct = is_element_present(answer_container, By.XPATH, square_xpath.format(correct_str, square_pos))
    return correct

def is_partially_correct(answer_container, square_xpath, square_pos):
    partial = is_element_present(answer_container, By.XPATH, square_xpath.format(partial_str, square_pos))
    return partial

def is_release_date_superior(answer_container, square_xpath, square_pos):
    return is_element_present(answer_container, By.XPATH, square_xpath.format("square-superior", square_pos))
