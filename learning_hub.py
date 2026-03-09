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
    st.header("🧭 Navigation Guide")
    topics = [
        "Variables", "Data Types", "Lists", "Dictionaries", 
        "Loops", "Functions", "Lesson 8: Pandas", 
        "Lesson 9: Data Viz", "Lesson 10: try-except", "Lesson 11: APIs"
    ]
    selected_topic = st.selectbox("Choose a topic to learn more:", topics)

# --- MAIN APP UI ---
st.title("📋 Python & AI Learning Hub")
tab_learn, tab_practice, tab_ai = st.tabs(["📚 Learn Python", "🛠️ Practice Lab", "🤖 AI & Trading Tools"])

# --- TAB 1: THE BEGINNER'S MANUAL ---
with tab_learn:
    st.header(f"📖 Lesson: {selected_topic}")
    
    # --- LESSON: VARIABLES ---
    if selected_topic == "Variables":
        st.write("### 📦 The 'Labelled Box' Concept")
        st.write("Imagine you have a box. You put a value inside and put a label on the outside. In Python, we call this a Variable.")
        st.code("nifty_price = 22100  # 'nifty_price' is the label, 22100 is inside", language="python")
        
        with st.expander("❓ Variables Q&A"):
            st.write("**Q: Why do we use variables?**")
            st.write("A: So we can reuse information later without typing it again!")

    # --- LESSON: DATA TYPES ---
    elif selected_topic == "Data Types":
        st.write("### 🔢 Numbers vs. Text")
        st.write("Python needs to know if it's looking at a number (to do math) or text (to show words).")
        st.code("""
age = 25          # Integer (Whole Number)
price = 2200.50   # Float (Decimal)
name = "Hitesh"   # String (Text)
is_bullish = True # Boolean (Yes/No)
        """, language="python")
        
        with st.expander("❓ Data Types Q&A"):
            st.write("**Q: Can you add a String and an Integer?**")
            st.write("A: No! Python will give an error. You can't add 'Apple' + 5.")

    # --- LESSON: LISTS ---
    elif selected_topic == "Lists":
        st.write("### 🛒 The Shopping Bag")
        st.write("A List holds many items in a specific order. Perfect for a Stock Watchlist!")
        st.code("watchlist = ['RELIANCE', 'TCS', 'INFY']", language="python")
        
        [Image of a Python list visualization showing indices starting from 0 and elements inside square brackets]
        
        with st.expander("❓ Lists Q&A"):
            ans = st.text_input("How do you add an item to a list? (Type the method name)")
            if st.button("Check Answer"):
                if ans.lower() == "append": st.success("Correct! `list.append()` adds to the end.")
                else: st.error("Try again! Hint: starts with 'a'.")

    # --- LESSON: DICTIONARIES ---
    elif selected_topic == "Dictionaries":
        st.write("### 📖 The Key-Value Cupboard")
        st.write("Dictionaries store data with a 'Key' (label) and a 'Value' (info). Like a real dictionary!")
        st.code("stock_info = {'name': 'TCS', 'price': 3800}", language="python")
        
        with st.expander("❓ Dictionaries Q&A"):
            st.write("**Q: What is the benefit over a list?**")
            st.write("A: You can find data instantly using the Key, instead of searching the whole list.")

    # --- LESSON: LOOPS ---
    elif selected_topic == "Loops":
        st.write("### 🔄 The Task Repeater")
        st.write("Loops do the boring work for you. Want to check 100 stock prices? Use a loop!")
        st.code("for stock in watchlist:\n    print(f'Checking {stock}...')", language="python")
        
        [Image of a Python for loop flow chart showing the iteration process]

        with st.expander("❓ Loops Q&A"):
            st.write("**Q: What is a 'for' loop?**")
            st.write("A: It iterates through a collection (like a list) and performs an action on each item.")

    # --- LESSON: FUNCTIONS ---
    elif selected_topic == "Functions":
        st.write("### 📦 The Recipe Box")
        st.write("A function is a block of code that only runs when you call it. Like a recipe you keep in a drawer.")
        st.code("def calculate_tax(salary):\n    return salary * 0.10", language="python")
        
        with st.expander("❓ Functions Q&A"):
            st.write("**Q: What does 'def' stand for?**")
            st.write("A: It stands for 'Define'. You are defining a new tool for Python to use.")

    # --- LESSON: PANDAS ---
    elif selected_topic == "Lesson 8: Pandas":
        st.write("### 🐼 DataFrames (Excel for Python)")
        st.write("Pandas is the most important library for AI Engineers. It handles large tables of data.")
        df = pd.DataFrame({"Stock": ["NIFTY 50", "TCS"], "Price": [22100, 3800]})
        st.table(df)
        
        [Image of a Python Pandas DataFrame structure showing rows and columns like an Excel sheet]
        
        with st.expander("❓ Pandas Q&A"):
            st.write("**Q: What is a DataFrame?**")
            st.write("A: It's a 2-dimensional data structure, like a table with rows and columns.")

    # --- LESSON: DATA VIZ ---
    elif selected_topic == "Lesson 9: Data Viz":
        st.write("### 📊 Visualizing Trends")
        st.write("Charts reveal secrets that numbers hide. We use visualization to spot market trends.")
        if st.button("Fetch Live Nifty Trend"):
            prices = yf.Ticker("^NSEI").history(period="5d")['Close']
            st.line_chart(prices)
            
        with st.expander("❓ Data Viz Q&A"):
            st.write("**Q: Why use charts in AI?**")
            st.write("A: To visualize patterns, outliers, and correlations in data.")

    # --- LESSON: TRY-EXCEPT ---
    elif selected_topic == "Lesson 10: try-except":
        st.write("### 🛡️ Crash-Proofing Your Code")
        st.write("Error handling ensures your app doesn't die if a user enters bad data.")
        st.code("try:\n    # code that might fail\nexcept:\n    # what to do if it fails", language="python")
        
        with st.expander("❓ Error Handling Q&A"):
            st.write("**Q: What is a 'ValueError'?**")
            st.write("A: It occurs when a function receives an argument of the right type but inappropriate value (like text when a number is expected).")

    # --- LESSON: APIs ---
    elif selected_topic == "Lesson 11: APIs":
        st.write("### 🌐 Connecting to the World")
        st.write("APIs allow your app to talk to other apps. We use the Yahoo Finance API for live prices.")
        
        with st.expander("❓ APIs Q&A"):
            st.write("**Q: What does API stand for?**")
            st.write("A: Application Programming Interface.")

# --- TAB 2: PRACTICE LAB ---
with tab_practice:
    st.header("🏆 Knowledge Challenges")
    
    if 'quiz_score' not in st.session_state: st.session_state.quiz_score = 0
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⭐ Basic Quiz")
        q_basics = {
            "Which type is for text?": "String",
            "What symbol for a List?": "[]",
            "Which function prints?": "print()"
        }
        pick_b = st.selectbox("Pick a question:", list(q_basics.keys()))