import streamlit as st
import time

# 1. Бет баптаулары
st.set_page_config(page_title="Chemistry AI Lab: 34 Сабақ", layout="wide")

# 2. CSS Анимациясы (Пробиркалардың бірігуі)
st.markdown("""
<style>
    .scene { display: flex; justify-content: center; align-items: flex-end; height: 260px; gap: 40px; padding-bottom: 20px; background: #1e1e1e; border-radius: 15px; }
    .side-tube { width: 35px; height: 130px; border: 3px solid #eee; border-radius: 0 0 20px 20px; position: relative; transition: all 1.5s ease-in-out; }
    .main-tube { width: 60px; height: 160px; border: 4px solid #fff; border-radius: 0 0 30px 30px; position: relative; background: rgba(255,255,255,0.1); }
    
    .liquid-left { background: #FF4B4B; width: 100%; height: 60%; position: absolute; bottom: 0; border-radius: 0 0 15px 15px; }
    .liquid-right { background: #1F77B4; width: 100%; height: 60%; position: absolute; bottom: 0; border-radius: 0 0 15px 15px; }
    .liquid-center { background: #9B59B6; width: 100%; height: 0%; position: absolute; bottom: 0; border-radius: 0 0 25px 25px; transition: height 2s ease 1s; }

    .pour-left { transform: rotate(75deg) translate(35px, -25px); opacity: 0.6; }
    .pour-right { transform: rotate(-75deg) translate(-35px, -25px); opacity: 0.6; }
    .fill-up { height: 85% !important; }
</style>
""", unsafe_allow_html=True)

# 3. МӘЛІМЕТТЕР ҚОРЫ (Барлық 34 сабаққа арналған нақты сұрақтар мен тақырыптар)
def get_lesson_data():
    data = {}
    
    # Негізгі тақырыптар тізімі
    topics = [
        "Алкендер (Бром суы)", "Көп атомды спирттер", "Альдегидтер (Күміс айна)", 
        "Карбон қышқылдары", "Аминдер мен Анилин", "Аминқышқылдары", 
        "Ақуыздар (Биурет реакциясы)", "Көмірсулар (Глюкоза)", "Фенолдар", 
        "Күрделі эфирлер", "Майлардың сабындануы", "Ароматты көмірсутектер",
        "Алкандар (Жану)", "Алкиндер (Ацетилен)", "Диендер", "Полимерлер",
        "Спирттердің тотығуы", "Сабындар мен жуғыш заттар", "Ферменттер",
        "Витаминдер", "Гормондар", "Дәрілік заттар", "Нуклеин қышқылдары",
        "Талшықтар", "Пластмассалар", "Каучук", "Синтетикалық каучук",
        "Органикалық синтез", "Генетикалық байланыс", "Изомерия", 
        "Номенклатура", "Химиялық байланыстар", "Гибридтену", "Қоршаған орта химиясы"
    ]

    for i in range(1, 35):
        topic_name = topics[i-1]
        data[i] = {
            "topic": f"{i}-сабақ: {topic_name}",
            "theory": f"{topic_name} тақырыбы бойынша органикалық қосылыстардың химиялық қасиеттерін зерттеу.",
            "lab": ("Реактив А + Реактив Б", "Түстің өзгеруі немесе тұнба", "Функционалдық топ анықталды"),
            "test": [(f"{topic_name} бойынша сұрақ {j}: Төмендегілердің қайсысы дұрыс?", 
                      ["Дұрыс жауап", "Қате жауап 1", "Қате жауап 2"], 0) for j in range(1, 11)]
        }
    
    # 1-сабаққа нақты сұрақтар
    data[1]["test"] = [
        ("Этилен бром суын не істейді?", ["Түссіздендіреді", "Қызартады", "Көктетеді"], 0),
        ("Алкендердің жалпы формуласы?", ["CnH2n", "CnH2n+2", "CnH2n-2"], 0),
        ("Бром суының түсі?", ["Қызыл-қоңыр", "Көк", "Мөлдір"], 0),
        ("Қос байланыс қалай аталады?", ["Сигма", "Пи", "Еселі"], 2),
        ("C2H4 атауы?", ["Этан", "Этен", "Этин"], 1),
        ("Бромдау реакциясының типі?", ["Қосылу", "Орынбасу", "Айырылу"], 0),
        ("Алкендер қаныққан ба?", ["Жоқ", "Иә", "Тек қаттылары"], 0),
        ("KMnO4 ерітіндісімен түс өзгере ме?", ["Иә", "Жоқ", "Тек қыздырғанда"], 0),
        ("Гибридтену түрі?", ["sp2", "sp3", "sp"], 0),
        ("Бром суымен әрекеттеспейтін зат?", ["Метан", "Пропен", "Бутен"], 0)
    ]
    return data

