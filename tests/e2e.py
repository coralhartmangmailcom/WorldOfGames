from selenium import webdriver


def find_score_element(driver):
    score_element = None
    elements = driver.find_elements_by_id("score")  # Replace "score" with the actual ID of the score element
    if elements:
        score_element = elements[0]
    return score_element


def test_scores_service(application_url):
    driver = webdriver.Chrome()
    driver.get(application_url)
    score_element = find_score_element(driver)

    if score_element is not None:
        score_text = score_element.text
        if score_text.isdigit():
            score = int(score_text)
            if 1 <= score <= 1000:
                driver.quit()
                return True

    driver.quit()
    return False


def main_function(application_url):
    test_result = test_scores_service(application_url)
    if test_result:
        print("Tests passed.")
        return 0
    else:
        print("Tests failed.")
        return -1



