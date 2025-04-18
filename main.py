import os
from flask import Flask, render_template, request, redirect, url_for
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/')
def index():
    response = supabase.table('users').select("*").execute()
    users = response.data
    return render_template('users.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    
    supabase.table('users').insert({
        "name": name,
        "email": email
    }).execute()
    
    return redirect(url_for('index'))

@app.route('/delete/<user_id>')
def delete_user(user_id):
    supabase.table('users').delete().eq('id', user_id).execute()
    return redirect(url_for('index'))

@app.route('/update/<user_id>', methods=['POST'])
def update_user(user_id):
    name = request.form.get('name')
    email = request.form.get('email')
    
    supabase.table('users').update({
        "name": name,
        "email": email
    }).eq('id', user_id).execute()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)
