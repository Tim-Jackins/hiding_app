#!/usr/bin/env python

from flask import Flask, render_template, send_file, safe_join, request, redirect, flash, send_from_directory
import os

application  = Flask(__name__)
SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

@application .route('/')
def start_page():
    return render_template('index.html')

@application .route('/secret/')
def first_challange():
    filename = 'flag.wav'
    filepath = 'static/'
    return send_file(filename_or_fp=safe_join(filepath, filename),\
                    mimetype='audio/x-wav',\
                    as_attachment=True,\
                    attachment_filename=filename)

@application .route('/supersecret/', methods=['POST'])
def second_challenge():
    if 'flag{s0und5_g00d}' == request.form['guess'] or 's0und5_g00d' == request.form['guess']:
        filename = 'sshSecret'
        filepath = 'static/'
        return send_file(filename_or_fp=safe_join(filepath, filename),
                        as_attachment=True,
                        attachment_filename=filename)
    flash('warning|Not quite|Hmm, the noise seems to be annoying but also sneaky. There must be something hidden in it!')
    return redirect('/')

@application .route('/favicon.ico/')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    application .secret_key = SECRET_KEY
    application .run(host='0.0.0.0', port=80, debug=True)
