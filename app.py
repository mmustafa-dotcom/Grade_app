from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DB_NAME = "grades.db"

# Database yaratmaq
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            a INTEGER,
            b INTEGER,
            c INTEGER,
            d INTEGER,
            e INTEGER,
            f INTEGER,
            final_grade TEXT
        )
    """)
    conn.commit()
    conn.close()

# Database-ə qeyd etmək
def save_grade(a, b, c, d, e, f, final_grade):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO grades (a, b, c, d, e, f, final_grade)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (a, b, c, d, e, f, final_grade))
    conn.commit()
    conn.close()

# HTML form + nəticə
@app.route("/", methods=["GEt","POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            a = int(request.form.get("a"))
            b = int(request.form.get("b"))
            c = int(request.form.get("c"))
            d = int(request.form.get("d"))
            e = int(request.form.get("e"))
            f = int(request.form.get("f"))

            if not (0 < a <= 100 and 0 < b <= 100 and 0 < c <= 100 and 0 < d <= 100 and 50 <= e <= 100 and 0 < f <= 100):
                result = "Enter correct numbers!"
            elif e < 70:
                result = "You are failed!"
                save_grade(a, b, c, d, e, f, result)
            else:
                g = ((a+b+c)/10) + (d/10) + (e/10) + (f/2)
                if 0 <= g < 51:
                    result = "You are failed!"
                elif 51 <= g < 61:
                    result = f"{g} (F)"
                elif 61 <= g < 71:
                    result = f"{g} (D)"
                elif 71 <= g < 81:
                    result = f"{g} (C)"
                elif 81 <= g < 91:
                    result = f"{g} (B)"
                elif 91 <= g <= 100:
                    result = f"{g} (A)"
                else:
                    result = "Enter correct numbers!"
                save_grade(a, b, c, d, e, f, result)
        except:
            result = "Please enter valid numbers!"

    return render_template("index.html", result=result)

# API endpoint
@app.route("/api/calculate_grade", methods=["POST"])
def api_calculate_grade():
    data = request.get_json()

    try:
        a = int(data.get("a"))
        b = int(data.get("b"))
        c = int(data.get("c"))
        d = int(data.get("d"))
        e = int(data.get("e"))
        f = int(data.get("f"))

        if not (0 < a <= 100 and 0 < b <= 100 and 0 < c <= 100 and 0 < d <= 100 and 50 <= e <= 100 and 0 < f <= 100):
            return jsonify({"error": "Enter correct numbers!"}), 400
        if e < 70:
            final_grade = "You are failed!"
            save_grade(a, b, c, d, e, f, final_grade)
            return jsonify({"result": final_grade})

        g = ((a+b+c)/10) + (d/10) + (e/10) + (f/2)
        if 0 <= g < 51:
            final_grade = "You are failed!"
        elif 51 <= g < 61:
            final_grade = f"{g} (F)"
        elif 61 <= g < 71:
            final_grade = f"{g} (D)"
        elif 71 <= g < 81:
            final_grade = f"{g} (C)"
        elif 81 <= g < 91:
            final_grade = f"{g} (B)"
        elif 91 <= g <= 100:
            final_grade = f"{g} (A)"
        else:
            return jsonify({"error": "Enter correct numbers!"}), 400

        save_grade(a, b, c, d, e, f, final_grade)
        return jsonify({"result": final_grade}), 201

    except:
        return jsonify({"error": "Please enter valid numbers!"}), 400

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=8000)
