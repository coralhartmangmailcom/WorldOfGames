import os

SCORES_FILE_NAME = "Scores.txt"

def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5

    current_score = 0
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as file:
            score_content = file.read()
            if score_content.isdigit():
                current_score = int(score_content)

    current_score += points_of_winning

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(current_score))