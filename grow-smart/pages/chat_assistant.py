import streamlit as st
import time

def get_bot_response(user_message):
    """Simple rule-based chatbot for farming queries"""
    user_message = user_message.lower()
    
    # Predefined responses
    responses = {
        "weather": "Based on current data, we have partly cloudy weather with 28°C temperature. Good conditions for field work and irrigation. Check Weather page for detailed forecast.",
        "irrigation": "For most crops, water early morning (6-8 AM) or evening (4-6 PM). Avoid midday watering. Check soil moisture before irrigating - soil should be moist but not waterlogged.",
        "fertilizer": "Use balanced NPK fertilizer for vegetables. For wheat/rice, apply Urea 20 days after sowing. Always do soil test first. Organic compost is recommended for soil health.",
        "disease": "Common diseases: Leaf blight, powdery mildew, root rot. Upload plant image in Disease Detection page for accurate diagnosis and treatment.",
        "price": "Current market prices: Tomato ₹40/kg (↑25%), Potato ₹25/kg (↑15%), Onion ₹35/kg (↑10%). Visit Marketplace for complete price list.",
        "crop": "For winter season, recommended crops: Wheat, Potato, Tomato, Mustard, Carrot. Check Seasonal Crops page for detailed guide.",
        "loan": "Kisan Credit Card provides crop loans up to ₹3 lakhs at low interest. PM-KISAN gives ₹6000/year. Visit your nearest bank for application.",
        "soil": "Use Soil Analysis feature to check soil health. Take clear photo of soil sample. We'll analyze pH, nutrients, and recommend suitable crops.",
    }
    
    # Check for keywords
    for keyword, response in responses.items():
        if keyword in user_message:
            return response
    
    # Default response
    return "I'm here to help with farming questions! You can ask me about:\n\n• Weather and irrigation\n• Crop recommendations\n• Market prices\n• Disease treatment\n• Fertilizer advice\n• Government schemes\n• Soil health\n\nWhat would you like to know?"

def show():
    st.markdown("""
    <div class="app-header">
        <div class="app-title">
            💬 Chat Assistant
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Dashboard"):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown("---")
    
    st.markdown("""
    <div class="greeting-box">
        <h3 style="color: #2e7d32; margin: 0;">🤖 Farming Assistant</h3>
        <p style="color: #666; margin-top: 10px;">Ask me anything about farming in simple language!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize chat history in session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": "नमस्ते! 🙏 Hello Farmer! I'm your farming assistant. I can help you with:\n\n🌤️ Weather updates\n💧 Irrigation advice\n🌾 Crop recommendations\n🦠 Disease solutions\n💰 Market prices\n🌱 Fertilizer guidance\n\nWhat would you like to know today?"
            }
        ]
    
    # Quick question buttons
    st.markdown("### ⚡ Quick Questions")
    
    quick_questions = [
        "What's today's weather?",
        "When should I water my crops?",
        "Which crops to plant now?",
        "Current market prices?",
    ]
    col1, col2 = st.columns(2)

for i, question in enumerate(quick_questions):
    with col1 if i % 2 == 0 else col2:
        if st.button(question, key=f"quick_{i}", use_container_width=True):
            # Add user message
            st.session_state.chat_history.append({
                "role": "user",
                "content": question
            })
            
            # Get bot response
            response = get_bot_response(question)
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response
            })
            st.rerun()

st.markdown("---")

# Chat container
chat_container = st.container()

with chat_container:
    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"""
            <div style="background: #e3f2fd; padding: 15px; border-radius: 15px; 
                        margin: 10px 0; margin-left: 20%; text-align: right;">
                <strong style="color: #1565c0;">You:</strong><br>
                {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background: #f1f8e9; padding: 15px; border-radius: 15px; 
                        margin: 10px 0; margin-right: 20%; border-left: 4px solid #4caf50;">
                <strong style="color: #2e7d32;">🤖 Assistant:</strong><br>
                {message["content"]}
            </div>
            """, unsafe_allow_html=True)

# Chat input
st.markdown("---")

with st.form(key="chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input(
            "Type your question...",
            placeholder="Ask about weather, crops, prices, diseases...",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.form_submit_button("Send 📤", use_container_width=True)
    
    if send_button and user_input:
        # Add user message
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Simulate typing delay
        with st.spinner("Assistant is typing..."):
            time.sleep(1)
            response = get_bot_response(user_input)
        
        # Add bot response
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response
        })
        
        st.rerun()

# Clear chat button
if st.button("🗑️ Clear Chat History", use_container_width=True):
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "नमस्ते! 🙏 Hello Farmer! I'm your farming assistant. How can I help you today?"
        }
    ]
    st.rerun()

# Common topics
with st.expander("📚 Common Topics I Can Help With"):
    st.markdown("""
    **Weather & Irrigation:**
    - Current weather conditions
    - Best time to irrigate
    - Rainfall predictions
    - Soil moisture advice
    
    **Crops & Planting:**
    - Seasonal crop recommendations
    - Best crops for your soil
    - Planting calendar
    - Crop rotation advice
    
    **Disease & Pests:**
    - Disease identification
    - Treatment methods
    - Prevention tips
    - Organic solutions
    
    **Market & Prices:**
    - Current market rates
    - Price trends
    - Best time to sell
    - Nearby markets
    
    **Fertilizers & Nutrition:**
    - NPK recommendations
    - Organic fertilizers
    - Application timing
    - Soil amendments
    
    **Government Schemes:**
    - PM-KISAN details
    - Crop insurance
    - Kisan Credit Card
    - Subsidies
    """)

# Language support note
st.info("💬 **Language Support:** I understand English, Hindi, and Kannada (limited). Feel free to ask in your preferred language!")