from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
courses = [
    {
        'courseID': 1,
        'courseName': 'python programming'
    },
    {
        'courseID': 2,
        'courseName': 'data science'
    },
    {
        'courseID': 3,
        'courseName': 'web dev'
    },
    {
        'courseID': 4,
        'courseName': 'nlp'
    },

]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/app/api/courses/all')
def show():
    return jsonify(courses)


@app.route('/app/api/courses', methods=['GET'])
def id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "unknown request"

    result = []

    for course in courses:
        if course['courseID'] == id:
            result.append(course)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

