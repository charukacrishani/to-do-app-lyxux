import mysql.connector
from flask import Flask, request
from datetime import datetime


app = Flask (__name__)

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "todo"
)

cursor = conn.cursor()

@app.route('/', methods = ['GET'])
def index ():
    return "hello world"

@app.route('/gettask/<string:ddate>', methods=['GET'])
def get_task(ddate):
    # Execute SQL query to fetch tasks for the given date
    cursor.execute("SELECT id, task, isDone FROM tasks WHERE date = %s", (ddate,))
    task = cursor.fetchone()  # Assuming there's only one task per date
    if task:
        return ({
            "id": task[0],
            "task": task[1],
            "isDone": task[2]
        })
    else:
        return ({"error": f"No task found for date: {ddate}"}), 404

@app.route('/createnew', methods = ['POST'])
def create_new():
    data = request.get_json()
    task = data.get("task")
    ddate = data.get("ddate")
    isdone = data.get("isdone")
    cursor.execute ("INSERT INTO tasks (task, ddate, isdone) VALUES (%s, %s, %s, %s, %s)",(task, ddate, isdone))
    conn.commit()
    return{"message" : "task added"}

@app.route('/updateguest/<int:id>', methods = ['PUT'])
def update_task(id):
    data = request.get_json()
    task = data.get("task")
    ddate = data.get("ddate")
    isdone = data.get("isdone")
    cursor.execute('UPDATE tasks SET task = %s, ddate = %s, isdone = %s WHERE id = %s',(task, ddate, isdone, id))
    conn.commit()
    return{"message" : "task updated"}

@app.route('/delete/<int:id>', methods = ['DELETE'])
def delete_guest(id):
    cursor.execute('DELETE FROM tasks WHERE id = %s', (id,))
    conn.commit()
    return{"message" : " deleted"}

if __name__ == ('__main__'):
    app.run (debug = True)