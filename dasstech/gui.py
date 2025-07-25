import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
from excel_generator import generate_excel

def run_gui():
    def on_generate():
        user_id = entry_id.get()
        password = entry_pw.get()
        search_date = entry_date.get()
        btn["state"] = "disabled"
        progress_label["text"] = "진행중..."
        def task():
            try:
                filename = generate_excel(
                    user_id, password, search_date,
                    lambda msg: progress_label.after(0, progress_label.config, {"text": msg})
                )
                progress_label.after(0, progress_label.config, {"text": "완료!"})
                messagebox.showinfo("완료", f"엑셀 저장 완료: {filename}")
            except Exception as e:
                progress_label.after(0, progress_label.config, {"text": "오류 발생"})
                messagebox.showerror("오류", str(e))
            finally:
                btn["state"] = "normal"
        threading.Thread(target=task).start()

    root = tk.Tk()
    root.title("발전량 엑셀 생성기")
    root.geometry("350x260")

    tk.Label(root, text="아이디:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="비밀번호:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_pw = tk.Entry(root, show="*")
    entry_pw.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="날짜(YYYY.MM.DD):").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_date = tk.Entry(root)
    today_str = datetime.now().strftime("%Y.%m.%d")
    entry_date.insert(0, today_str)
    entry_date.grid(row=2, column=1, padx=10, pady=10)

    btn = tk.Button(root, text="엑셀 생성", command=on_generate)
    btn.grid(row=3, column=0, columnspan=2, pady=10)

    progress_label = tk.Label(root, text="")
    progress_label.grid(row=4, column=0, columnspan=2, pady=5)

    root.mainloop()