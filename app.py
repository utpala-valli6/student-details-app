from flask import Flask, render_template_string

app = Flask(__name__)

students = [
    {"id": "101", "name": "Aarav", "course": "Computer Science"},
    {"id": "102", "name": "Priya", "course": "Biology"},
    {"id": "103", "name": "Rohan", "course": "Maths"},
    {"id": "104", "name": "Ananya", "course": "Physics"}
]

html = """
<html>
<head>
    <title>Student List</title>
</head>
<body>
    <h2>Student Details</h2>
    <table border="1" cellpadding="10">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Course</th>
        </tr>
        {% for s in students %}
        <tr>
            <td>{{ s.id }}</td>
            <td>{{ s.name }}</td>
            <td>{{ s.course }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html, students=students)

if __name__ == '__main__':
    app.run()
