import flask.cli
from flask import redirect, url_for, render_template, request, flash
from datetime import datetime, time

from logger import app, db
from logger.models import Planes
from logger.forms import NewPlane

with app.app_context():
    db.create_all()
    db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def home():
    form = NewPlane()
    planes_db = db.session.execute(db.select(Planes)).scalars()
    planes = []
    if request.method == 'POST':
        if form.validate_on_submit():
            for index in planes_db:
                if index.registracion == str(form.reg.data).upper():
                    flash(f"{str(form.reg.data).upper()} már szerepel a rendszerben!", "danger")
                    break
            else:
                plane = Planes(registracion=str(form.reg.data).upper(),
                               takeofftime=time(int(datetime.now().hour), int(datetime.now().minute), int(datetime.now().second))
                               )
                db.session.add(plane)
                db.session.commit()
                flash(f"{str(form.reg.data).upper()} lajstromú repülőgépet sikeresen rögzítette.", "success")
            return redirect(url_for('home'))
    for index in planes_db:
        now = datetime.now().strftime('%H:%M:%S')
        if datetime.strptime(now, '%H:%M:%S') < datetime.strptime(str(index.takeofftime), "%H:%M:%S"):
            flash(f"{str(index.registracion).upper()} lajstromú repülőgép nem a mai napon szált fel utoljára!", "info")
            beforetime = "-0"
        else:
            beforetime = datetime.strptime(now, '%H:%M:%S') - datetime.strptime(str(index.takeofftime), "%H:%M:%S")
            beforetime = 60 - round(beforetime.total_seconds()/60)
            if beforetime < 0: beforetime = 0

        planes.append({
            'id': index.id,
            'registracion': index.registracion,
            'takeofftime': index.takeofftime,
            'beforetime': beforetime
        })
    return render_template('logging.html', form=form, planes=planes)

@app.route('/retakoff/<int:plane_id>')
def retakeoff(plane_id):
    current_plane = Planes.query.get_or_404(plane_id)
    current_plane.takeofftime = time(int(datetime.now().hour), int(datetime.now().minute), int(datetime.now().second))
    db.session.commit()
    flash(f"{str(current_plane.registracion).upper()} lajstromú repülőgépet sikeresen felszállította.", "success")
    return redirect(url_for('home'))

@app.route('/delplane/<int:plane_id>')
def delplane(plane_id):
    current_plane = Planes.query.get_or_404(plane_id)
    db.session.delete(current_plane)
    db.session.commit()
    flash(f"{str(current_plane.registracion).upper()} lajstromú repülőgépet sikeresen törölte.",  "success")
    return redirect(url_for('home'))

@app.route('/howto')
def howto():
    return render_template('howto.html')


@app.route('/about')
def about():
    return render_template('about.html')