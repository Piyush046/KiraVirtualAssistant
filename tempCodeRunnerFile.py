def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        win.destroy()
        pygame.mixer.music.stop()