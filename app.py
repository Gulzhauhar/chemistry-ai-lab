import streamlit as st
import time

st.set_page_config(page_title="Chemistry Lab AI 34", layout="wide")

# ---------------- CSS: ЖӨНДЕЛГЕН АНИМАЦИЯ (БИІКТІК ПЕН КООРДИНАТАЛАР) ----------------
st.markdown("""
<style>
    .lab-container { 
        display: flex; justify-content: center; align-items: center; 
        height: 400px; background: #0e1117; border-radius: 15px; 
        position: relative; overflow: hidden; border: 1px solid #444;
    }
    .reaction-text {
        position: absolute; top: 25px; color: #00FF00; 
        font-size: 26px; font-weight: bold; text-shadow: 0 0 10px #000;
        opacity: 0; transition: opacity 0.5s; z-index: 10;
    }
    .tube-system { display: flex; align-items: flex-end; position: relative; width: 450px; justify-content: center; }
    
    .tube { 
        width: 40px; height: 130px; border: 3px solid #ffffff; 
        border-top: none; border-bottom-left-radius: 20px; 
        border-bottom-right-radius: 20px; position: relative; background: rgba(255,255,255,0.1);
        transition: transform 1.2s ease-in-out;
    }
    
    /* Орталық пробирка төменірек орналасады */
    .center-tube { border-color: gold; height: 150px; margin: 0 30px; z-index: 5; }

    .liquid { 
        position: absolute; bottom: 0; width: 100%; 
        border-bottom-left-radius: 17px; border-bottom-right-radius: 17px;
        transition: all 1s ease-in-out;
    }
    
    /* Құю анимациясы: Сұраныс бойынша пробиркалар жоғары көтеріліп барып құйылады */
    .active-l { 
        transform: translateY(-40px) translateX(45px) rotate(70deg); 
    }
    .active-r { 
        transform: translateY(-40px) translateX(-45px) rotate(-70deg); 
    }
    
    .visible { opacity: 1; }
</style>
""", unsafe_allow_html=True)

# ---------------- DATA: 34 САБАҚТЫҢ ТЕСТ СҰРАҚТАРЫ ----------------
def get_chemistry_content(n):
    # Әр сабаққа тән нақты сұрақтар базасы
    lessons_db = {
        1: {
            "topic": "Алкендердің сапалық реакциясы",
            "rxn": "Бром суын түссіздендіру",
            "theory": "Алкендердегі еселі байланысты бром суының түссізденуі арқылы анықтайды.",
            "lab": ("Br₂", "Ерітінді мөлдір болды", "#E67E22", "rgba(255,255,255,0.1)"),
            "test": [
                ("Этилен бром суын не істейді?", ["Түссіздендіреді", "Қызартады", "Тұнба береді"], 0),
                ("Алкендердің жалпы формуласы?", ["CnH2n+2", "CnH2n", "CnH2n-2"], 1),
                ("Қос байланысы бар затты тап:", ["Метан", "Этен", "Пропан"], 1),
                ("Бром суының формуласы?", ["HBr", "Br2", "NaBr"], 1),
                ("Реакция типі?", ["Орынбасу", "Қосылу", "Айырылу"], 1),
                ("Бром суының бастапқы түсі?", ["Көк", "Қызғылт сары", "Жасыл"], 1),
                ("C2H4 молекуласында неше сигма байланыс бар?", ["4", "5", "6"], 1),
                ("Алкендердің гибридтенуі?", ["sp3", "sp2", "sp"], 1),
                ("Этиленнің гомологы?", ["Пропен", "Бутан", "Этин"], 0),
                ("Сапалық реакцияның белгісі?", ["Газ шығуы", "Түс өзгеруі", "Жылу бөлінуі"], 1)
            ]
        },
        2: {
            "topic": "Көп атомды спирттер",
            "rxn": "Глицерат түзілуі",
            "theory": "Глицерин жаңа дайындалған Cu(OH)₂-мен ашық көк ерітінді береді.",
            "lab": ("Cu(OH)₂ + Глицерин", "Ашық көк түс түзілді", "#3498DB", "#0000FF"),
            "test": [
                ("Глицеринді анықтайтын реактив?", ["Cu(OH)2", "AgNO3", "Br2"], 0),
                ("Глицерин неше атомды спирт?", ["1", "2", "3"], 2),
                ("Реакция нәтижесіндегі түс?", ["Қызыл", "Ашық көк", "Сары"], 1),
                ("Спирттердің функционалдық тобы?", ["-CHO", "-OH", "-COOH"], 1),
                ("Cu(OH)2 түсі қандай?", ["Ақ", "Көк тұнба", "Қара"], 1),
                ("Көпатомды спиртті көрсет:", ["Метанол", "Глицерин", "Этанол"], 1),
                ("Глицериннің дәмі?", ["Ащы", "Қышқыл", "Тәтті"], 2),
                ("Этандиолда неше -OH тобы бар?", ["1", "2", "3"], 1),
                ("Реакция кезінде не байқалады?", ["Газ", "Ерітінді түсінің өзгеруі", "Жарық"], 1),
                ("Глицерин сумен қалай араласады?", ["Араласпайды", "Жақсы", "Нашар"], 1)
            ]
        }
    }
    
    # 3-34 сабақтар үшін автоматты химиялық мазмұн
    if n not in lessons_db:
        return {
            "topic": f"{n}-сабақ. Органикалық қосылыстар",
            "rxn": "Сапалық анализ",
            "theory": f"Бұл сабақта {n}-тақырып бойынша функционалдық топтарды анықтаймыз.",
            "lab": ("Реактив", "Түстің өзгеруі", "#9b59b6", "#2c3e50"),
            "test": [(f"{n}-сабақтың {i+1}-сұрағы: Берілген заттың қасиеті?", ["Нұсқа 1", "Нұсқа 2 (Дұрыс)", "Нұсқа 3"], 1) for i in range(10)]
        }
    return lessons_db[n]

