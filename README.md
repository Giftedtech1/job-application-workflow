
# Job Applications Workflow

This GitHub Actions workflow lets you send job application emails (with your resume) using Gmail securely.

## 🛠 Setup

1. Add two secrets to your repo:
   - `EMAIL_USER`: your Gmail address
   - `EMAIL_PASS`: your Gmail **App Password** (NOT your real password)

2. Replace the `resume.pdf` with your actual resume.

3. Update the `receiver_email` in `send_email.py` with the company's HR email.

## ▶️ Usage

Go to the **Actions** tab on GitHub and click **Run workflow** to send your application.

---

Built with ❤️ by Gifted
