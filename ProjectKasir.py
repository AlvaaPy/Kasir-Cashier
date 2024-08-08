import string
from tkinter import *
import random
import time
from tkinter import messagebox
from tkinter import filedialog



# Membuat Frame aplikasi
root = Tk()

root.geometry("1275x720")  # menentukan ukuran window aplikasi
root.resizable(0, 0)
root.title("Cafe Amerysa Usyara")  # nama aplikasi

topFrame = Frame(root, bd=10, relief=RIDGE, bg='white')  # frame judul
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='Cafe Amerysa Usyara', font=('Montserrat', 25, 'bold'), fg='#b0b0b0', bg='#000000', bd=10,
                   width=60)  # judul aplikasi
labelTitle.grid(row=0, column=10)

root.config(bg='#FFFFFF')  # warna dasar / background

# VARIABLE
# Menentukan variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

# variabel menu brunch
e_sandwich = StringVar()
e_croissant = StringVar()
e_waffle = StringVar()
e_salad = StringVar()
e_burger = StringVar()
e_omelets = StringVar()
e_quiche = StringVar()
e_avocadotoast = StringVar()
e_tomatosoup = StringVar()

# variabel menu minuman
e_kopihitam = StringVar()
e_lemontea = StringVar()
e_milktea = StringVar()
e_espresso = StringVar()
e_cappucino = StringVar()
e_airmineral = StringVar()
e_americano = StringVar()
e_tea = StringVar()
e_latte = StringVar()

# variabel menu dessert
e_eskrim = StringVar()
e_cheesecake = StringVar()
e_brownies = StringVar()
e_pudding = StringVar()
e_tiramisu = StringVar()
e_pancake = StringVar()
e_cremebrulee = StringVar()
e_applepie = StringVar()
e_churros = StringVar()

# variabel Harga dalam struk
hargadaribrunchvar = StringVar()
hargadariminumanvar = StringVar()
hargadaridessertvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()
taxvaluevar = StringVar()

e_sandwich.set('0')
e_croissant.set('0')
e_waffle.set('0')
e_salad.set('0')
e_burger.set('0')
e_omelets.set('0')
e_quiche.set('0')
e_avocadotoast.set('0')
e_tomatosoup.set('0')

e_kopihitam.set('0')
e_lemontea.set('0')
e_milktea.set('0')
e_espresso.set('0')
e_cappucino.set('0')
e_airmineral.set('0')
e_americano.set('0')
e_tea.set('0')
e_latte.set('0')

e_eskrim.set('0')
e_cheesecake.set('0')
e_brownies.set('0')
e_pudding.set('0')
e_tiramisu.set('0')
e_pancake.set('0')
e_cremebrulee.set('0')
e_applepie.set('0')
e_churros.set('0')

# FUNGSI
# Awal fungsi perhitungan harga total
tax = (10 / 100)


