import streamlit as st
import time

# Бетті баптау
st.set_page_config(page_title="Chemistry Lab AI", layout="wide")

# ---------------- CSS АНИМАЦИЯ (Пробиркалар) ----------------
st.markdown("""
<style>
    .lab-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
        gap: 50px;
        background-color: #1e1e1e;
        border-radius: 15px;
        padding: 20px;
    }
    .tube {
        width: 35px;
        height: 110px;
        border: 3px solid #ffffff;
        border-radius: 0 0 20px 20px;
        position: relative;
    }
    .liquid {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 70%;
        border-radius: 0 0 17px 17px;
    }
    /* Құю анимациясы */
    @keyframes pour-left {
        0% { transform: rotate(0deg); }
        50% { transform: rotate(45deg) translate(20px, -15px); }
        100% { transform: rotate(0deg); }
    }
    @keyframes pour-right {
        0% { transform: rotate(0deg); }
        50% { transform: rotate(-45deg) translate(-20px, -15px); }
        100% { transform: rotate(0deg); }
    }
    .pouring-left { animation: pour-left 2s ease-in-out infinite; }
    .pouring-right { animation: pour-right 2s ease-in-out infinite; }
    .main-tube { width: 50px; height: 130px; border-width: 4px; }
</style>
""", unsafe_allow_html=True)

# ---------------- ДЕРЕКТЕРДІ ДАЙЫНДАУ ----------------
# Барлық 34 сабақты толтыру
lesson_data = {}
topics = [
    "Сапалық реакция ұғымы", "Функционалдық топтар", "Қауіпсіздік ережелері", 
    "Қанықпаған байланыс (Алкендер)", "Алкандар қасиеті", "Арендер (Бензол)", 
    "Бір атомды спирттер", "Көп атомды спирттер", "Фенолдар",
    "Альдегидтер", "Кетондар", "Карбон қышқылдары"
]

for i in range(1, 35):
    topic_name = topics[i-1] if i-1 < len(topics) else f"Органикалық химия №{i}"
    lesson_data[i] = {
        "topic": topic_name,
        "theory": f"Бұл {topic_name} тақырыбы бойынша негізгі теориялық мәліметтер.",
        "lab": ("Реактив А + Реактив Б", "Түстің өзгеруі байқалады", "Функционалдық топ дәлелденді"),
        "test": [(f"{topic_name} бойынша сұрақ {j+1}", ["А жауабы", "Б жауабы", "В жауабы"], 0) for j in range(10)]
    }

# ---------------- SIDEBAR ----------------
st.sidebar.title("📘 34 САБАҚТЫҚ КУРС")
lesson_selected = st.sidebar.selectbox("Сабақты таңдаңыз", [f"{i}-сабақ" for i in range(1, 35)])
mode = st.sidebar.radio("Режим", ["Оқушы", "Мұғалім"])

lesson_number = int(lesson_selected.split("-")[0])
data = lesson_data[lesson_number]

# ---------------- UI ФУНКЦИЯЛАРЫ ----------------
def show_pouring_animation(observation):
    st.markdown(f"""
    <div class="lab-container">
        <div class="tube pouring-left"><div class="liquid" style="background: #3498db;"></div></div>
        <div class="tube main-tube"><div class="liquid" style="background: #e74c3c; height: 30%;"></div></div>
        <div class="tube pouring-right"><div class="liquid" style="background: #f1c40f;"></div></div>
    </div>
    <p style="text-align: center; margin-top: 15px;">🔍 <b>Бақылау:</b> {observation}</p>
    """, unsafe_allow_html=True)

# ---------------- НЕГІЗГІ БЕТ ----------------
st.title(f"🧪 {data['topic']}")
st.caption(f"Ағымдағы сабақ: {lesson_number} | Пайдаланушы: {mode}")

tab1, tab2, tab3 = st.tabs(["📖 Теория", "🔬 Зертхана", "📝 Тест & AI"])

with tab1:
    st.info(data["theory"])
    # Сурет тегін кодтан тыс шығардық
    st.write("Төмендегі суретте функционалдық топтардың құрылымы көрсетілген:")
    st.write("")

with tab2:
    st.subheader("Тәжірибе жасау")
    st.write(f"**Керекті заттар:** {data['lab'][0]}")
    if st.button("Реакцияны бастау"):
        show_pouring_animation(data['lab'][1])
        st.success(f"Қорытынды: {data['lab'][2]}")
    st.write("")

with tab3:
    st.subheader("Тест (10 сұрақ)")
    score = 0
    for idx, (q, opts, correct) in enumerate(data["test"]):
        ans = st.radio(q, opts, key=f"L{lesson_number}_Q{idx}", index=None)
        if ans is not None and opts.index(ans) == correct:
            score += 1
    
    # Ұпай көрсету
    if score == 0:
        st.error(f"📊 Нәтиже: {score} / 10")
    elif score < 8:
        st.warning(f"📊 Нәтиже: {score} / 10")
    else:
        st.success(f"📊 Нәтиже: {score} / 10")

st.markdown("---")
st.caption("©️ Chemistry + AI | Streamlit оқу платформасы")
