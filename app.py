import streamlit as st
import time

st.set_page_config(page_title="Chemistry Lab AI 34", layout="wide")

# ---------------- CSS: УЛУЧШЕННАЯ АНИМАЦИЯ (ПОВТОР И ВЫСОТА) ----------------
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
    }
    
    .center-tube { border-color: gold; height: 150px; margin: 0 30px; z-index: 5; }

    .liquid { 
        position: absolute; bottom: 0; width: 100%; 
        border-bottom-left-radius: 17px; border-bottom-right-radius: 17px;
        transition: all 1s ease-in-out;
    }
    
    /* Анимация: Поднимаются выше и наклоняются */
    .active-l { 
        animation: pour-left-new 1.5s forwards;
    }
    .active-r { 
        animation: pour-right-new 1.5s forwards;
    }
    
    @keyframes pour-left-new {
        0% { transform: translateY(0) rotate(0); }
        50% { transform: translateY(-50px) rotate(0); }
        100% { transform: translateY(-50px) translateX(45px) rotate(70deg); }
    }
    @keyframes pour-right-new {
        0% { transform: translateY(0) rotate(0); }
        50% { transform: translateY(-50px) rotate(0); }
        100% { transform: translateY(-50px) translateX(-45px) rotate(-70deg); }
    }
    
    .visible { opacity: 1; }
</style>
""", unsafe_allow_html=True)

# ---------------- ДАННЫЕ: УРОКИ И ТЕСТЫ (ДОБАВЛЕН 3 УРОК) ----------------
def get_chemistry_content(n):
    lessons_db = {
        1: {
            "topic": "Качественная реакция на алкены",
            "rxn": "Обесцвечивание бромной воды",
            "theory": "Алкены обесцвечивают бромную воду (Br2) из-за разрыва кратной связи.",
            "lab": ("Br₂", "Раствор стал бесцветным", "#E67E22", "rgba(255,255,255,0.1)"),
            "test": [
                ("Что происходит с этиленом в бромной воде?", ["Обесцвечивается", "Краснеет", "Выпадает осадок"], 0),
                ("Общая формула алкенов?", ["CnH2n+2", "CnH2n", "CnH2n-2"], 1),
                ("Тип реакции с бромной водой?", ["Замещение", "Присоединение", "Отщепление"], 1),
                ("Формула бромной воды?", ["HBr", "Br2", "NaBr"], 1),
                ("Наличие какой связи доказывает эта реакция?", ["Одинарной", "Двойной", "Тройной"], 1)
            ]
        },
        2: {
            "topic": "Многоатомные спирты",
            "rxn": "Образование глицерата меди",
            "theory": "Глицерин с Cu(OH)2 образует ярко-синее окрашивание.",
            "lab": ("Cu(OH)₂ + Глицерин", "Ярко-синий раствор", "#3498DB", "#0000FF"),
            "test": [
                ("Реактив на глицерин?", ["Cu(OH)2", "AgNO3", "Br2"], 0),
                ("Цвет глицерата меди?", ["Красный", "Ярко-синий", "Желтый"], 1),
                ("Сколько групп -OH в глицерине?", ["1", "2", "3"], 2)
            ]
        },
        3: {
            "topic": "Альдегиды",
            "rxn": "Реакция серебряного зеркала",
            "theory": "Альдегиды окисляются аммиачным раствором оксида серебра, образуя налет серебра.",
            "lab": ("AgNO₃ + NH₃", "Появился зеркальный налет", "#BDC3C7", "#7F8C8D"),
            "test": [
                ("Как называется реакция на альдегиды?", ["Серебряное зеркало", "Биуретовая", "Бромирование"], 0),
                ("Функциональная группа альдегидов?", ["-OH", "-CHO", "-COOH"], 1),
                ("Что образуется при окислении альдегидов?", ["Спирт", "Карбоновая кислота", "Эфир"], 1),
                ("Формула уксусного альдегида?", ["HCHO", "CH3CHO", "C2H5CHO"], 1),
                ("Реактив для зеркала?", ["[Ag(NH3)2]OH", "Cu(OH)2", "KMnO4"], 0),
                ("Какое вещество выпадает на стенки?", ["Серебро", "Медь", "Золото"], 0),
                ("Является ли формальдегид газом?", ["Да", "Нет", "Только при нагреве"], 0),
                ("Название группы >C=O?", ["Карбонильная", "Карбоксильная", "Гидроксильная"], 0),
                ("Альдегиды — это...", ["Восстановители", "Индикаторы", "Соли"], 0),
                ("Тривиальное название метаналя?", ["Муравьиный альдегид", "Уксусный", "Масляный"], 0)
            ]
        }
    }
    
    if n not in lessons_db:
        return {
            "topic": f"Урок {n}. Химический анализ",
            "rxn": "Тестовая реакция",
            "theory": f"Изучение свойств веществ в рамках темы {n}.",
            "lab": ("Реактив", "Изменение цвета", "#9b59b6", "#2c3e50"),
            "test": [(f"Вопрос {i+1} по теме {n}?", ["Вариант 1", "Правильный ответ", "Вариант 3"], 1) for i in range(10)]
        }
    return lessons_db[n]

# ---------------- ЛОГИКА И ИНТЕРФЕЙС ----------------
lesson_selected = st.sidebar.selectbox("Выберите урок", [f"{i}-сабақ" for i in range(1, 35)])
n = int(lesson_selected.split("-")[0])
data = get_chemistry_content(n)

st.title(f"🧪 {data['topic']}")

col_ani, col_quiz = st.columns([1.5, 1])

with col_ani:
    st.subheader("🔬 Виртуальная лаборатория")
    
    # Кнопка перезапуска анимации через session_state
    if f'trigger_{n}' not in st.session_state:
        st.session_state[f'trigger_{n}'] = False

    def run_animation():
        st.session_state[f'trigger_{n}'] = True
        time.sleep(0.1) # Короткая пауза для сброса

    l_cls = "active-l" if st.session_state[f'trigger_{n}'] else ""
    r_cls = "active-r" if st.session_state[f'trigger_{n}'] else ""
    t_cls = "visible" if st.session_state[f'trigger_{n}'] else ""
    fill = 80 if st.session_state[f'trigger_{n}'] else 0

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

    if st.button("Запустить реакцию", key="btn_run", use_container_width=True):
        st.session_state[f'trigger_{n}'] = False # Сначала выключаем
        st.rerun() # Мгновенно обновляем, чтобы CSS сбросился и запустился снова

    if st.session_state[f'trigger_{n}']:
        st.success(f"Результат: {data['lab'][1]}")

with col_quiz:
    st.subheader("📝 Тест (10 вопросов)")
    score = 0
    for i, (q, opts, correct) in enumerate(data["test"]):
        ans = st.radio(f"{i+1}. {q}", opts, key=f"q_{n}_{i}", index=None)
        if ans is not None and opts.index(ans) == correct:
            score += 1
            
    st.divider()
    st.write(f"📊 Ваш результат: **{score} / {len(data['test'])}**")
    if score == len(data['test']): st.balloons()

st.markdown("---")
st.caption("Chemistry Lab AI © 2026 | Исправлено: 3 урок, повтор анимации, высота пробирок")
