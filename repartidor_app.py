import tkinter as tk

from repartidor.gui import RepartidorApp


def main():
    root = tk.Tk()
    app = RepartidorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
