# AgriScience



AgriScience is a Django-based platform designed to optimize crop growth and farm management using real-time data and predictive analytics. Tailored for small-scale farms, AgriScience empowers farmers with actionable insights to enhance productivity, sustainability, and decision-making processes.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Features

- **Real-Time Data Collection**: Integrates with IoT devices to gather real-time data on soil moisture, temperature, humidity, and more.
- **Predictive Analytics**: Utilizes machine learning algorithms to forecast crop yields and detect potential issues before they arise.
- **User-Friendly Dashboard**: Provides an intuitive interface for farmers to monitor farm conditions, view analytics, and manage resources.
- **Weather API Integration**: Incorporates weather data to assist in planning and optimizing farming activities.
- **Automated Alerts**: Sends notifications for critical events such as low soil moisture levels or upcoming adverse weather conditions.
- **Scalable Architecture**: Designed to support multiple farms and extensive datasets with ease.

## Technologies Used

- **Backend**:
  - [Django](https://www.djangoproject.com/) - Web framework
  - [MySQL](https://www.mysql.com/) - Database management
  - [Django REST Framework](https://www.django-rest-framework.org/) - API development

- **Frontend**:
  - [Bootstrap](https://getbootstrap.com/) - CSS framework
  - [JavaScript](https://www.javascript.com/) - Interactive elements
  - [Chart.js](https://www.chartjs.org/) - Data visualization

- **IoT Integration**:
  - [MQTT](https://mqtt.org/) - Messaging protocol
  - [Raspberry Pi](https://www.raspberrypi.org/) - Hardware for data collection

- **APIs**:
  - [OpenWeatherMap API](https://openweathermap.org/api) - Weather data

- **Others**:
  - [Docker](https://www.docker.com/) - Containerization
  - [Git](https://git-scm.com/) - Version control

## Installation

Follow these steps to set up AgriScience on your local machine:

### Prerequisites

- **Python 3.8+**
- **MySQL Server**
- **Docker** (optional, for containerization)
- **Git**

### Clone the Repository

```bash
git clone https://github.com/mantavya0807/AgriScience.git
cd AgriScience
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root directory and add the following variables:

```env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=agriscience_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306

# Weather API
WEATHER_API_KEY=your_openweathermap_api_key
```

### Set Up the Database

Ensure MySQL is running and create a database:

```sql
CREATE DATABASE agriscience_db;
CREATE USER 'your_db_user'@'localhost' IDENTIFIED BY 'your_db_password';
GRANT ALL PRIVILEGES ON agriscience_db.* TO 'your_db_user'@'localhost';
FLUSH PRIVILEGES;
```

### Apply Migrations

```bash
python manage.py migrate
```

### Load Initial Data (Optional)

If you have fixture files or initial data, load them using:

```bash
python manage.py loaddata initial_data.json
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

## Usage

1. **Dashboard**: After logging in, navigate to the dashboard to view real-time data collected from IoT devices.
2. **Analytics**: Access predictive analytics to forecast crop yields and monitor farm conditions.
3. **Settings**: Configure farm details, IoT devices, and notification preferences.
4. **Alerts**: Receive automated alerts for critical events and take timely actions.

## Screenshots

### Dashboard

![Dashboard](https://github.com/mantavya0807/AgriScience/raw/main/static/projects/agriscience-dashboard.png)

### Analytics

![Analytics](https://github.com/mantavya0807/AgriScience/raw/main/static/projects/agriscience-analytics.png)

### Settings

![Settings](https://github.com/mantavya0807/AgriScience/raw/main/static/projects/agriscience-settings.png)

## API Documentation

AgriScience provides RESTful APIs for integrating with external systems and IoT devices.

### Endpoints

- **Authentication**:
  - `POST /api/auth/login/` - User login
  - `POST /api/auth/logout/` - User logout

- **Devices**:
  - `GET /api/devices/` - List all IoT devices
  - `POST /api/devices/` - Add a new IoT device
  - `GET /api/devices/{id}/` - Retrieve a specific device
  - `PUT /api/devices/{id}/` - Update a device
  - `DELETE /api/devices/{id}/` - Delete a device

- **Data**:
  - `GET /api/data/` - Retrieve collected data
  - `POST /api/data/` - Submit new data

- **Analytics**:
  - `GET /api/analytics/yield/` - Get crop yield predictions
  - `GET /api/analytics/issues/` - Get potential issues based on data

### Authentication

AgriScience uses token-based authentication. Obtain a token by logging in and include it in the `Authorization` header for subsequent requests.

```http
Authorization: Token your_token_here
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a Feature Branch**

```bash
git checkout -b feature/YourFeature
```

3. **Commit Your Changes**

```bash
git commit -m "Add some feature"
```

4. **Push to the Branch**

```bash
git push origin feature/YourFeature
```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

- **Author**: Mantavya Mahajan
- **Email**: [mantavya@example.com](mailto:mantavya@example.com)
- **LinkedIn**: [linkedin.com/in/mantavya-mahajan-42972721b](https://www.linkedin.com/in/mantavya-mahajan-42972721b/)
- **GitHub**: [github.com/mantavya0807](https://github.com/mantavya0807)

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [OpenWeatherMap](https://openweathermap.org/)
- [Chart.js](https://www.chartjs.org/)
- [MQTT.org](https://mqtt.org/)

