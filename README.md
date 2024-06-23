# User Management Django Project

## Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/IsmailTitas1815/custom-user-management.git
   cd custom-user-management
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv        # On Mac (sometimes on Linux) use `python3 -m venv venv`
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

7. Find the `authentication_token` for users in the Django admin interface.
   - Visit [django admin](http://127.0.0.1:8000/admin/users/customuser/) and log in with the superuser credentials. (Assuming the application is running on `local machine using 8000 port`)

8. API Endpoints:
   
   - `GET /API/users/` - List all users (Only customer)
   - `GET /API/users/<username>/` - Get user detail (Only customer)
   - `POST /API/users/` - Create a new user (Only manager)
   - `PUT /API/users/<username>/` - Update a user (Only manager)
   - `PATCH /API/users/<username>/` - Partial Update a user (Only manager)
   - `DELETE /API/users/<username>/` - Delete a user (Only manager)

   ## N.B: Don't forget to add trailing slash in the end of the url like the above.

9. Postman API Documentation:
   - Download the Postman collection and environment files from [Google Drive](https://drive.google.com/drive/folders/1F-Dp4N5lltO-MnpNdtzq1UDUSZIQFK4W). 
   - Import the collection and environment file into Postman.

## Notes:
- For creating a user, you need to provide a `username`, `email`, and `password` in the `request body`.
- All requests must include the `token` as `authentication_token` in the `request body`(Not in the headers as per requirement) for authentication.
- Only manager type users can create, update, or delete users.
- Only customer type users can view the list of users or details of a user.
