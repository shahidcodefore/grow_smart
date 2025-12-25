import streamlit as st

def show():
    st.markdown("""
    <div class="app-header">
        <div class="app-title">
            🛒 Marketplace
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Dashboard"):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown("---")
    
    # Market Overview
    st.markdown("""
    <div class="greeting-box">
        <h3 style="color: #2e7d32; margin: 0;">📊 Today's Market Prices</h3>
        <p style="color: #666; margin-top: 10px;">Live prices from Bangalore APMC</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Price Cards
    st.markdown('<div class="section-title">🌾 Vegetables & Fruits</div>', unsafe_allow_html=True)
    
    products = [
        ("🍅 Tomato", "₹40/kg", "↑ 25%", "up", "High Demand"),
        ("🥔 Potato", "₹25/kg", "↑ 15%", "up", "Stable"),
        ("🧅 Onion", "₹35/kg", "↑ 10%", "up", "Good"),
        ("🥕 Carrot", "₹30/kg", "↓ 5%", "down", "Average"),
        ("🫑 Capsicum", "₹50/kg", "↑ 20%", "up", "High"),
        ("🥒 Cucumber", "₹20/kg", "→ 0%", "same", "Stable"),
        ("🍆 Brinjal", "₹28/kg", "↑ 12%", "up", "Good"),
        ("🥬 Cabbage", "₹18/kg", "↓ 8%", "down", "Average"),
    ]
    
    col1, col2 = st.columns(2)
    
    for i, (name, price, change, trend, demand) in enumerate(products):
        with col1 if i % 2 == 0 else col2:
            trend_color = "#4caf50" if trend == "up" else "#f44336" if trend == "down" else "#ff9800"
            st.markdown(f"""
            <div class="stats-card" style="margin: 10px 0;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="font-size: 20px; margin-bottom: 5px;">{name}</div>
                        <div style="font-size: 24px; font-weight: bold; color: #2e7d32;">{price}</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="color: {trend_color}; font-weight: bold; font-size: 18px;">{change}</div>
                        <div style="color: #666; font-size: 14px;">{demand}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Grains & Pulses
    st.markdown('<div class="section-title">🌾 Grains & Pulses</div>', unsafe_allow_html=True)
    
    grains = [
        ("🌾 Wheat", "₹2,200/quintal", "↑ 8%", "up"),
        ("🌾 Rice", "₹3,500/quintal", "↑ 5%", "up"),
        ("🫘 Tur Dal", "₹8,500/quintal", "↑ 12%", "up"),
        ("🫘 Moong Dal", "₹7,200/quintal", "↓ 3%", "down"),
    ]
    
    for name, price, change, trend in grains:
        trend_color = "#4caf50" if trend == "up" else "#f44336"
        st.markdown(f"""
        <div class="stats-card" style="margin: 10px 0; padding: 15px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="font-size: 18px; font-weight: bold; color: #2e7d32;">{name}</div>
                <div style="text-align: right;">
                    <div style="font-size: 20px; font-weight: bold; color: #2e7d32;">{price}</div>
                    <div style="color: {trend_color}; font-weight: bold;">{change}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Nearby Markets
    st.markdown('<div class="section-title">📍 Nearby Markets</div>', unsafe_allow_html=True)
    
    markets = [
        ("Bangalore APMC", "12 km", "Open: 6 AM - 2 PM"),
        ("KR Market", "8 km", "Open: 5 AM - 11 AM"),
        ("Yeshwanthpur Market", "15 km", "Open: 6 AM - 1 PM"),
        ("Malleswaram Market", "10 km", "Open: 7 AM - 12 PM"),
    ]
    
    for market, distance, timing in markets:
        st.markdown(f"""
        <div class="stats-card" style="margin: 10px 0; padding: 15px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 18px; font-weight: bold; color: #2e7d32;">📍 {market}</div>
                    <div style="color: #666; margin-top: 5px;">{timing}</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 16px; color: #1976d2; font-weight: bold;">{distance}</div>
                    <button style="background: #4caf50; color: white; border: none; padding: 8px 15px; 
                                   border-radius: 5px; margin-top: 5px; cursor: pointer;">
                        Get Directions
                    </button>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Market Tips
    st.markdown('<div class="section-title">💡 Market Tips</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-card">
        <div style="border-left: 4px solid #4caf50; padding: 12px; margin: 10px 0; background: #f1f8e9;">
            <strong style="color: #2e7d32;">🕐 Best Time to Sell:</strong><br>
            Visit market early morning (6-8 AM) for best prices and fresh bidding
        </div>
        
        <div style="border-left: 4px solid #2196f3; padding: 12px; margin: 10px 0; background: #e3f2fd;">
            <strong style="color: #1565c0;">📦 Quality Matters:</strong><br>
            Grade your produce properly - premium quality gets 20-30% higher price
        </div>
        
        <div style="border-left: 4px solid #ff9800; padding: 12px; margin: 10px 0; background: #fff3e0;">
            <strong style="color: #e65100;">📊 Market Research:</strong><br>
            Check prices at multiple markets before selling bulk produce
        </div>
        
        <div style="border-left: 4px solid #9c27b0; padding: 12px; margin: 10px 0; background: #f3e5f5;">
            <strong style="color: #6a1b9a;">🤝 Direct to Consumer:</strong><br>
            Consider farmer's markets for better margins and direct sales
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Demand Forecast
    st.markdown('<div class="section-title">📈 Demand Forecast (Next Week)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="weather-card" style="background: linear-gradient(135deg, #2196f3 0%, #1565c0 100%);">
        <h4>High Demand Expected:</h4>
        <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px; margin-top: 15px;">
            <strong>Vegetables:</strong> Tomato, Onion, Green Chilli<br>
            <strong>Reason:</strong> Festival season approaching<br>
            <strong>Expected Price Rise:</strong> 15-25%
        </div>
        
        <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px; margin-top: 15px;">
            <strong>💡 Recommendation:</strong><br>
            Hold produce for 3-4 days if possible for better prices
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Government Schemes
    st.markdown('<div class="section-title">🏛️ Government Support</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stats-card">
        <h4 style="color: #2e7d32; margin-bottom: 15px;">Available Schemes</h4>
        
        <div style="background: #e8f5e9; padding: 12px; border-radius: 8px; margin: 10px 0;">
            <strong>📋 PM-KISAN:</strong><br>
            ₹6,000 per year in three installments<br>
            <span style="color: #4caf50;">✓ Eligible</span>
        </div>
        
        <div style="background: #e8f5e9; padding: 12px; border-radius: 8px; margin: 10px 0;">
            <strong>🏦 Kisan Credit Card:</strong><br>
            Low-interest crop loans up to ₹3 lakhs<br>
            <span style="color: #4caf50;">✓ Apply Now</span>
        </div>
        
        <div style="background: #e8f5e9; padding: 12px; border-radius: 8px; margin: 10px 0;">
            <strong>🛡️ Crop Insurance:</strong><br>
            Protect crops from natural calamities<br>
            <span style="color: #2196f3;">ℹ️ Learn More</span>
        </div>
    </div>
    """, unsafe_allow_html=True)