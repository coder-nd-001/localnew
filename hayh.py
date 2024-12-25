from tkinter import *
from PIL import Image, ImageTk

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0") 
        self.root.title("Inventory Management System | Developed By ND")
        self.root.config(bg="white")

        # Title with Logo Image
        self.icon_image = PhotoImage(file=r"C:\Users\Nagesh\Desktop\yash\images\logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_image, 
                      compound=LEFT, font=("times new roman", 40, "bold"), 
                      bg="#010c48", fg="white", anchor='w', padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # Logout Button
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), 
                            bg="green", cursor="hand2")
        btn_logout.place(x=1150, y=10, height=50, width=150)

        # Clock Label
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", 
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # Left Menu
        self.left_menuicon = Image.open(r"C:\Users\Nagesh\Desktop\yash\images\menu_im.png")
        self.left_menuicon = self.left_menuicon.resize((200, 200), Image.Resampling.LANCZOS)
        self.left_menuicon = ImageTk.PhotoImage(self.left_menuicon)

        leftMenue = Frame(self.root, bd=2, relief=RIDGE, bg='White')
        leftMenue.place(x=0, y=102, width=200, height=565)

        # Left Menu Logo
        lbl_menueLogo = Label(leftMenue, image=self.left_menuicon)
        lbl_menueLogo.pack(side=TOP, fill=X)

        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), 
                            bg="green", cursor="hand2")
        btn_logout.place(x=1150, y=10, height=50, width=150)


# Main Window Execution
root = Tk()
ob = IMS(root)
root.mainloop()
