from flask import Flask, render_template, request, redirect, jsonify
import csv
import os

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

@app.route("/")
def home():
    # Create the `todo.csv` file if it doesn't exist
    if not os.path.exists("todo.csv"):
        with open("todo.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Task Name", "Completion Status"])

    # Read the `todo.csv` file and pass the data to the template
    todo_list = []
    with open("todo.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip the header row
        for row in reader:
            todo_list.append({"task_name": row[0], "completion_status": row[1]})
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add_task():
    # Add a new task to the `todo.csv` file
    new_task_name = request.form["new_task_name"]
    with open("todo.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_task_name, "incomplete"])
    return redirect("/")

@app.route("/complete", methods=["POST"])
def complete_task():
    # Update the completion status of a task in the `todo.csv` file
    task_index = int(request.form["task_index"])
    completion_status = "complete" if request.form.get("completion_status") else "incomplete"
    with open("todo.csv", "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    rows[task_index + 1][1] = completion_status
    with open("todo.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete_task():
    # Delete a task from the `todo.csv` file
    task_index = int(request.form["task_index"])
    with open("todo.csv", "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    del rows[task_index + 1]
    with open("todo.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return redirect("/")

@app.route("/status")
def get_status():
    # Read the `todo.csv` file and return the data as a JSON object
    todo_list = []
    with open("todo.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip the header row
        for row in reader:
            todo_list.append({"task_name": row[0], "completion_status": row[1]})
    return jsonify(todo_list)

if __name__ == "__main__":
    app.run(debug=True)