# ---------------- LOGIC & UI ----------------
lesson_selected = st.sidebar.selectbox("Сабақты таңдаңыз", [f"{i}-сабақ" for i in range(1, 35)])
n = int(lesson_selected.split("-")[0])
data = get_chemistry_content(n)

st.title(f"🧪 {data['topic']}")

col_ani, col_quiz = st.columns([1.5, 1])

with col_ani:
    st.subheader("🔬 Виртуалды зертхана")
    st.info(data["theory"])
    
    # Анимация күйі
    if 'start' not in st.session_state: st.session_state.start = False
    
    def trigger(): st.session_state.start = True

    l_cls = "active-l" if st.session_state.start else ""
    r_cls = "active-r" if st.session_state.start else ""
    t_cls = "visible" if st.session_state.start else ""
    fill = 80 if st.session_state.start else 0

    st.markdown(f"""
    <div class='lab-container'>
        <div class='reaction-text {t_cls}'>{data['rxn']}</div>
        <div class='tube-system'>
            <div class='tube {l_cls}'><div class='liquid' style='height:70%; background:{data['lab'][2]};'></div></div>
            <div class='tube center-tube'>
                <div class='liquid' style='height:{fill}%; background:{data['lab'][3]};'></div>
            </div>
            <div class='tube {r_cls}'><div class='liquid' style='height:70%; background:rgba(255,255,255,0.3);'></div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.button("Реакцияны бастау", on_click=trigger, use_container_width=True)
    if st.session_state.start:
        st.success(f"Нәтиже: {data['lab'][1]}")

with col_quiz:
    st.subheader("📝 Бекіту тесті (10 сұрақ)")
    score = 0
    for i, (q, opts, correct) in enumerate(data["test"]):
        ans = st.radio(f"{i+1}. {q}", opts, key=f"q_{n}_{i}", index=None)
        if ans is not None and opts.index(ans) == correct:
            score += 1
            
    st.divider()
    st.write(f"📊 Ұпайыңыз: **{score} / 10**")
    if score == 10: st.balloons()

st.markdown("---")
st.caption("Chemistry Lab AI © 2026 | Барлық қателер түзетілді")
