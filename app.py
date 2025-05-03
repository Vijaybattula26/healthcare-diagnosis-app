from flask import Flask, render_template, request
from model.diagnosis_model import diagnose

app = Flask(__name__)

# Define possible diseases (this can be expanded with a medical knowledge graph)
diseases = ["Flu", "Cold", "Covid-19", "Migraine", "Pneumonia",
            "Allergy", "Asthma", "Stomach Infection", "Tuberculosis"]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symptoms = request.form['symptoms']

        # Call the diagnose function with the symptoms
        diagnosis_result = diagnose(symptoms)

        # Find the index of the disease with the highest confidence score
        max_score_index = diagnosis_result['scores'].index(max(diagnosis_result['scores']))

        # Get the disease name and confidence score of the highest confidence disease
        predicted_disease = diagnosis_result['labels'][max_score_index]
        # Convert to percentage
        confidence_score = diagnosis_result['scores'][max_score_index] * 100

        # Return only the highest confidence disease
        return render_template('index.html', predicted_disease=predicted_disease,
                               confidence_score=confidence_score, symptoms=symptoms)

    return render_template('index.html', predicted_disease=None)


if __name__ == "__main__":
    app.run(debug=True)
