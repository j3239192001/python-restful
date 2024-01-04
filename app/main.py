from flask import Flask, request
import threading

app = Flask(__name__)

taskList = []
taskNum = 0
lock = threading.Lock()

@app.route('/tasks', methods=['GET'])
def getTaskList():
    resp = {'result': taskList}
    return resp, {'Content-Type': 'application/json'}

@app.route('/task', methods=['POST'])
def addTask():
    req = request.json
    if 'name' in req:
        name = req['name']
        newId = genUniqueId()
        newTask = {'name': name, 'status': 0, 'id': newId}
        global taskList
        taskList.append(newTask)
        resp = {'result': newTask}
        return resp
    else:
        resp = {'result': 'Field \'name\' is required.'}
        return resp

@app.route('/task/<int:id>', methods=['PUT'])
def updateTask(id):
    newTask = []
    global taskList
    for task in taskList:
        if task['id'] == id:
            newTask = taskList.pop(taskList.index(task))
            break
    if newTask == []:
        resp = {'result': f'Record {id} not found.'}
        return resp, 201
    else:
        req = request.json
        if 'name' in req:
            newTask['name'] = req['name']
        if 'status' in req:
            newTask['status'] = req['status']
        # if 'id' in req:
        #     newTask['id'] = req['id']
        taskList.append(newTask)
        resp = {'result': newTask}
        return resp, 201

@app.route('/task/<int:id>', methods=['DELETE'])
def deletTask(id):
    global taskList
    for task in taskList:
        if task['id'] == id:
            taskList.pop(taskList.index(task))
    return ""

def genUniqueId():
    global taskNum
    with lock:
        taskNum += 1
        return taskNum

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = int('8080'), debug=False)