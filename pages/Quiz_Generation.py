import streamlit as st
import time  # Import the time module for the delay

# Define the questions, options, correct answers, and explanations
questions = [
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?",
    "What year did World War II end?",
    "Which ocean is the largest?"
]

options = [
    ["Paris", "London", "Berlin"],
    ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso"],
    ["Jupiter", "Saturn", "Mars"],
    ["1945", "1939", "1941"],
    ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean"]
]

correct_answers = ["Paris", "Leonardo da Vinci", "Jupiter", "1945", "Pacific Ocean"]

explanations = [
    "Paris is the capital of France.",
    "Leonardo da Vinci painted the Mona Lisa.",
    "Jupiter is the largest planet in our solar system.",
    "World War II ended in 1945.",
    "The Pacific Ocean is the largest ocean on Earth."
]

# Initialize variables for score and question index
score = 0

# Add dropdown menu for content selection
st.title("Quiz Time!")
content_type = st.selectbox("Select Content Type:", ["Text", "Youtube Video", "Document"])

# Add content based on selection
if content_type == "Text":
    st.text_input("Enter Text:")
elif content_type == "Youtube Video":
    st.text_input("Enter Youtube Video URL:")
elif content_type == "Document":
    uploaded_file = st.file_uploader("Upload Document:", type=['pdf'])

# Add button to generate quiz
if st.button("Generate Quiz"):
    with st.spinner("Generating Quiz..."):  # Display a spinner while generating the quiz
        time.sleep(2)  # Add a 2-second delay
        for i in range(len(questions)):
            st.header(f"Question {i + 1}: {questions[i]}")
            options_list = options[i]
            selected_option = st.radio(f"Select an option for Question {i + 1}:", options_list)
            if selected_option == correct_answers[i]:
                score += 1
                st.success("Correct!")
            else:
                st.error("Incorrect!")
            st.write(f"Explanation: {explanations[i]}")

        st.title("Quiz Completed!")
        st.write(f"You scored {score} out of {len(questions)}.")
