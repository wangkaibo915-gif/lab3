import tkinter as tk
import random


root = tk.Tk()
root.withdraw()  # 隐藏


def window():
    global popup
    popup = tk.Toplevel(root)
    popup.title(f"love yourself")
    
    colors=[ '#FFB6C1','#87CEEB','#98FB98','#DDA0DD'
            ,'#FFD700','#F0E68C','#E6E6FA','#B0E0E6']
    bg_color = random.choice(colors)
    popup.configure(bg=bg_color)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    b = 400 
    c = 150
    x= random.randint(0,screen_width - b)
    y= random.randint(0,screen_height - c)
    popup.geometry(f'{b}x{c}+{x}+{y}')

    a = ["天气凉了，要注意身体哦姐姐","压力大也要少熬夜 姐姐～",
         "笑对每一天 姐姐","姐姐好爱你","会好的,会好起来的"
         ,"落日,晚霞，海鸥 我想和你一直在一起","想你了姐姐","давай!","спокойная ночь"
         ,"姐姐是光的方向","把发霉的情绪晒一晒姐姐～","爱你爱你","明天也要加油!"]
    select_char = random.choice(a)

    label = tk.Label(popup,text=f"{select_char}",bg=bg_color,
                     fg='black',font=("Arial",14,"bold"))
    label.pack(pady=30)

    button = tk.Button(popup,text="谢谢你",command = popup.destroy,bg="white"
                       ,fg="black",font=("Arial",10))
    button.pack(pady=10)

    popup.after(9000, popup.destroy) 
    root.after(500,window)

window()
root.after(30000, root.quit) 
root.mainloop()