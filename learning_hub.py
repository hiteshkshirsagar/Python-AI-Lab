import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="Hitesh's AI Academy", layout="wide")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.header("👤 User Profile")
    user_data = {
        "Name": "Hitesh",
        "Target Role": "AI Engineer",
        "Current Shift": "2 PM - 11 PM IST",
        "Favorite Index": "Nifty 50"
    }
    st.write(f"Welcome, **{user_data['Name']}**!")
    st.json(user_data)
    
    st.divider()
    st.header("🧭 Navigation")
    # This helps your friends navigate the "Learn" tab
    selected_topic = st.selectbox("Choose a topic to learn:", 
                                ["Variables", "Data Types", "Lists", "Dictionaries", "Loops", "Functions"])

# --- MAIN APP UI ---
st.title("📋 Python & AI Learning Hub")

tab_learn, tab_practice, tab_ai = st.tabs(["📚 Learn Python", "🛠️ Practice Lab", "🤖 AI & Trading Tools"])

# --- TAB 1: LEARNING CONTENT ---
with tab_learn:
    st.header(f"📝 Topic: {selected_topic}")
    
    if selected_topic == "Variables":
        st.write("A **Variable** is a labeled box for data.")
        st.code("name = 'Hitesh'\nsalary = 12", language="python")
        
    elif selected_topic == "Data Types":
        st.write("Python handles Numbers (int/float) and Text (strings) differently.")
        st.code("age = 25  # Integer\nprice = 22000.50 # Float\nname = 'Nifty' # String", language="python")

    elif selected_topic == "Lists":
        st.write("A **List** is a shopping bag of items.")
        st.code("my_portfolio = ['Tata Small Cap', 'Nifty 50']", language="python")
        st.info("Try adding a new fund using .append()")

    elif selected_topic == "Dictionaries":
        st.write("A **Dictionary** uses 'Keys' (labels) and 'Values' (data).")
        st.code("stock = {'name': 'TCS', 'price': 3800}", language="python")

    elif selected_topic == "Loops":
        st.write("Loops do the same task over and over—like checking 50 stock prices at once!")
        st.code("for price in prices:\n    print(price)", language="python")

    elif selected_topic == "Functions":
        st.write("A **Function** is a recipe you can reuse.")
        st.code("def calculate_tax(income):\n    return income * 0.1", language="python")

    st.divider()
    st.header("❓ Quick Q&A")
    python_qa = {
        "What is a Variable?": "A container for storing data values.",
        "What is a List?": "An ordered collection.",
        "What is Streamlit?": "A tool to build web apps with Python."
    }
    q = st.selectbox("Pick a question:", list(python_qa.keys()))
    if st.button("Reveal Answer"):
        st.info(python_qa[q])

# --- TAB 2: PRACTICE LAB ---
with tab_practice:
    st.header("📈 Interactive Portfolio")
    if 'my_portfolio' not in st.session_state:
        st.session_state.my_portfolio = ["Tata Small Cap", "Axis Silver FoF"]

    new_stock = st.text_input("Add a new stock/fund:")
    if st.button("Add to Portfolio"):
        if new_stock:
            st.session_state.my_portfolio.append(new_stock)
            st.success(f"Added {new_stock}!")

    st.write("Current Assets:", st.session_state.my_portfolio)

    st.divider()
    st.header("📊 Market Trend Analyzer")
    price_input = st.text_input("Enter last 5 days Nifty prices (comma separated):", "22100, 22050, 22200, 21900, 22300")
    try:
        price_list = [float(p.strip()) for p in price_input.split(",")]
        if st.button("Analyze Trend"):
            avg = sum(price_list) / len(price_list)
            st.metric("Average Price", f"₹{avg:,.2f}")
            if price_list[-1] > avg:
                st.success("BULLISH Trend 🚀")
            else:
                st.warning("BEARISH Trend ⚠️")
    except:
        st.error("Please enter valid numbers.")

# --- TAB 3: AI & TRADING TOOLS ---
with tab_ai:
    st.header("📈 Live Market Data")
    try:
        if st.button("Fetch Live Nifty 50"):
            price = yf.Ticker("^NSEI").history(period="1d")['Close'].iloc[-1]
            st.metric("Live Nifty 50", f"₹{price:,.2f}")
    except:
        st.warning("Could not fetch live data. Ensure 'yfinance' is in requirements.txt")

    st.divider()
    st.header("💰 Investment & Goals")
    
    buy_price = st.number_input("Purchase Price (₹):", value=100.0)
    qty = st.number_input("Quantity:", min_value=1)
    st.write(f"Total Investment: **₹{buy_price * qty:,.2f}**")

    st.divider()
    st.header("🎯 Target: The 1 Lakh Club")
    invested = st.number_input("Current Investment (₹):", min_value=0)
    progress = min(invested / 100000, 1.0)
    st.progress(progress)
    if invested < 100000:
        st.info(f"You need ₹{100000 - invested:,} more to reach your goal!")
    else:
        st.balloons()
        st.success("Goal Reached! 🏆")