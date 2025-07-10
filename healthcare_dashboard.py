import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Healthcare Insurance Cost Analysis",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .calculator-section {
        background-color: #e8f4fd;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load data function
@st.cache_data
def load_data():
    try:
        # Try different file names in case of variations
        file_options = [
            'insurance_etl_final.csv',
            'insurance_dashboard_ready.csv',
            'insurancedashboard.csv',
            'insurance_clean_final.csv',
            'insurance.csv'
        ]
        
        for file in file_options:
            try:
                df = pd.read_csv(file)
                st.success(f"✅ Data loaded successfully from {file}")
                return df
            except FileNotFoundError:
                continue
                
        # If no file found, create sample data
        st.warning("⚠️ No data file found. Creating sample data for demonstration.")
        return create_sample_data()
        
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return create_sample_data()

def create_sample_data():
    """Create sample data if no file is found"""
    np.random.seed(42)
    n_samples = 1000
    
    ages = np.random.randint(18, 65, n_samples)
    bmis = np.random.normal(26, 4, n_samples)
    bmis = np.clip(bmis, 15, 50)
    smokers = np.random.choice(['yes', 'no'], n_samples, p=[0.2, 0.8])
    regions = np.random.choice(['northeast', 'northwest', 'southeast', 'southwest'], n_samples)
    sexes = np.random.choice(['male', 'female'], n_samples)
    children = np.random.poisson(1, n_samples)
    children = np.clip(children, 0, 5)
    
    # Calculate charges based on factors
    base_charges = 5000 + ages * 100 + bmis * 50 + children * 500
    smoking_multiplier = np.where(smokers == 'yes', 3.5, 1.0)
    charges = base_charges * smoking_multiplier + np.random.normal(0, 2000, n_samples)
    charges = np.clip(charges, 1000, 60000)
    
    sample_df = pd.DataFrame({
        'age': ages,
        'sex': sexes,
        'bmi': bmis,
        'children': children,
        'smoker': smokers,
        'region': regions,
        'charges': charges
    })
    
    return sample_df

# Load the data
df = load_data()

# Dashboard title and header
st.markdown('<h1 class="main-header">🏥 Healthcare Insurance Cost Analysis Dashboard</h1>', unsafe_allow_html=True)
st.markdown("### Team 4 - Data Analytics with AI Hackathon")

# Sidebar filters
st.sidebar.markdown("## 🔧 Dashboard Filters")
st.sidebar.markdown("---")

smoker_filter = st.sidebar.selectbox(
    "🚬 Smoking Status", 
    ['All', 'yes', 'no'],
    help="Filter by smoking status"
)

region_filter = st.sidebar.selectbox(
    "🗺️ Region",
    ['All'] + sorted(df['region'].unique().tolist()),
    help="Filter by geographic region"
)

age_range = st.sidebar.slider(
    "👤 Age Range", 
    int(df['age'].min()), 
    int(df['age'].max()), 
    (int(df['age'].min()), int(df['age'].max())),
    help="Select age range for analysis"
)

bmi_range = st.sidebar.slider(
    "⚖️ BMI Range",
    float(df['bmi'].min()),
    float(df['bmi'].max()),
    (float(df['bmi'].min()), float(df['bmi'].max())),
    help="Select BMI range for analysis"
)

# Apply filters
filtered_df = df.copy()
filtered_df = filtered_df[
    (filtered_df['age'] >= age_range[0]) &
    (filtered_df['age'] <= age_range[1]) &
    (filtered_df['bmi'] >= bmi_range[0]) &
    (filtered_df['bmi'] <= bmi_range[1])
]

if smoker_filter != 'All':
    filtered_df = filtered_df[filtered_df['smoker'] == smoker_filter]
if region_filter != 'All':
    filtered_df = filtered_df[filtered_df['region'] == region_filter]

