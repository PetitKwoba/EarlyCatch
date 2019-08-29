from tkinter import*
from tkinter import filedialog
from tkinter import ttk
import tensorflow as tf
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from numpy import asarray
import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageTk, Image
global window
global FrameOne

window = Tk()
def Algorithm(filename):
    photo = load_img(filename,target_size=(50,50))
    # convert to numpy array
    photo = img_to_array(photo)
    photo = asarray(photo)
    print(plt.imshow(photo))

    img = Image.fromarray(photo.astype(np.uint8))
    img = img.resize((300,300), resample=Image.BILINEAR)
    img = ImageTk.PhotoImage(image=img)
    PhotoL.configure(image=img)

    PhotoL.image=img

    photo = np.expand_dims(photo,axis=0)

    pred = model.predict(photo)



    ShowPrediction = str(pred[0][1])
    print(photo.shape)
    print(model.predict(photo))

    return (pred[0][1])

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    #Algorithm(filename)
    SHOWINFO = "Cancer risk\n"+ str(round(Algorithm(filename) * 100,2)) + "%"
    ShowPrediction = Label(MainFrame,text=SHOWINFO,font=("Helvetica",30))
    ShowPrediction.place(x=380,y=280, width=200)

def Quit():
    sys.exit()

MainFrame = window

window.title('EARLYCATCH AI Screening')
ECLabel = Label(MainFrame, text = "EarlyCatch",font=("Helvetica", 36))
ECLabel.grid(column=0,row=0,sticky=W+E,padx=180)
Title = Label(MainFrame, text = 'Breast Cancer AI Screening',font=("Helvetica", 30))
Title.grid(columnspan=3,row=1,column=0,sticky=W+E,padx=120)
Intro = Label(MainFrame, text = " \nDISCLAIMER: \nThis model is currently a prototype, and is still in development"
                            ,font=("Helvetica", 10))
Intro.place(x=120,y=400)
s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 20))


model = tf.keras.models.load_model('model.h5')


MainFrame.geometry('600x480')
LabelF = LabelFrame(MainFrame,text="User Upload")
LabelF.place(x=400,y=120)

UploadB = Button(MainFrame,text="Upload",command=UploadAction,font=("Helvetica",19))
UploadB.place(x=400,y=120,height = 110,width=140)


img = np.zeros((50,50,3)).astype(np.uint8)
img = Image.fromarray(img)
img = img.resize((300,300))
img = ImageTk.PhotoImage(image=img)
PhotoL = Label(MainFrame,image=img)
PhotoL.place(x=10,y=100,width=300,height=300)

window.mainloop()



