import streamlit as st
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Grow Smart",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for mobile-responsive green theme
st.markdown("""
<style>
    /* Main theme */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8f5e9 100%);
    }
    
    /* Header */
    .app-header {
        background: linear-gradient(135deg, #2e7d32 0%, #1b5e20 100%);
        padding: 20px;
        border-radius: 0 0 20px 20px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .app-title {
        font-size: 28px;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Greeting Section */
    .greeting-box {
        background: white;
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .greeting-text {
        font-size: 24px;
        color: #2e7d32;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .date-text {
        color: #666;
        font-size: 16px;
    }
    
    /* Weather Card */
    .weather-card {
        background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
        color: white;
        padding: 25px;
        border-radius: 20px;
        margin: 15px 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .location {
        font-size: 18px;
        margin-bottom: 10px;
        opacity: 0.9;
    }
    
    .temperature {
        font-size: 48px;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .weather-condition {
        font-size: 20px;
        margin-bottom: 15px;
    }
    
    .weather-details {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255,255,255,0.3);
    }
    
    .weather-item {
        text-align: center;
    }
    
    .weather-label {
        font-size: 12px;
        opacity: 0.8;
    }
    
    .weather-value {
        font-size: 18px;
        font-weight: bold;
        margin-top: 5px;
    }
    
    .weather-message {
        background: rgba(255,255,255,0.2);
        padding: 12px;
        border-radius: 10px;
        margin-top: 15px;
        font-size: 14px;
    }
    
    /* Quick Stats */
    .stats-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .stats-title {
        font-size: 20px;
        color: #2e7d32;
        font-weight: bold;
        margin-bottom: 15px;
    }
    
    .stat-item {
        margin: 15px 0;
    }
    
    .stat-label {
        font-size: 16px;
        color: #555;
        margin-bottom: 8px;
    }
    
    .irrigation-reminder {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 12px;
        border-radius: 8px;
        margin-top: 15px;
    }
    
    /* Feature Cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
        margin: 20px 0;
    }
    
    .feature-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 2px solid transparent;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.15);
        border-color: #4caf50;
    }
    
    .feature-icon {
        font-size: 40px;
        margin-bottom: 10px;
    }
    
    .feature-title {
        font-size: 16px;
        color: #2e7d32;
        font-weight: bold;
    }
    
    /* Section Title */
    .section-title {
        font-size: 22px;
        color: #2e7d32;
        font-weight: bold;
        margin: 25px 0 15px 0;
        padding-left: 10px;
        border-left: 4px solid #4caf50;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .feature-grid {
            grid-template-columns: 1fr;
        }
        .weather-details {
            grid-template-columns: repeat(3, 1fr);
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Sidebar menu
with st.sidebar:
    st.markdown("### 🌱 Grow Smart Menu")
    st.markdown("---")
    
    menu_items = {
        "🏠 Dashboard": "home",
        "🌾 Soil Analysis": "soil",
        "🦠 Disease Detection": "disease",
        "🌤️ Weather": "weather",
        "📊 Seasonal Crops": "seasonal",
        "🛒 Marketplace": "marketplace",
        "💬 Chat Assistant": "chat"
    }
    
    for label, page in menu_items.items():
        if st.button(label, key=f"menu_{page}", use_container_width=True):
            st.session_state.page = page
            st.rerun()

# Main content based on page
if st.session_state.page == 'home':
    # Header
    st.markdown("""
    <div class="app-header">
        <div class="app-title">
            🌱 Grow Smart
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Greeting Section
    current_hour = datetime.now().hour
    greeting = "Good Morning" if current_hour < 12 else "Good Afternoon" if current_hour < 18 else "Good Evening"
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    
    st.markdown(f"""
    <div class="greeting-box">
        <div class="greeting-text">{greeting}, Farmer! 👨‍🌾</div>
        <div class="date-text">📅 {current_date}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Weather Card
    st.markdown("""
    <div class="weather-card">
        <div class="location">📍 Bangalore, Karnataka</div>
        <div class="temperature">28°C</div>
        <div class="weather-condition">⛅ Partly Cloudy</div>
        <div style="font-size: 14px; opacity: 0.9;">H: 32° L: 24°</div>
        
        <div class="weather-details">
            <div class="weather-item">
                <div class="weather-label">Humidity</div>
                <div class="weather-value">💧 65%</div>
            </div>
            <div class="weather-item">
                <div class="weather-label">Wind Speed</div>
                <div class="weather-value">🌬️ 12 km/h</div>
            </div>
            <div class="weather-item">
                <div class="weather-label">Soil Temp</div>
                <div class="weather-value">🌡️ 26°C</div>
            </div>
        </div>
        
        <div class="weather-message">
            ✅ Fair weather, good for irrigation
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats Section
    st.markdown("""
    <div class="stats-card">
        <div class="stats-title">📊 Quick Stats</div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="stat-item">', unsafe_allow_html=True)
    st.markdown('<div class="stat-label">💧 Soil Moisture</div>', unsafe_allow_html=True)
    st.progress(0.72)
    st.markdown('<div style="text-align: right; color: #2e7d32; font-weight: bold;">72% - Good</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="stat-item">', unsafe_allow_html=True)
    st.markdown('<div class="stat-label">🌱 Crop Health</div>', unsafe_allow_html=True)
    st.progress(0.85)
    st.markdown('<div style="text-align: right; color: #2e7d32; font-weight: bold;">85% - Excellent</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="irrigation-reminder">
            💧 <strong>Irrigation Reminder:</strong> Water crops in 2-3 days
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature Cards
    st.markdown('<div class="section-title">⚡ Quick Actions</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🌤️\n\n**Weather**", use_container_width=True, key="weather_btn"):
            st.session_state.page = 'weather'
            st.rerun()
        
        if st.button("🦠\n\n**Disease Detection**", use_container_width=True, key="disease_btn"):
            st.session_state.page = 'disease'
            st.rerun()
    
    with col2:
        if st.button("🌾\n\n**Soil Analysis**", use_container_width=True, key="soil_btn"):
            st.session_state.page = 'soil'
            st.rerun()
        
        if st.button("🌾\n\n**Seasonal Crops**", use_container_width=True, key="seasonal_btn"):
            st.session_state.page = 'seasonal'
            st.rerun()

elif st.session_state.page == 'soil':
    from pages import soil_analysis
    soil_analysis.show()

elif st.session_state.page == 'disease':
    from pages import disease_detection
    disease_detection.show()

elif st.session_state.page == 'weather':
    from pages import weather
    weather.show()

elif st.session_state.page == 'seasonal':
    from pages import seasonal_crops
    seasonal_crops.show()

elif st.session_state.page == 'marketplace':
    from pages import marketplace
    marketplace.show()

elif st.session_state.page == 'chat':
    from pages import chat_assistant
    chat_assistant.show()
