from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask import render_template
from file2 import makePrediction
import numpy as np

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('age', type=str)
parser.add_argument('gender', type=str)
parser.add_argument('self_emp', type=str)
parser.add_argument('mental_disorders', type=str)
parser.add_argument('mental_healthinPast', type=str)
parser.add_argument('work_from_home', type=str)
parser.add_argument('technology', type=str)
parser.add_argument('benefits', type=str)
parser.add_argument('know_benefits', type=str)
parser.add_argument('wellness', type=str)
parser.add_argument('mental_issues', type=str)
parser.add_argument('mental_health', type=str)
    

@app.route('/survey', methods = ['POST', 'GET'])
def funcPost():
    c = None
    if request.method == 'POST':
        try:
            age = int(request.form['group0'])
            age2 = age
            if age2 < 15:
                age = 0
            elif age2 > 15 and age2 <= 35:
                age = 2
            else:
                age = 1
        except:
            age = 1

        dict1 = {"Male":2, "Female":0, "Other":1}
        gender = dict1[request.form['group1']]

        dict1 = {"Yes":0, "No":1}
        self_emp = dict1[request.form['group2']]

        dict1 = {"Yes":2, "Don't Know":1, "No":0}
        family_mental_disorders = dict1[request.form['group3']]

        dict1 = {"Yes":1, "No":0}
        mental_healthinPast = dict1[request.form['group4']]

        dict1 = {"Yes":1, "No":2, "Sometimes":0}
        work_from_home = dict1[request.form['group5']]

        dict1 = {"Yes":2, "No":0, "Kind off":1}
        long_working_hours = dict1[request.form['group6']]

        dict1 = {"Yes":0, "No":2, "Sometimes":1}
        work_recognition = dict1[request.form['group8']]

        dict1 = {"Good":0, "Bad":2, "Mixed":1}
        culture = dict1[request.form['group9']]

#        dict1 = {"Yes":2, "No":1, "May be":0}
#        wellness = dict1[request.form['group9']]

        dict1 = {"Yes":0, "No":2, "Sometimes":1}
        mental_issues = dict1[request.form['group10']]

        dict1 = {"Yes":0, "No":2, "May be":1}
        developed = dict1[request.form['group11']]

#        arr1 = [age, gender, self_emp, mental_disorders, mental_healthinPast, work_from_home, technology, benefits, know_benefits, wellness, mental_issues, mental_health]
        
        print(age)
        print(gender)
        print(work_from_home)
        result = age + gender + self_emp + family_mental_disorders + mental_healthinPast + work_from_home + long_working_hours + work_recognition + culture + mental_issues + developed
#        try:
#            #c = makePrediction(np.array(arr1,dtype='int'))
#            #c = c[0]
#        except:
#            c = 2
        dict1 = {0:"Mild", 1:"No", 2:"Depression"}
        if result <= 8:
            result = 1
        elif result <= 15:
            result = 0
        else:
            result = 2
        return render_template('results.html', result = dict1[result])
    return render_template('survey.html', result = c)

# @app.route('/query')
# def respond():
#     age = request.args['age']
#     gender = request.args['gender']
#     self_emp = request.args['self_emp']
#     mental_disorders  = request.args['mental_disorders ']
#     mental_healthinPast = request.args['mental_healthinPast']
#     work_from_home = request.args['work_from_home']
#     technology = request.args['technology']
#     benefits = request.args['benefits']
#     know_benefits = request.args['know_benefits']
#     wellness = request.args['wellness']
#     mental_issues = request.args['mental_issues']
#     mental_health = request.args['mental_health']

@app.route('/')
def index():
    return render_template('index.html')
#FAA831

class HelloWorld(Resource):
    def get(self):
        args = parser.parse_args()
        # un = str(args['username'])
        # pw = str(args['password'])
        age = int(args['age'])
        gender = int(args['gender'])
        self_emp = int(args['self_emp'])
        mental_disorders  = int(args['mental_disorders'])
        mental_healthinPast = int(args['mental_healthinPast'])
        work_from_home = int(args['work_from_home'])
        technology = int(args['technology'])
        benefits = int(args['benefits'])
        know_benefits = int(args['know_benefits'])
        wellness = int(args['wellness'])
        mental_issues = int(args['mental_issues'])
        mental_health = int(args['mental_health'])
        arr1 = [age, gender, self_emp, mental_disorders, mental_healthinPast, work_from_home, technology, benefits, know_benefits, wellness, mental_issues, mental_health]
        try:
            c = makePrediction(np.array(arr1,dtype='int'))
            c = str(c[0])
        except:
            c = "2"
        return jsonify(result=c)

api.add_resource(HelloWorld, '/testing')

if __name__ == "__main__":
    app.run(debug=True)

#2 - Depression
#1-No
#0-mild
