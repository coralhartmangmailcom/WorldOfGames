from flask import Flask
import os

SCORES_FILE_NAME = "Scores.txt"

app = Flask(__name__)


def score_server():
    error_message = None
    score = None

    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as file:
            score_content = file.read()
            if score_content.isdigit():
                score = score_content

    if score is not None:
        html = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    else:
        error_message = "Error reading score"

    if error_message:
        html = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1><div id="score" style="color:red">{error_message}</div></h1>
        </body>
        </html>
        """

    return html


@app.route("/score")
def show_score():
    return score_server()


if __name__ == "__main__":
    app.run()
