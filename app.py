import pickle
from flask import Flask,request,app,url_for,render_template
import numpy as np
import pandas as pd
from flask import flash
from flask import session
from Sudoku_code.sudoku_solver import issafe,solve_sudoku
from Sudoku_code.sudoku_validator import *
import copy




app=Flask(__name__, template_folder='./templates', static_folder='./static')

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'sudoku_solver_is_running'

@app.route("/")
def index():
    return render_template("input.html")

# NOTE : Tips below are most important
# Most important tip name attribute for input fields is important or else you can't fetch the data it will return empty list
# and request.form.values() will fetch all the values as input and name attribute even button of type submit is returned as " " value
# Do'nt give name to button if you give then filter its value while fetching values from form


# Refactor this
@app.route("/solve",methods=["POST"])  # methods has list of type of url hits Here only post is allowed not get as it was not listed
def solve():
    values=np.array(list(map(lambda a: 0 if a=='' else int(a),[x for x in list(request.form.values())]))).reshape((9,9))
    input_data=copy.deepcopy(values)
    # print(values)
    if isValidConfig(values, 9):
        # print(values)
        if (solve_sudoku(values, 0, 0)==1):
            solved_data=values
    else:
        return render_template("error_page.html")
    return render_template("solution.html",solution=solved_data,user_data=input_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001, debug=True)