def totalcost():
    # mengglobalkan beberapa variable terlebih dahulu
    global hargadaribrunch, hargadariminuman, hargadaridessert, subtotalItems, totaltax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
            var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
            var26.get() != 0 or var27.get() != 0:

        item1 = int(e_sandwich.get())
        item2 = int(e_croissant.get())
        item3 = int(e_waffle.get())
        item4 = int(e_salad.get())
        item5 = int(e_burger.get())
        item6 = int(e_omelets.get())
        item7 = int(e_quiche.get())
        item8 = int(e_avocadotoast.get())
        item9 = int(e_tomatosoup.get())

        item10 = int(e_kopihitam.get())
        item11 = int(e_lemontea.get())
        item12 = int(e_milktea.get())
        item13 = int(e_espresso.get())
        item14 = int(e_cappucino.get())
        item15 = int(e_airmineral.get())
        item16 = int(e_americano.get())
        item17 = int(e_tea.get())
        item18 = int(e_latte.get())

        item19 = int(e_eskrim.get())
        item20 = int(e_cheesecake.get())
        item21 = int(e_brownies.get())
        item22 = int(e_pudding.get())
        item23 = int(e_tiramisu.get())
        item24 = int(e_pancake.get())
        item25 = int(e_cremebrulee.get())
        item26 = int(e_applepie.get())
        item27 = int(e_churros.get())

        hargadaribrunch = (item1 * 20000) + (item2 * 25000) + (item3 * 18000) + (item4 * 25000) + (item5 * 35000) + \
                          (item6 * 22000) + (item7 * 30000) + (item8 * 27000) + (item9 * 26000)
        hargadariminuman = (item10 * 15000) + (item11 * 15000) + (item12 * 15000) + (item13 * 15000) + \
                           (item14 * 20000) + (item15 * 10000) + (item16 * 20000) + (item17 * 10000) + \
                           (item18 * 20000)
        hargadaridessert = (item19 * 18000) + (item20 * 25000) + (item21 * 20000) + (item22 * 20000) + \
                           (item23 * 28000) + (item24 * 21000) + (item25 * 23000) + (item26 * 22000) + \
                           (item27 * 30000)

        hargadaribrunchvar.set(str(hargadaribrunch))
        hargadariminumanvar.set(str(hargadariminuman))
        hargadaridessertvar.set(str(hargadaridessert))

        subtotalItems = hargadaribrunch + hargadariminuman + hargadaridessert
        subtotalvar.set(str(subtotalItems))

        #tax=(10/100)
        taxvaluevar.set(str(tax))
        totaltax = subtotalItems * tax

        servicetaxvar.set(totaltax)

        totalcost = subtotalItems + totaltax
        totalcostvar.set(str(totalcost))
    else:
        messagebox.showerror('Error', 'Tidak ada item yang dipilih')


