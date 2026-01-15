import streamlit as st
import time

st.set_page_config(page_title="Органикалық функционалдық топтардың сапалық реакциялары", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📘 34 САБАҚ")
lessons = [f"{i}-сабақ" for i in range(1, 35)]
lesson_selected = st.sidebar.selectbox("Сабақты таңдаңыз", lessons)
st.sidebar.markdown("---")
mode = st.sidebar.radio("Режим", ["Оқушы", "Мұғалім"])

st.title("🧪 Органикалық функционалдық топтардың сапалық реакциялары")
st.caption(f"Таңдалған: {lesson_selected} | Режим: {mode}")

# ---------------- DATA ----------------
lesson_data = {
    1: {"topic": "Сапалық реакция ұғымы",
        "theory": "Сапалық реакция – функционалдық топты реакция белгісі арқылы анықтау әдісі.",
        "lab": ("Br₂ (Бром суы)", "Түс қызыл-қоңырдан түссізге өзгереді", "Алкен (қанықпаған байланыс) бар екенін көрсетеді"),
        "colors": ["#A52A2A", "#FFFFFF"], # Қоңырдан түссізге
        "ai": "Берілген қосылыстың функционалдық тобын AI арқылы болжа",
        "test": [
            ("Br₂ нені анықтайды?", ["Алкан", "Алкен", "Спирт"], 1),
            ("Сапалық реакция мақсаты?", ["Белгі", "Баға", "Иіс"], 0),
            ("Қай қосылыс қос байланысқа ие?", ["CH₄", "C₂H₄", "C₂H₆"], 1),
            ("Br₂ реакциясы қалай жүреді?", ["Түссіздену", "Қызару", "Көк түске өзгеру"], 0),
            ("Қос байланыс белгісі?", ["Br₂", "KMnO₄", "NaOH"], 0),
            ("Алкендердің реакциясы?", ["Қанықпағандық", "Сілтілік", "Қышқылдық"], 0),
            ("Түссіздену байқалады ма?", ["Иә", "Жоқ", "Тек қышқылда"], 0),
            ("Сапалық реакция түрі?", ["Функционалдық топты анықтау", "Бағалау", "Талдау"], 0),
            ("Қай реактив қолданылды?", ["Br₂", "HCl", "CuSO₄"], 0),
            ("Қай қосылыс реакцияға түссізденді?", ["C₂H₄", "CH₄", "C₂H₆"], 0)
        ]
    },
    2: {"topic": "Функционалдық топтар",
        "theory": "Органикалық қосылыстар функционалдық топтар арқылы жіктеледі.",
        "lab": ("Cu(OH)₂ (Мыс гидроксиді)", "Көк түсті ерітінді ашық көк/күлгінге ауысады", "Көп атомды спирт бар екенін көрсетеді"),
        "colors": ["#add8e6", "#0000ff"], # Ашық көктен қанық көкке
        "ai": "Берілген формуладан топты анықта",
        "test": [
            ("–OH қай топ?", ["Амин", "Спирт", "Қышқыл"], 1),
            ("Спирттің белгісі?", ["Cu(OH)₂", "Br₂", "KMnO₄"], 0),
            ("Функционалдық топ не үшін керек?", ["Жіктеу", "Түс", "Иіс"], 0),
            ("Көбіне қандай реакция?", ["Сапалық", "Сандық", "Теориялық"], 0),
            ("–COOH қай топ?", ["Спирт", "Қышқыл", "Амин"], 1),
            ("–NH₂ қай топ?", ["Амин", "Қышқыл", "Спирт"], 0),
            ("–CHO қай топ?", ["Альдегид", "Кетон", "Спирт"], 0),
            ("Функционалдық топ қандай?", ["–OH", "–CH₃", "–H"], 0),
            ("Сапалық реакцияны не үшін қолданамыз?", ["Белгі", "Иіс", "Түс"], 0),
            ("Топты анықтаудың реактиві?", ["Cu(OH)₂", "Br₂", "HCl"], 0)
        ]
    }
}

# ---------------- UI BLOCKS ----------------
def show_theory(text):
    st.subheader("📖 Теория")
    st.info(text)

def show_lab(reagents, observation, conclusion, colors=["#3498db", "#e74c3c"]):
    st.subheader("🔬 Зертханалық жұмыс")
    
    # CSS Анимация стилі
    st.markdown("""
    <style>
    .test-tube-container { display: flex; justify-content: center; padding: 20px; }
    .test-tube {
        width: 50px; height: 180px; border: 4px solid #F0F2F6;
        border-bottom-left-radius: 25px; border-bottom-right-radius: 25px;
        position: relative; overflow: hidden; background: rgba(255,255,255,0.1);
    }
    .liquid {
        position: absolute; bottom: 0; width: 100%; height: 0%;
        transition: all 0.5s ease;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    
    with col1:
        tube_placeholder = st.empty()
        # Бастапқы бос пробирка
        tube_placeholder.markdown('<div class="test-tube-container"><div class="test-tube"><div class="liquid"></div></div></div>', unsafe_allow_html=True)

    with col2:
        st.write(f"**Реактивтер:** {reagents}")
        if st.button("🧪 Реакцияны бастау"):
            progress_bar = st.progress(0)
            status = st.empty()
            
            for i in range(1, 101):
                time.sleep(0.02)
                progress_bar.progress(i)
                
                if i < 40:
                    status.text("Реактив қосылуда...")
                    tube_placeholder.markdown(f'<div class="test-tube-container"><div class="test-tube"><div class="liquid" style="height: 50%; background-color: {colors[0]};"></div></div></div>', unsafe_allow_html=True)
                elif i < 80:
                    status.text(f"Бақылау: {observation}")
                    tube_placeholder.markdown(f'<div class="test-tube-container"><div class="test-tube"><div class="liquid" style="height: 70%; background-color: {colors[1]}; shadow: inset 0 0 10px rgba(0,0,0,0.2);"></div></div></div>', unsafe_allow_html=True)
                else:
                    status.success(f"Қорытынды: {conclusion}")
                    tube_placeholder.markdown(f'<div class="test-tube-container"><div class="test-tube"><div class="liquid" style="height: 85%; background-color: {colors[1]};"></div></div></div>', unsafe_allow_html=True)

def show_ai(task):
    st.subheader("🤖 AI-симуляция тапсырмасы")
    st.text_area("AI жауабы / ойыңды жаз", key="ai_input")
    if st.button("AI-дан үлгі жауап"):
        st.success(task)

def show_test(test_items):
    st.subheader("📝 Тест")
    score = 0
    for idx, (q, opts, correct) in enumerate(test_items):
        ans = st.radio(f"{idx+1}. {q}", opts, key=f"q{idx}_{lesson_selected}")
        if ans and opts.index(ans) == correct:
            score += 1
    st.write(f"✅ Ұпай: {score} / {len(test_items)}")

# ---------------- CONTENT ----------------
lesson_number = int(lesson_selected.split("-")[0])
data = lesson_data.get(lesson_number, None)

if data:
    st.header(f"{lesson_number}-сабақ. {data['topic']}")
    show_theory(data["theory"])
    # lab мәліметтеріне түстерді қосып жібереміз
    show_lab(data["lab"][0], data["lab"][1], data["lab"][2], data.get("colors", ["#3498db", "#e74c3c"]))
    show_ai(data["ai"])
    show_test(data["test"])
else:
    st.warning("Бұл сабаққа контент кезең-кезеңімен қосылады")

st.markdown("---")
st.caption("© Chemistry + AI | Streamlit оқу платформасы")
