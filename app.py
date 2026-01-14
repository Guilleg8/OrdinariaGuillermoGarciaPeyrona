from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Service, Reservation

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_secreto_super_seguro'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicializar extensiones
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# --- función para crear datos iniciales ---
def seed_data():
    with app.app_context():
        db.create_all()
        # crear usuarios si no existen
        if not User.query.first():
            usuarios = [
                User(username='residente1', password='a123456789'),
                User(username='residente2', password='b123456789'),
                User(username='residente3', password='c123456789'),
                User(username='residente4', password='d123456789')
            ]
            db.session.add_all(usuarios)
            db.session.commit()
        # crear servicios si no existen
        if not Service.query.first():
            gym = Service(name='Gimnasio', max_capacity=2)  # Capacidad baja para probar
            pool = Service(name='Piscina', max_capacity=5)
            sauna = Service(name='Sauna', max_capacity=1)
            db.session.add_all([gym, pool, sauna])

        db.session.commit()


# --- rutas ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos.')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def dashboard():
    # mostrar reservas del usuario actual
    my_reservations = Reservation.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', reservations=my_reservations, user=current_user)


@app.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    services = Service.query.all()

    if request.method == 'POST':
        service_id = int(request.form.get('service'))
        date = request.form.get('date')
        time = request.form.get('time')

        service = Service.query.get(service_id)

        # --- lógica crítica de capacidad ---
        current_bookings = Reservation.query.filter_by(
            service_id=service_id,
            date=date,
            time_slot=time
        ).count()

        if current_bookings >= service.max_capacity:
            flash(f'Error: El servicio {service.name} está lleno para ese horario (Máx: {service.max_capacity}).',
                  'error')
        else:
            new_res = Reservation(
                user_id=current_user.id,
                service_id=service_id,
                date=date,
                time_slot=time
            )
            db.session.add(new_res)
            db.session.commit()
            flash('¡Reserva creada con éxito!', 'success')
            return redirect(url_for('dashboard'))

    return render_template('book.html', services=services)


if __name__ == '__main__':
    seed_data()  # crear tablas y datos de prueba al iniciar
    app.run(debug=True)