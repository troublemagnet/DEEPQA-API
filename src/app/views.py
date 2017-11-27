import sys
import json
from app import app
from app.retrieveanswer import RetrieveAnswer
from flask import request, make_response, jsonify

""" This is the function which adds answer to a particular queation"""
@app.route('/stuff', methods = ['POST'])
def ws_receive():
    """
    Args:
        message (Obj): object containing the User's query
    """
    print ('nikhil')
    print (request.method)
    print (request.form)
    data = request.form['text']
    print (data)
    # Compute the prediction
    question = data
    try:
        answer = RetrieveAnswer.callBot(question)
    except:  # Catching all possible mistakes
        answer = 'Error: Internal problem'

    print (answer)
    # Check eventual error
    if not answer:
    	answer = 'Error: Try a shorter sentence'
    else:
    	return jsonify(answer)



# @app.route('/stuff', methods = ['GET'])
# def ws_send(answer):
# 	"""
# 	For sending answer  to the rails app"""
# 	return jsonify(answer)
