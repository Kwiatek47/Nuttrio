import streamlit as st
from agent.agent_init import run_llama

from analysis.calories import return_plot

def app():
        # Set the page configuration
        st.set_page_config(
            page_title="Nuttrio - Your Personal Diet Assistant",
            page_icon="🍏",
            initial_sidebar_state="expanded"
        )
        st.title("Nuttrio - Your Personal Diet Assistant")
        st.write("Welcome to Nuttrio! Your personal diet assistant for healthy eating.")
        st.write("Here you can track your meals, get personalized diet plans, get statistics about your current diet situation, and even more.")

        # Display bar plot from analysis/calories.py
        st.write("Calories consumed in the last 7 days:")
        plot = return_plot()
        st.pyplot(plot)

        st.write("Ask me anything about your diet! I can help you track your meals, get personalized diet plans, and provide statistics about your current diet situation.")
        st.write("Type your question below and I'll do my best to assist you.")

        # Initialize chat history
        if "messages" not in st.session_state:
                st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                        st.markdown(message["content"])

        if prompt := st.chat_input("Ask me anything about your diet!"):
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})

                # Display user message
                with st.chat_message("user"):
                        st.markdown(prompt)
                
                with st.chat_message("assistant"):
                        message_placeholder = st.empty()
                        message_placeholder.markdown("⌛ Thinking…")
                        response = run_llama(prompt)
                        message_placeholder.markdown(response)

                # Add assistant message to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})


app()