import os

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

bookings = []


@app.route("/")
def home():
    return render_template(
        "index.html",
        bookings=bookings,
        commit=os.getenv("RENDER_GIT_COMMIT", "local"),
    )


@app.route("/book", methods=["POST"])
def book_service():
    customer_name = request.form.get("customer_name", "").strip()
    vehicle_number = request.form.get("vehicle_number", "").strip()
    vehicle_type = request.form.get("vehicle_type", "").strip()
    service_type = request.form.get("service_type", "").strip()
    service_date = request.form.get("service_date", "").strip()
    contact_number = request.form.get("contact_number", "").strip()

    if (
        not customer_name
        or not vehicle_number
        or not vehicle_type
        or not service_type
        or not service_date
        or not contact_number
    ):
        return "All fields are required.", 400

    booking = {
        "customer_name": customer_name,
        "vehicle_number": vehicle_number,
        "vehicle_type": vehicle_type,
        "service_type": service_type,
        "service_date": service_date,
        "contact_number": contact_number,
    }

    bookings.append(booking)

    return redirect(url_for("home"))


@app.route("/api/bookings")
def api_bookings():
    return jsonify(bookings)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=True,
    )
