# VR User Behavior & Safety Analytics: Trust & Safety Pipeline

## 📖 Project Overview

This repository documents the end-to-end development of a **Trust & Safety Analytics Pipeline** designed for Virtual Reality environments.
The goal of this project is to demonstrate full-stack data capability: from the **Data Engineering** task of simulating complex, unstructured telemetry logs to the **Product Analytics** task of identifying "griefing" (harassment) patterns in real-time. It highlights the ability to generate synthetic datasets, ingest them into enterprise tools (Amplitude), and write SQL logic to isolate high-risk user behaviors.

## ⚙️ Technical Highlights

This project displays technical proficiency across two distinct phases of the data lifecycle:

### Phase 1: Data Simulation (Python Engine)
* **Behavioral Modeling:** Designed a Python simulation engine using `pandas` and `numpy` to generate realistic user telemetry, creating distinct profiles for "Normal Users" vs. "Griefers" (Bad Actors) based on probabilistic distributions.
* **Unstructured Data Generation:** Simulated messy, high-volume data points including 3D spatial coordinates `(x, y)`, voice intensity levels (decibels), and asset interaction logs.

### Phase 2: Ingestion & Intelligence (SQL & Amplitude)
* **Real-Time API Integration:** Built a Python script to push "live" event data to **Amplitude**, resolving timestamp latency issues to simulate a real-time production stream.
* **Risk Scoring Logic:** Wrote complex SQL queries to join session data with report logs, calculating a "Toxicity Score" for specific in-game assets (e.g., verifying that the "Gun" asset had a 30% higher report rate than the "Flower").

## 🔍 Analytical Logic (Key Metrics)

The table below illustrates how raw telemetry data was transformed into actionable business insights during the analysis:

| Feature | Raw Telemetry (Input) | Business Insight (Output) |
| :--- | :--- | :--- |
| **Voice Toxicity** | `voice_vol_db: 88.5` | **Flag:** Volume > 80db correlates with 5x report rate. |
| **Spatial Clustering** | `x: 5.2, y: 4.1` | **Insight:** Griefing events cluster in "Spawn Zones" (0-10 coords). |
| **Asset Risk** | `asset_id: "gun_01"` | **Risk Score:** 32% "Toxic Conversion" rate for this item. |
| **User Journey** | Timestamp Sequence | **Funnel:** Spawn Item → Scream → Report (Time to Ban < 60s). |

## ✨ Functional Features

### 1. Data Engineering Pipeline
* **User Simulation:** A script that generates unique user sessions, differentiating behavior patterns (e.g., rapid movement vs. idle exploration) to create a realistic test dataset.
* **Live Stream Injection:** A script that "replays" historical data as current events, allowing for real-time dashboard testing in Amplitude.

### 2. Safety Intelligence & Visualization
* **High-Risk Identification:** SQL logic that isolates specific assets and behaviors that precede a user report, allowing for proactive moderation.
* **User Funnels:** Amplitude charts that visualize the exact sequence of events a "Griefer" takes before committing a violation.

## 🛠️ Technology Stack

* **Scripting:** Python (Pandas, Numpy, Requests)
* **Database:** SQLite (Relational Data Warehousing)
* **Product Analytics:** Amplitude (Behavioral Cohorts & Funnels)
* **Querying:** SQL (Aggregations, Joins, Case Logic)

## 🗄️ File Structure

The repository is organized to facilitate a review of the data pipeline:

* `/generate_data.py`: The simulation engine that creates the raw CSV logs.
* `/send_to_amplitude.py`: The script that handles API ingestion to the cloud.
* `/analysis.sql`: The logic used to calculate risk scores and identify bad actors.
* `/vr_telemetry.csv`: The generated dataset used for analysis.

## 🚀 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/VR-Safety-Analytics.git](https://github.com/YourUsername/VR-Safety-Analytics.git)
    ```

2.  **Generate Data:**
    Run the simulation script to create the raw telemetry logs:
    ```bash
    python generate_data.py
    ```

3.  **Run SQL Analysis:**
    Open `analysis.sql` in VS Code (using the SQLite extension) to execute the risk queries against the generated database.

4.  **Visualize in Amplitude (API Setup):**
    * Sign up for a free account at [Amplitude](https://amplitude.com/).
    * Create a new project and retrieve your **API Key**.
    * Open `send_to_amplitude.py` and replace the placeholder with your own key:
        ```python
        API_KEY = 'YOUR_AMPLITUDE_API_KEY_HERE'
        ```
    * Run the script to stream the data:
        ```bash
        python send_to_amplitude.py
        ```