# Batas fungsi perhitungan harga total
def struk():
    global billnumber, date
    if hargadaribrunchvar.get() != '' or hargadaridessertvar.get() != '' or hargadariminumanvar.get() != '':
        textStruk.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')
        textStruk.insert(END, 'Resep Ref:\t        ' + billnumber + '\t         ' + date + '\n')
        textStruk.insert(END, '******************\n')
        textStruk.insert(END, 'Items:\t\t          Harga Total (Rp)\n')
        textStruk.insert(END, '******************\n')
        if e_sandwich.get() != '0':
            textStruk.insert(END, f'sandwich\t\t\tRp. {int(e_sandwich.get()) * 20000}\n\n')

        if e_croissant.get() != '0':
            textStruk.insert(END, f'croissant\t\t\tRp. {int(e_croissant.get()) * 25000}\n\n')

        if e_waffle.get() != '0':
            textStruk.insert(END, f'waffle\t\t\tRp. {int(e_waffle.get()) * 18000}\n\n')

        if e_salad.get() != '0':
            textStruk.insert(END, f'salad\t\t\tRp. {int(e_salad.get()) * 25000}\n\n')

        if e_burger.get() != '0':
            textStruk.insert(END, f'burger\t\t\tRp. {int(e_burger.get()) * 35000}\n\n')

        if e_omelets.get() != '0':
            textStruk.insert(END, f'omelets\t\t\tRp. {int(e_omelets.get()) * 22000}\n\n')

        if e_quiche.get() != '0':
            textStruk.insert(END, f'quiche\t\t\tRp. {int(e_quiche.get()) * 30000}\n\n')

        if e_avocadotoast.get() != '0':
            textStruk.insert(END, f'avocado toast\t\t\tRp. {int(e_avocadotoast.get()) * 27000}\n\n')

        if e_tomatosoup.get() != '0':
            textStruk.insert(END, f'tomato soup\t\t\tRp. {int(e_tomatosoup.get()) * 26000}\n\n')

        if e_kopihitam.get() != '0':
            textStruk.insert(END, f'kopi hitam\t\t\tRp. {int(e_kopihitam.get()) * 15000}\n\n')

        if e_lemontea.get() != '0':
            textStruk.insert(END, f'lemon tea\t\t\tRp. {int(e_lemontea.get()) * 15000}\n\n')

        if e_milktea.get() != '0':
            textStruk.insert(END, f'milk tea\t\t\tRp. {int(e_milktea.get()) * 15000}\n\n')

        if e_espresso.get() != '0':
            textStruk.insert(END, f'espresso\t\t\tRp. {int(e_espresso.get()) * 15000}\n\n')

        if e_cappucino.get() != '0':
            textStruk.insert(END, f'cappucino\t\t\tRp. {int(e_cappucino.get()) * 20000}\n\n')

        if e_airmineral.get() != '0':
            textStruk.insert(END, f'air mineral\t\t\tRp. {int(e_airmineral.get()) * 10000}\n\n')

        if e_americano.get() != '0':
            textStruk.insert(END, f'americano\t\t\tRp. {int(e_americano.get()) * 20000}\n\n')

        if e_tea.get() != '0':
            textStruk.insert(END, f'tea\t\t\tRp. {int(e_tea.get()) * 10000}\n\n')

        if e_latte.get() != '0':
            textStruk.insert(END, f'latte\t\t\tRp. {int(e_latte.get()) * 20000}\n\n')

        if e_eskrim.get() != '0':
            textStruk.insert(END, f'es krim\t\t\tRp. {int(e_eskrim.get()) * 18000}\n\n')

        if e_cheesecake.get() != '0':
            textStruk.insert(END, f'cheesecake\t\t\tRp. {int(e_cheesecake.get()) * 25000}\n\n')

        if e_brownies.get() != '0':
            textStruk.insert(END, f'brownies\t\t\tRp. {int(e_brownies.get()) * 20000}\n\n')

        if e_pudding.get() != '0':
            textStruk.insert(END, f'pudding\t\t\tRp. {int(e_pudding.get()) * 20000}\n\n')

        if e_tiramisu.get() != '0':
            textStruk.insert(END, f'tiramisu\t\t\tRp. {int(e_tiramisu.get()) * 28000}\n\n')

        if e_pancake.get() != '0':
            textStruk.insert(END, f'pancake\t\t\tRp. {int(e_pancake.get()) * 21000}\n\n')

        if e_cremebrulee.get() != '0':
            textStruk.insert(END, f'creme brulee\t\t\tRp. {int(e_cremebrulee.get()) * 23000}\n\n')

        if e_applepie.get() != '0':
            textStruk.insert(END, f'apple pie\t\t\tRp. {int(e_applepie.get()) * 22000}\n\n')

        if e_churros.get() != '0':
            textStruk.insert(END, f'churros\t\t\tRp. {int(e_churros.get()) * 30000}\n\n')

        textStruk.insert(END, '******************\n')
        if hargadaribrunchvar.get() != 'Rp 0':
            textStruk.insert(END, f'Harga makanan\t\t\tRp. {hargadaribrunch}\n\n')
        if hargadariminumanvar.get() != 'Rp 0':
            textStruk.insert(END, f'Harga minuman\t\t\tRp. {hargadariminuman}\n\n')
        if hargadaridessertvar.get() != 'Rp 0':
            textStruk.insert(END, f'Harga jajanan\t\t\tRp. {hargadaridessert}\n\n')

        textStruk.insert(END, f'Sub Total\t\t\tRp. {subtotalItems}\n\n')
        textStruk.insert(END, f'Service Tax\t\t\tRp. {totaltax}\n\n')
        textStruk.insert(END, f'Harga total\t\t\tRP. {subtotalItems + totaltax}\n\n')
        textStruk.insert(END, '******************\n')
        textStruk.insert(END, 'Terima kasih telah mengunjungi Cafe kami!')
    else:
        messagebox.showerror('Error', 'Tidak ada item yang dipilih')


# Batas fungsi cetak struk

