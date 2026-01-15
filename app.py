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
    }
    .tube {
        width: 30px;
        height: 100px;
        border: 3px solid #fff;
        border-radius: 0 0 15px 15px;
        position: relative;
        background: rgba(255,255,255,0.1);
    }
    .liquid {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 70%;
        border-radius: 0 0 12px 12px;
        transition: all 1s;
    }
    /* Анимация эффектілері */
    @keyframes pour-left {
        0% { transform: rotate(0deg); }
        50% { transform: rotate(45deg) translate(20px, -20px); }
        100% { transform: rotate(0deg); }
    }
    @keyframes pour-right {
        0% { transform: rotate(0deg); }
        50% { transform: rotate(-45deg) translate(-20px, -20px); }
        100% { transform: rotate(0deg); }
    }
    .pouring-left { animation: pour-left 2s infinite; }
    .pouring-right { animation: pour-right 2s infinite; }
    
    .main-tube { width: 45px; height: 120px; border-width: 4px; }
</style>
""", unsafe_allow_html=True)

# ---------------- ТЕСТ ЖӘНЕ САБАҚТАР ДЕРЕКҚОРЫ ----------------
# Барлық 34 сабақты циклмен толтыру (үлгі ретінде)
lesson_data = {}
topics = [
    "Сапалық реакция ұғымы", "Функционалдық топтар", "Қауіпсіздік ережелері", 
    "Қанықпаған байланыс", "Алкандар қасиеті", "Арендерді анықтау", 
    "Спирттердің тотығуы", "Көп атомды спирттер", "Фенолдың сапалық реакциясы",
    "Альдегидтер: Күміс айна", "Кетондарды анықтау", "Карбон қышқылдары"
    # ... 34-ке дейін жалғасады
]

for i in range(1, 35):
    topic_name = topics[i-1] if i-1 < len(topics) else f"Органикалық қосылыстар №{i}"
    lesson_data[i] = {
        "topic": topic_name,
        "theory": f"{topic_name} бойынша теориялық мәліметтер мен химиялық теңдеулер.",
        "lab": ("Реактив А + Реактив Б", "Түстің өзгеруі немесе тұнба", "Функционалдық топ анықталды"),
        "ai": f"{topic_name} тақырыбындағы AI тапсырмасы: Реакция өнімін болжаңыз.",
        "test": [
            (f"{topic_name} бойынша сұрақ {j+1}?", ["Жауап А", "Жауап Б", "Жауап В"], 0) for j in range(10)
        ]
    }

# ---------------- SIDEBAR ----------------
st.sidebar.title("📘 34 САБАҚТЫҚ КУРС")
lesson_selected = st.sidebar.selectbox("Сабақты таңдаңыз", [f"{i}-сабақ" for i in range(1, 35)])
mode = st.sidebar.radio("Режим", ["Оқушы", "Мұғалім"])

# ---------------- UI ФУНКЦИЯЛАРЫ ----------------
def show_pouring_animation(observation):
    st.subheader("🔬 Зертханалық симуляция")
    
    # Анимацияны көрсету үшін HTML
    st.markdown(f"""
    <div class="lab-container">
        <div class="tube pouring-left"><div class="liquid" style="background: #3498db;"></div></div>
        <div class="tube main-tube"><div class="liquid" style="background: #e74c3c; height: 40%;"></div></div>
        <div class="tube pouring-right"><div class="liquid" style="background: #f1c40f;"></div></div>
    </div>
    <p style="text-align: center; margin-top: 20px;"><b>Реакция барысы:</b> {observation}</p>
    """, unsafe_allow_html=True)
    
    progress_bar = st.progress(0)
    for i in range(101):
        time.sleep(0.01)
        progress_bar.progress(i)

def show_test(test_items, lesson_id):
    st.subheader("📝 Телімдік тест (10 сұрақ)")
    score = 0
    # session_state қолдану арқылы жауаптарды сақтаймыз
    for idx, (q, opts, correct) in enumerate(test_items):
        key = f"lesson_{lesson_id}_q_{idx}"
        ans = st.radio(f"{idx+1}. {q}", opts, key=key, index=None)
        if ans is not None and opts.index(ans) == correct:
            score += 1
    
    st.divider()
    if score == 0:
        st.error(f"📊 Нәтиже: {score} / {len(test_items)}")
    elif score < 7:
        st.warning(f"📊 Нәтиже: {score} / {len(test_items)}")
    else:
        st.success(f"📊 Нәтиже: {score} / {len(test_items)}")

# ---------------- НЕГІЗГІ БЕТ ----------------
lesson_number = int(lesson_selected.split("-")[0])
data = lesson_data[lesson_number]

st.title(f"🧪 {data['topic']}")
st.info(f"Сабақ: {lesson_number} | Режим: {mode}")

tab1, tab2, tab3 = st.tabs(["📖 Теория", "🔬 Эксперимент", "📝 Тест & AI"])

with tab1:
    st.write(data["theory"])
    

[Image of chemical structure of organic functional groups]


with tab2:
    st.write(f"**Қолданылатын заттар:** {data['lab'][0]}")
    if st.button("Реакцияны бастау"):
        show_pouring_animation(data['lab'][1])
        st.success(f"Қорытынды: {data['lab'][2]}")
    

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        show_test(data["test"], lesson_number)
    with col2:
        st.subheader("🤖 AI Тапсырма")
        st.write(data["ai"])
        st.text_area("Жауабыңызды осында жазыңыз...")
        if st.button("Тексеру"):
            st.write("AI жауапты қабылдады. Жарайсың!")

st.markdown("---")
st.caption("©️ Chemistry + AI | Streamlit оқу платформасы")
