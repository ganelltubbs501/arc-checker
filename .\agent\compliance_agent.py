# agent/compliance_agent.py

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage  
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
from langgraph.prebuilt import create_react_agent
from config import OPENAI_API_KEY

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=OPENAI_API_KEY)

# Simulated compliance scanner tool
@tool
def scan_file_for_compliance_issues(file_path: str, keywords: list) -> list:
    """
    Scans a file for potential compliance issues based on keyword matches.
    
    Args:
        file_path (str): Path to the file to scan
        keywords (list): List of compliance-related keywords to search for

    Returns:
        list: A list of lines containing potential compliance issues
    """
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
        
        issues = []
        for i, line in enumerate(lines):
            for keyword in keywords:
                if keyword.lower() in line.lower():
                    issues.append({
                        "line_number": i + 1,
                        "line_content": line.strip(),
                        "matched_keyword": keyword
                    })
        return issues
    except Exception as e:
        return [{"error": str(e)}]

# Simulated AI analysis tool
@tool
def check_compliance_issue(description: str, context: str) -> str:
    """
    Uses the LLM to determine if a potential issue is an actual violation.
    
    Args:
        description (str): Description of the rule
        context (str): The code/config line where a keyword was found

    Returns:
        str: LLM-generated analysis of whether this is a real issue
    """
    prompt = (
        "You are a regulatory compliance expert.\n"
        f"Rule Description: {description}\n"
        f"Found in Context: {context}\n\n"
        "Is this a compliance violation? Explain why or why not."
    )
    response = llm.invoke(prompt)
    return response.content

# Simulated explanation generator
@tool
def generate_explanation(rule_description: str, suggested_fix: str) -> str:
    """
    Generates a plain-English explanation of a compliance issue and fix.
    
    Args:
        rule_description (str): Full description of the rule
        suggested_fix (str): Suggested action to resolve the issue

    Returns:
        str: Human-readable explanation
    """
    explanation_prompt = (
        f"Explain the following compliance requirement in simple terms:\n\n"
        f"{rule_description}\n\n"
        f"Suggested Fix: {suggested_fix}\n\n"
        "Why is this important and how should it be fixed?"
    )
    response = llm.invoke(explanation_prompt)
    return response.content


# Define tools list
tools = [scan_file_for_compliance_issues, check_compliance_issue, generate_explanation]

# âœ… Define system prompt explicitly
system_prompt = SystemMessage(content="""
You are a regulatory compliance assistant.
Your job is to help identify, explain, and fix potential violations of standards like HIPAA, SOC2, CMS CoPs, and CFR Part 2.
""")

# Create ReAct-style agent
agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt
)

# Wrap agent with message history
message_history = InMemoryChatMessageHistory()

