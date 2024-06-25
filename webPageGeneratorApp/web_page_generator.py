import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #creates button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        #positions button
        self.btn.grid(row=2, column=1, padx=(200,0), pady=(20,15))
        #creates button
        self.submit_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        #positions button
        self.submit_btn.grid(row=2, column=2, padx=(10,40), pady=(20,15))

        #label for input
        self.lbl_input = tk.Label(self.master,text='Enter custom text or click the Default HTML page button')
        self.lbl_input.grid(row=0, column=0, padx=(20,0), pady=(20,0), sticky=N+W)

        #text entry box
        self.txt_input = tk.Entry(self.master,text='')
        self.txt_input.grid(row=1, column=0, rowspan=1, columnspan=3, padx=(30,40), pady=(0,0), sticky=N+E+W)

    #Function to generate default HTML page
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    #Function to generate custom HTML page
    def customHTML(self):
        # Get the user input from the text entry box
        customText = self.txt_input.get()
        # Open an HTML file in write mode
        htmlFile = open("index.html", "w")
        # Write the HTML content with the custom text
        htmlContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        # Open the generated HTML page in a new browser tab
        webbrowser.open_new_tab("index.html")





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
