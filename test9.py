from tkinter import *


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Shapes")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
##        canvas.create_oval(10, 10, 80, 80, outline="red", 
##            fill="green", width=2)
##        canvas.create_oval(110, 10, 210, 80, outline="#f11", 
##            fill="#1f1", width=2)
##        canvas.create_rectangle(230, 10, 290, 60, 
##            outline="#f11", fill="#1f1", width=2)
##        canvas.create_arc(30, 200, 90, 100, start=0, 
##            extent=210, outline="#f11", fill="#1f1", width=2)
        x1=5
        y1=5
        points = [x1-3, y1+3, x1-2, y1,x1-1, y1-3,x1+1, y1-4,x1+3, y1-3,x1+2, y1,x1, y1-1,x1-2, y1]
        canvas.create_polygon(points, outline='red', 
            fill='green', width=2)
        
        canvas.pack(fill=BOTH, expand=1)


def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("10x10+10+10")
    root.mainloop()  


if __name__ == '__main__':
    main()  
