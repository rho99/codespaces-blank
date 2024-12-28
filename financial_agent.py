from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

## Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the Web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

## Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

## Multi AI Agent
multi_ai_agent = Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Always include sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

## Calling Multi AI Agent to display Response in console for hardcoded message.
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)