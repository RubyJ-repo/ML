from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        exercise = request.form['exercise']
        duration = request.form['duration']
        with open('exercise_log.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([exercise, duration])
        return redirect('/log')
    else:
        exercises = []
        with open('exercise_log.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                exercises.append({'exercise': row[0], 'duration': row[1]})
        return render_template('log.html', exercises=exercises)

if __name__ == '__main__':
    app.run(debug=True)
