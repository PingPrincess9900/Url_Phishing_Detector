import tkinter as tk
from tkinter import messagebox
import tldextract
import re

# --- Detection logic with detailed reasons ---
def check_url_details(url):
    reasons = []
    suspicious_keywords = ["login", "verify", "secure", "update", "signin", "banking"]

    # Check for raw IP
    if re.match(r'^http[s]?://\d{1,3}(\.\d{1,3}){3}', url):
        reasons.append("Contains IP address instead of domain.")

    # Check for phishing keywords
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        reasons.append("Contains suspicious keywords.")

    # Check for long subdomain
    parts = tldextract.extract(url)
    if len(parts.subdomain.split('.')) > 2:
        reasons.append("Unusually long subdomain.")

    # Check for hyphens in domain
    if '-' in parts.domain:
        reasons.append("Domain contains hyphen.")

    is_phishing = len(reasons) > 0
    return is_phishing, reasons

# --- GUI logic ---
def check_url():
    url = entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    is_phish, reasons = check_url_details(url)
    result_text = ""

    if is_phish:
        result_text += "⚠ Potential phishing URL detected!\n\nReasons:\n"
        for reason in reasons:
            result_text += f"- {reason}\n"
        result_label.config(text=result_text, fg="red", justify="left")
    else:
        result_label.config(text="✅ Legitimate URL", fg="green")

# --- GUI setup ---
root = tk.Tk()
root.title("URL Phishing Detector")
root.geometry("500x300")

tk.Label(root, text="Enter a URL:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=60)
entry.pack()

tk.Button(root, text="Check URL", command=check_url).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), wraplength=450, justify="left")
result_label.pack(pady=10)

root.mainloop()

