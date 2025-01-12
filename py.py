from pywebio.input import input, TEXT
from pywebio.output import put_text
from pywebio import start_server

def greet():
    # Take user input
    name = input("What's your name?", type=TEXT)
    
    # Display a greeting message
    put_text(f"Hello, {name}!")

# Start the PyWebIO server with the greet function
if __name__ == '__main__':
    start_server(greet, port=8080)