import textwrap

def formatted_text(text,width):
    print(textwrap.fill(text,width))

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut."
formatted_text(text,50)