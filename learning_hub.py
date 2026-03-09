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
    selected_topic = st.selectbox("Choose a topic:", topics)
    st.metric("Your Learning Score", f"{st.session_state.score} pts")

# --- 3. MAIN APP STRUCTURE ---
st.title("📋 Python & AI Learning Hub")
tab_learn, tab_practice, tab_ai = st.tabs(["📚 Learn Python", "🛠️ Practice Lab", "🤖 AI Tools"])

with tab_learn:
    st.header(f"📝 Lesson: {selected_topic}")
    
    # ... (Keep your previous if/elif blocks for Lessons 1-13) ...
    # I'll show the new 4 lessons here:

    if selected_topic == "Lesson 14: Logic & Decisions":
        st.write("### ⚖️ Concept: How Computers Think")
        st.write("""
        Logic is the brain of your trading bot. We use `if`, `elif`, and `else` to tell Python 
        exactly what to do when certain conditions are met.
        """)
        
        st.code("""
price = 22100
if price > 22000:
    print("Market is Bullish")
elif price == 22000:
    print("Market is Neutral")
else:
    print("Market is Bearish")
        """, language="python")
        with st.expander("❓ Lesson 14 Q&A"):
            st.info("Q: What is the difference between = and ==?\nA: = assigns a value, while == checks if two values are equal.")

    elif selected_topic == "Lesson 15: List Comprehension":
        st.write("### ⚡ Concept: The Python Shortcut")
        st.write("""
        AI Engineers love writing clean code. List comprehension is a one-line way 
        to create or modify lists, making your data processing much faster.
        """)
        st.code("""
prices = [100, 200, 300]
# Add 10% tax to every price in one line
taxed_prices = [p * 1.1 for p in prices]
        """, language="python")
        with st.expander("❓ Lesson 15 Q&A"):
            st.info("Q: Is list comprehension faster than a regular for-loop?\nA: Yes! Python optimizes these one-liners to run faster in the background.")

    elif selected_topic == "Lesson 16: Modules & Packages":
        st.write("### 📦 Concept: Standing on the Shoulders of Giants")
        st.write("""
        You don't have to write everything from scratch. Modules (like `pandas` or `yfinance`) 
        are toolkits written by other experts that you can 'import' into your app.
        """)
        
        st.code("""
import math 
print(math.sqrt(16)) # Uses the pre-written square root tool
        """, language="python")
        with st.expander("❓ Lesson 16 Q&A"):
            st.info("Q: What is a 'Package'?\nA: A package is a collection of multiple modules. Think of it as a toolbox (Package) containing many tools (Modules).")

    elif selected_topic == "Lesson 17: Data Cleaning":
        st.write("### 🧹 Concept: Garbage In, Garbage Out")
        st.write("""
        Real-world data is messy (missing values, typos). Data Cleaning is the process 
        of fixing these errors before feeding data to an AI model.
        """)
        
        st.code("""
df.dropna() # Removes rows with empty values
df.fillna(0) # Fills empty values with zero
        """, language="python")
        with st.expander("❓ Lesson 17 Q&A"):
            st.info("Q: Why is cleaning data important for AI?\nA: If your data is wrong, your AI's predictions will be wrong. Clean data = Accurate AI.")

    # (For brevity, ensure you include the code for Lessons 1-13 from your previous version here)

# --- TAB 2: PRACTICE & CERTIFICATION ---
with tab_practice:
    st.header("🏆 Certification Lab")
    
    st.subheader("Quick Quiz")
    # Updated Quiz with more questions
    q_dict = {
        "Which library is used for DataFrames?": "Pandas",
        "What does API stand for?": "Application Programming Interface",
        "Which block handles errors?": "try-except",
        "Which symbol is used for 'equal to' comparison?": "==",
        "What command removes missing values in Pandas?": "dropna()"
    }
    
    q_sel = st.selectbox("Select a question to answer:", list(q_dict.keys()))
    ans = st.text_input("Your Answer:")
    
    if st.button("Submit Answer"):
        if ans.lower() == q_dict[q_sel].lower():
            st.session_state.score += 20
            st.success(f"Correct! +20 points. Total: {st.session_state.score}")
        else:
            st.error("Not quite! Try again.")

    st.divider()
    st.header("🎓 Final Certification")
    if st.session_state.score >= 100: # Increased requirement because we have more lessons!
        st.success("🌟 Congratulations! You have unlocked your Certificate.")
        # ... (Keep your existing PDF generation code here) ...
        cert_bytes = create_certificate(user_data['Name'])
        st.download_button(label="📥 Download Certificate", data=cert_bytes, file_name="Certificate.pdf", mime="application/pdf")
    else:
        st.warning(f"You need 100 points to unlock your certificate. Current: {st.session_state.score}")

# --- TAB 3: AI TOOLS ---
with tab_ai:
    # ... (Keep your existing Market Tools code here) ...
    st.header("🤖 Live Market Tools")
    if st.button("Fetch Live Nifty 50 Price"):
        p = yf.Ticker("^NSEI").history(period="1d")['Close'].iloc[-1]
        st.metric("Nifty 50", f"₹{p:,.2f}")