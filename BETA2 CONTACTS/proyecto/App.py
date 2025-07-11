from flask import Flask, render_template, request, redirect , url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)


# MYSQL Conection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'thomas2009'
app.config['MYSQL_DB'] = 'FLASKCONTACTS'
mysql = MySQL(app)

#settings

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        NOMBRES = request.form['NOMBRES']
        CONTACTO = request.form['CONTACTO']
        EMAIL = request.form['EMAIL']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO CONTACTS (NOMBRES, CONTACTO, EMAIL) VALUES (%s, %s, %s)',
                    (NOMBRES,CONTACTO,EMAIL))
        mysql.connection.commit()
        flash('conctato añadido satisfactoriamente')
        return redirect(url_for('Index'))


@app.route('/edit/<ID>')
def get_contact(ID):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE ID = %s', (ID,))
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<ID>', methods=['POST'])
def update_contact(ID):
    if request.method == 'POST':
        NOMBRES = request.form['NOMBRES']
        CONTACTO = request.form['CONTACTO']
        EMAIL = request.form['EMAIL']
    cur=mysql.connection.cursor()
    cur.execute("""
     UPDATE contacts
    SET NOMBRES = %s,
        EMAIL = %s,
        CONTACTO = %s
    WHERE ID = %s                     
    """, (NOMBRES, EMAIL, CONTACTO, ID))
    mysql.connection.commit()
    flash('contacto actualizado satisfactoriamente')
    return redirect(url_for('Index'))


@app.route('/delete/<ID>')
def delete_contact(ID):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE ID ={0}'.format(ID))
    mysql.connection.commit()
    flash('contacto removido satisfactoriamente')
    return redirect (url_for('Index'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)