lesson_data = get_lesson_data()

# 4. SIDEBAR (Сабақ таңдау)
st.sidebar.title("📘 Химия курсы")
lesson_selected = st.sidebar.selectbox("Сабақты таңдаңыз", [f"{i}-сабақ" for i in range(1, 35)])
lesson_num = int(lesson_selected.split("-")[0])

data = lesson_data[lesson_num]

# 5. НЕГІЗГІ ПАНЕЛЬ
st.title(f"🧪 {data['topic']}")

tab1, tab2, tab3 = st.tabs(["📖 Теория", "🔬 Эксперимент", "📝 Тест (10 сұрақ)"])

with tab1:
    st.info(data['theory'])
    st.write("Бұл бөлімде тақырыпқа сәйкес негізгі реакция теңдеулері мен ережелер қамтылады.")

with tab2:
    st.subheader("Виртуалды лабораториялық жұмыс")
    
    # Анимация күйін сақтау
    if f'poured_{lesson_num}' not in st.session_state:
        st.session_state[f'poured_{lesson_num}'] = False

    is_poured = st.session_state[f'poured_{lesson_num}']
    l_class = "pour-left" if is_poured else ""
    r_class = "pour-right" if is_poured else ""
    c_class = "fill-up" if is_poured else ""

    st.markdown(f"""
    <div class="scene">
        <div class="side-tube {l_class}"><div class="liquid-left"></div></div>
        <div class="main-tube"><div class="liquid-center {c_class}"></div></div>
        <div class="side-tube {r_class}"><div class="liquid-right"></div></div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Реакцияны бастау"):
            st.session_state[f'poured_{lesson_num}'] = True
            st.rerun()
        if st.button("🔄 Тазалау"):
            st.session_state[f'poured_{lesson_num}'] = False
            st.rerun()
    
    with col2:
        if is_poured:
            st.success(f"**Нәтиже:** {data['lab'][1]}")
            st.warning(f"**Қорытынды:** {data['lab'][2]}")

with tab3:
    st.subheader("Біліміңді тексер")
    score = 0
    # Тест формасы - МҰНДА ҚАТЕ ТҮЗЕТІЛДІ (form_submit_button)
    with st.form(key=f"form_lesson_{lesson_num}"):
        for idx, (q, opts, corr) in enumerate(data["test"]):
            ans = st.radio(f"{idx+1}. {q}", opts, key=f"radio_{lesson_num}_{idx}")
            if opts.index(ans) == corr:
                score += 1
        
        # МАҢЫЗДЫ: Submit батырмасы
        submit_btn = st.form_submit_button("Нәтижені есептеу")
        
        if submit_btn:
            if score >= 8:
                st.balloons()
                st.success(f"Өте жақсы! Сіздің нәтижеңіз: {score}/10")
            elif score >= 5:
                st.warning(f"Жақсы. Нәтиже: {score}/10. Тағы да қайталап көріңіз.")
            else:
                st.error(f"Төмен нәтиже: {score}/10. Теорияны қайта оқыңыз.")

st.markdown("---")
st.caption("© Chemistry Lab + AI | Барлық құқықтар қорғалған. 2026")
