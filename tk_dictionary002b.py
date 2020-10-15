from nltk.corpus import wordnet as wn
from tkinter import (Frame,Tk,Canvas,Button,Label,Entry,
                     Text,Checkbutton,IntVar)
import logging, nltk

logging.basicConfig(level= logging.DEBUG)
#logging.disable(logging.CRITICAL)

help_str= """
Enter your correctly spelled word into the entry widget
and press submit.
Output color code:
blue= synset.name()
none= synset.definitions()
red=  lemma_names()
purple= synset.examples()
"""

class MyDictionary(Frame):
    def __init__(self, parent=None):        
        self.parent= parent
        self.parent.title('NLTK Dictionary')
        Frame.__init__(self, self.parent)
        self.pack(expand='yes',fill='both')
        self.canvas= Canvas(self)
        self.canvas.config(width=900, height=850, bg='gray80')
        self.canvas.pack(expand='yes', fill='both')
        self.make_components()
        
    def make_components(self):
        font_1= ('times',16,'normal')
        font_2= ('times',16,'bold')
        self.label= Label(self.canvas, text='Word to submit',font=font_1)
        self.label.place(x=60,y=100)
        self.entry1= Entry(self.canvas, width=70,font=font_1,)
        self.entry1.insert('end', 'mint')
        self.entry1.focus()
        self.entry1.place(x=200,y=100)
        self.btn= Button(self.canvas, text= 'Submit',font=font_1,
                         command= self.find_def)
        self.btn.place(x=775,y=165)
        self.text= Text(self.canvas, relief='sunken',font=font_1,
                        wrap='word', )
        self.text.tag_configure('n.',foreground='blue',font=font_2)
        self.text.tag_configure('*.',foreground='red',font=font_2)
        self.text.tag_configure('p.',foreground='purple',font=font_2)
        self.text.tag_configure('hyp',foreground='green',font=font_2)
        self.text.tag_configure('hpe',foreground='orange',font=font_2)
        self.text.tag_configure('qq',foreground='dodgerblue',font=font_2)
        self.text.place(x=30,y=200)
        self.var_8= IntVar()
        self.c_box8= Checkbutton(self.canvas, variable=self.var_8,
                                 text= 'member holonyms', font=font_1)
        self.c_box8.place(x=550,y=150)
        self.var_7= IntVar()
        self.c_box7= Checkbutton(self.canvas, variable=self.var_7,
                                 text= 'entailments', font=font_1)
        self.c_box7.place(x=550,y=175)
        self.var_6= IntVar()
        self.c_box6= Checkbutton(self.canvas, variable=self.var_6,
                                 text= 'substance meronyms', font=font_1)
        self.c_box6.place(x=350,y=175)
        self.var_5= IntVar()
        self.c_box5= Checkbutton(self.canvas, variable=self.var_5,
                                 text= 'part meronyms', font=font_1)
        self.c_box5.place(x=350,y=150)
        self.var_4= IntVar()
        self.c_box4= Checkbutton(self.canvas, variable=self.var_4,
                                 text= 'hypernyms', font=font_1)
        self.c_box4.place(x=350,y=125)
        self.var_3= IntVar()
        self.c_box3= Checkbutton(self.canvas, variable=self.var_3,
                                 text= 'hyponyms', font=font_1)
        self.c_box3.place(x=150,y=125)
        self.var_1= IntVar()
        self.c_box= Checkbutton(self.canvas, text='lemma name',
                                font=font_1, variable=self.var_1)
        self.c_box.place(x=150,y=150)
        self.var_2= IntVar()
        self.c_box2= Checkbutton(self.canvas, text='def example',
                                 font=font_1,variable=self.var_2)
        self.c_box2.place(x=150,y=175)
        self.btn.invoke()
        
    def find_def(self):       
        logging.debug('looking for definition...')#be patient first lookup
        word= self.entry1.get()                  #get the entry
        defs= wn.synsets(word)                   #feed entry to dictionary
        lem= self.var_1.get()                    #checkbutton info twice
        ex_= self.var_2.get()
        hym= self.var_3.get()
        hyp= self.var_4.get()
        pm=  self.var_5.get()
        sm=  self.var_6.get()
        ent=  self.var_7.get()
        hol=  self.var_8.get()
        
        self.text.delete('1.0','end')
        for synset in defs:
            name= synset.name()                   #output name            
            d_f= synset.definition()             #output definition            
            
            self.text.insert('end',name,'n.')            
            self.text.insert('end','\n')            
            self.text.insert('end',d_f)                        
            self.text.insert('end','\n')
            l_n= synset.lemma_names()
            exa= synset.examples()
            h_y= synset.hyponyms()
            h_m= synset.hypernyms()
            p_m= synset.part_meronyms()
            s_m= synset.substance_meronyms() 
            m_h= synset.member_holonyms()
            ant= synset.entailments()
            #a_m= wn.lemma(l_n).antonyms()
            
            
            if lem:                                #output lemma name
                self.text.insert('end', l_n, '*.')
                self.text.insert('end','\n')
            if ex_:                                # ouput example purple
                self.text.insert('end', exa, 'p.')
                self.text.insert('end','\n')
            if hym:
                self.text.insert('end', h_y, 'hyp')
                self.text.insert('end', '\n')
            if hyp:
                self.text.insert('end', h_m, 'hpe')
                self.text.insert('end', '\n')
            if pm:
                self.text.insert('end', p_m, 'qq')
                self.text.insert('end', '\n')
            if sm:
                self.text.insert('end', s_m, '*.')
                self.text.insert('end', '\n')
            if ent:
                self.text.insert('end', ant, 'p.')
                self.text.insert('end', '\n')
            if hol:
                self.text.insert('end', m_h, 'hyp')
                self.text.insert('end', '\n')
            
       
if __name__ == '__main__':
    root= Tk()
    MyDictionary(root)
    root.mainloop()
        
