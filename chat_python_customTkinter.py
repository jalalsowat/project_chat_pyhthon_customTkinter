import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_window_scaling(0.7)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1024x720")
        self.title("Chat App")
      
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=5)

        self.upperFrame = ctk.CTkFrame(self,fg_color="#191919",corner_radius=0)
        self.upperFrame.grid(row=0,column=0,columnspan=2,sticky="nswe")

        self.upperFrame.grid_rowconfigure(0,weight=1)


        self.lblLogo = ctk.CTkLabel(self.upperFrame,text="Chat App",font=("arial",22,"bold"))
        self.lblLogo.grid(row=0,column=0,padx=10,pady=10)

        self.leftFrame = ctk.CTkScrollableFrame(self,fg_color="#403F3F",corner_radius=0)
        self.leftFrame.grid(row=1,column=0,sticky="nswe")

        self.rightFrame = ctk.CTkFrame(self,fg_color="transparent",corner_radius=0)
        self.rightFrame.grid(row=1,column=1,sticky="nswe")

        self.rightFrame.grid_columnconfigure(0,weight=1)
        self.rightFrame.grid_rowconfigure((0,2),weight=0)
        self.rightFrame.grid_rowconfigure(1,weight=1)

        self.headerFrame = ctk.CTkFrame(self.rightFrame,corner_radius=0,fg_color="#212222")
        self.headerFrame.grid(row=0,column=0,sticky="nswe")

        self.headerFrame.grid_rowconfigure(0,weight=1)

        self.lblChatName = ctk.CTkLabel(self.headerFrame,text="Ahmed Ali",font=("arial",20,"bold"))
        self.lblChatName.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        self.chatframe = ctk.CTkScrollableFrame(self.rightFrame,corner_radius=0,fg_color="#212222")
        self.chatframe.grid(row=1,column=0,sticky="nswe")

        self.footerFrame = ctk.CTkFrame(self.rightFrame,corner_radius=0)
        self.footerFrame.grid(row=2,column=0,sticky="nswe")

        self.footerFrame.grid_rowconfigure(0,weight=1)
        self.footerFrame.grid_columnconfigure(0,weight=1)
        self.footerFrame.grid_columnconfigure(1,weight=0)

        self.ent = ctk.CTkEntry(self.footerFrame,placeholder_text="write here")
        self.ent.grid(row=0,column=0,padx=5,pady=10,sticky="nswe")

        self.btn_send = ctk.CTkButton(self.footerFrame,text="Send",font=("arial",18))
        self.btn_send.grid(row=0,column=1,padx=5,pady=10)








if __name__ == "__main__":
    app =App()
    app.mainloop()



