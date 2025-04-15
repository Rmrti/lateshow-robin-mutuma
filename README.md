# Lateshow API – Robin Mutuma

This is a RESTful API built with Flask for managing guest appearances on a fictional late-night talk show. It allows you to track guests, episodes, and their appearances.

---

## Features

- Add new guest appearances
- List all episodes and guests
- Retrieve a specific episode
- Delete an episode by ID
- Persistent storage with SQLite
- Database migrations with Alembic
- Postman collection for testing included

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/lateshow-robin-mutuma.git
cd lateshow-robin-mutuma
```

### 2. Install dependencies and activate virtual environment

```bash
pip install -r requirements.txt
python3.12 -m venv venv
source venv/bin/activate (used venv since my laptop had issues with pipenv)
```

### 3. Run database migrations

```bash
flask upgrade head
```

### 4. Start the server

```bash
python run.py
```

The server will run at http://127.0.0.1:5555

---

## API Endpoints

| Method | Endpoint              | Description                         |
|--------|-----------------------|-------------------------------------|
| GET    | /episodes             | Retrieve all episodes               |
| GET    | /guests               | Retrieve all guests                 |
| GET    | /episode/<int:id>     | Retrieve a specific episode         |
| DELETE | /episodes/<int:id>    | Delete a specific episode by ID     |
| POST   | /appearances          | Create a new appearance entry       |

---

## Project Structure

```
lateshow/
├── run.py
├── requirements.txt
├── server/
│   ├── app.py
│   ├── models.py
│   └── lateshow.db
├── migrations/
└── challenge-4-lateshow.postman_collection.json
```

---

## Postman

A Postman collection is included in the root of the project:

`challenge-4-lateshow.postman_collection.json`

Use it to quickly test all endpoints.

---


---

## Author

Robin Mutuma

---

## License

This project is for educational/demo purposes only.
