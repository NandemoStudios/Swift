from tkinter import *
import webbrowser

# Create a class for the application
class Application(Frame):
    # Create the application
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_toolbar()
    
    # Create the widgets
    def create_toolbar(self):
        # Create menu
        self.menu = Menu(self)
        self.master.config(menu=self.menu)

        # Create file section to menu
        self.file_menu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", state=DISABLED)
        self.file_menu.add_command(label="Open", state=DISABLED)
        self.file_menu.add_command(label="Save", state=DISABLED)
        self.file_menu.add_command(label="Save As", state=DISABLED)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.destroy)

        # Create edit section to menu
        self.edit_menu = Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", state=DISABLED)
        self.edit_menu.add_command(label="Redo", state=DISABLED)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", state=DISABLED)
        self.edit_menu.add_command(label="Copy", state=DISABLED)
        self.edit_menu.add_command(label="Paste", state=DISABLED)
        self.edit_menu.add_command(label="Delete", state=DISABLED)

        # Create view section to menu  
        self.view_menu = Menu(self.menu)
        self.menu.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Zoom In", state=DISABLED)
        self.view_menu.add_command(label="Zoom Out", state=DISABLED)
        self.view_menu.add_separator()
        self.view_menu.add_command(label="Full Screen", command=self.full_screen)
        self.view_menu.add_separator()
        self.view_menu.add_checkbutton(label="Dark Mode", command=self.dark_mode)
        self.view_menu.add_checkbutton(label="Show Line Numbers")

        # Create help section to menu
        self.help_menu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Help/About", command=self.help_about)
    
    # Create full screen function
    def full_screen(self):
        # Get the state of the window
        state = self.master.attributes("-fullscreen")
        # If the window is not full screen, make it full screen
        if state == False:
            self.master.attributes("-fullscreen", True)
        # If the window is full screen, make it not full screen
        else:
            self.master.attributes("-fullscreen", False)

    # Create help/about function
    def help_about(self):
        # Redirect the user the the github page
        webbrowser.open("https://github.com/NandemoStudios/Swift")
    
    # Create dark mode function
    def dark_mode(self):
        # Check if dark mode is enabled
        if self.view_menu.entrycget(6, "label") == "Dark Mode":
            # Change the label to light mode
            self.view_menu.entryconfigure(6, label="Light Mode")
            # Change the background color to black
            self.master.config(bg="gray")
        # If dark mode is not enabled
        else:
            # Change the label to dark mode
            self.view_menu.entryconfigure(6, label="Dark Mode")
            # Change the background color to white
            self.master.config(bg="white")
# Create the window
root = Tk()
root.title("Swift Engine")
root.geometry("1280x720")
#allow the window to be resizable
root.resizable(True, True)

# Create the application
app = Application(root)
root.mainloop()
