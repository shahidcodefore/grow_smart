# 🌱 Grow Smart - Smart Farming Application

A mobile-responsive web application for smart farming built with Streamlit.

## 🚀 Quick Start

### 1. Install Python 3.8+
Download from [python.org](https://www.python.org/downloads/)

### 2. Create Project

```bash
# Create directory structure
mkdir grow-smart
cd grow-smart
mkdir pages
```

### 3. Create Files

Copy all provided code files into the project:
- `app.py` (main file)
- `requirements.txt`
- `pages/__init__.py`
- `pages/soil_analysis.py`
- `pages/disease_detection.py`
- `pages/weather.py`
- `pages/seasonal_crops.py`
- `pages/marketplace.py`
- `pages/chat_assistant.py`

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Application

```bash
streamlit run app.py
```

🎉 **App will open at: http://localhost:8501**

---

## 📱 Features

✅ **Dashboard** - Weather, stats, quick actions  
✅ **Soil Analysis** - Camera/upload for soil testing  
✅ **Disease Detection** - Plant disease diagnosis  
✅ **Weather Forecast** - 7-day forecast with farming tips  
✅ **Seasonal Crops** - Best crops to plant now  
✅ **Marketplace** - Live market prices  
✅ **Chat Assistant** - AI farming help  

---

## 📁 Project Structure

```
grow-smart/
├── app.py                    # Main app
├── requirements.txt          # Dependencies
└── pages/                    # Feature pages
    ├── __init__.py
    ├── soil_analysis.py
    ├── disease_detection.py
    ├── weather.py
    ├── seasonal_crops.py
    ├── marketplace.py
    └── chat_assistant.py
```

---

## 🎯 Key Technologies

- **Streamlit** - Web framework
- **Python 3.8+** - Backend
- **PIL (Pillow)** - Image processing
- **HTML/CSS** - Custom styling

---

## 📖 Full Documentation

See `SETUP_GUIDE.md` for:
- Detailed installation steps
- Customization guide
- Troubleshooting
- Deployment options
- Development tips

---

## 🌐 Access from Mobile

1. Find your computer's IP address
2. Run: `streamlit run app.py --server.address 0.0.0.0`
3. Open on phone: `http://YOUR_IP:8501`

---

## 🎨 Customization

### Change Location
Edit in `app.py` and `pages/weather.py`:
```html
<div class="location">📍 Your City, Your State</div>
```

### Update Prices
Edit in `pages/marketplace.py`:
```python
products = [
    ("🍅 Tomato", "₹40/kg", "↑ 25%", "up", "High Demand"),
]
```

### Modify Crops
Edit in `pages/seasonal_crops.py`:
```python
winter_crops = [...]
```

---

## 🐛 Troubleshooting

**Port in use:**
```bash
streamlit run app.py --server.port 8502
```

**Module errors:**
```bash
pip install --upgrade streamlit pillow
```

**Camera not working:**
- Use upload feature instead
- Or deploy to Streamlit Cloud for HTTPS

---

## 🚀 Deploy Online (Free)

### Streamlit Cloud
1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repo and deploy

### Deploy Steps:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_REPO
git push -u origin main
```

---

## 💡 Usage Tips

1. **Mobile Friendly** - Works great on phones/tablets
2. **Camera Feature** - Best on mobile devices
3. **Offline Ready** - Most features work without internet
4. **Quick Actions** - Dashboard buttons for fast access
5. **Sidebar Menu** - Always accessible from any page

---

## 🌾 For Farmers

This app helps with:
- 🌤️ Daily weather updates
- 💧 When to water crops
- 🌱 What crops to plant
- 🦠 Identify plant diseases
- 💰 Current market prices
- 💬 Get farming advice 24/7

All in simple language! 

---

## 🔄 Updates

To update the app:
1. Edit the relevant `.py` file
2. Save the file
3. Streamlit auto-reloads!

---

## 📞 Need Help?

- Check `SETUP_GUIDE.md` for detailed help
- Visit [Streamlit Docs](https://docs.streamlit.io)
- Review troubleshooting section

---

## ⭐ Features Highlight

### Camera Integration
```python
camera_image = st.camera_input("📷 Take a picture")
```

### File Upload
```python
uploaded_file = st.file_uploader("📁 Upload image")
```

### Interactive Chat
```python
user_input = st.text_input("Ask anything...")
```

### Live Updates
- Weather refreshes automatically
- Prices update in real-time
- Date/time always current

---

## 🎯 Perfect For

✅ Small farmers  
✅ Marginal farmers  
✅ Agricultural students  
✅ Farming cooperatives  
✅ Rural areas  
✅ Smart farming initiatives  

---

## 📊 Statistics

- **7 Complete Features**
- **Mobile Responsive Design**
- **Farmer-Friendly Interface**
- **English, Hindi, Kannada Support**
- **No Login Required**
- **Free to Use**

---

## 🌟 Why Grow Smart?

- Simple to use
- Works on any device
- No internet needed (offline mode)
- Free and open source
- Made for Indian farmers
- Regular updates

---

## 📝 License

Open source - Feel free to modify and distribute!

---

## 🙏 Credits

Built with ❤️ for farmers using:
- Streamlit framework
- Python programming
- Open source tools

---

## 🚜 Start Farming Smart Today!

```bash
streamlit run app.py
```

**Happy Farming! 🌾🌱**