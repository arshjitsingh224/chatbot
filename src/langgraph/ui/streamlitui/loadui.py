import streamlit as st
import os 

from src.langgraph.ui.streamlitui.uiconfigfile import Config

class LoadStreamlitUI:

    def __init__(self):

        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):

        st.set_page_config(page_title= "*" + self.config.get_page_title(), layout="wide")
        st.header ("e " + self.config.get_page_title())
        st.session_state.time_frame = ''
        st.session_state.isFetchButtonClicked = False

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st. selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                #Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls ["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls ["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input ("API Key", type="password")
                # Valídate API key 
                if not self.user_controls ["GROQ_API_KEY"]:
                    st.warning("Please enter your GROQ API key to proceed. Don't have? refer : https://console.grog.com/keys ")

            ## USecase selection 
            self.user_controls ["selected_usecase"]=st.selectbox("Select Usecases", usecase_options)
            
            if self.user_controls["selected_usecase"] == "Chatbot With Web" or self.user_controls["selected_usecase"] == "AI News":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("Tavily API Key", type = "password")

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your tavily api key to proceed. Don't have? refer to https://app.tavily.com/")

            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("AI news Explorer")

                with st.sidebar:
                    time_frame = st.selectbox(
                        "Select Time Frame",
                        ["Daily","Weekly","Monthly"],
                        index = 0
                    )
                if st.button("Fetch LatestAI News", use_container_width=True):
                    st.session_state.isFetchButtonClicked = True
                    st.session_state.timeframe = time_frame            

            return self.user_controls
