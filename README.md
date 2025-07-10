# Healthcare Insurance Cost Analysis Dashboard 

**Healthcare Insurance Cost Analysis Dashboard** is a comprehensive data analytics solution designed to streamline healthcare insurance cost exploration, statistical analysis, and interactive visualization. The tool supports multiple analytical approaches and provides an intuitive Streamlit interface for both technical and non-technical stakeholders in the insurance industry.

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Team](https://img.shields.io/badge/Team-4-purple)

## Executive Summary

This comprehensive analysis of the `insurance.csv` dataset aims to identify the key factors influencing medical insurance charges. Our findings reveal that **smoking status** is by far the most dominant predictor of higher charges, followed significantly by **age** and **BMI category (obesity)**. Other factors like sex, number of children, and geographic region show less pronounced impacts, though regional nuances exist. These insights are crucial for insurance providers to refine risk assessment, optimize premium structures, and develop targeted wellness programs.

The project delivers a complete data analytics solution featuring an advanced ETL pipeline, rigorous statistical hypothesis testing, and interactive dashboards (both Streamlit and Power BI) that transform complex healthcare insurance data into actionable business intelligence.

## Dataset Content

The dataset contains **1,338 healthcare insurance records** from a medical cost personal dataset sourced from Kaggle. The dataset includes comprehensive policyholder information with the following features:

- **age**: Age of primary beneficiary (18-64 years)
- **sex**: Insurance contractor gender (female/male) 
- **bmi**: Body mass index (15.96-53.13)
- **children**: Number of children covered by health insurance (0-5)
- **smoker**: Smoking status (yes/no)
- **region**: Beneficiary's residential area (northeast, northwest, southeast, southwest)
- **charges**: Individual medical costs billed by health insurance ($1,122-$63,770)

### Data Completeness
- **Dataset Quality**: 100% complete data with zero missing values across all columns
- **Data Integrity**: 1 duplicate record removed during cleaning process
- **Sample Distribution**: Balanced representation across demographics and regions
- **Dataset Size**: Manageable at approximately 55KB, well within repository limits

### Initial Observations
- **Age**: Ranges from 18 to 64, with relatively even distribution across age groups
- **BMI**: Right-skewed distribution with significant portion in overweight/obese categories (54% of sample)
- **Charges**: Highly right-skewed, indicating most charges are moderate with small percentage of high-cost claims
- **Categorical Balance**:
  - Sex: Fairly balanced (50.5% male, 49.5% female)
  - Smoker: Imbalanced with 20.5% smokers, 79.5% non-smokers
  - Region: Relatively balanced across four geographical regions

## Business Requirements

Develop an automated ETL pipeline to process healthcare insurance data and ensure data quality validation for reliable analysis.

Identify primary cost drivers in healthcare insurance through statistical hypothesis testing to inform pricing strategies and risk assessment.

Create interactive data visualizations that communicate complex insurance cost relationships to both technical and non-technical stakeholders.

Design a prototype premium calculator based on statistical findings to enable real-time insurance quote estimation and risk scoring.

Provide actionable business intelligence recommendations for insurance pricing optimization, wellness programs, and regional strategy development.

## Hypothesis and How to Validate?

**H1: Smoking significantly increases healthcare insurance costs**
- *Validation Method*: Two-sample t-test comparing smokers vs non-smokers charges
- *Result*: t=57.32, p<0.001 (HIGHLY SIGNIFICANT) 
- *Effect Size*: 3.5x cost multiplier ($32,050 vs $8,434 average)
- *Business Impact*: Smoking status is the strongest predictor of high insurance costs

**H2: Age positively correlates with insurance costs**
- *Validation Method*: Pearson correlation analysis between age and charges
- *Result*: r=0.299, p<0.001 (SIGNIFICANT)
- *Interpretation*: Moderate positive relationship supporting age-based pricing

**H3: BMI impacts healthcare costs, particularly obesity (BMI ≥ 30)**
- *Validation Method*: Correlation analysis and BMI category comparison
- *Result*: r=0.198, p<0.001 (SIGNIFICANT)
- *Business Impact*: Obesity threshold adds approximately $4,623 annually

**H4: Regional differences exist in healthcare insurance costs**
- *Validation Method*: One-way ANOVA across four regions
- *Result*: F=2.74, p<0.05 (SIGNIFICANT)
- *Finding*: Southeast region shows highest costs with notable outliers

## Project Plan

### High-Level Analysis Steps:
1. **Data Collection & Exploration** (Day 1)
   - Dataset acquisition from Kaggle with automated download fallback
   - Comprehensive data quality assessment and profiling
   - Exploratory data analysis to identify patterns and distributions

2. **ETL Pipeline Development** (Day 1-2)
   - Data extraction with validation and integrity checks
   - Comprehensive data cleaning and standardization
   - Feature engineering including BMI categorization and risk scoring
   - Data quality validation with assertion-based testing

3. **Statistical Analysis** (Day 2)
   - Hypothesis formulation based on business requirements
   - Rigorous statistical testing using appropriate methods
   - Effect size calculation and business impact assessment
   - Correlation analysis and interaction effect exploration

4. **Dashboard Development** (Day 2-3)
   - Interactive Streamlit application development
   - Power BI dashboard creation for executive reporting
   - Real-time filtering and dynamic visualization implementation
   - Premium calculator prototype with risk assessment
   - User experience optimization and responsive design

5. **Documentation & Business Intelligence** (Day 3)
   - Comprehensive documentation and README creation
   - Business insight synthesis with actionable recommendations
   - Statistical summary and methodology documentation

### Data Management Approach:
- **Collection**: Kaggle API integration with local fallback mechanisms
- **Processing**: Pandas-based ETL pipeline with comprehensive validation
- **Analysis**: Statistical testing using scipy with business-focused interpretation
- **Storage**: Clean, analysis-ready datasets with enhanced features

### Research Methodology Rationale:
- **Quantitative Approach**: Ensures objective, data-driven insights with statistical validation
- **Hypothesis Testing**: Provides credible, evidence-based business recommendations
- **Interactive Visualization**: Enables stakeholder engagement without technical expertise
- **Prototype Development**: Demonstrates practical business application and ROI

## The Rationale to Map Business Requirements to Data Visualizations

| Business Requirement | Data Visualization | Rationale |
|---------------------|-------------------|-----------|
| **ETL Pipeline** | Data Quality Metrics Dashboard | Real-time monitoring of data integrity, completeness, and processing status |
| **Cost Drivers** | Box Plots, Scatter Plots, Interaction Charts | Clear visual comparison of cost distributions and factor relationships |
| **Interactive Insights** | Streamlit Filters & Dynamic Charts | Enables stakeholder exploration and analysis without technical expertise |
| **Premium Calculator** | Interactive Form with Real-time Results | Demonstrates practical application of statistical findings for business use |
| **Business Intelligence** | Correlation Matrix, Summary Metrics, Trend Analysis | Quantifies relationships and provides evidence-based recommendations |

## Analysis Techniques Used

### Primary Analysis Methods:
1. **Descriptive Statistics**: Comprehensive summary statistics, quartiles, and distribution analysis
2. **Inferential Statistics**: Two-sample t-tests, ANOVA, Pearson correlation for hypothesis validation
3. **Interactive Visualization**: Plotly-based charts with filtering capabilities and real-time updates
4. **Feature Engineering**: BMI categorization, age grouping, risk scoring algorithms based on statistical relationships

### Analysis Structure Justification:
- **Hypothesis-Driven Approach**: Ensures focused analysis aligned with clear business objectives
- **Statistical Validation**: Provides credible, evidence-based recommendations with quantified confidence
- **Interactive Dashboard Design**: Bridges technical analysis with business usability and stakeholder engagement
- **Prototype Development**: Demonstrates practical implementation value and potential ROI

### Data Limitations & Alternative Approaches:
- **Cross-sectional Data**: No temporal analysis available - focused on current state insights and relationships
- **Limited Sample Size**: 1,338 records addressed through robust statistical testing and confidence intervals
- **Missing Healthcare History**: No claims history - compensated with comprehensive risk scoring algorithm
- **Regional Granularity**: State-level data unavailable - used regional aggregation for meaningful patterns

### Generative AI Tool Usage:
- **GitHub Copilot**: Code optimization, debugging assistance, and best practice implementation
- **AI-Assisted Documentation**: Structure refinement, clarity enhancement, and technical writing support
- **Statistical Method Validation**: Confirmation of appropriate test selection and interpretation guidance
- **Dashboard UX Enhancement**: Design pattern suggestions and accessibility improvement recommendations

## Ethical Considerations

### Data Privacy & Security:
- **Anonymized Dataset**: No personally identifiable information present in source data
- **Public Dataset Usage**: Kaggle-sourced dataset with appropriate usage rights and attribution
- **Secure Data Handling**: Local processing environment with no external data transmission
- **Code Transparency**: Full methodology and code availability for audit and validation

### Bias & Fairness Assessment:
- **Sample Representativeness**: Dataset covers diverse demographics across age, gender, and geographic regions
- **Statistical Objectivity**: Hypothesis testing methodology prevents selective result reporting
- **Transparent Limitations**: Clear documentation of data constraints and analytical boundaries
- **Inclusive Analysis**: Considerations for different demographic groups in recommendations

### Legal & Societal Compliance:
- **Non-Discriminatory Analysis**: Focus on health-related factors rather than protected characteristics
- **Evidence-Based Pricing**: Statistical justification for all pricing recommendations and risk assessments
- **Wellness Program Ethics**: Recommendations promote health improvement rather than penalty-based approaches
- **Regulatory Alignment**: Considerations for insurance industry regulations and fair pricing practices

## Dashboard Design

### Dual Dashboard Architecture:

#### **Streamlit Interactive Dashboard**
1. **Executive Header Section**
   - Project branding and team identification
   - Key performance indicators (KPIs) with real-time calculations
   - Executive summary metrics and primary findings

2. **Interactive Control Panel**
   - Age range slider with dynamic filtering (18-64 years)
   - BMI range slider with health category indicators
   - Smoking status dropdown with impact visualization
   - Regional selection with cost index display
   - Real-time data subset updates across all visualizations

3. **Core Visualization Suite**
   - **Smoking Impact Analysis**: Box plots comparing cost distributions with statistical annotations
   - **Age Correlation Display**: Scatter plots with trend lines and confidence intervals
   - **BMI Risk Assessment**: Category-based analysis with health thresholds
   - **Regional Cost Comparison**: Bar charts with cost index overlays
   - **Distribution Analysis**: Histograms with density curves and quartile markers
   - **Correlation Matrix**: Interactive heatmap with statistical significance indicators

4. **Premium Calculator Module**
   - User-friendly input form with validation and guidance
   - Real-time premium calculation based on statistical models
   - Risk factor identification with explanatory text
   - Premium breakdown showing component contributions
   - Comparison tools for scenario analysis

#### **Power BI Executive Dashboard**
- **Executive Summary View**: High-level KPIs and insights for leadership
- **Risk Factor Analysis**: Visual breakdown of cost drivers and their impact
- **Regional Performance**: Geographic analysis with interactive maps
- **Trend Analysis**: Historical patterns and forecasting capabilities
- **Mobile-Optimized**: Responsive design for executive mobile access

### Communication Strategy by Audience:
- **Technical Stakeholders**: Detailed statistical results, p-values, confidence intervals, methodology documentation
- **Business Executives**: Visual comparisons, percentage impacts, dollar amounts, ROI projections (Power BI)
- **Operations Teams**: Practical applications, implementation guidance, process integration recommendations (Streamlit)
- **Sales Teams**: Premium calculator tools, risk assessment guidance, customer communication templates

## Unfixed Bugs

### Known Technical Limitations:
1. **Premium Calculator Edge Cases**: Limited validation for extreme input values (BMI >50, age boundaries)
   - *Reason*: Acceptable for prototype phase, would require actuarial validation for production
   - *Mitigation*: Input range restrictions and warning messages implemented

2. **Mobile Responsiveness**: Minor layout issues on small screens for correlation matrix
   - *Reason*: Streamlit framework limitations with complex visualizations
   - *Workaround*: Responsive design principles applied where possible

3. **Large Dataset Performance**: Potential lag with datasets >5,000 records
   - *Reason*: Streamlit processing limitations with real-time calculations
   - *Mitigation*: Data caching and optimization techniques implemented

### Framework Limitations Encountered:
- **Streamlit State Management**: Limited session state persistence across interactions
- **Plotly Integration**: Some advanced customization options not available through Streamlit wrapper
- **Statistical Library Integration**: Minor compatibility issues between pandas and scipy versions

### Knowledge Development & Learning:
- **Statistical Testing Selection**: Initially uncertain about appropriate test methods - resolved through statistical literature review and expert consultation
- **Dashboard UX Design**: Learned through iterative development and user feedback incorporation
- **Business Intelligence Presentation**: Enhanced through stakeholder feedback and industry best practices research

## Development Roadmap

### Project Challenges & Solutions:
1. **Data Quality Assurance**: Implemented comprehensive validation pipeline with automated quality checks
2. **Statistical Significance Interpretation**: Ensured proper test selection, effect size calculation, and business relevance
3. **Dashboard Performance Optimization**: Applied caching strategies and efficient data processing techniques
4. **Business Insight Communication**: Developed clear narrative structure connecting statistical findings to actionable recommendations

### Technical Skill Development:
- **Advanced Statistical Analysis**: Hypothesis testing, effect size calculation, confidence interval interpretation
- **Interactive Dashboard Design**: User experience principles, responsive design, accessibility considerations
- **Business Intelligence Translation**: Converting technical findings into actionable business recommendations
- **Code Quality & Documentation**: Professional development practices, comprehensive documentation, reproducibility

### Future Learning Objectives:
- **Machine Learning Integration**: Predictive modeling with Random Forest, XGBoost for premium prediction
- **Advanced Statistical Methods**: Time series analysis, survival analysis, multivariate modeling
- **Production Deployment**: Docker containerization, cloud deployment, API development
- **Business Process Integration**: CRM integration, automated reporting, real-time data pipelines

## Deployment

### Streamlit Community Cloud
* The App live link is: https://healthcare-insurance-analysis.streamlit.app/
* The project was deployed to Streamlit Community Cloud using the following steps:

1. **Repository Preparation**: Ensured all required files (requirements.txt, .streamlit/config.toml) are present
2. **Streamlit Account Setup**: Connected GitHub account to Streamlit Community Cloud
3. **App Configuration**: Selected repository, branch (main), and main file (healthcare_dashboard.py)
4. **Dependency Management**: Verified Python version and package requirements compatibility
5. **Deployment Execution**: Initiated deployment with automatic dependency installation
6. **Quality Assurance**: Tested functionality, performance, and user experience in production environment

### Power BI Integration
* **Power BI Dashboard**: Created complementary executive dashboard for leadership reporting
* **Data Connection**: Connected to processed CSV files for real-time updates
* **Visualization Suite**: Executive KPIs, geographic analysis, and trend forecasting
* **Mobile Optimization**: Responsive design for executive mobile access

### Local Development Setup
```bash
# Clone repository
git clone https://github.com/your-username/healthcare-insurance-cost-analysis.git
cd healthcare-insurance-cost-analysis

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit dashboard
streamlit run healthcare_dashboard.py

# Access dashboard
# Local URL: http://localhost:8501
```

## Main Data Analysis Libraries

### Core Data Science Stack:

**pandas (>=1.5.0)**: Data manipulation, cleaning, and analysis
```python
# Data loading and transformation
df = pd.read_csv('insurance.csv')
df['bmi_category'] = df['bmi'].apply(categorize_bmi)
df = df.drop_duplicates()
```

**numpy (>=1.24.0)**: Numerical computations and statistical calculations
```python
# Statistical calculations and array operations
correlation_matrix = np.corrcoef(df[['age', 'bmi', 'charges']].T)
risk_scores = np.where(df['smoker'] == 'yes', 
                      df['base_risk'] * 3.5, df['base_risk'])
```

**streamlit (>=1.28.0)**: Interactive web application framework
```python
# Dashboard components and user interface
st.sidebar.slider("Age Range", 18, 64, (18, 64))
st.plotly_chart(fig, use_container_width=True)
st.metric("Average Charges", f"${avg_charges:,.0f}")
```

**plotly (>=5.15.0)**: Interactive data visualization and charting
```python
# Interactive visualizations
fig = px.scatter(df, x='age', y='charges', color='smoker',
                title="Age vs Insurance Charges")
fig.update_layout(title_font_size=16, title_x=0.5)
```

**scipy (>=1.10.0)**: Statistical testing and hypothesis validation
```python
# Statistical hypothesis testing
t_stat, p_value = stats.ttest_ind(smoker_charges, non_smoker_charges)
correlation, p_value = stats.pearsonr(df['age'], df['charges'])
f_stat, p_value = stats.f_oneway(*regional_groups)
```

**matplotlib & seaborn**: Statistical visualization and publication-quality charts
```python
# Correlation heatmap and statistical plots
sns.heatmap(correlation_matrix, annot=True, cmap='RdBu_r', center=0)
plt.figure(figsize=(12, 8))
```

## Credits

### Content & Data Sources
- Healthcare insurance dataset obtained from [Kaggle - Medical Cost Personal Dataset](https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance) under public license
- Statistical testing methodology guided by [SciPy Statistical Functions Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
- BMI categorization standards based on [WHO BMI Classification Guidelines](https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight)
- Insurance industry actuarial principles referenced from [Society of Actuaries](https://www.soa.org/) publications

### Technical Implementation Resources
- Streamlit dashboard framework from [Streamlit Documentation](https://docs.streamlit.io/) and community examples
- Power BI visualization techniques from [Microsoft Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/) and community gallery
- Interactive visualization techniques from [Plotly Python Documentation](https://plotly.com/python/) and gallery examples
- ETL pipeline design patterns from [Pandas Documentation](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- Statistical analysis methodology from [Real Statistics Using Excel](https://www.real-statistics.com/hypothesis-testing/) educational resources

### Design & Accessibility
- Dashboard color schemes follow [WCAG 2.1 Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) for inclusive design
- User interface patterns inspired by [Streamlit Component Gallery](https://streamlit.io/gallery) best practices
- Data visualization principles from [Edward Tufte's visualization guidelines](https://www.edwardtufte.com/tufte/) and modern dashboard design

### Development Tools & AI Assistance
- Code optimization and debugging supported by **GitHub Copilot**
- Documentation structure enhanced with AI writing assistance
- Statistical method validation through AI-powered research tools
- Code quality improvements using automated linting and formatting tools

## Acknowledgements

### Team 4 Collaboration
Special recognition to **Team 4** members for their collaborative contributions:
- **Younus**: Project coordination, repository management, and milestone tracking
- **James**: Data validation, technical review, and quality assurance
- **Rasi**: User experience design, visual optimization, and dashboard aesthetics
- **Midaso**: Lead data analyst, statistical analysis, dashboard development, and documentation

### Educational & Platform Support
- **Code Institute**: Providing the hackathon framework, learning resources, and assessment structure
- **Kaggle Community**: Maintaining high-quality, accessible datasets for educational and research purposes
- **Streamlit Team**: Developing an excellent open-source framework for data science applications
- **Microsoft Power BI**: Providing robust business intelligence tools for executive reporting
- **Open Source Community**: Contributing to the robust Python data science ecosystem with pandas, numpy, scipy, and plotly

### Professional Development
- **Statistical Consulting**: Online resources and academic papers for statistical methodology validation
- **Industry Best Practices**: Insurance industry professionals who provided context for business recommendations
- **Peer Review**: Fellow participants and mentors who provided feedback during development
- **Documentation Standards**: Professional technical writing resources and examples

---

**Team 4 - Healthcare Insurance Cost Analysis Dashboard**  
*Transforming healthcare insurance decision-making through rigorous data analytics, statistical validation, and interactive business intelligence*

**Repository**: [GitHub - Healthcare Insurance Cost Analysis](https://github.com/Midaso2/healthcare-insurance-cost-analysis)  
**Live Dashboard**: [Streamlit App - Healthcare Insurance Analysis](https://healthcare-insurance-analysis.streamlit.app/)  
**Contact**: Available for questions, demonstrations, and further collaboration
