# AI Attendance System

An AI-powered attendance management system built with **Streamlit** that allows teachers to create classes and take attendance using **face recognition or voice recognition**, while students can register, join classes, and maintain their attendance records.

## Features

### 👨‍🏫 Teacher

* Register and securely log in
* Create and manage classes
* Generate a unique class joining code
* Share classes through:

  * Joining code
  * QR code
  * Shareable link
* View enrolled students
* Take attendance using:

  * Face recognition
  * Voice recognition
  * Photo upload
* Store attendance records in Supabase

### 👨‍🎓 Student

* Register and securely log in
* Register with:

  * Name
  * Profile photo
  * Voice sample
* Join classes using a joining code or QR code
* View joined classes
* Participate in AI-based attendance
* Attendance data is stored securely in the database

## Tech Stack

### Frontend / Application

* **Python 3.11**
* **Streamlit**

### AI / Computer Vision

* **face_recognition_models** — Pre-trained face recognition models
* **dlib** — Face detection and recognition
* **scikit-learn** — Machine learning utilities
* **OpenCV** — Image and computer vision processing

### Voice Recognition

* **librosa** — Audio processing
* **Resemblyzer** — Voice embeddings and speaker verification

### Database & Security

* **Supabase** — Database and backend
* **bcrypt** — Password hashing

### Utilities

* **NumPy**
* **Pandas**
* **Pillow** — Image processing
* **Segno** — QR code generation


## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ai-attendance-project-app
```

### 2. Create a virtual environment

Make sure you are using **Python 3.11**.

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Supabase

Create a Supabase project and obtain your project URL and client key.

Create the following file:

```text
.streamlit/secrets.toml
```

Add:

```toml
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-publishable-key"
```

> Do not commit `secrets.toml` to GitHub.

Add it to `.gitignore`:

```gitignore
.streamlit/secrets.toml
venv/
__pycache__/
```

### 5. Set up the database

Create the required tables in your Supabase project according to the application's database schema.

The application uses Supabase to store:

* Teacher accounts
* Student accounts
* Classes
* Class memberships
* Attendance records
* Face/voice-related data required by the application

### 6. Run the application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## Face Recognition

The application uses face embeddings to identify registered students.

The face recognition pipeline broadly follows:

```text
Student Photo
      ↓
Face Detection
      ↓
Face Encoding
      ↓
Face Embedding
      ↓
Compare with Registered Students
      ↓
Identify Student
      ↓
Mark Attendance
```

The project uses `face_recognition_models` together with `dlib` for the face recognition pipeline.

## Voice Recognition

Voice attendance follows a similar embedding-based approach:

```text
Student Voice
      ↓
Audio Processing
      ↓
Voice Embedding
      ↓
Compare with Registered Voice
      ↓
Verify Speaker
      ↓
Mark Attendance
```

`librosa` is used for audio processing and `Resemblyzer` is used for speaker embeddings and verification.

## QR Code Attendance / Class Joining

Teachers can generate a unique class identifier that students can use to join a class.

```text
Teacher creates class
        ↓
Unique joining code
        ↓
QR code / Link
        ↓
Student scans or enters code
        ↓
Student joins class
```

## Requirements

The project is developed and tested with:

```text
Python 3.11
Streamlit
NumPy
Pandas
scikit-learn
dlib-bin
face_recognition_models
setuptools < 70.0.0
Supabase
bcrypt
Segno
Pillow
librosa
Resemblyzer
```

For the exact dependency versions, see:

```text
requirements.txt
```

## Important Notes

* Use **Python 3.11** for compatibility with the computer vision and audio dependencies.
* Keep your Supabase credentials inside `.streamlit/secrets.toml`.
* Never commit API keys, passwords, or other secrets to GitHub.
* `setuptools<70.0.0` is used for compatibility with some project dependencies.
* Face and voice recognition performance can vary depending on image quality, lighting, audio quality, and environmental conditions.

## Future Improvements

* Attendance analytics and visual reports
* Student attendance percentage tracking
* Email notifications
* Admin dashboard
* Improved anti-spoofing / liveness detection
* More robust voice verification
* Cloud deployment
* Mobile-friendly interface

## Author

**Kashish Maurya**
