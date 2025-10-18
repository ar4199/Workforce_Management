import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Industrial Workforce Dashboard", page_icon="🏭", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("final_cleaned_industry_data.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filters")

# --- Level Selection (State / District) ---
view_level = st.sidebar.radio("View Data By:", ["State", "District"])

# Dropdowns for State and District
if view_level == "State":
    selected_state = st.sidebar.selectbox(
        "Select State", ["All"] + sorted(df['state_name'].dropna().unique().tolist())
    )
    selected_group = st.sidebar.selectbox(
        "Select Industry Group", ["All"] + sorted(df['industry_group'].unique().tolist())
    )

    filtered_df = df.copy()
    if selected_state != "All":
        filtered_df = filtered_df[filtered_df['state_name'] == selected_state]
    if selected_group != "All":
        filtered_df = filtered_df[filtered_df['industry_group'] == selected_group]

else:  # District level
    selected_state = st.sidebar.selectbox(
        "Select State", ["All"] + sorted(df['state_name'].dropna().unique().tolist())
    )

    if selected_state != "All":
        district_options = df[df['state_name'] == selected_state]['district_name'].dropna().unique().tolist()
    else:
        district_options = df['district_name'].dropna().unique().tolist()

    selected_district = st.sidebar.selectbox("Select District", ["All"] + sorted(district_options))
    selected_group = st.sidebar.selectbox(
        "Select Industry Group", ["All"] + sorted(df['industry_group'].unique().tolist())
    )

    filtered_df = df.copy()
    if selected_state != "All":
        filtered_df = filtered_df[filtered_df['state_name'] == selected_state]
    if selected_district != "All":
        filtered_df = filtered_df[filtered_df['district_name'] == selected_district]
    if selected_group != "All":
        filtered_df = filtered_df[filtered_df['industry_group'] == selected_group]

# Header
st.title("🏭 Industrial Workforce Analysis in India")
st.markdown("Explore main and marginal workers across various industries, states, and districts.")

# --- KPIs ---
total_workers = filtered_df['total_workers'].sum()
male_share = filtered_df['male_share'].mean() * 100
female_share = filtered_df['female_share'].mean() * 100

col1, col2, col3 = st.columns(3)
col1.metric("👷 Total Workers", f"{total_workers:,.0f}")
col2.metric("👨 Male Share (%)", f"{male_share:.2f}%")
col3.metric("👩 Female Share (%)", f"{female_share:.2f}%")

st.markdown("---")

# --- Chart 1: Top Industry Groups ---
top_groups = (
    filtered_df.groupby("industry_group")["total_workers"]
    .sum()
    .reset_index()
    .sort_values("total_workers", ascending=False)
)
fig1 = px.bar(top_groups.head(15), x="total_workers", y="industry_group", orientation="h",
              title=f"Top Industry Groups by Total Workers ({view_level}-wise)", color="industry_group")
st.plotly_chart(fig1, use_container_width=True)

# --- Chart 2: Gender and Work Type Composition ---
agg_cols = ["male_main", "female_main", "male_marginal", "female_marginal"]
if view_level == "State":
    entity_col = "state_name"
else:
    entity_col = "district_name"

entity_agg = (
    filtered_df.groupby(entity_col)[agg_cols]
    .sum()
    .reset_index()
)
fig2 = px.bar(entity_agg, x=entity_col, y=agg_cols,
              title=f"Workers by Gender and Work Type ({view_level}-wise)", barmode="stack")
st.plotly_chart(fig2, use_container_width=True)

# --- Chart 3: Sunburst Chart ---
grp_hierarchy = filtered_df.groupby(['state_name','district_name','industry_group'])['total_workers'].sum().reset_index()
if view_level == "State":
    fig3 = px.sunburst(grp_hierarchy, path=['state_name', 'industry_group'], values='total_workers',
                       title='State → Industry Group Distribution', maxdepth=2)
else:
    fig3 = px.sunburst(grp_hierarchy, path=['state_name','district_name','industry_group'], values='total_workers',
                       title='State → District → Industry Group Distribution', maxdepth=3)
st.plotly_chart(fig3, use_container_width=True)