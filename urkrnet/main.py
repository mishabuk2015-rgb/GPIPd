from pywebio import start_server
from pywebio.input import input
from pywebio.output import put_text

from jinja2 import Environment, FileSystemLoader

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def get_data():
    name = input("Введіть ім'я")
    text = input("Введіть рядок")
    receiver = input("Введіть email одержувача")
    return name, text.strip(), receiver


def create_message(name, text):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("string.html")
    return template.render(
        name=name,
        text=text,
        length=len(text)
    )


def send_email(receiver, html):
    sender = "mishabuk2015@ukr.net"
    password = "8XLrRI6OnvAM8N6i"

    msg = MIMEText(html, "html", "utf-8")
    msg["Subject"] = Header("Результат обчислення", "utf-8")
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP_SSL("smtp.ukr.net", 465)
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        put_text("Лист успішно відправлено!")
    except Exception as e:
        put_text(f"Помилка: {e}")


def main():
    name, text, receiver = get_data()
    html = create_message(name, text)
    send_email(receiver, html)


if __name__ == "__main__":
    start_server(main, port=8081)
