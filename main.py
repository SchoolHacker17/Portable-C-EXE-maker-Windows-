import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def compile_cpp():
    cpp_path = filedialog.askopenfilename(filetypes=[("C++ Files", "*.cpp")])
    if not cpp_path:
        return

    exe_name = os.path.splitext(os.path.basename(cpp_path))[0] + ".exe"
    output_path = os.path.join(os.path.dirname(cpp_path), exe_name)

    command = [
        "g++",
        "-static",
        "-std=c++17",
        "-o", output_path,
        cpp_path,
        "-lShell32"
    ]

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", f"Compiled to:\n{output_path}")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Compilation failed.\nCheck your source and g++ setup.")

# GUI setup
root = tk.Tk()
root.title("C++ to Portable EXE")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Compile C++ to Standalone EXE")
label.pack(pady=10)

button = tk.Button(frame, text="Select C++ File", command=compile_cpp)
button.pack()

root.mainloop()
