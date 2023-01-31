'''
Autor ==> Mohammad Hasan Anisi
github page ==> https://github.com/mohammadhasananisi
telegram ==> https://t.me/mohammadhasananisi
Linkedin https://linkedin.com/in/mohammadhasan-anisi-159757202
'''
import tkinter as tk
import tkinter.ttk  as ttk
import tkinter.font as tkFont

from enigma_machine import Enigma


class App(tk.Frame):

    
    def __init__(self, master):
        super().__init__(master)
        master.resizable(width=False, height=False)
        self.font = tkFont.Font(family='Times',size=13)
        self.widgets(master)
    
    def widgets_plugboard(self, app):
         ### Plugboard Started
        self.plugboard_lable =tk.Label(text="Plugboard: ", font =self.font)
        self.plugboard_lable.pack()
        self.plugboard_lable.place(x=1,y=550,width=80,height=30)
        
        
        
        self.choiceVar_plugboard_1_1 = tk.StringVar()
        self.plugboard_list_1_1 = ttk.Combobox(textvariable=self.choiceVar_plugboard_1_1)
        self.plugboard_list_1_1.pack()
        self.plugboard_list_1_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_1_1.current(0)
        self.plugboard_list_1_1.place(x=80,y=550,width=40,height=25)
        self.choiceVar_plugboard_1_2 = tk.StringVar()
        self.plugboard_list_1_2 = ttk.Combobox(textvariable=self.choiceVar_plugboard_1_2)
        self.plugboard_list_1_2.pack()
        self.plugboard_list_1_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_1_2.current(19)
        self.plugboard_list_1_2.place(x=120,y=550,width=40,height=25)


        self.choiceVar_plugboard_2_1 = tk.StringVar()
        self.plugboard_list_2_1 = ttk.Combobox(textvariable=self.choiceVar_plugboard_2_1)
        self.plugboard_list_2_1.pack()
        self.plugboard_list_2_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_2_1.current(1)
        self.plugboard_list_2_1.place(x=200,y=550,width=40,height=25)
        self.choiceVar_plugboard_2_2 = tk.StringVar()
        self.plugboard_list_2_2 = ttk.Combobox(textvariable=self.choiceVar_plugboard_2_2)
        self.plugboard_list_2_2.pack()
        self.plugboard_list_2_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_2_2.current(18)
        self.plugboard_list_2_2.place(x=240,y=550,width=40,height=25)


        self.choiceVar_plugboard_3_1 = tk.StringVar()
        self.plugboard_list_3_1 = ttk.Combobox(textvariable=self.choiceVar_plugboard_3_1)
        self.plugboard_list_3_1.pack()
        self.plugboard_list_3_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_3_1.current(3)
        self.plugboard_list_3_1.place(x=320,y=550,width=40,height=25)
        self.choiceVar_plugboard_3_2 = tk.StringVar()
        self.plugboard_list_3_2 = ttk.Combobox(textvariable=self.choiceVar_plugboard_3_2)
        self.plugboard_list_3_2.pack()
        self.plugboard_list_3_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_3_2.current(4)
        self.plugboard_list_3_2.place(x=360,y=550,width=40,height=25)


        self.choiceVar_plugboard_4_1 = tk.StringVar()
        self.plugboard_list_4_1 = ttk.Combobox(textvariable=self.choiceVar_plugboard_4_1)
        self.plugboard_list_4_1.pack()
        self.plugboard_list_4_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_4_1.current(5)
        self.plugboard_list_4_1.place(x=440,y=550,width=40,height=25)
        self.choiceVar_plugboard_4_2 = tk.StringVar()
        self.plugboard_list_4_2 = ttk.Combobox(textvariable=self.choiceVar_plugboard_4_2)
        self.plugboard_list_4_2.pack()
        self.plugboard_list_4_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_4_2.current(12)
        self.plugboard_list_4_2.place(x=480,y=550,width=40,height=25)

        self.choiceVar_plugboard_5_1 = tk.StringVar()
        self.plugboard_list_5_1 = ttk.Combobox(textvariable=self.choiceVar_plugboard_5_1)
        self.plugboard_list_5_1.pack()
        self.plugboard_list_5_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_5_1.current(8)
        self.plugboard_list_5_1.place(x=560,y=550,width=40,height=25)
        self.choiceVar_plugboard_5_2 = tk.StringVar()
        self.plugboard_list_5_2 = ttk.Combobox(textvariable=self.choiceVar_plugboard_5_2)
        self.plugboard_list_5_2.pack()
        self.plugboard_list_5_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_5_2.current(17)
        self.plugboard_list_5_2.place(x=600,y=550,width=40,height=25)


        self.choiceVar_plugboard_6_1 = tk.StringVar()
        self.plugboard_list_6_1 = ttk.Combobox(textvariable=self.choiceVar_plugboard_6_1)
        self.plugboard_list_6_1.pack()
        self.plugboard_list_6_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_6_1.current(10)
        self.plugboard_list_6_1.place(x=80,y=600,width=40,height=25)
        self.choiceVar_plugboard_6_2 = tk.StringVar()
        self.plugboard_list_6_2 = ttk.Combobox(textvariable=self.choiceVar_plugboard_6_2)
        self.plugboard_list_6_2.pack()
        self.plugboard_list_6_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_6_2.current(13)
        self.plugboard_list_6_2.place(x=120,y=600,width=40,height=25)


        self.choiceVar_plugboard_7_1 = tk.StringVar()
        self.plugboard_list_7_1 = ttk.Combobox(textvariable=self.choiceVar_plugboard_7_1)
        self.plugboard_list_7_1.pack()
        self.plugboard_list_7_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_7_1.current(11)
        self.plugboard_list_7_1.place(x=200,y=600,width=40,height=25)
        self.choiceVar_plugboard_7_2 = tk.StringVar()
        self.plugboard_list_7_2 = ttk.Combobox(textvariable=self.choiceVar_plugboard_7_2)
        self.plugboard_list_7_2.pack()
        self.plugboard_list_7_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_7_2.current(25)
        self.plugboard_list_7_2.place(x=240,y=600,width=40,height=25)


        self.choiceVar_plugboard_8_1 = tk.StringVar()
        self.plugboard_list_8_1 = ttk.Combobox(textvariable=self.choiceVar_plugboard_8_1)
        self.plugboard_list_8_1.pack()
        self.plugboard_list_8_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_8_1.current(14)
        self.plugboard_list_8_1.place(x=320,y=600,width=40,height=25)
        self.choiceVar_plugboard_8_2 = tk.StringVar()
        self.plugboard_list_8_2 = ttk.Combobox(textvariable=self.choiceVar_plugboard_8_2)
        self.plugboard_list_8_2.pack()
        self.plugboard_list_8_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_8_2.current(22)
        self.plugboard_list_8_2.place(x=360,y=600,width=40,height=25)


        self.choiceVar_plugboard_9_1 = tk.StringVar()
        self.plugboard_list_9_1 = ttk.Combobox(textvariable=self.choiceVar_plugboard_9_1)
        self.plugboard_list_9_1.pack()
        self.plugboard_list_9_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_9_1.current(15)
        self.plugboard_list_9_1.place(x=440,y=600,width=40,height=25)
        self.choiceVar_plugboard_9_2 = tk.StringVar()
        self.plugboard_list_9_2 = ttk.Combobox(textvariable=self.choiceVar_plugboard_9_2)
        self.plugboard_list_9_2.pack()
        self.plugboard_list_9_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_9_2.current(21)
        self.plugboard_list_9_2.place(x=480,y=600,width=40,height=25)


        self.choiceVar_plugboard_10_1 = tk.StringVar()
        self.plugboard_list_10_1 = ttk.Combobox(textvariable=self.choiceVar_plugboard_10_1)
        self.plugboard_list_10_1.pack()
        self.plugboard_list_10_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_10_1.current(23)
        self.plugboard_list_10_1.place(x=560,y=600,width=40,height=25)
        self.choiceVar_plugboard_10_2 = tk.StringVar()
        self.plugboard_list_10_2 = ttk.Combobox(textvariable=self.choiceVar_plugboard_10_2)
        self.plugboard_list_10_2.pack()
        self.plugboard_list_10_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.plugboard_list_10_2.current(24)
        self.plugboard_list_10_2.place(x=600,y=600,width=40,height=25)
        # End

    def widgets(self, app):

        self.lable_input = tk.Label(text="Enter Text or Code text", font=('Times', 24))
        self.lable_input.pack(padx=20, pady=20)
        # self.lable_input.place(x=50, y=330, width=70, height=25)


        self.input_code_or_str = tk.Entry(font=('Times', 24), width=40,)
        self.input_code_or_str.pack()
        self.contents = tk.StringVar()
        self.input_code_or_str["textvariable"] = self.contents


        self.input_code_or_str.bind('<Key-Return>', self.enigma_con)

        self.lable_result = tk.Label(text="", font=("Times", 22), height=5)
        self.lable_result.pack()

       
        

        self.btn_handeler = tk.Button(text="Convert", font=("Times", 20))
        self.btn_handeler.pack()
        self.btn_handeler.config(command=self.enigma_con)


        


        self.reflector_lable=tk.Label(text="Reflector", justify="center", font =self.font)
        self.reflector_lable.pack()
        self.reflector_lable.place(x=50,y=330,width=70,height=25)


        self.choiceVar_reflector_list = tk.StringVar()
        self.reflector_list = ttk.Combobox(textvariable=self.choiceVar_reflector_list)
        self.reflector_list.pack()
        self.reflector_list['values'] = ("UKW-B", "UKW-C")
        self.reflector_list.current(0)
        self.reflector_list.place(x=120,y=330,width=80,height=25)
        



        self.rotor_lable =tk.Label(text="Rotor", font =self.font)
        self.rotor_lable.pack()
        self.rotor_lable.place(x=200,y=360,width=70,height=25)

        self.choiceVar_rotor_list_1 = tk.StringVar()
        self.rotor_list_1 = ttk.Combobox(textvariable=self.choiceVar_rotor_list_1)
        self.rotor_list_1.pack()
        self.rotor_list_1['values'] = ('I', 'II', 'III', 'IV', 'V')
        self.rotor_list_1.current(0)
        self.rotor_list_1.place(x=300,y=360,width=80,height=25)
        
        self.choiceVar_rotor_list_2 = tk.StringVar()
        self.rotor_list_2 = ttk.Combobox(textvariable=self.choiceVar_rotor_list_2)
        self.rotor_list_2.pack()
        self.rotor_list_2['values'] = ('I', 'II', 'III', 'IV', 'V')
        self.rotor_list_2.current(1)
        self.rotor_list_2.place(x=400,y=360,width=80,height=25)

        self.choiceVar_rotor_list_3 = tk.StringVar()
        self.rotor_list_3 = ttk.Combobox(textvariable=self.choiceVar_rotor_list_3)
        self.rotor_list_3.pack()
        self.rotor_list_3['values'] = ('I', 'II', 'III', 'IV', 'V')
        self.rotor_list_3.current(2)
        self.rotor_list_3.place(x=500,y=360,width=80,height=25)
        



        self.ring_setting_lable =tk.Label(text="Ring Setting", font =self.font)
        self.ring_setting_lable.pack()
        self.ring_setting_lable.place(x=200,y=410,width=100,height=30)
        

        self.choiceVar_ring_ring_setting_list_1 = tk.StringVar()
        self.ring_setting_list_1 = ttk.Combobox(textvariable=self.choiceVar_ring_ring_setting_list_1)
        self.ring_setting_list_1.pack()
        self.ring_setting_list_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.ring_setting_list_1.current(0)
        self.ring_setting_list_1.place(x=300,y=420,width=80,height=25)
        

        self.choiceVar_ring_ring_setting_list_2 = tk.StringVar()
        self.ring_setting_list_2 = ttk.Combobox(textvariable=self.choiceVar_ring_ring_setting_list_2)
        self.ring_setting_list_2.pack()
        self.ring_setting_list_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.ring_setting_list_2.current(1)
        self.ring_setting_list_2.place(x=400,y=420,width=80,height=25)
        
        
        self.choiceVar_ring_ring_setting_list_3 = tk.StringVar()
        self.ring_setting_list_3 = ttk.Combobox(textvariable=self.choiceVar_ring_ring_setting_list_3)
        self.ring_setting_list_3.pack()
        self.ring_setting_list_3['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.ring_setting_list_3.current(2)
        self.ring_setting_list_3.place(x=500,y=420,width=80,height=25)
        



        self.initial_position_lable =tk.Label(text="Initial Position", font =self.font)
        self.initial_position_lable.pack()
        self.initial_position_lable.place(x=200,y=480,width=100,height=30)
        
        
        self.choiceVar_initial_position_list_1 = tk.StringVar()
        self.initial_position_list_1 = ttk.Combobox(textvariable=self.choiceVar_initial_position_list_1)
        self.initial_position_list_1.pack()
        self.initial_position_list_1['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.initial_position_list_1.current(3)
        self.initial_position_list_1.place(x=300,y=480,width=80,height=25)
        

        self.choiceVar_initial_position_list_2 = tk.StringVar()
        self.initial_position_list_2 = ttk.Combobox(textvariable=self.choiceVar_initial_position_list_2)
        self.initial_position_list_2.pack()
        self.initial_position_list_2['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.initial_position_list_2.current(4)
        self.initial_position_list_2.place(x=400,y=480,width=80,height=25)
        

        self.choiceVar_initial_position_list_3 = tk.StringVar()
        self.initial_position_list_3 = ttk.Combobox(textvariable=self.choiceVar_initial_position_list_3)
        self.initial_position_list_3.pack()
        self.initial_position_list_3['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        self.initial_position_list_3.current(5)
        self.initial_position_list_3.place(x=500,y=480,width=80,height=25)
        

        

        self.top_Rotor_lable_1=tk.Label(text="1 st Rotor:", font =self.font)
        self.top_Rotor_lable_1.pack()
        self.top_Rotor_lable_1.place(x=300,y=320,width=91,height=30)
        

        self.top_Rotor_lable_2=tk.Label(text="2 nd Rotor:", font =self.font)
        self.top_Rotor_lable_2.pack()
        self.top_Rotor_lable_2.place(x=400,y=320,width=88,height=30)
        

        self.top_Rotor_lable_3=tk.Label(text="3 rd Rotor:", font =self.font)
        self.top_Rotor_lable_3.pack()
        self.top_Rotor_lable_3.place(x=500,y=320,width=91,height=30)

        
        self.widgets_plugboard(app=app)



    
    def enigma_con(self, ev=None):
        plugboard = self.choiceVar_plugboard_1_1.get() + self.choiceVar_plugboard_1_2.get() + " "
        plugboard += self.choiceVar_plugboard_2_1.get() + self.choiceVar_plugboard_2_2.get() + " "

        plugboard += self.choiceVar_plugboard_3_1.get() + self.choiceVar_plugboard_3_2.get() + " "
        
        plugboard += self.choiceVar_plugboard_4_1.get() + self.choiceVar_plugboard_4_2.get() + " "

        plugboard += self.choiceVar_plugboard_5_1.get() + self.choiceVar_plugboard_5_2.get() + " "
        
        plugboard += self.choiceVar_plugboard_6_1.get() + self.choiceVar_plugboard_6_2.get() + " "

        plugboard += self.choiceVar_plugboard_7_1.get() + self.choiceVar_plugboard_7_2.get() + " "

        plugboard += self.choiceVar_plugboard_8_1.get() + self.choiceVar_plugboard_8_2.get() + " "

        plugboard += self.choiceVar_plugboard_9_1.get() + self.choiceVar_plugboard_9_2.get() + " "

        plugboard += self.choiceVar_plugboard_10_1.get() + self.choiceVar_plugboard_10_2.get()

        a = Enigma(
            rotors= (self.choiceVar_rotor_list_1.get(), self.choiceVar_rotor_list_2.get(), self.choiceVar_rotor_list_3.get()),
            reflector= self.choiceVar_reflector_list.get(),
            ringSettings= self.choiceVar_ring_ring_setting_list_1.get() + self.choiceVar_ring_ring_setting_list_2.get() + self.choiceVar_ring_ring_setting_list_3.get(),
            ringPositions= self.choiceVar_initial_position_list_1.get() + self.choiceVar_initial_position_list_2.get() + self.choiceVar_initial_position_list_3.get(), 
            plugboard= plugboard)
        
        self.lable_result.config(text=a.encode(self.contents.get()))


app = tk.Tk(className="Enigma Machine")
app.geometry("750x650")
myapp = App(app)
myapp.mainloop()