from flask import render_template

from . import admin


@admin.route('', methods=['GET'])
def index():
    return render_template('admin.html')
