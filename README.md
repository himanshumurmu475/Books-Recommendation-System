# 📚 My First Machine Learning Project: PageMatch (Books Recommender System)

Hey everyone! 👋 Welcome to my **PageMatch Books Recommender System** project! 

I built this project to create a book discovery and recommendation web application inspired by modern editorial design. It uses **Collaborative Filtering** with the **K-Nearest Neighbors (KNN)** algorithm to recommend books based on reading preferences and moods!

---

## 🌟 What Does This Project Do?

1. **Discover & Search**: Search for any book title or mood you are in.
2. **Curated For You**: Recommends similar books based on your taste using a Machine Learning KNN model.
3. **Book Spotlight Details**: Displays high-resolution book covers, authors, star ratings, page counts, synopses, and **VIBE TAGS** (*Slow Burn*, *Atmospheric*, *Dark Academia*).
4. **Reading List**: Save your favorite books to your personal browser reading list with local storage persistence!
5. **Surprise Me**: Click `Surprise Me` to discover random curated literary gems.

---

## 🧠 How Does It Work? (Simple Explanation)

* **Collaborative Filtering**: If readers who enjoyed *The Secret History* also loved *If We Were Villains* and *Bunny*, the system learns that these books share similar themes and tone!
* **K-Nearest Neighbors (KNN)**: We turn user ratings into a mathematical user-item matrix (pivot table) and use **Cosine Distance** to calculate the closest matching neighbor books in real time.

---

## 🛠️ Tech Stack & Tools Used

* **Python 3.10+** - Main programming language.
* **Flask** - Lightweight backend web server and REST API.
* **TailwindCSS & Google Fonts** - Custom editorial UI with *Playfair Display* & *Plus Jakarta Sans*.
* **Scikit-Learn** - Machine learning library powering the KNN recommendation engine.
* **Pandas & NumPy** - Data processing and user-item matrix creation.
* **AWS EC2** - Cloud deployment without needing Docker!

---

## 📁 Project Directory Structure

```text
Movie Recomandation System/
├── artifacts/              # Pre-trained ML model & matrix files (.pkl)
│   ├── model.pkl
│   ├── book_pivot.pkl
│   ├── book_names.pkl
│   └── final_rating.pkl
├── data/                   # Dataset CSVs
│   ├── books_dataset.csv
│   └── ratings_dataset.csv
├── templates/
│   └── index.html          # PageMatch Single Page Application UI
├── app.py                  # Main Flask application & KNN API server
├── create_dataset.py       # Script to generate book & rating datasets
├── train.py                # Machine learning training script (trains KNN)
├── requirements.txt        # Python library dependencies list
├── .gitignore              # Files ignored by Git
└── README.md               # Project documentation (You are here!)
```

---

## 💻 How to Run Locally (Step-by-Step for Beginners)

### Step 1: Open terminal in the project directory
```bash
cd "c:/Users/himan/Projects/Movie Recomandation System"
```

### Step 2: Create and activate virtual environment
* **Windows (PowerShell)**:
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
* **Mac / Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run dataset generation & model training (if not already done)
```bash
python create_dataset.py
python train.py
```

### Step 5: Launch the PageMatch Web App! 🎉
```bash
python app.py
```

Open your browser and navigate to: **`http://localhost:5000`**!

---

## ☁️ How to Deploy on AWS EC2 (Step-by-Step - No Docker Needed!)

### Step 1: Launch an AWS EC2 Instance
1. Log into your [AWS Management Console](https://aws.amazon.com/console/).
2. Search for **EC2** and click **Launch Instance**.
3. **Name**: `pagematch-server`
4. **AMI**: Select **Ubuntu** (Ubuntu Server 22.04 LTS - Free Tier).
5. **Instance Type**: `t2.micro` (Free Tier).
6. **Key Pair**: Select or create a `.pem` key pair (e.g. `my-key.pem`).
7. **Network Settings**: Allow SSH (`Port 22`) and HTTP (`Port 80`).
8. Click **Launch Instance**.

### Step 2: Configure Security Group (Open Port 5000)
1. Go to your EC2 instance details -> **Security** tab -> Click the **Security Group**.
2. Click **Edit Inbound Rules** -> **Add Rule**:
   * **Type**: Custom TCP
   * **Port Range**: `5000`
   * **Source**: Anywhere-IPv4 (`0.0.0.0/0`)
3. Click **Save rules**.

### Step 3: SSH into your EC2 Server
```bash
ssh -i "my-key.pem" ubuntu@<YOUR_EC2_PUBLIC_IP>
```

### Step 4: Install Python & Git on EC2
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

### Step 5: Clone your project repository onto EC2
```bash
git clone https://github.com/your-username/Books-Recommender-System.git
cd Books-Recommender-System
```

### Step 6: Set up virtual environment and install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 create_dataset.py
python3 train.py
```

### Step 7: Start the server in background with nohup
```bash
nohup python3 app.py > server.log 2>&1 &
```

### Step 8: Open your live website! 🚀
Visit: `http://<YOUR_EC2_PUBLIC_IP>:5000` in your web browser. Your project is now live on AWS! 🎉

---

## 🎓 What I Learned Building This

* Building machine learning recommendation models using Scikit-Learn's `NearestNeighbors`.
* Transforming user-item rating matrices with Pandas and NumPy.
* Designing editorial book interfaces with Tailwind CSS and Google Fonts.
* Building REST APIs with Flask and deploying cloud web applications on AWS EC2!

---

### Thank you for checking out PageMatch! ⭐ Give it a star on GitHub!
