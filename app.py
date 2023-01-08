from flask import Flask, render_template
import csv
import os, os.path
import time

app = Flask(__name__)

WORDGROUPS_DIR = "WordGroups"

#region Index

@app.route('/')
def index():
    wordgroup_stat = get_wordgroup_stat()
    return render_template('index/index.html',
                            wordgroup_stat = wordgroup_stat,
                            enumerate = enumerate,
                            rand = time.time()
            )

def get_wordgroup_stat():
    return {
        "wordlistCount" : len([name for name in os.listdir(WORDGROUPS_DIR)]),
        "wordCountInWordlist" : get_wordcount_in_wordgroup()
    }

def get_wordcount_in_wordgroup():
    csvfiles = [
                    open(os.path.join(WORDGROUPS_DIR, file), newline='', encoding='utf-8')
                    for file in os.listdir(WORDGROUPS_DIR)
               ]
    
    rowcounts = [
                    get_rowcount_of_csvfile(csvfile)
                    for csvfile in csvfiles
                ]
    
    return rowcounts

def get_rowcount_of_csvfile(csvfile):
    csvreader = csv.reader(csvfile, delimiter=';')
    row_count = sum(1 for row in csvreader)
    return row_count

#endregion


#region WordPractce

@app.route('/get_wordlist_landingpage/<int:group_no>')
def get_wordlist_landingpage(group_no):
    
    wordlist = get_wordlist(group_no)
    return render_template('word_list/wordlist_landingpage.html',
                            wordlist = wordlist,
                            enumerate = enumerate,
                            group_no = group_no,
                            rand = time.time()
    )

def get_wordlist(group_no):
    spamreader = ''
    filename = os.path.join(WORDGROUPS_DIR, f"group_{group_no}.csv")
    csvfile = open(filename, newline='', encoding='utf-8')
    spamreader = csv.reader(csvfile, delimiter=';')
        
    return spamreader

#endregion

if __name__ == "__main__":
    app.run(debug=True)