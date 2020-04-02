from selenium import webdriver
from selenium.webdriver.support.select import Select
import time



def t1():
    browser=webdriver.Chrome('/home/shadman/chromedriver')
    browser.get('http://a123.us-east-2.elasticbeanstalk.com/')
    # browser.get('http://127.0.0.1:5000/')

    t_age=browser.find_element_by_name('age')
    t_age.send_keys('37')

    select = Select(browser.find_element_by_name('gender'))
    select.select_by_visible_text('Male')

    select = Select(browser.find_element_by_name('chest_pain_type'))
    select.select_by_visible_text('2')

    t_resting_blood_pressure=browser.find_element_by_name('resting_blood_pressure')
    t_resting_blood_pressure.send_keys('130')

    t_serum_cholestoral=browser.find_element_by_name('serum_cholestoral')
    t_serum_cholestoral.send_keys('250')

    select = Select(browser.find_element_by_name('fasting_blood_sugar'))
    select.select_by_visible_text('fasting blood sugar < 120 mg/dl')

    select = Select(browser.find_element_by_name('resting_electrocardiographic_results'))
    select.select_by_visible_text('Value = 1')

    t_maximum_heart_rate_achieved=browser.find_element_by_name('maximum_heart_rate_achieved')
    t_maximum_heart_rate_achieved.send_keys('187')

    select = Select(browser.find_element_by_name('exercise_induced_angina'))
    select.select_by_visible_text('No')

    t_ST_depression_induced=browser.find_element_by_name('ST_depression_induced')
    t_ST_depression_induced.send_keys('3.5')

    select = Select(browser.find_element_by_name('slope_of_the_peak_exercise_ST_segment'))
    select.select_by_visible_text('0')

    select = Select(browser.find_element_by_name('major_vessels_colored_by_flourosopy'))
    select.select_by_visible_text('0')

    select = Select(browser.find_element_by_name('thal'))
    select.select_by_visible_text('Fixed Defect = 6')

    time.sleep(1)

    t_submit=browser.find_element_by_name('button')
    t_submit.click()
    time.sleep(5)

def t2():
    browser=webdriver.Chrome('/home/shadman/chromedriver')
    browser.get('http://a123.us-east-2.elasticbeanstalk.com/')
    # browser.get('http://127.0.0.1:5000/')

    time.sleep(1)
    t_age=browser.find_element_by_name('age')
    t_age.send_keys('37')

    select = Select(browser.find_element_by_name('gender'))
    select.select_by_visible_text('Male')

    select = Select(browser.find_element_by_name('chest_pain_type'))
    select.select_by_visible_text('2')

    t_resting_blood_pressure=browser.find_element_by_name('resting_blood_pressure')
    t_resting_blood_pressure.send_keys('130')

    t_serum_cholestoral=browser.find_element_by_name('serum_cholestoral')
    t_serum_cholestoral.send_keys('250')

    select = Select(browser.find_element_by_name('fasting_blood_sugar'))
    select.select_by_visible_text('fasting blood sugar < 120 mg/dl')

    select = Select(browser.find_element_by_name('resting_electrocardiographic_results'))
    select.select_by_visible_text('Value = 1')

    t_maximum_heart_rate_achieved=browser.find_element_by_name('maximum_heart_rate_achieved')
    t_maximum_heart_rate_achieved.send_keys('157')

    select = Select(browser.find_element_by_name('exercise_induced_angina'))
    select.select_by_visible_text('No')

    t_ST_depression_induced=browser.find_element_by_name('ST_depression_induced')
    t_ST_depression_induced.send_keys('3.5')

    select = Select(browser.find_element_by_name('slope_of_the_peak_exercise_ST_segment'))
    select.select_by_visible_text('0')

    select = Select(browser.find_element_by_name('major_vessels_colored_by_flourosopy'))
    select.select_by_visible_text('0')

    select = Select(browser.find_element_by_name('thal'))
    select.select_by_visible_text('Fixed Defect = 6')

    time.sleep(1)

    t_submit=browser.find_element_by_name('button')
    t_submit.click()
    time.sleep(5)


# for i in range(1):
t1()