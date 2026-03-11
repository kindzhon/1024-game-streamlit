import streamlit as st
import streamlit.components.v1 as components
import os

# 设置页面配置
st.set_page_config(
    page_title="经典坦克大战 - Streamlit 版",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 隐藏 Streamlit 默认的菜单和页脚，提供更像原生游戏的体验
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .main .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
            iframe {
                border-radius: 10px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 读取 HTML 文件内容
html_file_path = os.path.join(os.path.dirname(__file__), "tank.html")

try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        game_html = f.read()
    
    # 使用 components.html 渲染游戏
    # 设置高度为 900 像素以确保完整显示，允许滚动
    components.html(game_html, height=950, scrolling=True)

except FileNotFoundError:
    st.error("未找到 tank.html 文件，请确保它与 streamlit_app.py 在同一目录下。")
except Exception as e:
    st.error(f"加载游戏时出错: {e}")

# 在页面底部添加一些说明（可选）
with st.expander("操作说明"):
    st.write("""
    - **移动**: W, A, S, D 或 屏幕方向键
    - **射击**: 空格键, J 键 或 屏幕 FIRE 按钮
    - **提示**: 手机端请点击屏幕上的虚拟按键。
    """)
