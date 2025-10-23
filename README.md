# Workforce_Management

## 🏭 Industrial Workforce Analysis using NLP, Clustering & Streamlit Dashboard

### 📊 Overview
This project analyzes the **industrial classification of the workforce in India** using **data cleaning, NLP-based grouping, clustering, and visualization** techniques.  
It provides insights into workforce distribution by **industry, gender, and state**, with an **interactive Streamlit dashboard** and an **automated PowerPoint report**.

---

## 🧠 Project Objectives

- Update and analyze industrial classification data for the Indian workforce.  
- Understand **gender participation**, **state-level patterns**, and **industry-level trends**.  
- Use **NLP and clustering** to group similar industries.  
- Develop a **Streamlit dashboard** for interactive visualization.  
- Automate report generation using **PowerPoint (python-pptx)**.  

---

## 🧰 Tools Used

| Category | Tools/Libraries |
|-----------|----------------|
| **Programming Language** | Python |
| **Data Handling** | Pandas, NumPy |
| **Visualization** | Plotly, Seaborn, Matplotlib |
| **Machine Learning / NLP** | Scikit-learn, TF-IDF, KMeans |
| **Dashboard** | Streamlit |
| **Reporting** | python-pptx |
| **Environment** | Jupyter Notebook |

---


---

## ⚙️ Steps in the Project

### **1️⃣ Data Collection & Cleaning**
- Combined raw datasets containing **state-wise and industry-wise worker counts**.  
- Cleaned and standardized data, removed inconsistencies.  
- Extracted **State** and **District** into separate columns using text parsing.  

### **2️⃣ Feature Engineering**
- Created calculated fields:  
  - `male_total`, `female_total`, `male_share`, `female_share`  
  - `main_to_marginal_ratio`  
- Normalized shares for comparison.

### **3️⃣ NLP-based Industry Grouping**
- Applied **TF-IDF vectorization** to analyze industry text data.  
- Used **KMeans clustering** to identify coherent groups.  
- Added `industry_group` column for new NLP-based classification.

### **4️⃣ Exploratory Data Analysis (EDA)**
- Visualized trends using Plotly:
  - Top industries by total workers  
  - Gender distribution  
  - State-level comparisons  
- Discovered patterns in workforce diversity and employment type.

### **5️⃣ PowerPoint Report Automation**
- Generated slides with **python-pptx** summarizing key findings.  
- Included interactive visuals (bar charts, sunburst plots).  
- Exported report as `Industrial_Workforce_Analysis.pptx`.

### **6️⃣ Streamlit Dashboard**
- Built an interactive dashboard with filters for:
  - **State**, **District**, and **Industry Group**  
- Displayed KPIs, workforce composition, and sunburst charts.  
- Deployed locally and ready for Streamlit Cloud.

---

