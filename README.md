#  NammaMetro-Data-Engine: Urban Mobility & Digital Payment Pipeline

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)

##  Project Overview
This repository contains a high-fidelity data engineering and analytics pipeline designed to optimize **Bengaluru's NammaMetro** transit ecosystem. Unlike traditional descriptive reports, this project focuses on **feature engineering, data integrity, and prescriptive modeling** for 2026 ridership patterns.

> **Problem Statement:** How can we transform fragmented digital payment data (WhatsApp, Paytm, NCMC) into a unified urban mobility strategy to reduce station congestion and operational overhead?


(<img width="1681" height="773" alt="Screenshot (1032)" src="https://github.com/user-attachments/assets/b883fccc-35f2-40d8-bd3b-584c054ac5f6" />.png)

---

##  Data Architecture & Pipeline
I structured this project as an **End-to-End ETL (Extract, Transform, Load) Pipeline**:

1.  **Extraction:** Ingesting multi-source ridership data (14+ columns) including Digital QR, Smart Cards, and NCMC logs.
2.  **Transformation (Feature Engineering):**
    *   **Temporal Normalization:** Converted raw ISO-8601 strings into analytical datetime objects.
    *   **Vectorized Aggregations:** Engineered a `Total_Ridership` metric by synthesizing 5+ fragmented payment columns.
    *   **Contextual Labeling:** Developed Boolean logic for `Is_Weekend` and categorical mapping for `Day_Name` to identify behavioral patterns.
3.  **Analytical Layer:** Statistical thresholding (90th percentile) to identify "System Stress Points."

(<img width="1034" height="655" alt="Screenshot (1035)" src="https://github.com/user-attachments/assets/002ac868-d887-44bc-915b-8e3dd18589e9" />.png)
---

##  Data Schema & Dictionary
| Feature | Type | Description |
| :--- | :--- | :--- |
| `Record Date` | Datetime | Temporal Key for time-series indexing |
| `Total QR` | Integer | Aggregated Digital Payment Volume (WhatsApp + Paytm) |
| `Total NCMC` | Integer | National Common Mobility Card usage (Inter-modal transit) |
| `Stress_Level` | Boolean | Engineered feature identifying peak load anomalies |

---

##  Engineering Insights & Business Logic
*   **Digital Transformation Metric:** Identified a **[X]% shift** from physical token dependency to QR-based workflows, providing a data-backed roadmap for "Paperless Infrastructure."
*   **Anomaly Detection:** Leveraged statistical rolling averages to isolate ridership spikes, providing the logic for future **AI-driven Real-time Crowd Management**.
*   **Payment Ecosystem Fragmentation:** Analyzed the market share between Meta (WhatsApp) and Paytm to optimize third-party API integration strategies for the BMRCL.

---

##  Strategic Recommendations (Prescriptive Analytics)
*   **Dynamic Load Balancing:** Deploy Deep Learning (LSTMs) to predict station-level overflow 15 minutes in advance.
*   **Unified Transit Card:** Incentivize NCMC adoption to solve the "Last-Mile" connectivity gap between BMTC buses and the Metro.
*   **Operational Cost Reduction:** Phase out physical token manufacturing based on the observed 2026 digital adoption curve.

---

##  How to Reproduce
1. Clone the repository: `git clone https://github.com/YOUR_USERNAME/NammaMetro-Data-Engine.git`
2. Install dependencies: `pip install pandas seaborn matplotlib`
3. Run the notebook: `jupyter notebook NammaMetro_Analysis.ipynb`

---
**Author:** Deekshitha D V | [LinkedIn][(YOUR_LINKEDIN_URL)](https://www.linkedin.com/in/deekshithadv/) | [Kaggle Portfolio]([YOUR_KAGGLE_URL](https://www.kaggle.com/deekshithadv))
