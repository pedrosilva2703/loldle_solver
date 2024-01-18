from web_interactions import *
from champion import load_champions_from_xml

xml_file_path = "champions_data.xml"
loldle_website = "https://loldle.net/classic"
total_champions = 1 #168

champions_list = load_champions_from_xml(xml_file_path)
for champion in champions_list:
    champion.display_info()

options = wd.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

wd = wd.Chrome(options=options)
wd.get(loldle_website)

accept_cookies(wd)
set_english(wd)

input_guess(wd, "Fizz")
time.sleep(5)
answers_container = wd.find_element(By.CLASS_NAME, "answers-container.classic-answers-container")

first_container = answers_container.find_element(By.XPATH, './div/div[1]')

correct_gender = is_element_present(first_container, By.XPATH, '//div[contains(@class, "square-good") and contains(@class, "0")]')
if correct_gender:
    print("Gender correct")
else:
    print("Gender wrong")

  

for i in range(1, total_champions):
    #select first option from the list
    current_guess = champions_list[0]

    #input guess
    input_guess(current_guess.name)
    time.sleep(5)

    if is_finished(wd):
        break
    
    #retrieve info
        #is gender correct or partial?
            #keep only champions with that gender
        #else
            #remove champions with that gender
        #is position correct or partial?
            #keep only champions with that position
        #else
            #remove champions with that position
        #...





# answers_container = wd.find_element(By.CLASS_NAME, "answers-container.classic-answers-container")
# input_guess("Karma")
# second_container = answers_container.find_element(By.XPATH, './div[2]')

# correct_gender = is_element_present(second_container, By.XPATH, '//div[contains(@class, "square-good") and contains(@class, "0")]')   

# if correct_gender:
#     print("Gender correct")
# else:
#     print("Gender wrong")

#answers_container.find_element(By.XPATH, '//div[contains(@class, "square-good") and contains(@class, "0")]')

#/html/body/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[3]/div[2] Karma
#/html/body/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[3]/div[1] Fizz
#/html/body/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[3]/div[1]/div
#/html/body/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[3]/div[1]/div/div[2]
#/html/body/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[3] Box
    
#/html/body/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[3]/div               classic answer
#/html/body/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[3]/div/div           square container
#/html/body/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[3]/div/div/div[3]    square position
    