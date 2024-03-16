from tkinter import END
import customtkinter as ctk
from threading import Thread
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100
duration =5

ctk.set_appearance_mode("Dark")
ctk.set_window_scaling(0.7)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1024x720")
        self.title("Chat App")

        self.bind('<Return>',self.bt_send_com)

        self.list_person =[]
        self.list_chat =[]
        self.list_frames = []
        self.list_labels_info = []

        self.recording = 0
        self.index_chat =-1
        self.index_mode = 0 # 0==>text   1==>recoding  2==>stop record
        self.my_name = ''
        self.get_chats_Net()
      
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=5)

        self.upperFrame = ctk.CTkFrame(self,fg_color="#191919",corner_radius=0)
        self.upperFrame.grid(row=0,column=0,columnspan=2,sticky="nswe")

        self.upperFrame.grid_rowconfigure(0,weight=1)
        self.upperFrame.grid_columnconfigure((0,2,3),weight=0)
        self.upperFrame.grid_columnconfigure(1,weight=1)

        self.ch = ctk.CTkLabel(self.upperFrame, text=self.my_name[0], corner_radius=10,font=("arial",16,"bold"),height=30,width=30,fg_color="#03cc62")
        self.ch.grid(row=0,column=3,padx=10,pady=10,sticky="e")

        self.lbl_text = ctk.CTkLabel(self.upperFrame, text=self.my_name, font=("arial",15)) 
        self.lbl_text.grid(row =0 , column=2 ,pady=5,sticky="e")

        self.bt_logOut = ctk.CTkButton(self.upperFrame,text="Log Out",fg_color="#037562",height=30,width=100,command=self.bt_logout_com)
        self.bt_logOut.grid(row=0,column=1,pady=5,sticky="ws")


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

        self.headerFrame = ctk.CTkFrame(self.rightFrame,corner_radius=0,fg_color="#231aa3",height=0)
        self.headerFrame.grid(row=0,column=0,sticky="nswe")

        self.headerFrame.grid_rowconfigure(0,weight=1)
        self.headerFrame.grid_columnconfigure(0,weight=0)
        self.headerFrame.grid_columnconfigure(1,weight=1)

       # self.lblChatName = ctk.CTkLabel(self.headerFrame,text=self.list_person[self.index_chat]["name"],font=("arial",20,"bold"))
       # self.lblChatName.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        self.chatframe = ctk.CTkScrollableFrame(self.rightFrame,corner_radius=0,fg_color="#212222")
        self.chatframe.grid(row=1,column=0,sticky="nswe")
        self.chatframe.grid_columnconfigure(0,weight=1)
     
        self.footerFrame = ctk.CTkFrame(self.rightFrame,corner_radius=0,height=5)
        self.footerFrame.grid(row=2,column=0,sticky="nswe")

        self.footerFrame.grid_rowconfigure(0,weight=1)
        self.footerFrame.grid_columnconfigure(0,weight=1)
        self.footerFrame.grid_columnconfigure(1,weight=0)


        self.load_chats(self.list_person)
        self.init_chat(None, self.index_chat,self.list_chat[self.index_chat])


    def bt_logout_com(self):
        pass

    def bt_send_com(self,e=None):
         ent_user = self.ent.get()
         self.ent.delete(0,END)
         
         if self.index_mode == 0:
            if ent_user !='':
                
                self.bsk_frame = ctk.CTkFrame(self.chatframe,corner_radius=0,fg_color="transparent")
                self.bsk_frame.grid(row=len(self.list_frames),column=0,sticky='e')

                self.bsk_frame.grid_columnconfigure((0,1),weight=0)
                self.bsk_frame.grid_rowconfigure(0,weight=1)

                self.ch = ctk.CTkLabel(self.bsk_frame, text=self.my_name[0], corner_radius=10,font=("arial",20,"bold"),fg_color="#037562",height=30,width=30)
                self.ch.grid(row=0,column=1,padx=10,pady=10)

                self.frame_text = ctk.CTkFrame(self.bsk_frame,corner_radius=10,height=30)
                self.frame_text.grid(row=0,column=0,padx=10,pady=10)

                self.lbl_text = ctk.CTkLabel(self.frame_text, text=ent_user, font=("arial",15)) 
                self.lbl_text.pack(padx=10,pady=5)

                self.list_frames.append(self.bsk_frame)
                self.list_labels_info[self.index_chat].configure(text=ent_user)
                self.list_chat[self.index_chat].append({'M':ent_user})
            else:
                t1 = Thread(target=self.record_fcn)
                t1.start()
                self.btn_send.configure(text="Stop")
                self.index = 1
         elif self.index_mode == 1:
            print(self.recording)
            sd.stop()
            print(self.recording)
            wv.write("recording1.wav", self.recording, freq, sampwidth=2)
            self.index_mode = 2 

    def record_fcn(self):
        self.recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)



    def get_chats_Net(self):
        self.my_name = "Jalal Alsowat"
        self.list_person=[
       {
           "name": "jalal",
           "time": "8:26 PM"
       },
        {
           "name": "Ahmed",
           "time": "9:46 PM"
       },

        ]

        self.list_chat = [
         [{'H':'hello'},{'M':'hello'},{"H":"How are you?"},{"M":"I'm good thanks!"}],
        [{'H':'hello'},{'M':'hello'},{"H":"How old you?"},{"M":"15"}],
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
            self.lbl_ch.bind("<Button-1>", lambda e, a =i,chat=self.list_chat[i] : self.init_chat(e,a,chat))
            

            self.frameInfo = ctk.CTkFrame(self.basicFrame,corner_radius=0,fg_color="transparent")
            self.frameInfo.grid(row=0,column=1,sticky="nswe")
            self.frameInfo.bind("<Button-1>", lambda e, a =i,chat=self.list_chat[i] : self.init_chat(e,a,chat))

            self.frameInfo.grid_columnconfigure(0,weight=1)
            self.frameInfo.grid_rowconfigure((1,2,3),weight=0)
            self.frameInfo.grid_rowconfigure((0,4),weight=1)

            self.lbl_name = ctk.CTkLabel(self.frameInfo, text=ListPerson[i]["name"], font=("arial",18,"bold"))
            self.lbl_name.grid(row=1,column=0,sticky="w")
            self.lbl_name.bind("<Button-1>", lambda e, a =i,chat=self.list_chat[i] : self.init_chat(e,a,chat))
            

            self.lbl_info = ctk.CTkLabel(self.frameInfo, text=list(self.list_chat[i][-1].values())[0], font=("arial",15))
            self.lbl_info.grid(row=2,column=0,sticky="w")
            self.lbl_info.bind("<Button-1>", lambda e, a =i,chat=self.list_chat[i] : self.init_chat(e,a,chat))
            self.list_labels_info.append(self.lbl_info)

            self.lbl_time = ctk.CTkLabel(self.frameInfo, text=ListPerson[i]["time"], font=("arial",15))
            self.lbl_time.grid(row=3,column=0,sticky="w")
            self.lbl_time.bind("<Button-1>", lambda e, a =i,chat=self.list_chat[i] : self.init_chat(e,a,chat))

            self.lbl_divider =ctk.CTkFrame(self.basicFrame,fg_color="#1AA1BF",height=3)
            self.lbl_divider.grid(row=4,column=0,columnspan=2,sticky="nswe",padx=5,pady=5)


    def init_chat(self,e, index , list_chat):

        if self.index_chat==-1 and self.index_chat!=index:
           
            self.ent = ctk.CTkEntry(self.footerFrame,placeholder_text="Write here")
            self.ent.grid(row=0,column=0,padx=5,pady=10,sticky="nswe")

            self.btn_send = ctk.CTkButton(self.footerFrame,text="Send\Rec",font=("arial",18),command=self.bt_send_com)
            self.btn_send.grid(row=0,column=1,padx=5,pady=10)
        

          

        if self.index_chat != index:
            self.index_chat = index

            self.headerFrame.grid_forget()
            self.headerFrame = ctk.CTkFrame(self.rightFrame,corner_radius=0,fg_color="#231aa3",height=0)
            self.headerFrame.grid(row=0,column=0,sticky="nswe")
          
            self.ch = ctk.CTkLabel(self.headerFrame, text=self.list_person[index]["name"][0], corner_radius=10,font=("arial",16,"bold"),fg_color="#1AA1BF",height=30,width=30)
            self.ch.grid(row=0,column=0,padx=10,pady=10)

            self.lbl_text = ctk.CTkLabel(self.headerFrame, text=self.list_person[index]["name"], font=("arial",15)) 
            self.lbl_text.grid(row =0 , column=1 ,pady=5,sticky="w")
                      

            for i in range(len(self.list_frames)):
                    self.list_frames[i].grid_forget()
            self.list_frames = []


        
            for i in range(len(list_chat)):

                stick = "e"
                row_pos =1
                ch = self.my_name[0]
                color ="#037562"

                if list(list_chat[i].keys())[0]=="H":
                    stick = "w"
                    row_pos = 0
                    ch = self.list_person[index]["name"][0]
                    color = "#1AA1BF"



                self.bsk_frame = ctk.CTkFrame(self.chatframe,corner_radius=0,fg_color="transparent")
                self.bsk_frame.grid(row=i,column=0,sticky=stick)

                self.bsk_frame.grid_columnconfigure((0,1),weight=0)
                self.bsk_frame.grid_rowconfigure(0,weight=1)

                self.ch = ctk.CTkLabel(self.bsk_frame, text=ch, corner_radius=5,font=("arial",20,"bold"),fg_color=color,height=30,width=30)
                self.ch.grid(row=0,column=row_pos,padx=10,pady=10)

                self.frame_text = ctk.CTkFrame(self.bsk_frame,corner_radius=10,height=30)
                self.frame_text.grid(row=0,column=1- row_pos,padx=10,pady=10)

                self.lbl_text = ctk.CTkLabel(self.frame_text, text=list(list_chat[i].values())[0], font=("arial",15)) 
                self.lbl_text.pack(padx=10,pady=5)
                self.list_frames.append(self.bsk_frame)







if __name__ == "__main__":
    app =App()
    app.mainloop()



