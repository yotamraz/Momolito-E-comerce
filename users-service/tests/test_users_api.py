def test_health_check(client):
    """Test root health-check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "users-service"


def test_create_user(client):
    """Test creating a new user."""
    response = client.post(
        "/usuarios/",
        json={"nombre": "Juan Pérez", "email": "juan@example.com"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Juan Pérez"
    assert data["email"] == "juan@example.com"
    assert "id" in data


def test_create_user_duplicate_email(client):
    """Test that creating a user with a duplicate email returns 400."""
    client.post(
        "/usuarios/",
        json={"nombre": "Juan Pérez", "email": "juan@example.com"},
    )
    response = client.post(
        "/usuarios/",
        json={"nombre": "Otro Juan", "email": "juan@example.com"},
    )
    assert response.status_code == 400
    assert "email ya está registrado" in response.json()["detail"]


def test_list_users_empty(client):
    """Test listing users when no users exist."""
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert response.json() == []


def test_list_users(client):
    """Test listing users after creating some."""
    client.post(
        "/usuarios/",
        json={"nombre": "Juan", "email": "juan@example.com"},
    )
    client.post(
        "/usuarios/",
        json={"nombre": "María", "email": "maria@example.com"},
    )
    response = client.get("/usuarios/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_get_user_by_id(client):
    """Test retrieving a user by ID."""
    create_response = client.post(
        "/usuarios/",
        json={"nombre": "Juan", "email": "juan@example.com"},
    )
    user_id = create_response.json()["id"]

    response = client.get(f"/usuarios/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["nombre"] == "Juan"
    assert data["email"] == "juan@example.com"


def test_get_user_not_found(client):
    """Test that requesting a non-existent user returns 404."""
    response = client.get("/usuarios/999")
    assert response.status_code == 404
    assert "Usuario no encontrado" in response.json()["detail"]


def test_create_user_missing_nombre(client):
    """Test that creating a user without nombre returns validation error."""
    response = client.post(
        "/usuarios/",
        json={"email": "test@example.com"},
    )
    assert response.status_code == 422


def test_create_user_empty_nombre(client):
    """Test that creating a user with empty nombre returns validation error."""
    response = client.post(
        "/usuarios/",
        json={"nombre": "", "email": "test@example.com"},
    )
    assert response.status_code == 422
