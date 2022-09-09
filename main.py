from flask import Flask
import utills
app = Flask(__name__)

@app.route("/")
def index():
    candidates = utills.get_candidates_all()
    result = "<br>"
    for candidate in candidates:
        result += candidate["name"] + "<br>"
        result += candidate["position"] + "<br>"
        result += candidate["skills"] + "<br>"
        result += "<br>"

    return f"<pre> {result} </pre>"


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utills.get_candidate_by_pk(pk)
    result = "<br>"
    result += candidate["name"] + "<br>"
    result += candidate["position"] + "<br>"
    result += candidate["skills"] + "<br>"
    result += "<br>"
    return f"""
    <img src="{candidate.index["picture"]}">
    <pre> {result} </pre>"
    """

@app.route("/candidate/<skill>")
def get_candidates_by_skills(skill):
    candidates = utills.get_candidates_by_skills(skill.lower())
    result = "<br>"
    for candidate in candidates:
        result += candidate["name"] + "<br>"
        result += candidate["position"] + "<br>"
        result += candidate["skills"] + "<br>"
        result += "<br>"

    return f"<pre> {result} </pre>"


app.run(debug=True)