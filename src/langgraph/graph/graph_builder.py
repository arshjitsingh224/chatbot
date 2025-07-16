from langgraph.graph import StateGraph, START, END
from src.langgraph.state.state import State
from src.langgraph.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraph.nodes.chatbot_with_tool_node import ChatbotWithToolNode
class GraphBuilder:

    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):

        self.basic_chatbot_node = BasicChatbotNode(self.llm)


        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_build_graph(self):

        tools = get_tools()
        tool_node = create_tool_node(tools)

        llm = self.llm

        obj_chatbot_node =ChatbotWithToolNode(llm) 

        self.graph_builder.add_node("chatbot",obj_chatbot_node.create_chatbot(tools))
        self.graph_builder.add_node("tools",tool_node)

        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot",END)







    def setup_graph(self,usecase):

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase == "Chatbot With Web":
            self.chatbot_with_tools_build_graph()    

        return self.graph_builder.compile()        