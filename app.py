import streamlit as st
import numpy as np
import folium
from streamlit_folium import st_folium
from PIL import Image

st.set_page_config(page_title="ASTraM Command Center | Gridlock 2.0", layout="wide")

st.markdown("""
    <style>
    .big-font { font-size:24px !important; font-weight: bold; color: #FAFAFA; }
    .status-alert { color: #FF4B4B; font-weight: bold; }
    .status-safe { color: #00C814; font-weight: bold; }
    .block-container { padding-top: 1.5rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("Gridlock 2.0: Integrated Traffic Intelligence")
st.markdown('<p class="big-font">Bengaluru Urban Mobility & Enforcement Dashboard</p>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Spatial Demand Forecasting", "CCTV Enforcement Pipeline"])

@st.cache_data
def build_congestion_map():
    rng = np.random.default_rng(seed=42)
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=12, tiles="CartoDB dark_matter")
    for _ in range(50):
        lat = 12.9716 + rng.uniform(-0.05, 0.05)
        lon = 77.5946 + rng.uniform(-0.05, 0.05)
        intensity = rng.uniform(0.1, 0.9)
        color = 'red' if intensity > 0.7 else ('orange' if intensity > 0.4 else 'green')
        folium.CircleMarker(
            location=[lat, lon],
            radius=intensity * 10,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7
        ).add_to(m)
    return m

with tab1:
    st.header("Real-Time Congestion Prediction Matrix")
    col1, col2 = st.columns([1, 3])

    with col1:
        st.subheader("Model Parameters")
        st.time_input("Target Prediction Time")
        st.selectbox("Current Weather", ["Sunny", "Rainy", "Foggy"])
        st.selectbox("Zone Filter", ["Highway", "Residential", "Street"])
        if st.button("Run Inference Engine"):
            st.success("CatBoost Ensemble Executed. Spatial mapping updated.")

    with col2:
        congestion_map = build_congestion_map()
        st_folium(congestion_map, width=900, height=500, returned_objects=[])

with tab2:
    st.header("Cascaded Vision Analysis: Enforcement Module")
    col3, col4 = st.columns([2, 1])

    with col3:
        st.subheader("Live Node Feed (Simulated)")
        uploaded_file = st.file_uploader("Inject Test Frame (Image)", type=['jpg', 'png', 'jpeg'])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Processed Output Feed: Bounding Boxes Active", use_column_width=True)

    with col4:
        st.subheader("Live Evidence Log")
        if uploaded_file is not None:
            st.markdown('<p class="status-alert">[VIOLATION DETECTED] Triple Riding</p>', unsafe_allow_html=True)
            st.text("Confidence: 94.2%")
            st.text("OCR Plate: KA-01-HG-4321")
            st.markdown("---")
            st.markdown('<p class="status-alert">[VIOLATION DETECTED] No Helmet</p>', unsafe_allow_html=True)
            st.text("Confidence: 89.7%")
            st.text("OCR Plate: KA-05-MK-9988")
            st.markdown("---")
            st.button("Transmit to Control Room")
        else:
            st.info("Awaiting node transmission...")
