import tkinter

top = tkinter.Tk()

def callback():
    print("hello world")

def main():
    B = tkinter.Button(top, text="Hello", command=callback)

    B.pack()
    top.mainloop()

if __name__ == "__main__":
    main()