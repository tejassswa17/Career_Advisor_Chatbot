# memory/memory_manager.py

from langchain_core.chat_history import InMemoryChatMessageHistory


class MemoryManager:

    def __init__(self):

        self.history = InMemoryChatMessageHistory()

        self.summary = ""

        self.max_messages = 10

        self.keep_recent = 5

    def get_recent_messages(self):

        return self.history.messages[-self.keep_recent:]

    def get_context(self):

        recent_chat = "\n".join(
            [
                f"{msg.type}: {msg.content}"
                for msg in self.get_recent_messages()
            ]
        )

        return f"""
Conversation Summary:
{self.summary}

Recent Conversation:
{recent_chat}
"""

    def update_summary(self, llm):

        if len(self.history.messages) <= self.max_messages:
            return

        old_messages = self.history.messages[:-self.keep_recent]

        conversation = "\n".join(
            [
                f"{msg.type}: {msg.content}"
                for msg in old_messages
            ]
        )

        prompt = f"""
Existing Summary:
{self.summary}

Conversation:
{conversation}

Create an updated memory summary.

Preserve the following information if available:
- Education
- Skills
- Projects
- Internships
- Certifications
- Career goals
- Preferences
- Location
- Work experience

Important:
- Never lose important user facts.
- Merge with the existing summary.
- Remove unnecessary conversational details.
- Keep the summary concise.
- Return only the updated summary.
"""

        response = llm.invoke(prompt)

        self.summary = response.content

        print("\n========== SUMMARY UPDATED ==========")
        print(self.summary)
        print("=====================================\n")

        recent_messages = self.history.messages[-self.keep_recent:]

        self.history.clear()

        self.history.add_messages(recent_messages)

    def get_summary(self):

        return self.summary