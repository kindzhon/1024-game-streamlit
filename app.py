"""
1024 游戏 - Streamlit 网页版
带动画效果、支持手机端
"""

import streamlit as st
import numpy as np
import random

# 页面配置
st.set_page_config(
    page_title="1024 游戏",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 颜色映射
COLOR_MAP = {
    2: "#EEE4DA",
    4: "#EDE0C8",
    8: "#F2B179",
    16: "#F59563",
    32: "#F67C5F",
    64: "#F65E3B",
    128: "#EDCF72",
    256: "#EDCC61",
    512: "#EDC850",
    1024: "#EDC53F",
    2048: "#FFD700",
}

def get_color(value):
    """获取数字对应的颜色"""
    if value in COLOR_MAP:
        return COLOR_MAP[value]
    return "#FFD700"  # 2048 以上用金色

def get_text_color(value):
    """获取文字颜色"""
    if value >= 2048:
        return "#FFFFFF"
    return "#776E65"

def init_game():
    """初始化游戏"""
    board = np.zeros((4, 4), dtype=int)
    return board

def add_new_number(board):
    """在随机位置添加一个新数字 (2 或 4)"""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i, j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i, j] = 2 if random.random() < 0.9 else 4
    return board

def can_move(board):
    """检查是否可以移动"""
    if np.any(board == 0):
        return True
    
    for i in range(4):
        for j in range(3):
            if board[i, j] == board[i, j + 1]:
                return True
    
    for j in range(4):
        for i in range(3):
            if board[i, j] == board[i + 1, j]:
                return True
    
    return False

def slide_row(row):
    """滑动一行"""
    new_row = [x for x in row if x != 0]
    while len(new_row) < 4:
        new_row.append(0)
    return new_row

def merge_row(row):
    """合并一行"""
    merged = False
    for i in range(3):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
            merged = True
    return row, merged

def move_left(board):
    """向左移动"""
    new_board = []
    for row in board:
        new_row = slide_row(list(row))
        new_row, _ = merge_row(new_row)
        new_row = slide_row(new_row)
        new_board.append(new_row)
    return np.array(new_board, dtype=int)

def move_right(board):
    """向右移动"""
    new_board = []
    for row in board:
        reversed_row = list(row[::-1])
        new_row = slide_row(reversed_row)
        new_row, _ = merge_row(new_row)
        new_row = slide_row(new_row)
        new_board.append(new_row[::-1])
    return np.array(new_board, dtype=int)

def move_up(board):
    """向上移动"""
    return move_left(board.T).T

def move_down(board):
    """向下移动"""
    return move_right(board.T).T

def check_win(board):
    """检查是否胜利 (出现 1024)"""
    return np.any(board >= 1024)

def check_game_over(board):
    """检查游戏是否结束"""
    return not can_move(board)

def calculate_score(board):
    """计算分数"""
    return int(np.sum(board))

def get_font_size(value):
    """根据数字长度调整字体大小"""
    if value < 100:
        return "36px"
    elif value < 1000:
        return "32px"
    elif value < 10000:
        return "28px"
    else:
        return "24px"

# 自定义 CSS
st.markdown("""
<style>
.game-board {
    background: #BBADA0;
    border-radius: 10px;
    padding: 15px;
    display: inline-block;
}
.cell {
    width: 80px;
    height: 80px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin: 5px;
    transition: all 0.15s ease-in-out;
}
@media (max-width: 500px) {
    .cell {
        width: 60px;
        height: 60px;
        margin: 3px;
    }
}
</style>
""", unsafe_allow_html=True)

# 主程序
def main():
    st.title("🎮 1024 游戏")
    st.markdown("滑动或按方向键操作 | 相同数字合并为双倍")
    
    # 初始化状态
    if 'board' not in st.session_state:
        st.session_state.board = init_game()
        st.session_state.board = add_new_number(st.session_state.board)
        st.session_state.board = add_new_number(st.session_state.board)
        st.session_state.score = 0
        st.session_state.game_over = False
        st.session_state.game_won = False
        st.session_state.high_score = 0
    
    # 显示分数
    col1, col2 = st.columns(2)
    with col1:
        st.metric("分数", st.session_state.score)
    with col2:
        st.metric("最高分", st.session_state.high_score)
    
    # 游戏状态提示
    if st.session_state.game_over:
        st.error("🎮 游戏结束！点击'新游戏'重新开始")
    elif st.session_state.game_won:
        st.success("🎉 恭喜达成 1024！继续挑战更高分")
    
    # 渲染游戏板
    board_html = '<div class="game-board">'
    for i in range(4):
        for j in range(4):
            value = int(st.session_state.board[i, j])
            color = get_color(value)
            text_color = get_text_color(value)
            font_size = get_font_size(value) if value > 0 else "0px"
            text = str(value) if value > 0 else ""
            
            # 空单元格用浅色背景
            if value == 0:
                color = "#CDC1B4"
                text_color = "#CDC1B4"
            
            board_html += f'''
            <span class="cell" style="
                background: {color};
                color: {text_color};
                font-size: {font_size};
                display: inline-block;
            ">{text}</span>'''
        board_html += '<br>'
    board_html += '</div>'
    
    st.markdown(board_html, unsafe_allow_html=True)
    
    # 控制按钮
    st.markdown("### 操作")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("⬆️ 上", use_container_width=True, key="up"):
            handle_move("up")
            st.rerun()
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("⬅️ 左", use_container_width=True, key="left"):
            handle_move("left")
            st.rerun()
    with col3:
        if st.button("➡️ 右", use_container_width=True, key="right"):
            handle_move("right")
            st.rerun()
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("⬇️ 下", use_container_width=True, key="down"):
            handle_move("down")
            st.rerun()
    
    # 功能按钮
    st.markdown("### 功能")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 新游戏", use_container_width=True):
            st.session_state.board = init_game()
            st.session_state.board = add_new_number(st.session_state.board)
            st.session_state.board = add_new_number(st.session_state.board)
            st.session_state.score = 0
            st.session_state.game_over = False
            st.session_state.game_won = False
            st.rerun()
    
    with col2:
        if st.button("❓ 帮助", use_container_width=True):
            st.markdown("""
            **游戏规则：**
            1. 每次滑动，所有方块会向该方向移动
            2. 相同数字的方块相撞时会合并
            3. 合并后的数字是原来的两倍
            4. 每次移动后会随机出现一个新数字 (2 或 4)
            5. 当出现 1024 时获胜，但可以继续挑战更高分
            6. 当没有空格且无法合并时游戏结束
            
            **操作方式：**
            - 电脑：点击方向按钮
            - 手机：点击方向按钮
            """)

def handle_move(direction):
    """处理移动"""
    if st.session_state.game_over:
        return
    
    board_before = st.session_state.board.copy()
    
    if direction == "left":
        new_board = move_left(st.session_state.board)
    elif direction == "right":
        new_board = move_right(st.session_state.board)
    elif direction == "up":
        new_board = move_up(st.session_state.board)
    elif direction == "down":
        new_board = move_down(st.session_state.board)
    
    # 检查是否有变化
    if not np.array_equal(board_before, new_board):
        st.session_state.board = new_board
        st.session_state.board = add_new_number(st.session_state.board)
        st.session_state.score = calculate_score(st.session_state.board)
        
        # 更新最高分
        if st.session_state.score > st.session_state.high_score:
            st.session_state.high_score = st.session_state.score
        
        # 检查游戏状态
        if check_win(st.session_state.board) and not st.session_state.game_won:
            st.session_state.game_won = True
        elif check_game_over(st.session_state.board):
            st.session_state.game_over = True

if __name__ == "__main__":
    main()
