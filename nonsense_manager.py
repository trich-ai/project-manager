import streamlit as st
import requests, random, time

# 🔑 Replace with your actual key
NEWS_API_KEY = "5fd0ebe13bec448f8f3241d962b8a450"

st.set_page_config(page_title="Project Nonsense Manager Pro", page_icon="🧠", layout="centered")

# ---------- SESSION STATE ----------
if "mode" not in st.session_state:
    st.session_state.mode = "😏 Sarcastic"
if "phase" not in st.session_state:
    st.session_state.phase = "start"
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ---------- HEADER ----------
st.title("🧠 Project Nonsense Manager Pro")
st.caption("A quick mental reset for when work nonsense strikes.")

# ---------- INPUT ----------
user_input = st.text_area(
    "What's bugging you?",
    value=st.session_state.user_input,
    placeholder="Type the latest absurd task..."
)
st.session_state.user_input = user_input

# ---------- MODE ----------
st.session_state.mode = st.radio("Choose your tone:", ["😏 Sarcastic", "😌 Gentle"], horizontal=True)

sarcastic = [
    "Hey dum-dum, catastrophizing won’t fix stupid.",
    "Relax, you’re not defusing a bomb.",
    "Congratulations! You’ve unlocked Level 10 Irritation.",
    "Breaking news: you’re overqualified for nonsense.",
    "The system may be broken, but you’re still functioning.",
]

gentle = [
    "You’ve handled tougher days — breathe.",
    "It’s just noise, not danger.",
    "You don’t need to feel fine to be fine.",
    "This moment will pass; you’ve proven that before.",
    "Let’s reset, one deep breath at a time.",
]

# ---------- FUNCTIONS ----------
def get_headlines():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=15&apiKey={NEWS_API_KEY}"
        news = requests.get(url, timeout=8).json()
        articles = random.sample(news.get("articles", []), k=min(3, len(news.get("articles", []))))
        st.markdown("### 🗞️ Today's Distractions")
        for a in articles:
            st.markdown(f"**{a.get('title','(no title)')}**")
            if a.get("url"):
                st.markdown(f"[Read more →]({a['url']})")
            if a.get("source") and a["source"].get("name"):
                st.caption(f"Source: {a['source']['name']}")
            st.divider()
    except Exception:
        st.info("Couldn’t fetch headlines — maybe the world finally calmed down?")

# ---------- PHASE HANDLING ----------
if st.session_state.phase == "start":
    if st.button("Reframe Me 🔁"):
        st.session_state.phase = "reframe"
        st.rerun()

elif st.session_state.phase == "reframe":
    st.subheader(random.choice(sarcastic if st.session_state.mode == "😏 Sarcastic" else gentle))
    get_headlines()

    st.markdown("### Your reaction?")
    col1, col2 = st.columns(2)
    if col1.button("😌 That Helped"):
        st.session_state.phase = "helped_message"
        st.rerun()
    if col2.button("😠 Not So Fast"):
        st.session_state.phase = "more_message"
        st.rerun()

elif st.session_state.phase == "helped_message":
    st.success(random.choice([
        "You learned a valuable lesson. 💪",
        "Goal achieved — resilience +1.",
        "Nice! Emotional agility unlocked.",
        "You handled that like a pro.",
        "Peace mode activated. 🧘"
    ]))
    time.sleep(2)
    st.session_state.user_input = ""
    st.session_state.phase = "start"
    st.rerun()

elif st.session_state.phase == "more_message":
    st.warning(random.choice([
        "Someone needs more headlines!",
        "Recalibrating your nonsense tolerance...",
        "Fetching extra chaos for context...",
        "Brace yourself — fresh absurdity incoming!"
    ]))
    time.sleep(2)
    st.session_state.phase = "reframe"
    st.rerun()

st.caption("No data saved — just vent, laugh, and move on.")
