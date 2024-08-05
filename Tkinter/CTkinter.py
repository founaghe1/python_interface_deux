import customtkinter

COUNTER = 0
# Creation de la function incrementer()
def incrementer():
    global COUNTER
    if COUNTER <= 99:
        # Incrementation de la valeur de la variable
        COUNTER += 1
        # Change le text du comteur
        label.configure(text=f"Compteur = {COUNTER}")
        # Change le progessbar
        progressbar.set(COUNTER/100)
        message_label.configure(text="")
    elif COUNTER == 100:
        print("Vous avez atteind le seuil ! ")
        # le message d'erreur
        message_label.configure(text="Vous avez atteind le seuil !")
    
def decrementer():
    global COUNTER
    if COUNTER > 0:
        # Decrementation de la valeur de la variable
        COUNTER -= 1
        label.configure(text=f"Compteur = {COUNTER}")
        progressbar.set(COUNTER/100)
        message_label.configure(text="")
    else:
        print("Vous ne pouvez pas descendre en dessous de 0 ! ")
        message_label.configure(text="Vous ne pouvez pas descendre en dessous de 0 ! ")
        
# methode pour change le theme de l'aplication
def change_theme():
    if customtkinter.get_appearance_mode() == "Dark":
        customtkinter.set_appearance_mode("Light")
    else:
        customtkinter.set_appearance_mode("Dark")
        

# creation de l'application
app = customtkinter.CTk()

# Creation de l'apparence
# customtkinter.set_appearance_mode("system")  # default
# customtkinter.set_appearance_mode("dark")
# customtkinter.set_appearance_mode("light")

# creation du titre
app.title("Application Tkinter")

# creation de la dimansion
app.geometry("500x350")

# creation de label
label = customtkinter.CTkLabel(app, text="Compteur = 0")
# afficher le label
label.grid(row=0, column=0, pady=(30, 10))

# creation du progressbar
progressbar = customtkinter.CTkProgressBar(app, orientation='horizontal')
# l'initialisation du progressbar
progressbar.set(0)
# appeler le progressbar
progressbar.grid(row=1, column=0, pady=(20, 20))

# creation du button Increment
button = customtkinter.CTkButton(app, text="Incrementer", command=incrementer)
# Affichage du button
button.grid(row=2, column=0, pady=(20, 20))

# creation du button decrement
button = customtkinter.CTkButton(app, text="Decrementer", command=decrementer)
button.grid(row=3, column=0, pady=(10))

# Toggle switch pour changer le theme
theme = customtkinter.CTkSwitch(app, text="Change Thème", command=change_theme)
theme.grid(row=6, column=0, pady=(10, 10))

# Center les elements dans la fenetre
app.grid_columnconfigure(0, weight=1)

# Creer un label pour le message d'erreur
message_label = customtkinter.CTkLabel(app, text="", text_color="orange")
message_label.grid(row=5, column=0, pady=(10, 10))

# lancer l'apllication avec main_loop()
app.mainloop()

