import streamlit as st
from logic import optimize_instruction

st.set_page_config(page_title="Prompt Alchemist", layout="wide", page_icon="⚗️")

# 侧边栏
with st.sidebar:
    st.header("⚗️ 提示词炼金术师")
    st.caption("Powered by DSPy & DeepSeek")
    st.info("输入一句简单的话，让 AI 帮你写出专家级的 Prompt。")

    st.markdown("---")
    st.markdown("### 💡 示例输入")
    if st.button("示例 1: 信息提取"):
        st.session_state.user_input = "帮我从这段财报里提取收入、利润和风险点，输出JSON。"
    if st.button("示例 2: 角色扮演"):
        st.session_state.user_input = "扮演一个苏格拉底式的老师，不要直接给答案，要通过提问引导学生。"

# 主界面
st.title("DSPy Prompt Optimizer")

# 获取输入
user_input = st.text_area(
    "请输入你的原始指令 (Raw Instruction)",
    value=st.session_state.get("user_input",""),
    height=100,
    placeholder="例如：帮我把这篇论文翻译成中文，但是保留专业术语不翻译..."
)

if st.button("开始炼制 (Optimize)", type="primary"):
    if not user_input:
        st.warning("请输入指令！")
    else:
        with st.spinner("DSPy 正在构建思维链..."):
            try:
                # 调用后端逻辑
                result = optimize_instruction(user_input)

                # 布局：左边是思考，右边是结果
                col1, col2 = st.columns([1, 1])

                with col1:
                    st.subheader("🧠 AI 的思考过程 (Reasoning)")
                    st.info("DSPy 自动触发了思维链，分析了你的意图：")
                    st.markdown(f"> {result['reasoning']}")

                with col2:
                    st.subheader("✨ 优化后的 Prompt")
                    st.success("这是可以直接用于生产环境的 System Prompt：")
                    st.code(result['refined_prompt'], language="markdown")

                    # 复制便利性（虽然 Streamlit 还没有原生的一键复制按钮，但代码块右上角自带复制）
                
            except Exception as e:
                st.error(f"发生错误: {str(e)}")