from flask import Flask, request, render_template_string

from default_blueprint import dft_blueprint
from translate import translate

app = Flask(__name__)

app.register_blueprint(dft_blueprint)

translate.load_data("../Database")

if __name__ == '__main__':
    app.run()
