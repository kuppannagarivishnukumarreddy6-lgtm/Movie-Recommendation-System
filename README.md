# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System built using **Python**, **Flask**, and **Scikit-learn**. This application recommends similar movies based on the movie selected by the user using a Content-Based Filtering approach.

---

## 📌 Project Overview

This project helps users discover movies similar to the one they like. It analyzes movie genres and calculates similarity using the **Cosine Similarity** algorithm.

---

## ✨ Features

- 🎬 Search for a movie
- 🤖 Machine Learning-based recommendations
- 📋 Displays Top 10 similar movies
- 🌐 User-friendly Flask web interface
- 📱 Responsive and modern UI
- 🎨 Attractive dark theme
- 📂 Movie dataset using MovieLens
- ⚡ Fast recommendation generation

---

## 🛠 Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML5
- CSS3
- Jinja2

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── recommendation.py
├── database.py
├── movies.csv
├── ratings.csv
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── favorites.html
│   ├── history.html
│   └── movie_details.html
│
└── static/
    ├── style.css
    └── bg.jpg
```

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Movie-Recommendation-System.git
```

### Go to the project folder

```bash
cd Movie-Recommendation-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Algorithm

This project uses **Content-Based Filtering**.

Steps:
1. Read movie dataset.
2. Extract movie genres.
3. Convert genres into vectors using CountVectorizer.
4. Calculate Cosine Similarity.
5. Recommend the Top 10 similar movies.

---

## 📊 Dataset

MovieLens Dataset

Files used:
- movies.csv
- ratings.csv

---

## 🚀 Future Improvements

- Movie Posters
- IMDb/TMDb Ratings
- Genre Filtering
- User Login
- Favorite Movies
- Search History
- TMDb API Integration
- Deployment on Render or AWS

---

## 📷 Screenshots

(Add screenshots of your homepage and recommendation page here.)

---

## 👨‍💻 Author

**Vishnu Kumar Reddy**

B.Tech – Computer Science Engineering

Machine Learning Internship Project

---

## ⭐ Support

If you found this project useful, please ⭐ star the repository on GitHub.
