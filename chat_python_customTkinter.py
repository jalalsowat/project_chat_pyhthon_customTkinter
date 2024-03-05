import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_window_scaling(0.7)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1024x720")
        self.title("Chat App")

        self.list_person =[]
        self.get_chats_Net()
      
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

        self.leftFrame.grid_columnconfigure(0,weight=1)

        self.rightFrame = ctk.CTkFrame(self,fg_color="transparent",corner_radius=0)
        self.rightFrame.grid(row=1,column=1,sticky="nswe")

        self.rightFrame.grid_columnconfigure(0,weight=1)
        self.rightFrame.grid_rowconfigure((0,2),weight=0)
        self.rightFrame.grid_rowconfigure(1,weight=1)

        self.headerFrame = ctk.CTkFrame(self.rightFrame,corner_radius=0,fg_color="#2B1123")
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

        self.ent = ctk.CTkEntry(self.footerFrame,placeholder_text="Write here")
        self.ent.grid(row=0,column=0,padx=5,pady=10,sticky="nswe")

        self.btn_send = ctk.CTkButton(self.footerFrame,text="Send",font=("arial",18))
        self.btn_send.grid(row=0,column=1,padx=5,pady=10)

        self.load_chats(self.list_person)

    def get_chats_Net(self):
        self.list_person=[
       {
           "name": "jalal",
           "info":"yes",
           "time": "8:26 PM"
       },
        {
           "name": "Ahmed",
           "info":"Yep",
           "time": "9:46 PM"
       },

        ]


    def load_chats(self,ListPerson):
        for i in range(len(ListPerson)):
            self.basicFrame = ctk.CTkFrame(self.leftFrame,corner_radius=0,fg_color="transparent",height=100)
            self.basicFrame.grid(row=i,column=0,sticky="nswe",pady=5)

            self.basicFrame.rowconfigure(0,weight=1)
            self.basicFrame.columnconfigure(0,weight=0)
            self.basicFrame.columnconfigure(1,weight=1)

            self.lbl_ch = ctk.CTkLabel(self.basicFrame, text=ListPerson[i]["name"][0], corner_radius=10,font=("arial",20,"bold"),fg_color="#1AA1BF",height=40,width=40)
            self.lbl_ch.grid(row=0,column=0,padx=10,pady=10,sticky="w")

            self.frameInfo = ctk.CTkFrame(self.basicFrame,corner_radius=0,fg_color="transparent")
            self.frameInfo.grid(row=0,column=1,sticky="nswe")

            self.frameInfo.grid_columnconfigure(0,weight=1)
            self.frameInfo.grid_rowconfigure((1,2,3),weight=0)
            self.frameInfo.grid_rowconfigure((0,4),weight=1)

            self.lbl_name = ctk.CTkLabel(self.frameInfo, text=ListPerson[i]["name"], font=("arial",18,"bold"))
            self.lbl_name.grid(row=1,column=0,sticky="w")

            self.lbl_info = ctk.CTkLabel(self.frameInfo, text=ListPerson[i]["info"], font=("arial",15))
            self.lbl_info.grid(row=2,column=0,sticky="w")

            self.lbl_time = ctk.CTkLabel(self.frameInfo, text=ListPerson[i]["time"], font=("arial",15))
            self.lbl_time.grid(row=3,column=0,sticky="w")

            self.lbl_divider =ctk.CTkFrame(self.basicFrame,fg_color="#1AA1BF",height=3)
            self.lbl_divider.grid(row=4,column=0,columnspan=2,sticky="nswe",padx=5,pady=5)








if __name__ == "__main__":
    app =App()
    app.mainloop()



