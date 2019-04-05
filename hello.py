from flask import Flask, request, render_template, send_file, redirect, url_for
import csv
import json
import io
import classify
import os

app = Flask(__name__)   #Create an instance of the class called __name__


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR,'static/images/plot.png')
csv_path = os.path.join(BASE_DIR,'static/images/sorted_tickets.csv')

print(BASE_DIR)
print(img_path)
print(csv_path)

def csv2json(data):
	reader = csv.DictReader(data)
	out = json.dumps([ row for row in reader ])
	return out

#Routing: Ties a URL to the return value of a python function
# @ = decorator - wrap a function and modify its behaviour

#Represent variables like this: <variable>
#<int:post_id> - for integer variables
#For non-strings, need to declare type

@app.route('/') #Root directory
def index():
    return 'Welcome to the home page.'

@app.route('/post', methods=['POST'])
def convert():
	f = request.files['file']
	file_contents = io.StringIO(f.stream.read().decode('utf-8'))
	result = csv2json(file_contents)
	classify.visualise(result, img_path, csv_path)
	return redirect(url_for('dataplot'))

@app.route('/dataplot')
def dataplot():
	return send_file(img_path, mimetype='image/png')

@app.route('/sorted1')
def show_sorted():
	return send_file(csv_path, mimetype='text/csv', attachment_filename='sorted_ticket_data.csv', as_attachment=True, cache_timeout=0)

if __name__ == '__main__':      #Check that we run only if the file is called directly
	print('About to run app...')
	app.run()       			#Start app
