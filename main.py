from web_interactions import *
from champion import load_champions_from_xml
import time

xml_file_path = "champions_data.xml"
loldle_website = "https://loldle.net/classic"
total_champions = 168
gender_pos = 0
position_pos = 1
species_pos = 2
resource_pos = 3
rangetype_pos = 4
regions_pos = 5
year_pos = 6


champions_list = load_champions_from_xml(xml_file_path)
#print(len(champions_list))
# for champion in champions_list:
#     champion.display_info()

options = wd.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--start-maximized")

wd = wd.Chrome(options=options)
wd.get(loldle_website)

accept_cookies(wd)
set_english(wd)
  
answers_container = wd.find_element(By.CLASS_NAME, "answers-container.classic-answers-container")

for i in range(1, total_champions):
    #select first option from the list
    current_guess = champions_list[0]

    #input guess
    input_guess(wd, current_guess.name)
    
    time.sleep(6)

    if is_finished(wd):
        print("GAME WON")
        break
    
    last_answer_container = answers_container.find_element(By.XPATH, f'./div[{i}]/div')
    square_xpath = './div[contains(@class, "{}") and contains(@class, "{}")]'
    
    #Filter gender
    if is_correct(last_answer_container, square_xpath, gender_pos):
        champions_list = [champion for champion in champions_list if champion.gender == current_guess.gender]
    else:
        champions_list = [champion for champion in champions_list if champion.gender != current_guess.gender]

    #Filter position 
    if is_correct(last_answer_container, square_xpath, position_pos):
        champions_list = [champion for champion in champions_list if set(champion.positions).intersection(current_guess.positions)]
    else:
        champions_list = [champion for champion in champions_list if not set(champion.positions).intersection(current_guess.positions)]

    #Filter species 
    if is_correct(last_answer_container, square_xpath, species_pos):
        champions_list = [champion for champion in champions_list if set(champion.species).intersection(current_guess.species)]
    else:
        champions_list = [champion for champion in champions_list if not set(champion.species).intersection(current_guess.species)]

    #Filter resource
    if is_correct(last_answer_container, square_xpath, resource_pos):
        champions_list = [champion for champion in champions_list if champion.resource == current_guess.resource]
    else:
        champions_list = [champion for champion in champions_list if champion.resource != current_guess.resource]

    #Filter rangetype 
    if is_correct(last_answer_container, square_xpath, rangetype_pos):
        champions_list = [champion for champion in champions_list if set(champion.range).intersection(current_guess.range)]
    else:
        champions_list = [champion for champion in champions_list if not set(champion.range).intersection(current_guess.range)]

    #Filter regions 
    if is_correct(last_answer_container, square_xpath, regions_pos):
        champions_list = [champion for champion in champions_list if set(champion.regions).intersection(current_guess.regions)]
    else:
        champions_list = [champion for champion in champions_list if not set(champion.regions).intersection(current_guess.regions)]


    #Filter year
    if is_correct(last_answer_container, square_xpath, year_pos):
        champions_list = [champion for champion in champions_list if champion.release_year == current_guess.release_year]
    elif is_release_date_superior(last_answer_container, square_xpath, year_pos):
        champions_list = [champion for champion in champions_list if champion.release_year > current_guess.release_year]
    else:
        champions_list = [champion for champion in champions_list if champion.release_year < current_guess.release_year]

