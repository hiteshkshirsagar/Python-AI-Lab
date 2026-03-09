import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="Hitesh's AI Academy", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.header("👤 User Profile")
    user_data = {"Name": "Hitesh", "Target": "AI Engineer"}
    st.write(f"Welcome, **{user_data['Name']}**!")
    st.divider()
    topics = ["Variables", "Data Types", "Lists", "Dictionaries", "Loops", "Functions", "Lesson 8: Pandas", "Lesson 9: Data Viz"]
    selected_topic = st.selectbox("Choose a topic:", topics)

# --- MAIN APP ---
st.title("📋 Python & AI Learning Hub")
tab_learn, tab_practice, tab_ai = st.tabs(["📚 Learn Python", "🛠️ Practice Lab", "🤖 AI Tools"])

with tab_learn:
    st.header(f"📝 Lesson: {selected_topic}")
    
    if selected_topic == "Variables":
        st.write("### 📦 Concept: The Labeled Box")
        st.code("price = 22000", language="python")
        with st.expander("❓ Variables Q&A"):
            st.info("Variables store data so you can reuse it later!")

    elif selected_topic == "Data Types":
        st.write("### 🔢 Concept: Numbers vs Text")
        st.code("name = 'Nifty' # String\nprice = 22000 # Integer", language="python")
        with st.expander("❓ Data Types Q&A"):
            st.info("Strings are for text, Integers are for whole numbers.")

    elif selected_topic == "Lists":
        st.write("### 🛒 Concept: The Shopping Bag")
        st.code("watchlist = ['TCS', 'INFY']", language="python")
        with st.expander("❓ Lists Q&A"):
            st.info("Use `.append()` to add items to a list.")

    elif selected_topic == "Dictionaries":
        st.write("### 📖 Concept: The Key-Value Cupboard")
        st.code("stock = {'name': 'TCS', 'price': 3800}", language="python")
        with st.expander("❓ Dictionaries Q&A"):
            st.info("Dictionaries use labels (keys) to find data instantly.")

    elif selected_topic == "Loops":
        st.write("### 🔄 Concept: The Task Repeater")
        st.code("for s in stocks:\n    print(s)", language="python")
        with st.expander("❓ Loops Q&A"):
            st.info("Loops repeat actions for every item in a collection.")

    elif selected_topic == "Functions":
        st.write("### 📦 Concept: The Reusable Recipe")
        st.code("def greet():\n    print('Hello!')", language="python")
        with st.expander("❓ Functions Q&A"):
            st.info("Functions let you write code once and use it many times.")

    elif selected_topic == "Lesson 8: Pandas":
        st.write("### 🐼 Concept: Excel on Steroids")
        df = pd.DataFrame({"Stock": ["NIFTY", "TCS"], "Price": [22000, 3800]})
        st.dataframe(df)
        with st.expander("❓ Pandas Q&A"):
            st.info("DataFrames are tables used for Big Data and AI.")

    elif selected_topic == "Lesson 9: Data Viz":
        st.write("### 📈 Concept: Seeing the Pattern")
        if st.button("Show Nifty Chart"):
            data = yf.Ticker("^NSEI").history(period="5d")['Close']
            st.line_chart(data)
        with st.expander("❓ Data Viz Q&A"):
            st.info("Charts help spot trends faster than looking at numbers.")

# --- PRACTICE & AI TOOLS ---
with tab_practice:
    st.header("🏆 Quiz")
    if 'score' not in st.session_state: st.session_state.score = 0
    ans = st.text_input("Which type is for text?")
    if st.button("Submit"):
        if "string" in ans.lower():
            st.session_state.score += 10
            st.success(f"Correct! Score: {st.session_state.score}")

with tab_ai:
    st.header("🤖 Live Nifty")
    if st.button("Fetch Price"):
        p = yf.Ticker("^NSEI").history(period="1d")['Close'].iloc[-1]
        st.metric("Nifty 50", f"₹{p:,.2f}")

from fpdf import FPDF
import io

st.divider()
st.header("🎓 Final Certification")

# Logic: Only unlock if score is 50 or more
if st.session_state.quiz_score >= 50:
    st.success("🌟 Congratulations! You have earned your Python Basics Certificate.")
    
    # Create the PDF Function
    def create_certificate(name):
        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", 'B', 30)
        
        # Add a border
        pdf.rect(10, 10, 277, 190)
        
        # Certificate Text
        pdf.cell(0, 40, "CERTIFICATE OF COMPLETION", ln=True, align='C')
        pdf.set_font("Arial", '', 20)
        pdf.cell(0, 20, "This is proudly presented to", ln=True, align='C')
        pdf.set_font("Arial", 'I', 35)
        pdf.cell(0, 30, name, ln=True, align='C')
        pdf.set_font("Arial", '', 18)
        pdf.cell(0, 20, "For successfully mastering the Python & AI Foundations Course.", ln=True, align='C')
        
        # Return as bytes
        return pdf.output(dest='S').encode('latin-1')

    # Download Button
    cert_bytes = create_certificate(user_data['Name'])
    st.download_button(
        label="📥 Download My Certificate",
        data=cert_bytes,
        file_name="Python_Certificate.pdf",
        mime="application/pdf"
    )
else:
    st.warning(f"Keep practicing! You need **{50 - st.session_state.quiz_score}** more points to unlock your certificate.")