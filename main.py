import os
from flask import Flask, render_template, request, send_file, send_from_directory, url_for
import requests
import csv
import urllib.parse
import sys

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("HomePage.html")

@app.route("/processData", methods = ["POST"])
def process_data():
    form = request.form
    country = form["country"]
    files = request.files.getlist("csvFile")
    # print(country)
    # print(files)
    filter_data(files)
    return "<h1> Thanks!!! </h1>"



def filter_data(files):
    open("output.txt","w").close()
    open("ex_output.txt","w").close()
    output_file = open("output.txt", "a")
    ex_output_file = open("ex_output.txt", "a")
    for file in files:
        file.save(file.filename)
        output = ""
        exception_output = ""
        with open(file.filename) as f:
            for line in f:
                if ((not line.isspace()) and (line.startswith("/") or line.startswith(" "))):
                    line= line.strip()
                    line = line.replace('\t', ' ')
                    line = ' '.join(line.split())+"\n"
                    output += line
                else:
                    exception_output+= line

        output_file.write(output)
        output_file.seek(0)
        ex_output_file.write(exception_output)

    
    for file in files:
        os.remove(file.filename)
    
    convert_txt_to_csv("output.txt")
    
    

def convert_txt_to_csv(txt_filename):
    #for redirect csv
    #csvFileName="Redirect_List.csv"
    with open(txt_filename, "r") as txt_file:
        lines = [line.split(" ")[:-1] for line in txt_file]
        lines = [["https://www.volvocars.com"+line[0], "https://www.volvocars.com"+ line[1]] for line in lines]
        #print(lines)
        with open("output.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(lines)
    #return render_template("DownloadAndPreviewPage.html",data={"output.csv":csvFileName})


def error_msg(msg):
    return '<b style="color: red">'+msg+'</b>'

def print_progress(num,den):
    sys.stdout.write(f"\r{num}/{den}")
    sys.stdout.flush()
    
if __name__ == '__main__':
    app.run(debug=True)