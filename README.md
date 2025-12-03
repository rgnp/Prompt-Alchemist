# ⚗️ Prompt Alchemist: 基于 DSPy 的提示词炼金术师

![Status](https://img.shields.io/badge/Status-Active-success)
![Stack](https://img.shields.io/badge/DSPy-DeepSeek-Streamlit)
![License](https://img.shields.io/badge/License-MIT-blue)

> **"Stop writing prompts. Start programming them."**
> 这是一个基于 **DSPy (Declarative Self-improving Python)** 框架构建的元提示词优化工具。它利用思维链 (Chain of Thought) 技术，将用户简单的自然语言指令，自动“炼制”为结构严谨、专家级的 System Prompts。

---



## 🌟 核心理念 (Why DSPy?)

传统的 Prompt Engineering 就像**“炼丹”**（不断手动试错、修改字符串）。
本项目采用 **DSPy** 框架，将 Prompt 视为**“代码”**：

1.  **声明式编程 (Declarative)**：我们定义“输入是什么”和“输出要什么”（Signature），而不是写死具体的 Prompt 字符串。
2.  **思维链 (Chain of Thought)**：内置 `dspy.ChainOfThought` 模块，强迫 AI 在生成 Prompt 之前先进行逻辑推理 (Reasoning)，显著提升了输出质量。
3.  **模块化 (Modular)**：提示词生成逻辑被封装为 Python 类，易于维护和扩展。

---

## 🛠️ 技术架构

* **核心框架**: [DSPy](https://github.com/stanfordnlp/dspy) - 斯坦福大学推出的提示词编程框架。
* **推理大脑**: [DeepSeek-V3](https://api.deepseek.com/) - 提供强大的逻辑推理能力（经测试，DeepSeek 对指令遵循的效果极佳）。
* **交互界面**: Streamlit - 轻量级 Web UI。

---

## 🚀 快速开始 (Quick Start)

### 1. 克隆仓库
```bash
git clone [https://github.com/rgnp/DSPy-Prompt-Optimizer.git](https://github.com/rgnp/DSPy-Prompt-Optimizer.git)
cd DSPy-Prompt-Optimizer
```

### 2. 环境配置
建议使用虚拟环境:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```
安装依赖:
```bash
pip install -r requirements.txt
```

### 3. 配置密钥
在根目录新建 `.env` 文件，填入你的 API Key：
```.env
# 本项目使用 DeepSeek (兼容 OpenAI 协议)
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
DEEPSEEK_BASE_URL=[https://api.deepseek.com](https://api.deepseek.com)
```
### 4. 启动炼金术师
```bash
streamlit run src/app.py
```

## 💻 核心代码预览
这就是 DSPy 的魅力，我们通过定义 签名 (Signature) 来控制 AI：

```python
class PromptOptimizer(dspy.Signature):
    """
    你是一位精通 LLM 原理的提示词工程专家。
    你的任务是将简单的指令转化为高质量的 System Prompt。
    """
    user_instruction = dspy.InputField(desc="用户想让AI做的事情")
    refined_prompt = dspy.OutputField(desc="优化后的专业 System Prompt")

# 自动加入思维链
optimizer_program = dspy.ChainOfThought(PromptOptimizer)
```

## 📝 示例 (Examples)

你的输入 (Raw)  |AI 思考 (Reasoning) |炼制结果 (Refined Prompt) |
| --- | --- | --- |
帮我提取财报里的数字|用户需要进行信息抽取，特别是财务数据。需要考虑货币单位、时间周期，输出格式最好是结构化的 JSON...|你是一个专业的金融数据分析师。请从文本中提取以下字段：营收、净利润... 输出格式：JSON...|
扮演苏格拉底|用户希望进行引导式教学，而不是直接给出答案。核心策略是反问和启发...|你现在是苏格拉底。请不要直接回答学生的问题，而是通过一系列层层递进的提问，引导学生自己得出结论...|

## 🔮 Future Roadmap
- [ ] Few-Shot Learning: 引入 DSPy 的 Teleprompter，通过提供几个优秀 Prompt 的例子，自动训练优化器。

- [ ] Prompt 评测: 增加一个模块，自动测试生成的 Prompt 效果如何。

---
Built with ❤️ by [RGNP] - Exploring the future of AI Engineering.