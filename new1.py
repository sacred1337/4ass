from flask import Flask, request, session, redirect, url_for, render_template
import requests
import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash


conn= psycopg2.connect(user="postgres", password="123", host="127.0.0.1", port="5433", database="nft_db")
cursor= conn.cursor()


def solana(conn, cursor, address):


    url = f'https://solana-gateway.moralis.io/nft/mainnet/' + address + '/metadata'
    headers = {"accept": "application/json",
               "X-API-Key": "u8emWI08OHGRqpKRzmO3Y3gW4OhbTdOdVRuJobooGeSvYRGjep6bmjuIDVu8RqEI"}
    response = requests.get(url, headers=headers)


    cursor.execute(
        "INSERT INTO nft (address, info) values (" + "'" + address + "'" + "," + "'" + response.text + "'" + ")");
    conn.commit()

    return f''' 
                    <h1>infp: {response.text} </h1>
                                    '''






app = Flask(__name__)
app.secret_key = "dfjngbhbdvjdsvbisdb"

@app.route('/', methods=["POST", "GET"])
def index():
    if 'loggedin' in session:
            if request.method=='POST':
                address =request.form.get('nftaddress')

                try:
                    postgreSQL_select_Query = "SELECT info FROM nft WHERE address=" + "'" + address + "'" + ";"
                    cursor.execute(postgreSQL_select_Query)
                    mobile_records = cursor.fetchall()

                    if mobile_records== []:
                        solana(address)
                    else:
                        for row in mobile_records:
                            return f''' 
                                        <h1>infp: {row[0]} </h1>
                                                        '''


                except:
                    return solana(conn, cursor, address)




                cursor.close()
                conn.close()


            return f'''
                            <form method="POST">
                                <div><label>Get address: <input type="text" name="nftaddress"></label></div>
                                <input type="submit" value="Submit">
                            </form>
                            <a href="{url_for('out')}">Logout</a>
'''
            

    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':
        username = request.form['username']
        pass1 = request.form['pass1']

        cur.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cur.fetchone()

        if account:
            password_rs = account['pass1']
            if check_password_hash(password_rs, pass1):
                session['loggedin'] = True
                return redirect(url_for('index'))
            else:
                return redirect(url_for('err'))
        else:
            return redirect(url_for('err'))

    return render_template('login.html')

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST' and 'username' in request.form and 'pass1' in request.form:
        mail = request.form['mail']
        username = request.form['username']
        pass1 = request.form['pass1']

        _hashed_password = generate_password_hash(pass1)

        cur.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cur.fetchone()

        if account:
            return redirect(url_for('err'))
        else:

            cur.execute("INSERT INTO users (mail, username, pass1) VALUES (%s,%s,%s) RETURNING *", (mail, username, _hashed_password))
            account = cur.fetchone()
            conn.commit()
            session['loggedin'] = True
            session['username'] = account['username']
            return redirect(url_for('index'))

    elif request.method == 'POST':

        return redirect(url_for('err'))


    return render_template('reg.html')

@app.route('/out')
def out():
    session.pop('loggedin', None)

    return redirect(url_for('login'))

@app.route('/err')
def err():
    return render_template('err.html')


if __name__ == '__main__':
    app.run(debug=True)