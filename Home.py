import streamlit as st
from pages import Quiz_Generation, Summarizer, Chat_With_PDF

def main():
    st.title("Welcome to Student Assistant!")
    st.markdown("---")
    st.header("University Students' Study Assistant")
    st.markdown("""
    University students encounter difficulties in effectively managing, comprehending, and assessing
    their study material. Existing solutions often lack the sophistication needed to provide personalized
    assistance, generate targeted questions, and facilitate seamless integration with external resources.
    Moreover, students may struggle to find efficient methods for summarizing content, clarifying
    doubts, and evaluating their understanding through assessments.
    """)
    st.markdown("---")
    st.header("Solution Overview")
    st.markdown("""
    Our proposed solution is an intelligent chatbot specifically designed for university students.
    Leveraging cutting-edge Generative AI and Intel oneAPI toolkits, the chatbot offers the following
    features:
    1. Study Material Summarization: The chatbot analyzes uploaded documents (e.g., docx, pdf,
    research papers) and generates concise summaries, enabling students to grasp key concepts
    efficiently.
    2. Question Generation: Using advanced natural language processing algorithms, the chatbot
    generates relevant questions based on the summarized content, aiding in comprehension and
    retention.
    3. Doubt Resolution: Through interactive dialogue, the chatbot addresses students' queries and
    clarifies concepts in real-time, fostering a deeper understanding of the material.
    """)
    st.markdown("---")
    
if __name__ == "__main__":
    main()
