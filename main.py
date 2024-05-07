from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random, json



service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("FORM_URL")

n_of_responses = 300
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

for _ in range(n_of_responses):
    
    # Wait for the form to load
    
    qustions_list = wait.until(EC.presence_of_element_located((By.ID, "question-list")))
    questions = qustions_list.find_elements(By.XPATH, ".//div[@data-automation-id='questionItem']")


    for question in questions:
        question_container = question.find_element(By.XPATH, ".//*[contains(@class, '-bV-')]")
        question_type = question_container.find_element(By.TAG_NAME, "div")
        role = question_type.get_attribute("role")
        
        if role == "radiogroup":
            choices_list = question_type.find_elements(By.XPATH, ".//div[@data-automation-id='choiceItem']")
            choices_list.reverse()
            weights = [1 / (i + 1) for i in range(len(choices_list))]
            choice = random.choices(choices_list, weights=weights)[0]
            input = choice.find_element(By.TAG_NAME, "input")
            input.click()
        
        # text input    
        if role == None:
            # text input
            try:
                improvements = [
                    "Expanded workout options",
                    "More workout options would be awesome",
                    "More workout options",
                    "Maybe more workout options",
                    "Greater customization options",
                    "Better customization options",
                    "More customization options",
                    "More customization options would be good",
                    "Feedback mechanism",
                    "Feedback mechanism would be great",
                    "Better feedback mechanism",
                    "More feedback mechanism",
                    "More feedback mechanism probably",
                    "themes",
                    "More themes",
                    "Better themes",
                    "More themes would be great",
                    "More themes would be nice",
                    "probably could add themes",
                    "the layout of the settings page can be improved",
                    "the settings page layout can be improved",
                    "the settings page layout can be better",
                    "the settings page layout can be improved",
                    "maybe a better settings page layout",
                ]

                text_container = question_container.find_element(By.XPATH, ".//*[contains(@class, 'text-container')]")
                text_intput = text_container.find_element(By.TAG_NAME, "input")
                text = random.choice(improvements) if random.choice([True, False, False, False]) else ""
                text_intput.send_keys(text)
            except:
                # rating
                ratings_list = question_type.find_elements(By.XPATH, ".//div[@role='radio']")
                weights = [1,  3, 7, 25, 50, 70, 90, 100, 90, 85]
                choice = random.choices(ratings_list, weights=weights, k=1)[0]
                input = choice
                input.click()
        
                    
        if role == "group":
            choices_list = question_type.find_elements(By.TAG_NAME, "input")
            probabilities = [0.7, 0.01, 0.7, 0.1, 0.15]  
            clicked = False
            for choice, prob in zip(choices_list, probabilities):
                if random.random() < prob:
                    choice.click()
                    clicked = True
            if not clicked and choices_list:
                random.choice(choices_list).click()

    time.sleep(random.randint(17, 32))            
    submit_button = driver.find_element(By.XPATH, "//button[contains(@data-automation-id, 'submitButton')]")
    submit_button.click()

    another_response = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@data-automation-id, 'submitAnother')]")))
    
    another_response.click()

driver.quit()

