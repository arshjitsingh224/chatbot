from src.langgraph.state.state import State

class ChatbotWithToolNode:

    def __init__(self,model):
        self.llm = model

    def create_chatbot(self,tools):

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            return {
                "messages": [llm_with_tools.invoke(state["messages"])]
            }    

        return chatbot_node    
