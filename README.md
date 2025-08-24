🍽️ Restaurant Rating Predictor

This project is a Streamlit web app that predicts restaurant ratings using a trained machine learning model.
It takes inputs like cuisine type, price range, and location, then outputs a predicted rating.

🚀 How to Run Locally

Clone the repo & move into it

git clone <your-repo-link>
cd <your-repo-folder>


Install dependencies
Create a virtual environment (optional but recommended), then install all requirements:

pip install -r requirements.txt


Run the app

streamlit run app.py


Open the URL shown in your terminal (default: http://localhost:8501).

🌐 Deploy Online
Option 1: Streamlit Cloud (free & simple)

Push your project to GitHub.

Go to Streamlit Cloud
.

Deploy by pointing to your repo and app.py.

Share the public link.

Option 2: Hugging Face Spaces

Create a new Space, choose Streamlit, upload your files (app.py, model .pkl files, requirements).

The app will build and give you a public link.

📦 Requirements

These are the libraries your app needs:

streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn

🧠 Project Files

app.py → Main Streamlit app

mlmodel.pkl / restaurant_rating_predictor_model.pkl → Trained ML model

scaler.pkl → Scaler for preprocessing

Dataset.csv → Restaurant dataset

Main.ipynb → Notebook with data prep & model training

🎯 Example Use

Select restaurant features (price, cuisine, etc.) in the app.

The trained model will predict a rating (e.g., ⭐⭐⭐⭐ 4.2).

✨ Built with Python, Streamlit & scikit-learn.
🍴 Turning data into taste buds!