# awal fungsi simpan dalam perangkat
def save():
    if textStruk.get(1.0, END) == '\n':
        pass
    else:
        # HANYA DALAM EXTENSION FILE .txt
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None:
            pass
        else:

            bill_data = textStruk.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Informasi', 'Struk Anda berhasil disimpan')


# Batas fungsi simpan dalam perangkat

# awal fungsi reset
def reset():
    textStruk.delete(1.0, END)
    e_croissant.set('0')
    e_waffle.set('0')
    e_salad.set('0')
    e_burger.set('0')
    e_omelets.set('0')
    e_quiche.set('0')
    e_avocadotoast.set('0')
    e_avocadotoast.set('0')
    e_tomatosoup.set('0')

    e_kopihitam.set('0')
    e_lemontea.set('0')
    e_milktea.set('0')
    e_espresso.set('0')
    e_cappucino.set('0')
    e_airmineral.set('0')
    e_americano.set('0')
    e_tea.set('0')
    e_latte.set('0')

    e_eskrim.set('0')
    e_cheesecake.set('0')
    e_brownies.set('0')
    e_pudding.set('0')
    e_tiramisu.set('0')
    e_pancake.set('0')
    e_cremebrulee.set('0')
    e_applepie.set('0')
    e_churros.set('0')
    # batas untuk variables

    textsandwich.config(state=DISABLED)
    textcroissant.config(state=DISABLED)
    textwaffle.config(state=DISABLED)
    textsalad.config(state=DISABLED)
    textburger.config(state=DISABLED)
    textomelets.config(state=DISABLED)
    textquiche.config(state=DISABLED)
    textavocadotoast.config(state=DISABLED)
    texttomatosoup.config(state=DISABLED)

    textkopihitam.config(state=DISABLED)
    textlemontea.config(state=DISABLED)
    textmilktea.config(state=DISABLED)
    textespresso.config(state=DISABLED)
    textcappucino.config(state=DISABLED)
    textairmineral.config(state=DISABLED)
    textamericano.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textlatte.config(state=DISABLED)

    texteskrim.config(state=DISABLED)
    textcheesecake.config(state=DISABLED)
    textbrownies.config(state=DISABLED)
    textpudding.config(state=DISABLED)
    texttiramisu.config(state=DISABLED)
    textpancake.config(state=DISABLED)
    textcremebrulee.config(state=DISABLED)
    textapplepie.config(state=DISABLED)
    textchurros.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    hargadariminumanvar.set('')
    hargadaribrunchvar.set('')
    hargadaridessertvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    taxvaluevar.set('')


# batas fungsi reset

# mengaktifkan fungsi entry brunch
def sandwich():
    if var1.get() == 1:
        textsandwich.config(state=NORMAL)
        textsandwich.delete(0, END)
        textsandwich.focus()
    else:
        textsandwich.config(state=DISABLED)
        e_sandwich.set('0')


def croissant():
    if var2.get() == 1:
        textcroissant.config(state=NORMAL)
        textcroissant.delete(0, END)
        textcroissant.focus()
    else:
        textcroissant.config(state=DISABLED)
        e_croissant.set('0')


def waffle():
    if var3.get() == 1:
        textwaffle.config(state=NORMAL)
        textwaffle.delete(0, END)
        textwaffle.focus()
    else:
        textwaffle.config(state=DISABLED)
        e_waffle.set('0')


def salad():
    if var4.get() == 1:
        textsalad.config(state=NORMAL)
        textsalad.delete(0, END)
        textsalad.focus()

    else:
        textsalad.config(state=DISABLED)
        e_salad.set('0')


def burger():
    if var5.get() == 1:
        textburger.config(state=NORMAL)
        textburger.delete(0, END)
        textburger.focus()
    else:
        textburger.config(state=DISABLED)
        e_burger.set('0')


def omelets():
    if var6.get() == 1:
        textomelets.config(state=NORMAL)
        textomelets.delete(0, END)
        textomelets.focus()
    else:
        textomelets.config(state=DISABLED)
        e_omelets.set('0')


