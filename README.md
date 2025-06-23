🔐 URL Phishing Detector

 📖 Overview

Phishing attacks often trick users into clicking on deceptive links. This tool helps identify such URLs using a rule-based analysis. It can be useful for:
- Cybersecurity learners
- Awareness programs
- Light-weight phishing detection demonstration tools


  ✅ Features

- 🔎 Detects suspicious **keywords** like `login`, `secure`, `verify`, etc.
- 🌐 Identifies if a **raw IP address** is used instead of a domain
- 🧩 Flags **long subdomains** which are often signs of phishing
- ✂ Detects **hyphenated domains**, commonly used in fake sites
- 🖥️ Simple and interactive **GUI interface** built using Tkinter
- ⚠️ Provides detailed reasons when a URL is flagged as phishing


   🧰 Technologies Used

- Python 3.13.3
- Tkinter – GUI
- tldextract – Extract subdomain, domain, and suffix for analysis
- re – Regular expressions for pattern matching


   👨‍💻 Work Flow
1. User enters a URL into the GUI input field.
2. On clicking **"Check URL"**, the app performs a set of checks on the URL.
3. The result is displayed:
   - ✅ If no issues found: “Legitimate URL”
   - ⚠️ If suspicious patterns are detected: A warning message is shown with a list of reasons
  
     ---

 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this project with proper credit.


🙏 Acknowledgements

- This project is part of my cybersecurity learning journey.
- Inspired by real-world phishing cases and awareness tools.
- Thanks to the open-source Python community.




