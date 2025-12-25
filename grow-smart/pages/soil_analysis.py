import streamlit as st
from PIL import Image
import io

def show():
    st.markdown("""
    <div class="app-header">
        <div class="app-title">
            🌾 Soil Analysis
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Dashboard"):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown("---")
    
    st.markdown("""
    <div class="greeting-box">
        <h3 style="color: #2e7d32; margin: 0;">📸 Capture or Upload Soil Image</h3>
        <p style="color: #666; margin-top: 10px;">Take a photo of your soil or upload an image for analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Camera input
    camera_image = st.camera_input("📷 Take a picture of soil")
    
    st.markdown("**OR**")
    
    # File uploader
    uploaded_file = st.file_uploader("📁 Upload soil image", type=['png', 'jpg', 'jpeg'])
    
    image_to_analyze = camera_image if camera_image else uploaded_file
    
    if image_to_analyze:
        st.image(image_to_analyze, caption="Captured Soil Image", use_container_width=True)
        
        if st.button("🔍 Analyze Soil", type="primary", use_container_width=True):
            with st.spinner("Analyzing soil properties..."):
                import time
                time.sleep(2)  # Simulate analysis
                
                st.success("✅ Analysis Complete!")
                
                # Display results
                st.markdown("""
                <div class="stats-card">
                    <h3 style="color: #2e7d32; margin-bottom: 20px;">📊 Soil Analysis Results</h3>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("🌱 Soil Type", "Loamy Soil")
                    st.metric("💧 pH Level", "6.5", delta="Optimal")
                    st.metric("🌾 Nitrogen", "Medium", delta="Good")
                
                with col2:
                    st.metric("🔥 Organic Matter", "High")
                    st.metric("💎 Phosphorus", "Low", delta="-10%")
                    st.metric("⚡ Potassium", "Medium")
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Recommendations
                st.markdown("""
                <div class="weather-card" style="margin-top: 20px;">
                    <h4 style="margin-bottom: 15px;">🌾 Recommended Crops</h4>
                    <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px; margin: 10px 0;">
                        <strong>Best suited for:</strong><br>
                        🌾 Rice, 🌽 Maize, 🥔 Potato, 🍅 Tomato, 🥕 Carrot
                    </div>
                    
                    <h4 style="margin-top: 20px; margin-bottom: 15px;">💡 Improvement Tips</h4>
                    <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px;">
                        <ul style="margin: 0; padding-left: 20px;">
                            <li>Add phosphorus-rich fertilizer</li>
                            <li>Current pH is ideal for most crops</li>
                            <li>Maintain organic matter with compost</li>
                            <li>Good moisture retention capacity</li>
                        </ul>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Save results button
                if st.button("💾 Save Analysis Report", use_container_width=True):
                    st.success("Report saved to your dashboard!")
    else:
        st.info("👆 Please capture or upload a soil image to begin analysis")
        
        # Example guide
        with st.expander("📖 How to take a good soil sample photo"):
            st.markdown("""
            **Tips for best results:**
            
            1. 🌞 Take photo in good natural lighting
            2. 📏 Hold camera 15-20 cm above soil
            3. 🧹 Clear any debris from surface
            4. 💧 Capture soil in natural moisture state
            5. 📐 Fill entire frame with soil sample
            """)