def quiche():
    if var7.get() == 1:
        textquiche.config(state=NORMAL)
        textquiche.delete(0, END)
        textquiche.focus()
    else:
        textquiche.config(state=DISABLED)
        e_quiche.set('0')


def avocadotoast():
    if var8.get() == 1:
        textavocadotoast.config(state=NORMAL)
        textavocadotoast.delete(0, END)
        textavocadotoast.focus()
    else:
        textavocadotoast.config(state=DISABLED)
        e_avocadotoast.set('0')


def tomatosoup():
    if var9.get() == 1:
        texttomatosoup.config(state=NORMAL)
        texttomatosoup.delete(0, END)
        texttomatosoup.focus()
    else:
        texttomatosoup.config(state=DISABLED)
        e_tomatosoup.set('0')


# batas mengaktifkan entry menu makanan

# mengaktifkan entry menu minuman
def kopihitam():
    if var10.get() == 1:
        textkopihitam.config(state=NORMAL)
        textkopihitam.delete(0, END)
        textkopihitam.focus()
    else:
        textkopihitam.config(state=DISABLED)
        e_kopihitam.set('0')


def lemontea():
    if var11.get() == 1:
        textlemontea.config(state=NORMAL)
        textlemontea.focus()
        textlemontea.delete(0, END)
    else:
        textlemontea.config(state=DISABLED)
        e_lemontea.set('0')


def milktea():
    if var12.get() == 1:
        textmilktea.config(state=NORMAL)
        textmilktea.delete(0, END)
        textmilktea.focus()
    else:
        textmilktea.config(state=DISABLED)
        e_milktea.set('0')


def espresso():
    if var13.get() == 1:
        textespresso.config(state=NORMAL)
        textespresso.delete(0, END)
        textespresso.focus()
    else:
        textespresso.config(state=DISABLED)
        e_espresso.set('0')


def cappucino():
    if var14.get() == 1:
        textcappucino.config(state=NORMAL)
        textcappucino.delete(0, END)
        textcappucino.focus()
    else:
        textcappucino.config(state=DISABLED)
        e_cappucino.set('0')


def airmineral():
    if var15.get() == 1:
        textairmineral.config(state=NORMAL)
        textairmineral.delete(0, END)
        textairmineral.focus()
    else:
        textairmineral.config(state=DISABLED)
        e_airmineral.set('0')


def americano():
    if var16.get() == 1:
        textamericano.config(state=NORMAL)
        textamericano.delete(0, END)
        textamericano.focus()
    else:
        textamericano.config(state=DISABLED)
        e_americano.set('0')


def tea():
    if var17.get() == 1:
        texttea.config(state=NORMAL)
        texttea.delete(0, END)
        texttea.focus()
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')


def latte():
    if var18.get() == 1:
        textlatte.config(state=NORMAL)
        textlatte.delete(0, END)
        textlatte.focus()
    else:
        textlatte.config(state=DISABLED)
        e_latte.set('0')


# batas mengaktifkan entry minuman

# mengaktifkan entry menu dessert
def eskrim():
    if var19.get() == 1:
        texteskrim.config(state=NORMAL)
        texteskrim.focus()
        texteskrim.delete(0, END)
    else:
        texteskrim.config(state=DISABLED)
        e_eskrim.set('0')


def cheesecake():
    if var20.get() == 1:
        textcheesecake.config(state=NORMAL)
        textcheesecake.delete(0, END)
        textcheesecake.focus()
    else:
        textcheesecake.config(state=DISABLED)
        e_cheesecake.set('0')


def brownies():
    if var21.get() == 1:
        textbrownies.config(state=NORMAL)
        textbrownies.delete(0, END)
        textbrownies.focus()
    else:
        textbrownies.config(state=DISABLED)
        e_brownies.set('0')


