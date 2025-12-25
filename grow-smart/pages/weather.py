import streamlit as st
from datetime import datetime, timedelta

def show():
    st.markdown("""
    <div class="app-header">
        <div class="app-title">
            🌤️ Weather Forecast
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Dashboard"):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown("---")
    
    # Current Weather
    st.markdown("""
    <div class="weather-card">
        <div class="location">📍 Bangalore, Karnataka</div>
        <div class="temperature">28°C</div>
        <div class="weather-condition">⛅ Partly Cloudy</div>
        <div style="font-size: 14px; opacity: 0.9; margin-top: 5px;">Feels like 30°C</div>
        
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
                <div class="weather-label">Visibility</div>
                <div class="weather-value">👁️ 10 km</div>
            </div>
            <div class="weather-item">
                <div class="weather-label">UV Index</div>
                <div class="weather-value">☀️ 6 (High)</div>
            </div>
            <div class="weather-item">
                <div class="weather-label">Pressure</div>
                <div class="weather-value">🎚️ 1012 mb</div>
            </div>
            <div class="weather-item">
                <div class="weather-label">Soil Temp</div>
                <div class="weather-value">🌡️ 26°C</div>
            </div>
        </div>
        
        <div class="weather-message">
            ✅ Fair weather, good for irrigation and field work
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 7-Day Forecast
    st.markdown('<div class="section-title">📅 7-Day Forecast</div>', unsafe_allow_html=True)
    
    forecast_data = [
        ("Today", "⛅", 28, 24, 65),
        ("Tomorrow", "🌤️", 30, 25, 60),
        ("Friday", "☀️", 32, 26, 55),
        ("Saturday", "🌧️", 27, 23, 80),
        ("Sunday", "⛈️", 26, 22, 85),
        ("Monday", "🌤️", 29, 24, 70),
        ("Tuesday", "☀️", 31, 25, 58),
    ]
    
    for day, icon, high, low, humidity in forecast_data:
        st.markdown(f"""
        <div class="stats-card" style="margin: 10px 0; padding: 15px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="flex: 1;">
                    <strong style="color: #2e7d32; font-size: 16px;">{day}</strong>
                </div>
                <div style="flex: 1; text-align: center; font-size: 32px;">
                    {icon}
                </div>
                <div style="flex: 1; text-align: center;">
                    <div style="font-size: 18px; font-weight: bold; color: #d32f2f;">{high}°</div>
                    <div style="font-size: 14px; color: #666;">{low}°</div>
                </div>
                <div style="flex: 1; text-align: right; color: #1976d2;">
                    💧 {humidity}%
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Farming Advisory
    st.markdown('<div class="section-title">🌾 Farming Advisory</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-card">
        <h4 style="color: #2e7d32; margin-bottom: 15px;">Today's Recommendations</h4>
        
        <div style="border-left: 4px solid #4caf50; padding: 12px; margin: 10px 0; background: #f1f8e9;">
            <strong style="color: #2e7d32;">✅ Good for:</strong><br>
            • Irrigation and watering<br>
            • Spraying pesticides<br>
            • Field preparation<br>
            • Harvesting crops
        </div>
        
        <div style="border-left: 4px solid #ffa726; padding: 12px; margin: 10px 0; background: #fff3e0;">
            <strong style="color: #e65100;">⚠️ Be Careful:</strong><br>
            • High UV index - work in morning/evening<br>
            • Check soil moisture before irrigation
        </div>
        
        <div style="border-left: 4px solid #42a5f5; padding: 12px; margin: 10px 0; background: #e3f2fd;">
            <strong style="color: #1565c0;">💡 Upcoming:</strong><br>
            • Rain expected on Saturday-Sunday<br>
            • Plan indoor activities for weekend<br>
            • Cover harvested crops
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Rainfall Data
    st.markdown('<div class="section-title">🌧️ Rainfall Information</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Today", "0 mm", delta="Dry")
    
    with col2:
        st.metric("This Week", "15 mm", delta="↑ 5mm")
    
    with col3:
        st.metric("This Month", "85 mm", delta="Normal")
    
    # Alerts
    if True:  # Simulate alert condition
        st.markdown("""
        <div style="background: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; 
                    border-radius: 8px; margin: 20px 0;">
            <strong style="color: #856404;">⚠️ Weather Alert:</strong><br>
            Heavy rain expected on Sunday. Secure crops and equipment.
        </div>
        """, unsafe_allow_html=True)