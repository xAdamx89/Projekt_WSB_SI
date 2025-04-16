import gradio as gr
from main import odczyt_OCR


demo = gr.Interface(
    fn=odczyt_OCR,
    inputs=gr.Image(type="pil", label="Przeciągnij zdjęcie z tekstem"),
    outputs=gr.Textbox(label="Odczytany tekst"),
    title="OCR - rozpoznawanie tekstu ze zdjęcia"
)


demo.launch(share=True)