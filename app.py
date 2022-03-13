from flask import Flask, render_template # jsonify
import random
import sqlite3


# df = pd.read_csv("proverb_scrapping.csv") # , encoding='cp1252')
# print(df.head())
app = Flask(__name__)

@app.route('/')
def home():
    # return "<h1>Welcome to Coding</h1>"
    # return "Welcome to Proverb App. Here you can get random proverb, search proverb based on word or author."
    return render_template("home.html")

@app.route('/Random_Proverb', methods = ['GET'])
def Random_Proverb_Fetcher():
    conn = sqlite3.Connection("proverb_db.db")
    cur = conn.cursor()
    proverb_num_lst = list(cur.execute("SELECT Proverb_Num FROM proverbs"))
    proverb_count = max(proverb_num_lst)
    rand_num = (-1,)
    while rand_num not in proverb_num_lst:
        num = random.randint(1, proverb_count[0])
        rand_num = (num,)
    random_proverb = cur.execute("Select Proverb from proverbs where Proverb_Num = ?",rand_num).fetchone()
    conn.commit()
    conn.close()
    return render_template('random_proverb.html', prvb = random_proverb[0])


@app.route('/Keyword_Search/<string:keyword>') 
def Keyword_Search(keyword):
    keyword = str(keyword)
    conn = sqlite3.Connection("proverb_db.db")
    cur = conn.cursor()
    keyword_lst = {keyword.lower(), keyword.upper(), keyword.title(), keyword.capitalize()}
    result = set()
    for kw in keyword_lst:
        sett = set(conn.execute("Select Proverb from proverbs where proverb like ?",('%'+kw+'%',)))
        result = sett.union(result)
    # return jsonify(list(result))
    return render_template('keyword_search.html', kywd = keyword, result = result, len_result = len(result))

@app.route('/Author_Search/<string:athr_name>')
def Author_Search(athr_name):
    athr_name = str(athr_name).lower()
    conn = sqlite3.Connection("proverb_db.db")
    cur = conn.cursor()
    result = cur.execute("Select Proverb from proverbs where Author = ?",(athr_name,)).fetchall()
    result = list(result)
    conn.commit()
    conn.close()
    # return jsonify(result)
    return render_template('author_search.html', athr = athr_name, result = result, len_result = len(result))

# app.run(port=5000)


if __name__ == "__main__":
    app.run(debug=True)


