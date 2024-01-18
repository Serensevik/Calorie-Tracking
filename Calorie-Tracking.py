from tkinter import *

def calculate():
    try:
        yas, cinsiyet, kilo, boy = int(yas_var.get()), gender_var.get(), float(kilo_var.get()), float(boy_var.get())
        c1, hm, wm, am = (66, 6.2 * boy, 12.7 * kilo, 6.76 * yas) if cinsiyet == 'Erkek' else (655.1, 4.35 * boy, 4.7 * kilo, 4.7 * yas)
        bmr_result = c1 + hm + wm - am
        aktivite_seviyesi = activity_level_var.get()
        aktivite_seviyesi = {'Sedanter': 1.2, 'Az Hareketli': 1.375, 'Orta Derece Hareketli': 1.55, 'Çok Hareketli': 1.725, 'Aşırı Hareketli': 1.9}.get(aktivite_seviyesi, 1) * bmr_result
        hedef = goal_var.get()
        hedefler = {'Zayıflamak': -500, 'Kilo Almak': 500, 'Hızlı Kilo Almak': 1000, 'Kiloyu Korumak': 0}
        kalori = aktivite_seviyesi + hedefler.get(hedef, 0)
        result_label.config(text=f'Günlük Alman gereken kalori miktarı: {int(kalori)}')
    except ValueError:
        result_label.config(text="Lütfen geçerli değerler girin.")

root = Tk()
root.title("KALORİ İHTİYACI HESAPLAMA")

# LabelFrame for Information
info_frame = LabelFrame(root, text="Kişisel Bilgiler", padx=20, pady=10)
info_frame.grid(row=0, column=0, padx=10, pady=10)

Label(info_frame, text="Yaş:").grid(row=0, column=0)
yas_var = StringVar()
Entry(info_frame, textvariable=yas_var).grid(row=0, column=1)

Label(info_frame, text="Cinsiyet:").grid(row=1, column=0)
gender_var = StringVar()
Radiobutton(info_frame, text="Erkek", variable=gender_var, value='Erkek').grid(row=1, column=1)
Radiobutton(info_frame, text="Kadın", variable=gender_var, value='Kadın').grid(row=1, column=2)

Label(info_frame, text="Kilo (kg):").grid(row=2, column=0)
kilo_var = StringVar()
Entry(info_frame, textvariable=kilo_var).grid(row=2, column=1)

Label(info_frame, text="Boy (cm):").grid(row=3, column=0)
boy_var = StringVar()
Entry(info_frame, textvariable=boy_var).grid(row=3, column=1)

# LabelFrame for Activity Level and Goal
activity_frame = LabelFrame(root, text="Aktivite Seviyesi ve Hedef", padx=20, pady=10)
activity_frame.grid(row=0, column=1, padx=10, pady=10)

Label(activity_frame, text="Aktivite Seviyesi:").grid(row=0, column=0)
activity_levels = ['Sedanter', 'Az Hareketli', 'Orta Derece Hareketli', 'Çok Hareketli', 'Aşırı Hareketli']
activity_level_var = StringVar()
activity_level_var.set(activity_levels[0])  # Default value
OptionMenu(activity_frame, activity_level_var, *activity_levels).grid(row=0, column=1)

Label(activity_frame, text="Hedef:").grid(row=1, column=0)
goals = ['Zayıflamak', 'Kilo Almak', 'Hızlı Kilo Almak', 'Kiloyu Korumak']
goal_var = StringVar()
goal_var.set(goals[0])  # Default value
OptionMenu(activity_frame, goal_var, *goals).grid(row=1, column=1)

# Button to calculate
Button(root, width=15, text="Hesapla", command=calculate).grid(row=1, column=0, columnspan=2, pady=20)

# Label to display result
result_label = Label(root, font=("Helvetica 15 bold"))
result_label.grid(row=2, column=0, columnspan=2, pady=[0, 20])

root.mainloop()
