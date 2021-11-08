from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'my_temp_secret_key'