import csv
from flask import Flask,url_for ,render_template,request, redirect 
#send_from_directory
app = Flask(__name__)
#print(__name__)
@app.route('/')
def my_home():
    return render_template('index.html') #ker je datoteka v enaki mapi, ne rabimo celotne poti

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name) 

#@app.route('/favicon.ico')
#def favicon():
	#return send_from_directory(os.path.join(app.root_path, 'static'),
                               #'favicon.ico')

#@app.route('/blog')
#def blog():
#	return 'These are my thoughts on blog'

#@app.route('/blog/2020/dogs')
#def blog2():
#	return 'This is my dog'
def write_to_file(data): #mode a means append
	with open('database.txt',mode='a') as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data): #mode a means append
	with open('database.csv',newline='' ,mode='a') as csvfile:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		writer=csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=="POST":
    	try:
    		data=request.form.to_dict()
    		#write_to_file(data)
    		write_to_csv(data)
    		return redirect('thankyou.html')
    	except:
    		return 'did not save to database'
    else:
    	return 'Something went wrong. Try again!'