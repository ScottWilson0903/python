import ctypes, time, os, tkinter
correct_length = False
correct_choice = False

class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()

while correct_choice == False:
    choice = input("Enter 1, 2, 3 or 4:\n1)Break Windows \n2)Shutdown Computer \n3)Disable Mouse\n4)Exit \n")
    if choice == "1" or choice == "2" or choice == "3" or choice == "4":
      correct_choice = True

if choice == "1":
  os.system("taskkill /IM explorer.exe /F")
  
elif choice == "2":
  os.system("shutdown /s /f /t 1")
    
elif choice == "3":
    
    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_ulong), ("y", ctypes.c_ulong)]

    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    cursor_x = pt.x
    cursor_y = pt.y
  
    while correct_length == False:
        correct_length = True
        length = input("Disable mouse for how long? (in seconds)\t")
    try:
        int(length)
    except ValueError:
        correct_length = False

    def task():  
        timeout = time.time() + int(length)

        while True:
            if time.time() > timeout:
                break
            ctypes.windll.user32.SetCursorPos(0, 0)
        ctypes.windll.user32.SetCursorPos(cursor_x,cursor_y)

    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.call('wm', 'attributes', '.', '-topmost', '1')
    app = Application(master=root)
    app.after(1, task)
    app.after(int(length)*1000, lambda: root.destroy())
    app.mainloop()

    