# Calculate key metrics
if len(filtered_df) > 0:
    smoker_yes_data = filtered_df[filtered_df['smoker'] == 'yes']['charges']
    smoker_no_data = filtered_df[filtered_df['smoker'] == 'no']['charges']
    
    smoker_yes_mean = smoker_yes_data.mean() if len(smoker_yes_data) > 0 else 0
    smoker_no_mean = smoker_no_data.mean() if len(smoker_no_data) > 0 else 1
    
    smoker_multiplier = smoker_yes_mean / smoker_no_mean if smoker_no_mean > 0 else 0
else:
    smoker_multiplier = 0

# Key metrics section
st.markdown("## 📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📋 Total Records", 
        f"{len(filtered_df):,}",
        delta=f"{len(filtered_df) - len(df):,} from total"
    )

with col2:
    avg_charges = filtered_df['charges'].mean() if len(filtered_df) > 0 else 0
    st.metric(
        "💰 Average Charges", 
        f"${avg_charges:,.0f}",
        delta=f"${avg_charges - df['charges'].mean():,.0f} vs overall"
    )

with col3:
    st.metric(
        "🚬 Smoking Multiplier", 
        f"{smoker_multiplier:.1f}x",
        help="How much more smokers pay vs non-smokers"
    )

with col4:
    max_charges = filtered_df['charges'].max() if len(filtered_df) > 0 else 0
    st.metric(
        "📈 Max Charges", 
        f"${max_charges:,.0f}"
    )

