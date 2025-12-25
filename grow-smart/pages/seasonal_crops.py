import streamlit as st

def show():
    st.markdown("""
    <div class="app-header">
        <div class="app-title">
            🌾 Seasonal Crops Guide
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Dashboard"):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown("---")
    
    # Current Season
    st.markdown("""
    <div class="greeting-box">
        <h3 style="color: #2e7d32; margin: 0;">🌤️ Current Season: Winter (Rabi)</h3>
        <p style="color: #666; margin-top: 10px;">December - March | Best crops for this season</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Recommended Crops
    st.markdown('<div class="section-title">⭐ Recommended Crops for Winter</div>', unsafe_allow_html=True)
    
    winter_crops = [
        {
            "name": "🌾 Wheat",
            "season": "Rabi",
            "duration": "120-150 days",
            "yield": "40-50 quintals/hectare",
            "tips": "Requires cool weather. Sow in November-December. Needs 4-5 irrigations."
        },
        {
            "name": "🌾 Barley",
            "season": "Rabi",
            "duration": "120-140 days",
            "yield": "35-40 quintals/hectare",
            "tips": "Tolerates saline soil. Less water needed than wheat."
        },
        {
            "name": "🥔 Potato",
            "season": "Rabi",
            "duration": "90-120 days",
            "yield": "200-250 quintals/hectare",
            "tips": "Plant in October-November. Requires well-drained soil."
        },
        {
            "name": "🍅 Tomato",
            "season": "Rabi",
            "duration": "75-90 days",
            "yield": "300-400 quintals/hectare",
            "tips": "Requires support structure. Regular watering needed."
        },
        {
            "name": "🌿 Mustard",
            "season": "Rabi",
            "duration": "90-110 days",
            "yield": "12-15 quintals/hectare",
            "tips": "Cool season crop. Sow in October-November."
        },
        {
            "name": "🥕 Carrot",
            "season": "Rabi",
            "duration": "90-120 days",
            "yield": "150-200 quintals/hectare",
            "tips": "Needs loose, well-drained soil. Regular watering important."
        }
    ]
    
    for crop in winter_crops:
        st.markdown(f"""
        <div class="stats-card" style="margin: 15px 0;">
            <h3 style="color: #2e7d32; margin-bottom: 15px;">{crop['name']}</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                <div>
                    <div style="color: #666; font-size: 14px;">Duration</div>
                    <div style="font-weight: bold; color: #2e7d32;">⏱️ {crop['duration']}</div>
                </div>
                <div>
                    <div style="color: #666; font-size: 14px;">Expected Yield</div>
                    <div style="font-weight: bold; color: #2e7d32;">📊 {crop['yield']}</div>
                </div>
            </div>
            <div style="background: #f1f8e9; padding: 12px; border-radius: 8px; border-left: 4px solid #4caf50;">
                <strong style="color: #2e7d32;">💡 Tips:</strong><br>
                {crop['tips']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Upcoming Season
    st.markdown('<div class="section-title">🌻 Upcoming Season: Summer (Zaid)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="weather-card" style="background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);">
        <h4 style="margin-bottom: 15px;">March - June Crops</h4>
        <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px;">
            <strong>Prepare for these crops:</strong><br><br>
            🥒 Cucumber • 🍉 Watermelon • 🥭 Mango<br>
            🍈 Muskmelon • 🥜 Groundnut • 🌻 Sunflower<br>
            🌶️ Chilli • 🍆 Brinjal • 🫘 Green Gram
        </div>
        
        <div style="margin-top: 15px; padding: 12px; background: rgba(255,255,255,0.2); border-radius: 8px;">
            <strong>📅 Start Preparation:</strong><br>
            Begin field preparation in late February for best results
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Crop Calendar
    st.markdown('<div class="section-title">📅 Annual Crop Calendar</div>', unsafe_allow_html=True)
    
    seasons = [
        ("🌧️ Kharif (Monsoon)", "June - October", "Rice, Maize, Cotton, Soybean, Sugarcane, Bajra, Jowar"),
        ("❄️ Rabi (Winter)", "November - March", "Wheat, Barley, Mustard, Potato, Tomato, Onion"),
        ("☀️ Zaid (Summer)", "March - June", "Cucumber, Watermelon, Muskmelon, Bitter Gourd")
    ]
    
    for season, period, crops in seasons:
        st.markdown(f"""
        <div class="stats-card" style="margin: 15px 0;">
            <h4 style="color: #2e7d32; margin-bottom: 10px;">{season}</h4>
            <div style="color: #666; margin-bottom: 10px;">📅 {period}</div>
            <div style="background: #f1f8e9; padding: 12px; border-radius: 8px;">
                <strong>Crops:</strong> {crops}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Market Demand
    st.markdown('<div class="section-title">💰 High Demand Crops</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-card">
        <p style="color: #666; margin-bottom: 15px;">Based on current market trends</p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🥔 Potato", "₹25/kg", delta="↑ 15%")
    
    with col2:
        st.metric("🍅 Tomato", "₹40/kg", delta="↑ 25%")
    
    with col3:
        st.metric("🧅 Onion", "₹35/kg", delta="↑ 10%")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Tips Section
    st.markdown('<div class="section-title">💡 Farming Tips</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-card">
        <div style="border-left: 4px solid #4caf50; padding: 12px; margin: 10px 0; background: #f1f8e9;">
            <strong style="color: #2e7d32;">🌱 Crop Rotation:</strong><br>
            Practice crop rotation to maintain soil health and prevent pest buildup
        </div>
        
        <div style="border-left: 4px solid #2196f3; padding: 12px; margin: 10px 0; background: #e3f2fd;">
            <strong style="color: #1565c0;">💧 Water Management:</strong><br>
            Use drip irrigation to save water and improve crop yield
        </div>
        
        <div style="border-left: 4px solid #ff9800; padding: 12px; margin: 10px 0; background: #fff3e0;">
            <strong style="color: #e65100;">🌾 Seed Selection:</strong><br>
            Always use certified seeds for better germination and disease resistance
        </div>
        
        <div style="border-left: 4px solid #9c27b0; padding: 12px; margin: 10px 0; background: #f3e5f5;">
            <strong style="color: #6a1b9a;">🌿 Organic Farming:</strong><br>
            Consider organic methods for better market prices and soil health
        </div>
    </div>
    """, unsafe_allow_html=True)