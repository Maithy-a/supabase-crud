# Supabase-CRUD

A Python-based **Flask web application** for performing CRUD (Create, Read, Update, Delete) operations on a Supabase database table.

This app provides a simple, browser-based interface to display, create, edit, and delete user records, leveraging Supabase's real-time capabilities and Flask's lightweight structure for efficient data management.

---

## Features

- **Display**: View all user records from a Supabase table in a dynamic web interface.
- **Create**: Add new users easily through a form (Name and Email fields).
- **Edit**: Update existing user details in real time.
- **Delete**: Remove users with a simple button click.
- **Real-time Updates**: Powered by Supabase backend services.
- **Built with Flask**: Lightweight Python web framework for rapid development.
- **Supabase Python Client**: For seamless interaction with your database.

---

## Tech Stack

- **Python**: Backend programming language.
- **Flask**: Web framework for server-side logic and routing.
- **Supabase**: Backend-as-a-service platform providing database and authentication.
- **Supabase Python Client**: Python SDK to perform database operations.
- **HTML/CSS/JavaScript**: For frontend templates and user interactions.
---

## Installation

1. **Clone the Repository**

```bash
git clone https://github.com/Maithy-a/supabase-crud.git
cd supabase-crud

```

1. **Create a Virtual Environment (Recommended)**

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux

.venv\Scripts\activate      # Windows

```

1. **Install Dependencies**

```bash
pip install -r requirements.txt

```

If `requirements.txt` is not provided, you can manually install:

```bash
pip install flask supabase python-dotenv

```

1. **Environment Variables**

Create a `.env` file in the project root and add:

```
SUPABASE_URL=your-supabase-project-url
SUPABASE_KEY=your-supabase-api-key

```

---

## Configuration

Make sure your Supabase project includes the following `users` table:

```sql
CREATE TABLE public.users (
  id UUID NOT NULL DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  CONSTRAINT users_pkey PRIMARY KEY (id),
  CONSTRAINT users_id_key UNIQUE (id)
) TABLESPACE pg_default;

```

✅ Also, ensure the appropriate **Row Level Security (RLS)** policies are enabled or disabled as needed.

---

## Usage

1. **Run the Flask App**

```bash
python app.py

```

1. **Open your browser**

Navigate to:

```
http://localhost:5000

```

You can now:

- View all users
- Add a new user
- Edit a user's information
- Delete a user

---
## Troubleshooting

- **Invalid Supabase Credentials**: Check your `.env` file for mistakes.
- **CORS Errors**: Flask might need CORS support if you’re expanding to separate frontends.
- **Database Permissions**: Review your Supabase RLS settings if data actions fail.
- **Port Conflicts**: If `localhost:5000` is occupied, configure Flask to run on another port.

---

## Contributors

- [Maithy-a](https://github.com/Maithy-a)

## License

This project is licensed under the [MIT License](https://chatgpt.com/g/g-wpMtgVmzG-readme-generator/c/LICENSE).