def pudding():
    if var22.get() == 1:
        textpudding.config(state=NORMAL)
        textpudding.delete(0, END)
        textpudding.focus()
    else:
        textpudding.config(state=DISABLED)
        e_pudding.set('0')


def tiramisu():
    if var23.get() == 1:
        texttiramisu.config(state=NORMAL)
        texttiramisu.delete(0, END)
        texttiramisu.focus()
    else:
        texttiramisu.config(state=DISABLED)
        e_tiramisu.set('0')


def pancake():
    if var24.get() == 1:
        textpancake.config(state=NORMAL)
        textpancake.delete(0, END)
        textpancake.focus()
    else:
        textpancake.config(state=DISABLED)
        e_pancake.set('0')


def cremebrulle():
    if var25.get() == 1:
        textcremebrulee.config(state=NORMAL)
        textcremebrulee.delete(0, END)
        textcremebrulee.focus()
    else:
        textcremebrulee.config(state=DISABLED)
        e_cremebrulee.set('0')


def applepie():
    if var26.get() == 1:
        textapplepie.config(state=NORMAL)
        textapplepie.delete(0, END)
        textapplepie.focus()
    else:
        textapplepie.config(state=DISABLED)
        e_applepie.set('0')


def churros():
    if var27.get() == 1:
        textchurros.config(state=NORMAL)
        textchurros.delete(0, END)
        textchurros.focus()
    else:
        textchurros.config(state=DISABLED)
        e_churros.set('0')

# FRAME KIRI
# Membuat frame kiri untuk menu cafe

# Membuat frame kiri untuk menu cafe
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
menuFrame.pack(side=LEFT)

hargaFrame=Frame(menuFrame,bd=9,relief=RIDGE,bg='#050206',pady=12)
hargaFrame.pack(side=BOTTOM)

brunchFrame=LabelFrame(menuFrame,text=' Brunch ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
brunchFrame.pack(side=LEFT)

minumanFrame=LabelFrame(menuFrame,text=' Minuman ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
minumanFrame.pack(side=LEFT)

dessertFrame=LabelFrame(menuFrame,text=' Dessert ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
dessertFrame.pack(side=LEFT)
# batas frame kiri (menu cafe)

# membuat tampilan daftar menu makanan
sandwich=Checkbutton(brunchFrame,text=' Sandwich ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var1,
                        command=sandwich, bg='#f6f6f6')
sandwich.grid(row=0,column=0,sticky=W)

croissant=Checkbutton(brunchFrame,text=' Croissant ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var2,
                        command=croissant, bg='#f6f6f6')
croissant.grid(row=1,column=0,sticky=W)

waffle=Checkbutton(brunchFrame,text=' Waffle ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var3,
                        command=waffle, bg='#f6f6f6')
waffle.grid(row=2,column=0,sticky=W)

salad=Checkbutton(brunchFrame,text=' Salad ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var4,
                        command=salad, bg='#f6f6f6')
salad.grid(row=3,column=0,sticky=W)

burger=Checkbutton(brunchFrame,text=' Burger ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var5,
                        command=burger, bg='#f6f6f6')
burger.grid(row=4,column=0,sticky=W)

omelets=Checkbutton(brunchFrame,text= ' Omelets ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var6,
                        command=omelets, bg='#f6f6f6')
omelets.grid(row=5,column=0,sticky=W)

quiche=Checkbutton(brunchFrame,text=' Quiche ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var7,
                        command=quiche, bg='#f6f6f6')
quiche.grid(row=6,column=0,sticky=W)

avocadotoast=Checkbutton(brunchFrame,text=' Avocado Toast',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var8,
                        command=avocadotoast, bg='#f6f6f6')
avocadotoast.grid(row=7,column=0,sticky=W)

tomatosoup=Checkbutton(brunchFrame,text=' Tomato Soup ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var9,
                        command=tomatosoup, bg='#f6f6f6')
tomatosoup.grid(row=8,column=0,sticky=W)

# menambahkan fields entri untuk item brunch
textsandwich=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_sandwich)
textsandwich.grid(row=0,column=1)

textcroissant=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_croissant)
textcroissant.grid(row=1,column=1)

textwaffle=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_waffle)
textwaffle.grid(row=2,column=1)

