from flask import Blueprint, render_template, request

from translate import translate

dft_blueprint = Blueprint("default", __name__)


@dft_blueprint.route("/", methods=['GET', 'POST'])
def main():
    output_text = ''
    if request.method == 'POST':
        input_text = request.form['input_text']
        action = request.form['action']
        output_text = translate.query(input_text, 'Mainland' if action == '大陆化' else 'Taiwan')
    return render_template("translate.html", output_text=output_text)
