import streamlit as st
import time

def show():
    st.markdown("""
    <div class="app-header">
        <div class="app-title">
            🦠 Disease Detection
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Dashboard"):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown("---")
    
    st.markdown("""
    <div class="greeting-box">
        <h3 style="color: #2e7d32; margin: 0;">🔍 Plant Disease Detection</h3>
        <p style="color: #666; margin-top: 10px;">Capture plant/leaf image to detect diseases and get treatment advice</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Camera input
    camera_image = st.camera_input("📷 Take a picture of plant/leaf")
    
    st.markdown("**OR**")
    
    # File uploader
    uploaded_file = st.file_uploader("📁 Upload plant/leaf image", type=['png', 'jpg', 'jpeg'])
    
    image_to_analyze = camera_image if camera_image else uploaded_file
    
    if image_to_analyze:
        st.image(image_to_analyze, caption="Captured Plant Image", use_container_width=True)
        
        if st.button("🔍 Detect Disease", type="primary", use_container_width=True):
            with st.spinner("Analyzing plant health..."):
                time.sleep(2)  # Simulate analysis
                
                # Results
                st.markdown("""
                <div class="stats-card">
                    <h3 style="color: #c62828;">⚠️ Disease Detected</h3>
                    <h2 style="color: #d32f2f; margin: 15px 0;">Leaf Blight</h2>
                    <p style="color: #666;">Confidence: 87%</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Disease Information
                st.markdown("""
                <div class="weather-card" style="background: linear-gradient(135deg, #ff6b6b 0%, #c92a2a 100%); margin-top: 20px;">
                    <h4>📋 Disease Information</h4>
                    <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px; margin: 15px 0;">
                        <strong>Symptoms:</strong><br>
                        • Brown or black spots on leaves<br>
                        • Wilting and yellowing of foliage<br>
                        • Reduced plant vigor<br>
                        • May spread to stems and fruits
                    </div>
                    
                    <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px; margin: 15px 0;">
                        <strong>Causes:</strong><br>
                        • High humidity conditions<br>
                        • Poor air circulation<br>
                        • Overhead watering<br>
                        • Dense plant spacing
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Treatment Recommendations
                st.markdown("""
                <div class="stats-card" style="margin-top: 20px;">
                    <h3 style="color: #2e7d32;">💊 Treatment Solutions</h3>
                    
                    <div style="border-left: 4px solid #4caf50; padding: 15px; margin: 15px 0; background: #f1f8e9;">
                        <h4 style="color: #2e7d32; margin-top: 0;">Immediate Actions:</h4>
                        <ul style="color: #555;">
                            <li>Remove and destroy infected leaves</li>
                            <li>Avoid overhead watering</li>
                            <li>Improve air circulation around plants</li>
                            <li>Water in the morning to allow foliage to dry</li>
                        </ul>
                    </div>
                    
                    <div style="border-left: 4px solid #ffa726; padding: 15px; margin: 15px 0; background: #fff3e0;">
                        <h4 style="color: #e65100; margin-top: 0;">Organic Treatment:</h4>
                        <ul style="color: #555;">
                            <li>Apply neem oil spray (10ml per liter water)</li>
                            <li>Use copper-based fungicide</li>
                            <li>Spray weekly until symptoms disappear</li>
                            <li>Apply in evening hours</li>
                        </ul>
                    </div>
                    
                    <div style="border-left: 4px solid #42a5f5; padding: 15px; margin: 15px 0; background: #e3f2fd;">
                        <h4 style="color: #1565c0; margin-top: 0;">Chemical Treatment:</h4>
                        <ul style="color: #555;">
                            <li>Mancozeb 75% WP @ 2g/liter</li>
                            <li>Carbendazim 50% WP @ 1g/liter</li>
                            <li>Spray every 7-10 days</li>
                            <li>Alternate fungicides to prevent resistance</li>
                        </ul>
                    </div>
                    
                    <div style="border-left: 4px solid #7e57c2; padding: 15px; margin: 15px 0; background: #ede7f6;">
                        <h4 style="color: #4527a0; margin-top: 0;">Prevention Tips:</h4>
                        <ul style="color: #555;">
                            <li>Plant resistant varieties</li>
                            <li>Maintain proper plant spacing</li>
                            <li>Practice crop rotation</li>
                            <li>Remove crop debris after harvest</li>
                        </ul>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Action buttons
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💾 Save Report", use_container_width=True):
                        st.success("Report saved!")
                with col2:
                    if st.button("📞 Contact Expert", use_container_width=True):
                        st.info("Connecting to agricultural expert...")
    else:
        st.info("👆 Please capture or upload a plant/leaf image to detect diseases")
        
        # Tips
        with st.expander("📖 How to capture plant image for best results"):
            st.markdown("""
            **Photography Tips:**
            
            1. 🌞 Use natural daylight
            2. 📸 Focus on affected leaf/area
            3. 🔍 Get close-up of symptoms
            4. 📐 Keep image clear and in focus
            5. 🎯 Include both healthy and affected parts
            6. 🌿 Clean background for better detection
            """)
        
        # Common diseases
        with st.expander("🦠 Common Plant Diseases We Detect"):
            st.markdown("""
            - **Leaf Blight** - Brown/black spots on leaves
            - **Powdery Mildew** - White powdery coating
            - **Rust** - Orange/brown pustules
            - **Bacterial Wilt** - Sudden wilting
            - **Mosaic Virus** - Yellow mottled patterns
            - **Root Rot** - Yellowing and drooping
            - **Anthracnose** - Dark lesions on leaves/fruits
            """)