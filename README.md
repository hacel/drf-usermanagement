# Learning authentication and user management on drf


## Endpoints

    # GET, POST
    localhost:8000/api/0.1/user/
    
    # GET, PUT, DELETE
    localhost:8000/api/0.1/user/<pk>

    # POST
    localhost:8000/api/0.1/token-auth/

## Fields

    {
        "username": "<username>",
        "password": "<password>",
        "is_admin": "<True/False>"
    }


### Examples

    # Get Authentication Token
    curl -H "Content-Type: application/json" -d '{"username":"<username>", "password":"<password>"}' http://localhost:8000/api/0.1/token-auth/

    # Get User List
    curl -H "Accepts: application/json" http://localhost:8000/api/0.1/user/
    
    # Create User
    curl -H "Content-Type: application/json" -d '{"username": "<username>", "password": "<password>", "is_admin": <bool>} http://localhost:8000/api/0.1/user/

    # Get User
    curl -H "Accepts: application/json" http://localhost:8000/api/0.1/user/<pk>/

    # Update User
    curl -H "Content-Type: application/json" -d '{"username": "<username>", "password": "<password>", "is_admin": <bool>} http://localhost:8000/api/0.1/user/<pk>/

    # Delete User
    curl -X DELETE http://localhost:8000/api/0.1/user/<pk>/

