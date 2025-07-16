import streamlit as st
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.llms.groqllm import GroqLLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.errr("Error: Failed to load user input from the UI.")
        return

    user_message = st.chat_input("Enter your message: ")

    if user_message:
            obj_llm_config = GroqLLM(user_controls_input = user_input)
            model = obj_llm_config.get_llm_model()

            usecase = user_input.get("selected_usecase")

            graph_builder = GraphBuilder(model)
            graph = graph_builder.setup_graph(usecase)
            DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
              