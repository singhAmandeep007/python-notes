# import Flask class from flask module
from flask import Flask, jsonify, render_template

# create an instance of Flask class, __name__ is special variable that evaluates to the name of the current module. If module is run directly, then it is set to "__main__".
app = Flask(__name__)
# secret key is used to secure the session data. It is used to cryptographically sign the session cookie.
app.config["SECRET_KEY"] = "thisissecret"

JOBS = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "Bangalore",
        "company": "Google",
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi",
        "company": "Amazon",
    },
    {
        "id": 3,
        "title": "Product Manager",
        "location": "Chennai",
        "company": "PWC",
    },
]


# route() decorator is used to bind a function to a URL. So whenever the home page is requested, the hello() function will be called and the output of this function will be returned to the client.
@app.route("/")
def show_home():
    return render_template("home.html", JOBS=JOBS)


@app.route("/jobs/<int:job_id>")
def show_job(job_id):
    job = next((job for job in JOBS if job["id"] == job_id), None)
    if job:
        return render_template("job_page.html", job=job)
    return "Job not found", 404


@app.route("/api/v1/jobs")
def get_jobs():
    return jsonify(JOBS)


# route with a parameter (dynamic route)
@app.route("/api/v1/jobs/<int:job_id>")
def get_job(job_id):
    job = next((job for job in JOBS if job["id"] == job_id), None)
    if job:
        return jsonify(job)
    return jsonify({"message": "Job not found"}), 404


# NOTE: if the script is run directly using python interpreter, then the __name__ variable is set to __main__.
if __name__ == "__main__":
    # make the server publicly available by setting host='0.0.0.0'
    # enabling debug mode, the server will automatically reload if code changes
    app.run(debug=True, host="0.0.0.0")
