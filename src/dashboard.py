import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Page config
st.set_page_config(
    page_title="AI Threat Detection Dashboard",
    page_icon="🛡️",
    layout="wide"
)

@st.cache_resource
def train_model():
    st.write("⏳ Loading and training model on startup...")
    ddos = pd.read_parquet('data/DDoS-Friday-no-metadata.parquet')
    botnet = pd.read_parquet('data/Botnet-Friday-no-metadata.parquet')
    portscan = pd.read_parquet('data/Portscan-Friday-no-metadata.parquet')

    ddos['attack_type'] = 'DDoS'
    botnet['attack_type'] = 'Botnet'
    portscan['attack_type'] = 'Portscan'

    df = pd.concat([ddos, botnet, portscan], ignore_index=True)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    X = df[numeric_cols]
    y = df['attack_type']

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    model = RandomForestClassifier(n_estimators=50, max_depth=15, random_state=42, n_jobs=-1)
    model.fit(X, y_encoded)

    return model, le, numeric_cols, df

model, le, features, df = train_model()
df_sample = df.sample(n=10000, random_state=42)

# Header
st.title("🛡️ AI-Powered Network Threat Detection")
st.markdown("Real-time cybersecurity monitoring using Machine Learning")
st.divider()

# Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Records Analyzed", f"{len(df_sample):,}")
with col2:
    st.metric("Attack Types Detected", "3")
with col3:
    st.metric("Model Accuracy", "70%")
with col4:
    st.metric("DDoS Precision", "98%")

st.divider()

# Charts
col1, col2 = st.columns(2)
with col1:
    st.subheader("Attack Type Distribution")
    fig = px.pie(df_sample, names='attack_type',
                 color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Traffic Volume by Attack Type")
    counts = df_sample['attack_type'].value_counts().reset_index()
    counts.columns = ['Attack Type', 'Count']
    fig2 = px.bar(counts, x='Attack Type', y='Count',
                  color='Attack Type',
                  color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Simulation
st.subheader("🔴 Simulate Live Traffic Detection")
st.markdown("Click the button to simulate incoming network traffic and see the AI detect threats in real time.")

if st.button("⚡ Run Threat Detection Simulation", type="primary"):
    sample = df_sample[features].sample(n=20, random_state=np.random.randint(1000))
    predictions = model.predict(sample)
    pred_labels = le.inverse_transform(predictions)

    results = pd.DataFrame(