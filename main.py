from tkinter import * 
from PIL import Image, ImageTk
from donnee import entrainer_ai
dico_neg, dico_pos = entrainer_ai()
def interface():
    nouvelle_couleur = "#FDF1B8"
    window = Tk()
    window.configure(bg= nouvelle_couleur)
    window.title("SentimentBot")
    window.geometry("900x700")
    emotion = ["Positif", "Negatif", "Neutre"]
    emotion_img = [None, None, None]
    color_emotion = [None,None,None]

    try :
        img_po_raw = Image.open("positif_emoji.png").resize((200, 200))
        img_neg_raw = Image.open("negatif_emoji.png").resize((200, 200))
        img_neu_raw = Image.open("neutre_emoji.png").resize((200, 200))

        # On transforme en PhotoImage pour Tkinter
        image_po = ImageTk.PhotoImage(img_po_raw)
        image_neg = ImageTk.PhotoImage(img_neg_raw)
        image_neu = ImageTk.PhotoImage(img_neu_raw)
        emotion_img = [image_po, image_neg, image_neu]
    except :
        print("L'initialisation des image a échoué. ")
    
    
    def analyser():
        score = 0
        phrase = my_entry.get().lower()
        



        mot_phrase = phrase.split()
        for mot in mot_phrase:
        # On récupère le nombre de fois où le mot a été vu
        # .get(mot, 0) permet de dire "donne moi la valeur, ou 0 si le mot est inconnu"
            points_pos = dico_pos.get(mot, 0)
            points_neg = dico_neg.get(mot, 0)
        score += (points_pos - points_neg)


        if score > 0:
            resultat = 0
            nouvelle_couleur = "#2ecc71"
        elif score < 0:
            resultat = 1
            nouvelle_couleur = "#e74c3c"
        else :
            resultat = 2
            nouvelle_couleur = "#3498db"

        label2.config(bg = nouvelle_couleur, text=emotion[resultat])
        window.configure(bg = nouvelle_couleur)
        label1.config(bg = nouvelle_couleur)
        my_entry.config(bg = nouvelle_couleur)
        button.config(bg = nouvelle_couleur)
        canva.config(bg = nouvelle_couleur, highlightbackground= nouvelle_couleur)
        
        if emotion_img[resultat]:
            canva.itemconfig(image_container, image=emotion_img[resultat])
            window.configure(bg = color_emotion[resultat])




    
    #entry pour taper la phrase
    my_entry = Entry(window, bg= "#FDF1B8", width=50, font=("Arial", 20))
    my_entry.place(x=400,y=100)
    #button
    button  = Button(window, bg="#FDF1B8", width= 20, font=("Arial", 20), text="Analyser", command=analyser)
    button.place(x=600, y=200)
    #first label
    label1= Label(window, bg="#FDF1B8", width= 50, font=("Arial", 20), text = "Le sentiment que vous ressentez est :")
    label1.place(x= 370, y=300)
    # second label
    label2 = Label(window, bg ="#FDF1B8", width= 50, font=("Arial", 20), text= "En attente...")
    label2.place(x=370, y=400)
    #canva
    canva = Canvas(window, bg = "#FDF1B8", width=400, height=300, highlightbackground="#FDF1B8")
    canva.place(x=570, y=450)
    image_container = canva.create_image(200, 150, image=None, anchor = CENTER)
    window.images_refs = emotion_img
    window.mainloop()
    

interface()