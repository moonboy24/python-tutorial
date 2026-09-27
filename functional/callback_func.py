

def on_btn_click(callback):
    print("Button Clicked")
    callback()
    
def show_msg():
    print("Hello , Welcome to Thailand")
    
on_btn_click(show_msg)