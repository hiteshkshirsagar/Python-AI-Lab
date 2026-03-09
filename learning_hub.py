import streamlit as st
import pandas as pd
import yfinance as yf
from fpdf import FPDF
import io

# --- 1. INITIALIZATION (The Safety Guard) ---
# This must be at the very top to prevent AttributeErrors
if 'score' not in st.session_state:
    st.session_state.score = 0

st.set_page_config(page_title="Hitesh's AI Academy", layout="wide")

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.header("👤 User Profile")
    user_data = {"Name": "Hitesh", "Target": "AI Engineer"}
    st.write(f"Welcome, **{user_data['Name']}**!")
    st.divider()
    
    # Complete Lesson List
    topics = [
        "Variables", "Data Types", "Lists", "Dictionaries", 
        "Loops", "Functions", "Lesson 8: Pandas", "Lesson 9: Data Viz",
        "Lesson 10: File Handling", "Lesson 11: APIs", 
        "Lesson 12: Classes & Objects", "Lesson 13: Intro to AI"
    ]
    selected_topic = st.selectbox("Choose a topic:", topics)
    st.metric("Your Learning Score", f"{st.session_state.score} pts")

# --- 3. MAIN APP STRUCTURE ---
st.title("📋 Python & AI Learning Hub")
tab_learn, tab_practice, tab_ai = st.tabs(["📚 Learn Python", "🛠️ Practice Lab", "🤖 AI Tools"])

# --- TAB 1: THE COMPREHENSIVE GUIDE ---
with tab_learn:
    st.header(f"📝 Lesson: {selected_topic}")
    
    if selected_topic == "Variables":
        st.write("### 📦 Concept: The Labeled Box")
        st.write("Think of a variable as a container. You give it a name so you can find your data later.")
        st.code("price = 22000", language="python")

    elif selected_topic == "Data Types":
        st.write("### 🔢 Concept: Numbers vs Text")
        st.write("Python handles math on 'Integers' and words in 'Strings'.")
        st.code("name = 'Nifty' # String\nprice = 22000 # Integer", language="python")

    elif selected_topic == "Lists":
        st.write("### 🛒 Concept: The Shopping Bag")
        st.write("Lists store multiple items in order. You access them by position (starting at 0).")
        st.code("watchlist = ['TCS', 'INFY']", language="python")

    elif selected_topic == "Dictionaries":
        st.write("### 📖 Concept: The Key-Value Cupboard")
        st.write("Dictionaries use 'Keys' (labels) to find 'Values' (data) instantly.")
        st.code("stock = {'name': 'TCS', 'price': 3800}", language="python")

    elif selected_topic == "Loops":
        st.write("### 🔄 Concept: The Task Repeater")
        st.write("Loops repeat code for every item in a list. Great for checking multiple stock prices.")
        st.code("for s in stocks:\n    print(s)", language="python")

    elif selected_topic == "Functions":
        st.write("### 📦 Concept: The Reusable Recipe")
        st.write("Functions are blocks of code you write once and call many times.")
        st.code("def greet():\n    print('Hello!')", language="python")

    elif selected_topic == "Lesson 8: Pandas":
        st.write("### 🐼 Concept: Excel on Steroids")
        st.write("Pandas handles Tables (DataFrames). This is where Data Engineering starts.")
        df = pd.DataFrame({"Stock": ["NIFTY", "TCS"], "Price": [22000, 3800]})
        st.dataframe(df)

    elif selected_topic == "Lesson 9: Data Viz":
        st.write("### 📈 Concept: Seeing the Pattern")
        st.write("Charts reveal trends that numbers hide. We use libraries like Plotly or Streamlit's native charts.")
        if st.button("Show Nifty 5-Day Chart"):
            data = yf.Ticker("^NSEI").history(period="5d")['Close']
            st.line_chart(data)

    elif selected_topic == "Lesson 10: File Handling":
        st.write("### 📄 Concept: Reading & Writing Data")
        st.write("AI Engineers often save data to files (CSV, TXT, PDF).")
        st.code("""
with open('data.txt', 'w') as f:
    f.write('Nifty is Bullish')
        """, language="python")

    elif selected_topic == "Lesson 11: APIs":
        st.write("### 🌐 Concept: Talking to other Computers")
        st.write("APIs (Application Programming Interfaces) let your app get live weather, news, or stock prices.")
        st.code("data = yf.Ticker('^NSEI').info # This is an API call", language="python")

    elif selected_topic == "Lesson 12: Classes & Objects":
        st.write("### 🏗️ Concept: The Blueprint (OOP)")
        st.write("A 'Class' is a blueprint for an object. For example, a 'Stock' class can create objects for TCS, INFY, etc.")
        st.code("""
class Stock:
    def __init__(self, name):
        self.name = name

s1 = Stock('TCS')
        """, language="python")

    elif selected_topic == "Lesson 13: Intro to AI":
        st.write("### 🤖 Concept: Teaching the Machine")
        st.write("AI isn't magic; it's math. We give data to a 'Model', and it learns to predict future prices.")
        st.info("Coming Soon: Building your first Linear Regression model!")

# --- TAB 2: PRACTICE & CERTIFICATION ---
with tab_practice:
    st.header("🏆 Certification Lab")
    
    # Simple Quiz logic to earn points
    st.subheader("Quick Quiz")
    q_dict = {
        "Which library is used for DataFrames?": "Pandas",
        "What does API stand for?": "Application Programming Interface",
        "Which block handles errors?": "try-except"
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

    if st.session_state.score >= 50:
        st.success("🌟 Congratulations! You have unlocked your Certificate.")
        
        def create_certificate(name):
            pdf = FPDF(orientation='L', unit='mm', format='A4')
            pdf.add_page()
            pdf.set_font("Arial", 'B', 30)
            pdf.rect(10, 10, 277, 190)
            pdf.cell(0, 40, "CERTIFICATE OF COMPLETION", ln=True, align='C')
            pdf.set_font("Arial", '', 20)
            pdf.cell(0, 20, "This is proudly presented to", ln=True, align='C')
            pdf.set_font("Arial", 'I', 35)
            pdf.cell(0, 30, name, ln=True, align='C')
            pdf.set_font("Arial", '', 18)
            pdf.cell(0, 20, "For successfully mastering the Python & AI Foundations Course.", ln=True, align='C')
            return pdf.output(dest='S').encode('latin-1')

        cert_bytes = create_certificate(user_data['Name'])
        st.download_button(label="📥 Download Certificate", data=cert_bytes, file_name="Certificate.pdf", mime="application/pdf")
    else:
        st.warning(f"You need 50 points to unlock your certificate. You currently have {st.session_state.score} points.")

# --- TAB 3: AI TOOLS ---
with tab_ai:
    st.header("🤖 Live Market Tools")
    if st.button("Fetch Live Nifty 50 Price"):
        p = yf.Ticker("^NSEI").history(period="1d")['Close'].iloc[-1]
        st.metric("Nifty 50", f"₹{p:,.2f}")
    
    st.divider()
    st.subheader("Market News Sentiment (Simulation)")
    st.info("Feature coming in Phase 2: AI will analyze news to tell you if it's Buy or Sell time!")