textsalad=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_salad)
textsalad.grid(row=3,column=1)

textburger=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_burger)
textburger.grid(row=4,column=1)

textomelets=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7, width=8,state=DISABLED,textvar=e_omelets)
textomelets.grid(row=5,column=1)

textquiche=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_quiche)
textquiche.grid(row=6,column=1)

textavocadotoast=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_avocadotoast)
textavocadotoast.grid(row=7,column=1)

texttomatosoup=Entry(brunchFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_tomatosoup)
texttomatosoup.grid(row=8,column=1)


# membuat tampilan daftar menu minuman
kopihitam=Checkbutton(minumanFrame,text='Kopi Hitam',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var10,
                        command=kopihitam, bg='#f6f6f6')
kopihitam.grid(row=0,column=0,sticky=W)

lemontea=Checkbutton(minumanFrame,text='Lemon Tea',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var11,
                        command=lemontea, bg='#f6f6f6')
lemontea.grid(row=1,column=0,sticky=W)

milktea=Checkbutton(minumanFrame,text='Milk Tea',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var12,
                        command=milktea, bg='#f6f6f6')
milktea.grid(row=2,column=0,sticky=W)

espresso=Checkbutton(minumanFrame,text='Espresso',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var13,
                        command=espresso, bg='#f6f6f6')
espresso.grid(row=3,column=0,sticky=W)

cappucino=Checkbutton(minumanFrame,text='Cappucino',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var14,
                        command=cappucino, bg='#f6f6f6')
cappucino.grid(row=4,column=0,sticky=W)

airmineral=Checkbutton(minumanFrame,text='Air Mineral',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var15,
                        command=airmineral, bg='#f6f6f6')
airmineral.grid(row=5,column=0,sticky=W)

americano=Checkbutton(minumanFrame,text='Americano',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var16,
                        command=americano, bg='#f6f6f6')
americano.grid(row=6,column=0,sticky=W)

tea=Checkbutton(minumanFrame,text='tea',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var17,
                        command=tea, bg='#f6f6f6')
tea.grid(row=7,column=0,sticky=W)

latte=Checkbutton(minumanFrame,text='Latte',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var18,
                        command=latte, bg='#f6f6f6')
latte.grid(row=8,column=0,sticky=W)

# menambahkan fields entri untuk item minuman
textkopihitam=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_kopihitam)
textkopihitam.grid(row=0,column=1)

textlemontea=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_lemontea)
textlemontea.grid(row=1,column=1)

textmilktea=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_milktea)
textmilktea.grid(row=2,column=1)

textespresso=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_espresso)
textespresso.grid(row=3,column=1)

textcappucino=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_cappucino)
textcappucino.grid(row=4,column=1)

textairmineral=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_airmineral)
textairmineral.grid(row=5,column=1)

textamericano=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_americano)
textamericano.grid(row=6,column=1)

texttea=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_tea)
texttea.grid(row=7,column=1)

textlatte=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_latte)
textlatte.grid(row=8,column=1)

# membuat tampilan daftar menu dessert
eskrim=Checkbutton(dessertFrame,text='Ice Cream',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var19,
            command=eskrim, bg='#f6f6f6')
eskrim.grid(row=0,column=0,sticky=W)

cheesecake=Checkbutton(dessertFrame,text='Cheesecake',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var20,
            command=cheesecake, bg='#f6f6f6')
cheesecake.grid(row=1,column=0,sticky=W)

brownies=Checkbutton(dessertFrame,text='Brownies',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var21,
            command=brownies, bg='#f6f6f6')
brownies.grid(row=2,column=0,sticky=W)

pudding=Checkbutton(dessertFrame,text='Pudding',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var22,
            command=pudding, bg='#f6f6f6')
