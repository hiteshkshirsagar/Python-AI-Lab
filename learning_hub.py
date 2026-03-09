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
    # All lessons added here
    topics = [
        "Variables", "Data Types", "Lists", "Dictionaries", 
        "Loops", "Functions", "Lesson 8: Pandas", 
        "Lesson 9: Data Viz", "Lesson 10: try-except", "Lesson 11: APIs"
    ]
    selected_topic = st.selectbox("Choose a topic to learn more:", topics)

# --- MAIN APP UI ---
st.title("📋 Python & AI Learning Hub")

tab_learn, tab_practice, tab_ai = st.tabs(["📚 Learn Python", "🛠️ Practice Lab", "🤖 AI & Trading Tools"])

# --- TAB 1: LEARNING CONTENT ---
with tab_learn:
    st.header(f"📝 Topic: {selected_topic}")
    
    # Logic to show ONLY the selected lesson
    if selected_topic == "Variables":
        st.write("A **Variable** is a labeled box for data.")
        st.code("name = 'Hitesh'\nsalary = 12", language="python")
        
    elif selected_topic == "Data Types":
        st.write("Python handles Numbers (int/float) and Text (strings) differently.")
        st.code("age = 25  # Integer\nprice = 22000.50 # Float\nname = 'Nifty' # String", language="python")

    elif selected_topic == "Lists":
        st.write("A **List** is a shopping bag of items.")
        st.code("my_portfolio = ['Tata Small Cap', 'Nifty 50']", language="python")
        st.info("💡 Pro Tip: Use .append() to add items to your list!")

    elif selected_topic == "Dictionaries":
        st.write("A **Dictionary** uses 'Keys' (labels) and 'Values' (data).")
        st.code("stock = {'name': 'TCS', 'price': 3800}", language="python")

    elif selected_topic == "Loops":
        st.write("Loops do the same task over and over—like checking 50 stock prices at once!")
        st.code("for price in nifty_prices:\n    print(price)", language="python")

    elif selected_topic == "Functions":
        st.write("A **Function** is a recipe you can reuse.")
        st.code("def calculate_tax(income):\n    return income * 0.1", language="python")

    elif selected_topic == "Lesson 8: Pandas":
        st.write("In AI, we use Tables (DataFrames) to manage large amounts of data.")
        data = {"Stock": ["NIFTY 50", "RELIANCE", "TCS"], "Price": [22100, 2900, 3800]}
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        st.info("💡 Pandas is like Excel for Python.")

    elif selected_topic == "Lesson 9: Data Viz":
        st.write("AI Engineers use charts to see patterns humans miss.")
        if st.button("Fetch 5-Day Trend Chart"):
            prices = yf.Ticker("^NSEI").history(period="5d")['Close']
            st.line_chart(prices)

    elif selected_topic == "Lesson 10: try-except":
        st.write("Use `try-except` to stop your app from crashing when users make mistakes.")
        user_num = st.text_input("Type a number (or a word to test the error catch):")
        if st.button("Check Number"):
            try:
                st.success(f"Result: {float(user_num)}")
            except ValueError:
                st.error("⚠️ Error Caught! You entered text instead of a number.")

    elif selected_topic == "Lesson 11: APIs":
        st.write("APIs let your app talk to other systems (like Yahoo Finance).")
        st.code("data = yf.Ticker('^NSEI').info", language="python")

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
    st.header("🏆 Knowledge Challenges")
    
    # --- QUIZ 1: BASICS ---
    st.subheader("⭐ Basics Quiz")
    if 'quiz_score' not in st.session_state: st.session_state.quiz_score = 0
    
    quiz_questions = {
        "Which data type is used for whole numbers?": "Integer",
        "What symbol is used for a List?": "[]",
        "Which function displays text?": "print()"
    }
    q_text = st.selectbox("Pick a question:", list(quiz_questions.keys()))
    user_ans = st.text_input("Your Answer:")
    
    if st.button("Submit Basic Answer"):
        if user_ans.strip().lower() == quiz_questions[q_text].lower():
            st.session_state.quiz_score += 10
            st.success("🎯 Correct! +10 Points")
        else:
            st.error("❌ Try again!")
    st.write(f"**Total Score: {st.session_state.quiz_score}**")

    st.divider()
    
    # --- QUIZ 2: ADVANCED ---
    st.subheader("🧠 Master Quiz (Lessons 8-11)")
    advanced_quiz = {
        "Which library handles DataFrames?": "Pandas",
        "Which block catches errors?": "except"
    }
    q_adv = st.selectbox("Pick Advanced Question:", list(advanced_quiz.keys()))
    ans_adv = st.text_input("Enter Advanced Answer:")
    if st.button("Verify Master Knowledge"):
        if ans_adv.strip().lower() == advanced_quiz[q_adv].lower():
            st.balloons()
            st.success("🔥 Master level reached!")

# --- TAB 3: AI & TRADING TOOLS ---
with tab_ai:
    st.header("🤖 AI & Market Dashboard")
    
    # Market Analyzer
    st.subheader("📊 Market Trend Analyzer")
    price_input = st.text_input("Enter last 5 Nifty prices (comma separated):", "22100, 22050, 22200, 21900, 22300")
    try:
        price_list = [float(p.strip()) for p in price_input.split(",")]
        if st.button("Analyze Trend"):
            avg = sum(price_list) / len(price_list)
            st.metric("Avg Price", f"₹{avg:,.2f}")
            if price_list[-1] > avg: st.success("BULLISH Trend 🚀")
            else: st.warning("BEARISH Trend ⚠️")
    except: st.error("Please enter numbers only.")

    st.divider()
    
    # Live Tracker
    st.subheader("📈 Live Nifty 50 Tracker")
    if st.button("Fetch Current Price"):
        try:
            price = yf.Ticker("^NSEI").history(period="1d")['Close'].iloc[-1]
            st.metric("Live Nifty 50", f"₹{price:,.2f}")
        except: st.error("Could not fetch data.")

    st.divider()
    
    # Goal Tracker
    st.subheader("🎯 Goal: 1 Lakh Club")
    invested = st.number_input("Current Investment (₹):", min_value=0)
    st.progress(min(invested / 100000, 1.0))
    if invested < 100000: st.info(f"Need ₹{100000 - invested:,} more!")
    else: st.success("Goal Achieved! 🏆")