import os
import dspy
from dotenv import load_dotenv

# 1. 加载环境变量
load_dotenv()

# 2. 配置 DSPy 连接 DeepSeek
# DSPy 支持通过 "openai/" 前缀调用兼容接口
lm = dspy.LM(
    model="openai/deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
    temperature=0.7,
    max_tokens=2000
)

# 全局配置：告诉 DSPy 使用这个模型
dspy.configure(lm=lm)

# 3. 定义签名 (Signature) —— 也就是任务的“契约”
# 我们告诉 DSPy：输入是什么，输出要什么。
class PromptOptimizer(dspy.Signature):
    """
    你是一位精通 LLM 原理的提示词工程专家 (Prompt Engineer)。
    你的任务是将用户输入的简单、模糊的指令，转化为结构化、高质量、生产级的 System Prompt。
    优化后的 Prompt 应包含：角色设定、详细的任务描述、约束条件、输出格式示例（如JSON/Markdown）。
    """

    # 输入：用户的原始想法
    user_instruction = dspy.InputField(desc="用户想让AI做的事情（简单描述）")

    # 输出：优化后的 Prompt
    refined_prompt = dspy.OutputField(desc="优化后的专业 System Prompt，结构清晰，包含各种边界条件处理")

# 4. 定义程序模块 (Module)
# 我们使用 ChainOfThought (思维链) 模块。
# 这意味着 DSPy 会先让 AI "思考" (Reasoning)，然后再 "输出" (Refined Prompt)。
optimizer_program = dspy.ChainOfThought(PromptOptimizer)

def optimize_instruction(raw_input):
    """
    封装好的调用函数
    """
    print(f"[DSPy] 正在优化指令: {raw_input[:20]}...")

    # 执行 DSPy 程序
    # 注意：DSPy 的调用方式就像调用函数一样简单
    result = optimizer_program(user_instruction=raw_input)

    return {
        "reasoning": result.reasoning,
        "refined_prompt": result.refined_prompt
    }

# --- 单元测试 ---
if __name__ == "__main__":
    test_input = "帮我从新闻里提取公司名字和股票代码"
    res = optimize_instruction(test_input)
    print("\n=== 思考过程 ===\n", res["reasoning"])
    print("\n=== 优化结果 ===\n", res["refined_prompt"])