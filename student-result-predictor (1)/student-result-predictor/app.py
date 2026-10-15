from flask import Flask, request, render_template_string
import pickle
import os

app = Flask(__name__)
MODEL_VERSION = "1.0"

with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Student Result Predictor</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 620px; margin: 40px auto; padding: 0 18px; }
    .card { border: 1px solid #ddd; border-radius: 12px; padding: 24px; }
    label { display: block; margin-top: 14px; font-weight: bold; }
    input { width: 100%; box-sizing: border-box; padding: 10px; margin-top: 6px; }
    button { margin-top: 20px; padding: 11px 18px; cursor: pointer; }
    .result { margin-top: 20px; padding: 12px; background: #f1f5f9; border-radius: 8px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Student Result Predictor</h1>
    <p>Model version: {{ version }}</p>
    <form method="post">
      <label for="hours">Study hours per day (0–10)</label>
      <input id="hours" name="hours" type="number" min="0" max="10" step="0.1" required value="{{ hours }}">
      <label for="attendance">Attendance percentage (0–100)</label>
      <input id="attendance" name="attendance" type="number" min="0" max="100" step="0.1" required value="{{ attendance }}">
      <label for="marks">Internal marks (0–100)</label>
      <input id="marks" name="marks" type="number" min="0" max="100" step="0.1" required value="{{ marks }}">
      <button type="submit">Predict Result</button>
    </form>
    {% if prediction %}
      <div class="result"><strong>Predicted result: {{ prediction }}</strong></div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    hours = attendance = marks = ""
    if request.method == "POST":
        try:
            hours = float(request.form["hours"])
            attendance = float(request.form["attendance"])
            marks = float(request.form["marks"])
            if not (0 <= hours <= 10 and 0 <= attendance <= 100 and 0 <= marks <= 100):
                raise ValueError("Inputs are outside the allowed range.")
            result = model.predict([[hours, attendance, marks]])[0]
            prediction = "Pass" if int(result) == 1 else "Fail"
        except (ValueError, TypeError):
            prediction = "Please enter valid values in the allowed ranges."
    return render_template_string(
        PAGE, version=MODEL_VERSION, prediction=prediction,
        hours=hours, attendance=attendance, marks=marks
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
