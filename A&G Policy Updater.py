import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("A&G Policy Update Automation")
        self.geometry(f"{1100}x{580}")
        # configure grid layout (4x4)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0, 0,), weight=1)

        # self.grid_columnconfigure((1, 1), weight=2)
        # self.grid_columnconfigure((2, 2), weight=2)
        # self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="A&G \n Policy Update \n Automation", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Scratch Card" )
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10,)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="E-PIN" )
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Scratch Card Platform", corner_radius=0)
        self.scrollable_frame.grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure((1,1), weight=2)
        self.scrollable_frame.grid_columnconfigure((2, 2), weight=2)
        self.scrollable_frame.grid_rowconfigure((0,1, 1), weight=1)
        self.scrollable_frame_switches = []


        # create radiobutton frame
        self.reg_correction_frame = customtkinter.CTkFrame(self.scrollable_frame, fg_color="blue")
        self.reg_correction_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0),  sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.reg_correction_frame, text="Reg Corrections")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        # create textbox
        self.reg_policy_number = customtkinter.CTkLabel(master=self.reg_correction_frame, text="Policy Number")
        self.reg_policy_number.grid(row=2, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.textbox = customtkinter.CTkTextbox(self.reg_correction_frame, width=200, height=10)
        self.textbox.grid(row=2, column=3, padx=(10, 0), pady=(10, 0), sticky="nsew")

        self.reg_policy_number = customtkinter.CTkLabel(master=self.reg_correction_frame, text="Reg Number")
        self.reg_policy_number.grid(row=3, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.textbox = customtkinter.CTkTextbox(self.reg_correction_frame, width=200, height=10)
        self.textbox.grid(row=3, column=3, padx=(10, 0), pady=(10, 0), sticky="nsew")

        # create radiobutton frame
        self.chassis_correction_frame = customtkinter.CTkFrame(self.scrollable_frame, fg_color="green")
        self.chassis_correction_frame.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.chassis_correction_frame, text="Chassis Corrections")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")

        # create textbox
        self.reg_policy_number = customtkinter.CTkLabel(master=self.chassis_correction_frame, text="Policy Number")
        self.reg_policy_number.grid(row=2, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.textbox = customtkinter.CTkTextbox(self.chassis_correction_frame, width=200, height=10)
        self.textbox.grid(row=2, column=3, padx=(10, 0), pady=(10, 0), sticky="nsew")

        self.reg_policy_number = customtkinter.CTkLabel(master=self.chassis_correction_frame, text="Chassis Number")
        self.reg_policy_number.grid(row=3, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.textbox = customtkinter.CTkTextbox(self.chassis_correction_frame, width=200, height=10)
        self.textbox.grid(row=3, column=3, padx=(10, 0), pady=(10, 0), sticky="nsew")

        self.reg_policy_number = customtkinter.CTkLabel(master=self.chassis_correction_frame, text="Reg Number")
        self.reg_policy_number.grid(row=4, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.textbox = customtkinter.CTkTextbox(self.chassis_correction_frame, width=200, height=10)
        self.textbox.grid(row=4, column=3, padx=(10, 0), pady=(10, 0), sticky="nsew")










    # def open_input_dialog_event(self):
    #     dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
    #     print("CTkInputDialog:", dialog.get_input())
    #
    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     customtkinter.set_appearance_mode(new_appearance_mode)
    #
    # def change_scaling_event(self, new_scaling: str):
    #     new_scaling_float = int(new_scaling.replace("%", "")) / 100
    #     customtkinter.set_widget_scaling(new_scaling_float)
    #
    # def sidebar_button_event(self):
    #     print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()