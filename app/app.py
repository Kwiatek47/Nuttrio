import streamlit as st

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
                
                # Simulate a response from the asssistant
                response = prompt

                with st.chat_message("assistant"):
                        st.markdown(response)
                # Add assistant message to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})

app()