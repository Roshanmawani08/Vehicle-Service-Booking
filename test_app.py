from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_add_booking():
    client = app.test_client()

    response = client.post(
        "/book",
        data={
            "customer_name": "Rahul",
            "vehicle_number": "MH12AB1234",
            "vehicle_type": "Car",
            "service_type": "General Service",
            "service_date": "2026-10-01",
            "contact_number": "9876543210",
        },
    )

    assert response.status_code == 302


def test_invalid_booking():
    client = app.test_client()

    response = client.post(
        "/book",
        data={
            "customer_name": "",
            "vehicle_number": "MH12AB1234",
            "vehicle_type": "Car",
            "service_type": "General Service",
            "service_date": "2026-10-01",
            "contact_number": "9876543210",
        },
    )

    assert response.status_code == 400
