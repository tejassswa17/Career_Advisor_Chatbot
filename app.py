# app.py

import streamlit as st

from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

from services.gemini_service import get_llm
from memory.memory_manager import MemoryManager
from prompts.career_prompt import CAREER_PROMPT
from utils.logger import logger


# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🎯"
)

st.title("🎯 AI Career Advisor Chatbot")

st.write(
    "Get career guidance, interview preparation tips, learning roadmaps, and skill recommendations."
)


# ==================================
# INITIALIZATION
# ==================================

llm = get_llm()

if "memory" not in st.session_state:
    st.session_state.memory = MemoryManager()

memory = st.session_state.memory


# ==================================
# DISPLAY CHAT HISTORY
# ==================================

for msg in memory.history.messages:

    role = "user" if msg.type == "human" else "assistant"

    with st.chat_message(role):
        st.markdown(msg.content)


# ==================================
# USER INPUT
# ==================================

query = st.chat_input(
    "Ask a career related question..."
)


# ==================================
# PROCESS QUERY
# ==================================

if query:

    try:

        # Display User Message
        with st.chat_message("user"):
            st.markdown(query)

        # Store User Message
        memory.history.add_message(
            HumanMessage(content=query)
        )

        logger.info(f"User Query: {query}")

        # Update Summary
        memory.update_summary(llm)

        # Get Context
        context = memory.get_context()

        # Prompt Construction
        final_prompt = CAREER_PROMPT.invoke(
            {
                "context": context,
                "query": query
            }
        )

        with st.spinner("Thinking..."):

            response = llm.invoke(
                final_prompt.to_messages()
            )

        answer = response.content

        # Save AI Response
        memory.history.add_message(
            AIMessage(content=answer)
        )

        logger.info(f"AI Response: {answer}")

        # Display AI Response
        with st.chat_message("assistant"):
            st.markdown(answer)

    except Exception as e:

        error_msg = str(e)

        logger.error(error_msg)

        if "RESOURCE_EXHAUSTED" in error_msg:

            with st.chat_message("assistant"):
                st.warning(
                    """
🚧 The AI service is currently busy or has reached its usage limit.

Please wait a few moments and try again.
                    """
                )

        elif "API_KEY_INVALID" in error_msg:

            with st.chat_message("assistant"):
                st.error(
                    """
🔑 Invalid API Key.

Please contact the administrator.
                    """
                )

        else:

            with st.chat_message("assistant"):
                st.error(
                    """
⚠️ Something went wrong while processing your request.

Please try again later.
                    """
                )

            logger.exception("Unexpected Error")