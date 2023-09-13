#created by Richard Tanner 9/13/2023
import tkinter as Tk
import tkinter.messagebox as TkMb
import customtkinter as cTk
import requests
import json

cTk.set_appearance_mode("dark") #Environment light mode: "Dark", "Light"
cTk.set_default_color_theme("blue") #Set color mode: Themes: "blue", "green", "dark-blue"

class App(cTk.CTk):
    def __init__(self):
        super().__init__()

        #configure the window
        self.title("Python Multi Select UI")
        self.geometry(f"{1200}x{700}")

        #configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)

        #create sidebar frame with widgets
        self.sidebar_frame = cTk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        
        self.logo_label = cTk.CTkLabel(self.sidebar_frame, text="Python Multi Select UI", font=cTk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20,10))
        
        #create the appearance mode label and options
        self.apperence_mode_label = cTk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.apperence_mode_label.grid(row=6, column=0, padx=20, pady=(10,0))
        self.apperence_mode_optionmenu = cTk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"], command=self.change_appearance_mode_event)
        self.apperence_mode_optionmenu.grid(row=7, column=0, padx=20, pady=(10,10))
        
        #create the scaling options and label
        self.scaling_label = cTk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10,0))
        self.scaling_optionmenu = cTk.CTkOptionMenu(self.sidebar_frame, values=["50%", "75%", "100%", "125%", "150%"], command=self.change_scaling_event)
        self.scaling_optionmenu.grid(row=9, column=0, padx=20, pady=(10,20))

        #create a textbox for the middle
        self.textbox = cTk.CTkTextbox(self, width=250, font=("serif", 20))
        self.textbox.grid(row=0, column=1, rowspan=2, padx=(20,0), pady=(20,0), sticky="nsew")

        #create tabview for right frame
        self.tabview = cTk.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, rowspan=2, padx=(20,0), pady=(20,0), sticky="nsew")
        self.tabview.add("Option 1")
        self.tabview.add("Option 2")
        self.tabview.add("Option 3")

        #create options under Option 1 Tab on right frame
        self.tabview.tab("Option 1").grid_columnconfigure(0, weight=1)
        self.optionmenu1 = cTk.CTkOptionMenu(self.tabview.tab("Option 1"), dynamic_resizing=False, values=["Sub-Option 1", "Sub-Option 2", "Sub-Option 3"])
        self.optionmenu1.grid(row=0, column=0, padx=20, pady=(20,10))
        self.option1_menu_button = cTk.CTkButton(self.tabview.tab("Option 1"), text="Click to Submit", command=self.option1_button_click_event)
        self.option1_menu_button.grid(row=2, column=0, padx=20, pady=(20,10))

        #create options under Option 2 Tab on right frame
        self.tabview.tab("Option 2").grid_columnconfigure(0, weight=1)
        self.label_radio_group = cTk.CTkLabel(self.tabview.tab("Option 2"), text="Radio Button Option")
        self.label_radio_group.grid(row=0, column=0, columnspan=1, padx=10, sticky="")
        self.radio_var = Tk.IntVar(value=0)
        self.radio_button1 = cTk.CTkRadioButton(self.tabview.tab("Option 2"), variable=self.radio_var, value=0, text="Radio Button 1", command=self.radiobutton1_click_event)
        self.radio_button1.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        self.radio_button2 = cTk.CTkRadioButton(self.tabview.tab("Option 2"), variable=self.radio_var, value=1, text="Radio Button 2", command=self.radiobutton2_click_event)
        self.radio_button2.grid(row=2, column=0, padx=20, pady=10, sticky="n")

        #set default values
        self.apperence_mode_optionmenu.set("Dark")
        self.scaling_optionmenu.set("100%")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        cTk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        cTk.set_widget_scaling(new_scaling_float)

    def option1_button_click_event(self):
        if self.optionmenu1.get() == "Sub-Option 1":
            self.textbox.delete("0.0","end")
            self.textbox.insert("0.0","You have selected Sub-Option 1 in this menu")
        elif self.optionmenu1.get() == "Sub-Option 2":
            self.textbox.delete("0.0","end")
            self.textbox.insert("0.0","You have selected Sub-Option 2 in this menu")
        elif self.optionmenu1.get() == "Sub-Option 3":
            self.textbox.delete("0.0","end")
            self.textbox.insert("0.0","You have selected Sub-Option 3 in this menu")

    def radiobutton1_click_event(self):
        self.textbox.delete("0.0","end")
        self.textbox.insert("0.0","You have selected Radio Button 1")
    
    def radiobutton2_click_event(self):
        self.textbox.delete("0.0","end")
        self.textbox.insert("0.0","You have selected Radio Button 2")

if __name__ =="__main__":
    app = App()
    app.mainloop()