pudding.grid(row=3,column=0,sticky=W)

tiramisu=Checkbutton(dessertFrame,text='Tiramisu',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var23,
            command=tiramisu, bg='#f6f6f6')
tiramisu.grid(row=4,column=0,sticky=W)

pancake=Checkbutton(dessertFrame,text='Pancake',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var24,
            command=pancake, bg='#f6f6f6')
pancake.grid(row=5,column=0,sticky=W)

cremebrulee=Checkbutton(dessertFrame,text='Creme Brulee',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var25,
            command=cremebrulle, bg='#f6f6f6')
cremebrulee.grid(row=6,column=0,sticky=W)

applepie=Checkbutton(dessertFrame,text='Apple Pie',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var26,
            command=applepie, bg='#f6f6f6')
applepie.grid(row=7,column=0,sticky=W)

churros=Checkbutton(dessertFrame,text='Churros',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var27,
            command=churros, bg='#f6f6f6')
churros.grid(row=8,column=0,sticky=W)


# menambahkan fields entri untuk item dessert
texteskrim = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_eskrim)
texteskrim.grid(row=0, column=1)

textcheesecake = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_cheesecake)
textcheesecake.grid(row=1, column=1)

textbrownies = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_brownies)
textbrownies.grid(row=2, column=1)

textpudding = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_pudding)
textpudding.grid(row=3, column=1)

texttiramisu = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_tiramisu)
texttiramisu.grid(row=4, column=1)

textpancake = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_pancake)
textpancake.grid(row=5, column=1)

textcremebrulee = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_cremebrulee)
textcremebrulee.grid(row=6, column=1)

textapplepie = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvariable=e_applepie)
textapplepie.grid(row=7, column=1)

textchurros = Entry(dessertFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED,textvariable=e_churros)
textchurros.grid(row=8, column=1)

# FRAME KANAN

# Membuat frame kanan untuk (Struk)
rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

strukFrame=Frame(rightFrame,bd=1,relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()
# Batas frame kanan (Struk)

# membuat label harga dan kolom entrinya
LabelHargadariBrunch=Label(hargaFrame,text='    HARGA DARI BRUNCH', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariBrunch.grid(row=0,column=0)

textHargadariBrunch=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadaribrunchvar)
textHargadariBrunch.grid(row=0,column=1,padx=41)

LabelHargadariMinuman=Label(hargaFrame,text='    HARGA DARI MINUMAN', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariMinuman.grid(row=1,column=0)

textHargadariMinuman=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariminumanvar)
textHargadariMinuman.grid(row=1,column=1,padx=41)

LabelHargadariDessert=Label(hargaFrame,text='  HARGA DARI DESSERT', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariDessert.grid(row=2,column=0)

textHargadariDessert=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadaridessertvar)
textHargadariDessert.grid(row=2,column=1,padx=41)

LabelSubTotal=Label(hargaFrame,text='SUB TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

LabelTax=Label(hargaFrame,text='Pajak'+' '+str(tax*100)+'%', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelTax.grid(row=1,column=2)

textTax=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=servicetaxvar)
textTax.grid(row=1,column=3,padx=41)

LabelHargaTotal=Label(hargaFrame,text='HARGA TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargaTotal.grid(row=2,column=2)

textHargaTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=totalcostvar)
textHargaTotal.grid(row=2,column=3,padx=41)

# Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
buttonTotal= Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonStruk= Button(buttonFrame,text='Struk',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=struk)
buttonStruk.grid(row=0,column=1)

buttonSimpan= Button(buttonFrame,text='Simpan',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=save)
buttonSimpan.grid(row=0,column=2)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='#fefefe',bg='red',bd=3,padx=12,
            command=reset)
buttonReset.grid(row=0,column=4)

# menentukan teks pada frame struk
textStruk=Text(strukFrame,font=('arial',12,'bold'),bd=3,width=36,height=26)
textStruk.grid(row=0,column=0)

root.mainloop()
