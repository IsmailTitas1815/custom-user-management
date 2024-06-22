# User Management Django Project

## Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/IsmailTitas1815/custom-user-management.git
   cd custom-user-management
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `source venv/Scripts/activate`
   ```

3. Install the requirements
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server
   ```bash
   python manage.py runserver
   ```

7. API Endpoints:
   
   - `POST /API/users/` - Create a new user (Only manager)
   - `GET /API/users/` - List all users (Only customer)
   - `GET /API/users/<username>/` - Get user detail (Only customer)
   - `DELETE /API/users/<username>/` - Delete a user (Only manager)
   - `PUT /API/users/<username>/` - Update a user (Only manager)

   # N.B: Don't forget to add trailing slash in the end of the url like the above.

## Notes:
- For creating a user, you need to provide a `username`, `email`, and `password` in the `request body`.
- All requests must include the `token` as `authentication_token` in the `request body`(Not in the headers as per requirement) for authentication.
- Only manager type users can create, update, or delete users.
- Only customer type users can view the list of users or details of a user.
