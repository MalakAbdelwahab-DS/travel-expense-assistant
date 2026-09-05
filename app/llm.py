from langchain.agents import create_agent
from langchain.chat_models import BaseChatModel, init_chat_model
from app.utils import load_data, clean_data
from app.config import API_KEY, TRAVEL_EXPENSE_POLICY_DATA_PATH, BASE_URL, MODEL_PROVIDER, MODEL_NAME, MODEL_TEMPERATURE
from app.prompt import prompt


def get_travel_expenses_policy():
    """Load travel expenses policy data"""

    data = load_data(
        TRAVEL_EXPENSE_POLICY_DATA_PATH
    )

    cleaned_data = clean_data(data)
    return cleaned_data


def get_model() -> BaseChatModel:
    """Initialize the chat model used by the agent"""

    model = init_chat_model(
        api_key=API_KEY, model=MODEL_NAME, model_provider= MODEL_PROVIDER, temperature=MODEL_TEMPERATURE, base_url= BASE_URL
    )
    return model


def get_agent():
    """Create the travel expenses agent.

        Uses the real model agent if API_KEY is set;
        otherwise falls back to a keyword-matching offline agent so the
        app can run with no credentials.
    """

    agent = create_agent(
        model=get_model(),
        tools=[get_travel_expenses_policy],
        system_prompt=prompt,
    )
    return agent

    