# Main visualizations section
if len(filtered_df) > 0:
    st.markdown("## 📈 Data Visualizations")
    
    # Row 1: Smoking impact and Age correlation
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.box(
            filtered_df, 
            x='smoker', 
            y='charges',
            title="💨 Insurance Charges by Smoking Status",
            color='smoker',
            color_discrete_map={'yes': '#ff4444', 'no': '#44ff44'}
        )
        fig1.update_layout(
            showlegend=False,
            title_font_size=16,
            title_x=0.5
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # REMOVED trendline="ols" to fix the error
        fig2 = px.scatter(
            filtered_df, 
            x='age', 
            y='charges',
            color='smoker', 
            title="👤 Age vs Insurance Charges",
            color_discrete_map={'yes': '#ff4444', 'no': '#44ff44'}
        )
        fig2.update_layout(
            title_font_size=16,
            title_x=0.5
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Row 2: BMI analysis and Regional comparison
    col1, col2 = st.columns(2)
    
    with col1:
        # REMOVED trendline="ols" to fix the error
        fig3 = px.scatter(
            filtered_df,
            x='bmi',
            y='charges',
            color='smoker',
            title="⚖️ BMI vs Insurance Charges",
            color_discrete_map={'yes': '#ff4444', 'no': '#44ff44'}
        )
        fig3.update_layout(
            title_font_size=16,
            title_x=0.5
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        region_avg = filtered_df.groupby('region')['charges'].mean().reset_index()
        fig4 = px.bar(
            region_avg,
            x='region',
            y='charges',
            title="🗺️ Average Charges by Region",
            color='charges',
            color_continuous_scale='viridis'
        )
        fig4.update_layout(
            title_font_size=16,
            title_x=0.5,
            showlegend=False
        )
        st.plotly_chart(fig4, use_container_width=True)
    
    # Distribution analysis
    st.markdown("### 📊 Charge Distribution Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig5 = px.histogram(
            filtered_df,
            x='charges',
            nbins=30,
            title="💰 Distribution of Insurance Charges",
            color_discrete_sequence=['#1f77b4']
        )
        fig5.update_layout(
            title_font_size=16,
            title_x=0.5
        )
        st.plotly_chart(fig5, use_container_width=True)
    
    with col2:
        # Create age groups for better visualization
        filtered_df_copy = filtered_df.copy()
        # Fixed the age grouping to avoid pandas errors
        filtered_df_copy['age_group'] = pd.cut(
            filtered_df_copy['age'], 
            bins=[17, 30, 40, 50, 65], 
            labels=['18-29', '30-39', '40-49', '50+'],
            include_lowest=True
        )
        
        age_group_avg = filtered_df_copy.groupby('age_group', observed=True)['charges'].mean().reset_index()
        
        fig6 = px.bar(
            age_group_avg,
            x='age_group',
            y='charges',
            title="👥 Average Charges by Age Group",
            color='charges',
            color_continuous_scale='plasma'
        )
        fig6.update_layout(
            title_font_size=16,
            title_x=0.5,
            showlegend=False
        )
        st.plotly_chart(fig6, use_container_width=True)
    
    # Additional visualization: Correlation matrix
    st.markdown("### 🔗 Correlation Analysis")
    
    # Create correlation matrix for numerical columns
    numeric_columns = ['age', 'bmi', 'children', 'charges']
    available_columns = [col for col in numeric_columns if col in filtered_df.columns]
    
    if len(available_columns) >= 2:
        corr_matrix = filtered_df[available_columns].corr()
        
        fig_corr = px.imshow(
            corr_matrix,
            text_auto=True,
            aspect="auto",
            title="📊 Correlation Matrix - Healthcare Insurance Features",
            color_continuous_scale='RdBu_r'
        )
        fig_corr.update_layout(
            title_font_size=16,
            title_x=0.5
        )
        st.plotly_chart(fig_corr, use_container_width=True)

else:
    st.warning("⚠️ No data matches the current filters. Please adjust your selections.")

# Premium Calculator Section
st.markdown('<div class="calculator-section">', unsafe_allow_html=True)
st.markdown("## 🧮 Premium Calculator")
st.markdown("Use this calculator to estimate insurance premiums based on our statistical analysis.")

col1, col2, col3 = st.columns(3)

with col1:
    calc_age = st.number_input(
        "👤 Age", 
        min_value=18, 
        max_value=64, 
        value=35,
        help="Enter age between 18-64"
    )
    calc_bmi = st.number_input(
        "⚖️ BMI", 
        min_value=15.0, 
        max_value=50.0, 
        value=25.0,
        step=0.1,
        help="Body Mass Index (15-50)"
    )

with col2:
    calc_smoker = st.selectbox(
        "🚬 Smoking Status", 
        ['no', 'yes'],
        help="Current smoking status"
    )
    calc_region = st.selectbox(
        "🗺️ Region", 
        sorted(df['region'].unique()),
        help="Geographic region"
    )

with col3:
    calc_children = st.number_input(
        "👶 Number of Children", 
        min_value=0, 
        max_value=5, 
        value=0,
        help="Number of dependents (0-5)"
    )
    calc_sex = st.selectbox(
        "👥 Gender",
        ['male', 'female'],
        help="Gender"
    )

# Premium calculation
if st.button("💰 Calculate Premium", type="primary"):
    # Enhanced calculator based on your analysis
    base_premium = 8434 if calc_smoker == 'no' else 32050
    
    # Age adjustment (based on correlation)
    age_adjustment = (calc_age - 39.2) * 250
    
    # BMI adjustment (obesity premium)
    bmi_adjustment = 4623 if calc_bmi >= 30 else 0
    
    # Children adjustment
    children_adjustment = calc_children * 150
    
    # Regional multipliers
    regional_multipliers = {
        'southeast': 1.15,
        'northeast': 1.08,
        'northwest': 1.02,
        'southwest': 1.00
    }
    
    # Calculate total premium
    subtotal = base_premium + age_adjustment + bmi_adjustment + children_adjustment
    total_premium = subtotal * regional_multipliers.get(calc_region, 1.0)
    total_premium = max(1000, total_premium)  # Minimum premium floor
    
    # Display results
    st.success(f"🎯 **Estimated Annual Premium: ${total_premium:,.2f}**")
    
    # Risk assessment
    risk_factors = []
    if calc_smoker == 'yes':
        risk_factors.append("🚬 High Risk: Smoking (3.5x multiplier)")
    if calc_bmi >= 30:
        risk_factors.append("⚖️ Moderate Risk: BMI ≥ 30 (obesity premium)")
    if calc_age >= 50:
        risk_factors.append("👤 Age Risk: 50+ years")
    
    if risk_factors:
        st.warning("⚠️ **Risk Factors Identified:**")
        for factor in risk_factors:
            st.write(f"• {factor}")
    else:
        st.info("✅ **Low Risk Profile** - Standard premium rates apply")
    
    # Breakdown
    with st.expander("📊 Premium Breakdown"):
        st.write(f"**Base Premium:** ${base_premium:,.2f}")
        st.write(f"**Age Adjustment:** ${age_adjustment:,.2f}")
        st.write(f"**BMI Adjustment:** ${bmi_adjustment:,.2f}")
        st.write(f"**Children Adjustment:** ${children_adjustment:,.2f}")
        st.write(f"**Regional Multiplier:** {regional_multipliers.get(calc_region, 1.0):.2f}")
        st.write(f"**Total Premium:** ${total_premium:,.2f}")

st.markdown('</div>', unsafe_allow_html=True)

# Data insights section
st.markdown("## 💡 Key Insights")

insights_col1, insights_col2 = st.columns(2)

with insights_col1:
    st.markdown("""
    ### 🚬 **Smoking Impact**
    - Smoking is the **primary cost driver**
    - Smokers pay **3.5x more** than non-smokers
    - Represents the largest impact factor in the dataset
    
    ### 👤 **Age Factor**
    - Moderate positive correlation with charges
    - Seniors (50+) pay significantly more than young adults
    - Age-based pricing is justified by data
    """)

with insights_col2:
    st.markdown("""
    ### ⚖️ **BMI Impact**
    - Obesity (BMI ≥ 30) increases costs
    - Weak but significant correlation
    - Health programs could reduce costs
    
    ### 🗺️ **Regional Variations**
    - Southeast region has highest costs
    - Regional differences are moderate
    - May reflect healthcare cost variations
    """)

# Statistical Summary
st.markdown("## 📈 Statistical Summary")

if len(filtered_df) > 0:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Descriptive Statistics")
        available_numeric = [col for col in ['age', 'bmi', 'children', 'charges'] if col in filtered_df.columns]
        if available_numeric:
            st.dataframe(filtered_df[available_numeric].describe())
    
    with col2:
        st.markdown("### 🔢 Key Statistics")
        smoking_yes_pct = (filtered_df['smoker'] == 'yes').mean() * 100
        obesity_pct = (filtered_df['bmi'] >= 30).mean() * 100
        
        st.write(f"**Smoking Rate:** {smoking_yes_pct:.1f}%")
        st.write(f"**Obesity Rate:** {obesity_pct:.1f}%")
        st.write(f"**Average Age:** {filtered_df['age'].mean():.1f} years")
        st.write(f"**Average BMI:** {filtered_df['bmi'].mean():.1f}")
        st.write(f"**Median Charges:** ${filtered_df['charges'].median():,.0f}")

# Footer
st.markdown("---")
st.markdown("### 🏆 Team 4 - Healthcare Insurance Cost Analysis Dashboard")
st.markdown("*Data Analytics with AI Hackathon | Powered by Streamlit & Plotly*")

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Dataset Info")
st.sidebar.info(f"""
**Records:** {len(df):,}  
**Features:** {len(df.columns)}  
**Date Range:** All ages 18-64  
**Regions:** {len(df['region'].unique())}
""")

st.sidebar.markdown("### 🎯 Key Findings")
st.sidebar.success("""
✅ **Smoking:** Primary cost driver (3.5x)  
✅ **Age:** Moderate correlation  
✅ **BMI:** Obesity increases costs  
✅ **Regional:** Minor variations
""")
## cd "C:\Users\midas\Documents\2505-WMCA-Data-Git101\healthcare-insurance-cost-analysis"
##streamlit run healthcare_dashboard.py
## to stop Ctrl + C