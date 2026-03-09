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

st.divider()
st.header("🏆 Daily Knowledge Challenge")

# 1. Initialize Score in Session State
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0

# 2. Define the Questions (Dictionary)
quiz_questions = {
    "Which data type is used for whole numbers?": "Integer",
    "What symbol is used for a List?": "[]",
    "Which function displays text in the console?": "print()",
    "What is the label in a Dictionary called?": "Key"
}

# 3. Create the UI
st.write(f"### Current Score: ⭐ {st.session_state.quiz_score}")

q_text = st.selectbox("Pick a question to answer:", list(quiz_questions.keys()))
user_ans = st.text_input("Your Answer (Case Sensitive):")

if st.button("Submit My Answer"):
    correct_ans = quiz_questions[q_text]
    
    if user_ans.strip().lower() == correct_ans.lower():
        st.session_state.quiz_score += 10
        st.balloons()
        st.success(f"🎯 Correct! You earned 10 points. Total: {st.session_state.quiz_score}")
    else:
        st.error(f"❌ Not quite. The correct answer was '{correct_ans}'. Try another one!")

if st.button("Reset My Score"):
    st.session_state.quiz_score = 0
    st.rerun()

# --- ADD THESE TO YOUR SIDEBAR TOPICS LIST ---
# topics = ["Variables", ..., "Lesson 8: Pandas", "Lesson 9: Data Viz", "Lesson 10: try-except", "Lesson 11: APIs"]

if selected_topic == "Lesson 8: Pandas":
    st.header("🐼 Lesson 8: Tables with Pandas")
    st.write("In AI, we don't use single variables; we use Tables (DataFrames).")
    
    # Real-Time Practice: Create a Watchlist
    data = {
        "Stock": ["NIFTY 50", "RELIANCE", "TCS"],
        "Price": [22100, 2900, 3800],
        "Action": ["Hold", "Buy", "Wait"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    st.info("💡 Pro Tip: Pandas is the 'Excel' of Python. AI models read data from these tables.")

elif selected_topic == "Lesson 9: Data Viz":
    st.header("📈 Lesson 9: Visualizing Market Trends")
    st.write("AI Engineers use charts to see patterns that humans miss.")
    
    # Real-Time Project: 5-Day Trend
    if st.button("Fetch 5-Day Trend"):
        prices = yf.Ticker("^NSEI").history(period="5d")['Close']
        st.line_chart(prices)
        st.success("You just built a live data visualizer!")

elif selected_topic == "Lesson 10: try-except":
    st.header("🛡️ Lesson 10: Making Apps Crash-Proof")
    st.write("What if a user types 'Ten' instead of '10'? Your app crashes unless you use `try-except`.")
    
    user_num = st.text_input("Type a number (try typing a word to see what happens):")
    if st.button("Convert to Number"):
        try:
            result = float(user_num)
            st.success(f"Success! {result} is a valid number.")
        except ValueError:
            st.error("⚠️ Crash Prevented! You typed text, but I handled it safely.")

elif selected_topic == "Lesson 11: APIs":
    st.header("🌐 Lesson 11: Connecting to the World (APIs)")
    st.write("APIs allow your app to talk to other computers to get Live Weather, Stock Prices, or News.")
    
    st.code("""
import yfinance as yf
# This is an API call to Yahoo Finance
data = yf.Ticker('^NSEI').info
    """, language="python")
    st.write("Every time you click 'Fetch Price' in this app, you are using an API!")

st.divider()
st.header("🧠 Master Quiz: Lessons 8-11")

# Use a dictionary to store new advanced questions
advanced_quiz = {
    "Which library handles DataFrames?": "Pandas",
    "Which block catches errors?": "except",
    "What does 'Viz' stand for?": "Visualization"
}

q_adv = st.selectbox("Challenge your brain:", list(advanced_quiz.keys()))
ans_adv = st.text_input("Enter Answer:")

if st.button("Verify Knowledge"):
    if ans_adv.strip().lower() == advanced_quiz[q_adv].lower():
        st.balloons()
        st.success("Correct! You are moving toward Intermediate Python.")
    else:
        st.warning(f"Keep learning! The answer is {advanced_quiz[q_adv]}")