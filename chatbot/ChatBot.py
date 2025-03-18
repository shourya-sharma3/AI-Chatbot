iwontshowyoumyapikey = "Put Your Google Gemini API Key, Steps Explained In README"

import customtkinter as ctk
import google.generativeai as genai
import os
import pygame

pygame.init()
pygame.mixer.init()

os.environ["GEN_AI_KEY"] = iwontshowyoumyapikey
genai.configure(api_key=os.environ["GEN_AI_KEY"])

tk = ctk.CTk()
tk.geometry("400x600")
tk.title("AI Chatbot")
tk.configure(fg_color="#FFC0CB")
chat_frame = ctk.CTkFrame(tk, corner_radius=15)
chat_frame.pack(padx=10, pady=10, fill='both', expand=True)


def send_message():
    user_text = input_box.get()
    if user_text.strip():
        display_message(user_text, sender="user")

        prompt = (f"Reply to {user_text}, as if you are {input_box2.get()}")
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        bot_response = response.text.strip()

        display_message(bot_response, sender="bot")

        input_box.delete(0, 'end')

def display_message(text, sender):
    msg_frame = ctk.CTkFrame(chat_display, fg_color="#FFF", corner_radius=15)
    msg_frame.pack(anchor="w" if sender == "bot" else "e", pady=5, padx=10, fill="x")

    bg_color = "#FF69B4" if sender == "user" else "#6A5ACD"
    text_color = "#FFF"

    msg_label = ctk.CTkLabel(
        msg_frame, text=text, fg_color=bg_color, text_color=text_color,
        wraplength=280, padx=10, pady=5, corner_radius=15, font=("Arial", 14)
    )
    msg_label.pack(padx=5, pady=5, anchor="w" if sender == "bot" else "e")

    chat_display.update_idletasks()
    chat_display.update_idletasks()

name = ctk.CTkLabel(tk, text="Made By Shourya Sharma", text_color="black")
name.pack()
chat_display = ctk.CTkScrollableFrame(chat_frame, fg_color="#FFF", width=380, height=450)
chat_display.pack(fill='both', expand=True)

input_frame2 = ctk.CTkFrame(tk, fg_color="#FFF")
input_frame2.pack(fill='x')

input_frame = ctk.CTkFrame(tk, fg_color="#FFF")
input_frame.pack(fill='x')

input_box2 = ctk.CTkEntry(input_frame2, placeholder_text="Enter what you want to make it talk like",width=300, font=("Arial", 14))
input_box2.pack(fill="both",padx=5, pady=5, expand=True)

input_box = ctk.CTkEntry(input_frame,placeholder_text="Send Message", width=300, font=("Arial", 14))
input_box.pack(side='left', padx=5, pady=5, expand=True)
input_box.bind('<Return>', lambda event: send_message())

send_button = ctk.CTkButton(input_frame, text="Send", command=send_message)
send_button.pack(side='right', padx=5, pady=5)

tk.mainloop()




