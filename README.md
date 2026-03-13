# 🏥 EPS CitaMédica

Sistema web de gestión de citas médicas construido con **Flask + MySQL**.
Funciona tanto en local como desplegado en **Render** con base de datos **Aiven (MySQL)**.

---

## 🚀 Instalación Local

### 1. Clonar y crear entorno virtual
```bash
git clone <repo>
cd eps_citas_app
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
```bash
cp .env.example .env
# Edita .env con tus credenciales locales
```

Ejemplo de `.env` para desarrollo local:
```
FLASK_ENV=development
SECRET_KEY=cualquier-clave-segura
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=tu_password
MYSQL_DB=eps_citas
MYSQL_SSL=false
```

### 4. Crear la base de datos
```bash
mysql -u root -p < database.sql
```

### 5. Ejecutar
```bash
python app.py
# Abre http://localhost:5000
```

---

## ☁️ Despliegue en Render + Aiven

### Base de datos (Aiven)
1. Crea un servicio **MySQL** en [Aiven Console](https://console.aiven.io)
2. Copia el **Host**, **Port**, **User**, **Password** y **Database** del servicio
3. Ejecuta el archivo `database.sql` en tu instancia Aiven para crear las tablas

### App (Render)
1. Conecta tu repositorio en [Render Dashboard](https://dashboard.render.com)
2. Crea un **Web Service** con:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
3. Agrega las siguientes **Environment Variables**:

| Variable        | Valor                        |
|-----------------|------------------------------|
| `FLASK_ENV`     | `production`                 |
| `SECRET_KEY`    | genera uno aleatorio         |
| `MYSQL_HOST`    | `xxx.aivencloud.com`         |
| `MYSQL_PORT`    | `3306`                       |
| `MYSQL_USER`    | `avnadmin`                   |
| `MYSQL_PASSWORD`| tu contraseña de Aiven       |
| `MYSQL_DB`      | `defaultdb`                  |
| `MYSQL_SSL`     | `true`                       |

---

## 📁 Estructura del Proyecto

```
eps_citas_app/
├── app.py                  ← Rutas Flask
├── config.py               ← Configuración por entorno
├── database.py             ← Conexión MySQL (local + Aiven SSL)
├── database.sql            ← Esquema de tablas
├── models/
│   ├── pacientes.py        ← CRUD pacientes
│   └── citas.py            ← CRUD citas
├── templates/              ← HTML Jinja2
├── static/css/style.css    ← Estilos
├── .env.example            ← Plantilla de variables
├── requirements.txt
├── Procfile                ← Para Render/Heroku
└── render.yaml             ← Config automática Render
```

---

## 🔧 Funcionalidades

- ✅ Registrar pacientes
- ✅ Reservar citas (con médico, tipo, fecha, hora, dirección)
- ✅ Consultar citas por documento
- ✅ Actualizar citas existentes
- ✅ Eliminar citas
