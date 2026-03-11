# 🎮 1024 游戏 - Streamlit 网页版

经典的 1024 数字合并游戏，使用 Streamlit 构建，支持手机端操作。

## 🎯 特性

- ✅ 经典 4x4 网格玩法
- ✅ 响应式设计，支持手机/平板/PC
- ✅ 流畅的动画效果
- ✅ 不同数字对应不同颜色
- ✅ 分数统计和最高分记录
- ✅ 简洁直观的操作界面

## 🚀 快速开始

### 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行游戏
streamlit run app.py
```

### 在线体验

访问 [Streamlit Cloud](https://1024-game-streamlit.streamlit.app) 

## 📦 部署到 Streamlit Cloud

1. 访问 [share.streamlit.io](https://share.streamlit.io)
2. 点击 "Sign in with GitHub" 登录
3. 点击 "New app"
4. 选择此仓库：`1024-game-streamlit`
5. 分支选择 `main`，主文件路径填 `app.py`
6. 点击 "Deploy"

部署完成后，你将获得一个类似 `https://1024-game-streamlit.streamlit.app` 的公开链接！

## 🎮 游戏规则

1. 每次滑动，所有方块会向该方向移动
2. 相同数字的方块相撞时会合并为双倍
3. 每次移动后会随机出现一个新数字 (2 或 4)
4. 当出现 1024 时获胜
5. 当没有空格且无法合并时游戏结束

## 📱 操作方式

- **电脑端**: 点击方向按钮 (⬆️⬇️⬅️➡️)
- **手机端**: 点击方向按钮

## 🛠️ 技术栈

- **框架**: Streamlit
- **语言**: Python 3.8+
- **依赖**: numpy

## 📁 项目结构

```
1024-game/
├── app.py              # 主程序
├── requirements.txt    # 依赖列表
├── README.md          # 本文件
└── PRD.md             # 产品需求文档
```

## 📄 许可证

MIT License

---

**作者**: AI Assistant  
**创建时间**: 2026-03-10
