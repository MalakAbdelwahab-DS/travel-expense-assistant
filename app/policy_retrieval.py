from app.config import API_KEY, TRAVEL_EXPENSE_POLICY_DATA_PATH
from app.utils import load_data
from app.llm import get_agent


class PolicyRetrieval:
    """
    Single entry point for answering a user's question about the
    travel expense policy.

    Routes to the real model agent if API_KEY is set,
    otherwise falls back to direct CSV retrieval.
    """

    def __init__(self):
        self.data = load_data(TRAVEL_EXPENSE_POLICY_DATA_PATH)

    def answer(self, question: str) -> str:
        if API_KEY:
            return self._answer_with_llm(question)
        return self._answer_with_retrieval(question)

    def _answer_with_llm(self, question: str) -> str:
        """Real model path: ask the AI agent."""
        agent = get_agent()
        result = agent.invoke({"messages": [{"role": "user", "content": question}]})
        return result["messages"][-1].content_blocks[0]["text"]

    def _answer_with_retrieval(self, question: str) -> str:
        """Offline path: look the answer up directly in the CSV, no LLM involved."""
        words = question.lower().split()

        matches = self.data[self.data.apply(
            lambda row: any(
                w in " ".join(str(v).lower() for v in row)
                for w in words
            ),
            axis=1
        )]

        if matches.empty:
            text = (
                "Sorry, I cannot answer your question as it isn't covered "
                "by the travel expense policy."
            )
        else:
            text = (
                "## Travel Expense Policy\n\n"
                + matches.to_markdown(index=False)
            )

        return text