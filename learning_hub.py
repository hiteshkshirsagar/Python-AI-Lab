import streamlit as st
import pandas as pd
import yfinance as yf
from fpdf import FPDF
import io

# --- 1. INITIALIZATION ---
if 'score' not in st.session_state:
    st.session_state.score = 0

st.set_page_config(page_title="Hitesh's AI Academy", layout="wide")

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.header("👤 User Profile")
    user_data = {"Name": "Hitesh", "Target": "AI Engineer"}
    st.write(f"Welcome, **{user_data['Name']}**!")
    st.divider()
    
    topics = [
        "Variables", "Data Types", "Lists", "Dictionaries", 
        "Loops", "Functions", "Lesson 8: Pandas", "Lesson 9: Data Viz",
        "Lesson 10: File Handling", "Lesson 11: APIs", 
        "Lesson 12: Classes & Objects", "Lesson 13: Intro to AI",
        "Lesson 14: Logic & Decisions", "Lesson 15: List Comprehension",
        "Lesson 16: Modules & Packages", "Lesson 17: Data Cleaning"
    ]
    selected_topic = st.selectbox("📖 Choose a Lesson:", topics)
    st.metric("Your Learning Score", f"{st.session_state.score} pts")

# --- 3. MAIN APP STRUCTURE ---
st.title("📋 Python & AI Learning Hub")
tab_learn, tab_practice, tab_ai, tab_glossary = st.tabs(["📚 Learn", "🛠️ Practice", "🤖 AI Tools", "📖 Glossary"])

# --- TAB 1: THE COMPLETE MANUAL ---
with tab_learn:
    st.header(f"📝 Topic: {selected_topic}")
    st.divider()

    if selected_topic == "Variables":
        st.write("### 📦 The Concept: The Labeled Box")
        st.write("""
        In Python, a **Variable** is like a storage box. You put data inside and slap a label (name) on it. 
        Instead of remembering the number `22123.45`, you just remember the name `nifty_price`.
        """)
        
        st.code("nifty_price = 22123\n# Now you can use 'nifty_price' anywhere!", language="python")
        with st.expander("❓ Lesson Q&A"):
            st.write("**Q: Why use variables?**")
            st.info("A: They make code readable. 'nifty_price' is easier to understand than a random number.")

    elif selected_topic == "Data Types":
        st.write("### 🔢 The Concept: Numbers vs. Text")
        st.write("""
        Computers see `10` (a number) and `"10"` (text) differently. You can't add a name to a number! 
        - **Integer (int):** Whole numbers like 5, 100.
        - **Float:** Decimals like 22.50.
        - **String (str):** Text inside quotes like 'Nifty'.
        """)
        
        st.code("age = 25  # int\nprice = 22.5  # float\nname = 'Hitesh' # str", language="python")

    elif selected_topic == "Lists":
        st.write("### 🛒 The Concept: The Shopping Bag")
        st.write("""
        A **List** is a collection of items kept in order. It's like your stock watchlist.
        """)
        
        st.code("watchlist = ['TCS', 'INFY', 'RELIANCE']\n# To get the first item: watchlist[0]", language="python")
        with st.expander("❓ Lesson Q&A"):
            st.write("**Q: How do I add a new stock?**")
            st.info("A: Use `watchlist.append('NEW_STOCK')`.")

    elif selected_topic == "Dictionaries":
        st.write("### 📖 The Concept: The Key-Value Cupboard")
        st.write("""
        A **Dictionary** stores data in pairs: a **Key** (label) and a **Value** (info). 
        It's like looking up a word in a real dictionary.
        """)
        
        st.code("stock_info = {'name': 'TCS', 'price': 3800}\n# Get price: stock_info['price']", language="python")

    elif selected_topic == "Lesson 8: Pandas":
        st.write("### 🐼 The Concept: Excel on Steroids")
        st.write("""
        **Pandas** is the most important library for AI Engineers. It handles **DataFrames** (tables). 
        It allows you to process 1,000,000 rows of stock data in a split second.
        """)
        
        df_ex = pd.DataFrame({"Stock": ["NIFTY", "RELIANCE"], "Price": [22000, 2900]})
        st.table(df_ex)

    elif selected_topic == "Lesson 14: Logic & Decisions":
        st.write("### ⚖️ The Concept: How Computers Decide")
        st.write("""
        AI and Trading bots use logic to make choices. If a condition is met, do action A. 
        If not, do action B.
        """)
        
        st.code("if price > 22000:\n    print('Bullish!')\nelse:\n    print('Bearish')", language="python")

    elif selected_topic == "Lesson 17: Data Cleaning":
        st.write("### 🧹 The Concept: Garbage In, Garbage Out")
        st.write("""
        AI models fail if the data is dirty (missing values, typos). 
        **Data Cleaning** is the process of fixing your data before the AI sees it.
        """)
        
        st.code("df.dropna() # Delete missing data\ndf.fillna(0) # Fill gaps with 0", language="python")

    # (Note: I have kept space for all 17 lessons here)
    else:
        st.info("This lesson is being prepared. Try 'Variables', 'Lists', or 'Pandas'!")

# --- TAB 2: PRACTICE ---
with tab_practice:
    st.header("🏆 Certification Lab")
    q_sel = st.selectbox("Pick a Question:", ["Which type is for text?", "What library handles Tables?"])
    ans = st.text_input("Your Answer:")
    if st.button("Submit"):
        if ans.lower() in ["string", "pandas"]:
            st.session_state.score += 20
            st.success("Correct! Points updated.")
        else:
            st.error("Try again!")

# --- TAB 3: AI TOOLS ---
with tab_ai:
    st.header("🤖 Live Market Tracker")
    if st.button("Fetch Nifty 50"):
        p = yf.Ticker("^NSEI").history(period="1d")['Close'].iloc[-1]
        st.metric("Nifty 50", f"₹{p:,.2f}")

# --- TAB 4: GLOSSARY ---
with tab_glossary:
    st.header("📖 AI Engineer's Glossary")
    search = st.text_input("Search term (e.g. API, Loop):")
    glossary = {"API": "A bridge between apps.", "Loop": "Repeat code.", "Pandas": "Table manager."}
    if search in glossary:
        st.write(f"**{search}**: {glossary[search]}")