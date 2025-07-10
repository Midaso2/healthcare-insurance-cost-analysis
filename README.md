# Healthcare Insurance Cost Analysis Dashboard
This comprehensive analysis of the `insurance.csv` dataset aims to identify the key factors influencing medical insurance charges. Our findings reveal that **smoking status** is by far the most dominant predictor of higher charges, followed significantly by **age** and **BMI category (obesity)**. Other factors like sex, number of children, and geographic region show less pronounced impacts, though regional nuances exist. These insights are crucial for insurance providers to refine risk assessment, optimize premium structures, and develop targeted wellness programs. Help me to get clear introduction for the above paragraph. remove and keep only important parts

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Team](https://img.shields.io/badge/Team-4-purple)

---

## Executive Summary

Our project takes a close look at the `insurance.csv` dataset to uncover what really impacts medical insurance charges. We found that **smoking** is by far the strongest factor in raising costs, followed by **age** and whether someone is **obese** (BMI category). Other factors—such as gender, number of children, and where people live—play a smaller, but still meaningful, role. These insights give insurance providers the tools they need to improve risk assessment, set fairer premiums, and design effective wellness programs.

Our solution covers the whole data journey: from building a robust ETL pipeline and running solid statistical tests, to delivering interactive dashboards (in both Streamlit and Power BI) that turn complex insurance data into clear, actionable insights.

---

## Dataset Overview

We analyzed **1,338 real insurance records** from Kaggle, each including:

- **age**: 18–64 years
- **sex**: female/male
- **bmi**: 15.96–53.13
- **children**: 0–5 dependents
- **smoker**: yes/no
- **region**: northeast, northwest, southeast, southwest
- **charges**: $1,122–$63,770

**Data at a Glance:**
- No missing values, only one duplicate removed
- Well-balanced mix of ages, genders, and regions
- About 20% of the sample are smokers; over half are overweight or obese
- Most insurance charges are moderate, but a few people have very high costs

---

## Project Goals

- Build an automated ETL pipeline for clean, reliable data
- Pinpoint the biggest cost drivers using solid statistical methods
- Create interactive visualizations that anyone can use and understand
- Prototype a premium calculator so users can estimate insurance costs instantly
- Deliver business recommendations that insurers can act on—like optimizing pricing, promoting wellness, or targeting key regions

---

## What Did We Test? What Did We Find?

- **Does smoking drive up costs?**
  - Yes—smokers pay about 3.5 times more. (Very significant difference.)
- **Does age matter?**
  - Yes—older people generally pay more.
- **Does obesity (BMI ≥ 30) raise costs?**
  - Yes—being obese adds about $4,600/year on average.
- **Do costs differ by region?**
  - Yes—the Southeast has the highest average charges.

All findings were validated with robust statistical tests (t-tests, correlation, ANOVA).

---

## How We Worked

### Step-by-Step Approach

1. **Data Collection & Exploration:** Pulled and cleaned the dataset, checked quality, and explored patterns.
2. **ETL Pipeline:** Automated all cleaning, transformation, and feature engineering (like BMI categories and risk scores).
3. **Statistical Analysis:** Tested our main questions using proven statistical methods.
4. **Dashboard Development:** Built interactive dashboards in Streamlit and Power BI—easy for anyone to explore, filter, and visualize results.
5. **Documentation:** Wrote clear guides and summaries to make our process transparent and easy to follow.

---

## Why These Visuals?

| Goal | Visual | Why It Helps |
|------|--------|--------------|
| Monitor data quality | Data quality dashboard | Spot issues early and keep data reliable |
| Highlight key cost drivers | Box/scatter plots, interaction charts | Instantly see who is most affected and why |
| User-driven exploration | Interactive filters and charts | Let anyone ask their own questions, not just analysts |
| Premium calculator | Simple input form with instant results | Real-world use—see what a client might pay |
| Show relationships | Correlation matrices, summary cards | Make complex connections clear at a glance |

---

## Limitations & Lessons Learned

- **Snapshot data:** No year-over-year trends—just a single point in time
- **Sample size:** 1,338 records—enough for solid stats, but not huge
- **No claims history:** Can't analyze repeated claims, but risk scoring helps
- **Regional detail:** Only four regions, not granular by state

### What We Learned
- Improved our statistical testing and dashboard design skills
- Learned new ways to turn data into clear business recommendations
- Became better at collaborating, debugging, and documenting as a team

---

## Ethics & Fairness

- **Privacy:** All data is fully anonymized and public
- **Fairness:** We checked for bias and documented any data limits
- **Transparency:** All code and methods are open and reproducible
- **Compliance:** Focused only on health-related factors, not protected characteristics

---

## Dashboard Features

### Streamlit Dashboard
- Executive summary and KPIs
- Interactive controls for age, BMI, smoker status, and region
- Visuals: box plots, scatter plots, histograms, correlation heatmaps
- Premium calculator: enter your details, get a cost estimate

### Power BI Dashboard
- High-level KPIs for leadership
- Breakdowns by risk factors and region
- Geographic and trend analysis
- Mobile-friendly design

---

## Team & Thanks

**Team 4:**
- Younus: Project management and repo lead
- James: Data validation and quality control
- Rasi: User experience and dashboard design
- Midaso: Lead analyst, dashboard builder, and documentation

**Special Thanks:**  
- Code Institute for the hackathon framework
- Kaggle, Streamlit, Power BI, and the open-source community for tools and data
- All mentors and teams for feedback and support

---

## Try It Yourself!

- **Live Streamlit App:** [Healthcare Insurance Analysis Dashboard](https://healthcare-insurance-analysis.streamlit.app/)
- **GitHub Repo:** [healthcare-insurance-cost-analysis](https://github.com/Midaso2/healthcare-insurance-cost-analysis)

### Run Locally
```bash
git clone https://github.com/your-username/healthcare-insurance-cost-analysis.git
cd healthcare-insurance-cost-analysis
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run healthcare_dashboard.py
```
Visit [http://localhost:8501](http://localhost:8501) to start exploring.

---

## Licensing & Credits

- Data: [Kaggle - Medical Cost Personal Dataset](https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance)
- Methods: SciPy, WHO, SOA, and industry best practices
- Visuals: Plotly, Streamlit, Power BI, Matplotlib, and Seaborn
- AI Support: GitHub Copilot and AI writing tools for code, docs, and design

---

*Team 4 – Turning healthcare data into real-world business insights.*

Questions or feedback? Reach out via GitHub or the live dashboard!
