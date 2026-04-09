import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pickle
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI Threat Detection Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Load model and data
@st.cache_resource
def load_model():
    with open('src/model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('src/label_encoder.pkl', 'rb') as f:
        le = pickle.load(f)
    with open('src/feature_names.pkl', 'rb') as f:
        features = pickle.load(f)
    return model, le, features

@st.cache_data
def load_data():
    return pd.read_parquet('src/dashboard_data.parquet')

model, le, features = load_model()
df = load_data()

# Header
st.title("🛡️ AI-Powered Network Threat Detection")
st.markdown("Real-time cybersecurity monitoring using Machine Learning")
st.divider()

# Top metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Records Analyzed", f"{len(df):,}")
with col2:
    st.metric("Attack Types Detected", "3")
with col3:
    st.metric("Model Accuracy", "70%")
with col4:
    st.metric("DDoS Precision", "98%")

st.divider()

# Charts row
col1, col2 = st.columns(2)

with col1:
    st.subheader("Attack Type Distribution")
    fig = px.pie(df, names='attack_type',
                 color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Traffic Volume by Attack Type")
    counts = df['attack_type'].value_counts().reset_index()
    counts.columns = ['Attack Type', 'Count']
    fig2 = px.bar(counts, x='Attack Type', y='Count',
                  color='Attack Type',
                  color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Simulate attack section
st.subheader("🔴 Simulate Live Traffic Detection")
st.markdown("Click the button to simulate incoming network traffic and see the AI detect threats in real time.")

if st.button("⚡ Run Threat Detection Simulation", type="primary"):
    sample = df[features].sample(n=20, random_state=np.random.randint(1000))
    predictions = model.predict(sample)
    pred_labels = le.inverse_transform(predictions)

    results = pd.DataFrame({
        'Timestamp': [datetime.now().strftime("%H:%M:%S")] * 20,
        'Threat Detected': pred_labels,
        'Risk Level': ['🔴 HIGH' if p != 'Benign' else '🟢 LOW' for p in pred_labels]
    })

    st.dataframe(results, use_container_width=True)

    threat_count = sum(1 for p in pred_labels if p != 'Benign')
    if threat_count > 0:
        st.error(f"⚠️ {threat_count} threats detected in this batch!")
    else:
        st.success("✅ No threats detected in this batch.")

st.divider()
st.caption("Built by Subhavi Somesula | CICIDS 2017 Dataset | Random Forest Classifier")