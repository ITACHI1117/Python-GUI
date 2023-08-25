import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("500x500")
app.title("CustomTkinter simple_example.py")


def login():
    print("Test")


frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand="True")

label = customtkinter.CTkLabel(master=frame, text="Login System",)
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password" )
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)


app.mainloop()