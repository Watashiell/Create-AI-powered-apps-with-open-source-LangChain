import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain_openai import ChatOpenAI
openai_api_key = "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"
os.environ["OPENAI_API_KEY"] = openai_api_key
# Mendefinisikan model AI
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key= openai_api_key
)
# Mendefinisikan PromptTemplate sebagai format prompt untuk input dari user
prompt = PromptTemplate(
    input_variables=["hero"],
    template="Buatkan saya tutorial bermain hero Mobile Legends {hero}"
)
# Define a function to generate a cover letter using the llm and user input
def generate_cover_letter(hero: str) -> str:
    formatted_prompt = prompt.format(hero=hero)
    response = llm.invoke(formatted_prompt).content
    return response

# Define the Gradio interface inputs
inputs = [
    gr.Textbox(label="Hero"),
]
# Define the Gradio interface output
output = gr.Textbox(label="Tutorial Bermain Hero di Mobile Legends")
# Launch the Gradio interface
gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(server_name="0.0.0.0", server_port= 7860, share=True)