import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B06XQBNFT7/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

respo = requests.get(url, headers=header)

soup = BeautifulSoup(respo.content, "lxml")

preço = soup.find(id="a-offscreen").get_text()
preço_sem_moeda = preço.split("$")[1]
preço_com_float = float(preço_sem_moeda)

title = soup.find(id="productTitle").get_text().strip()


if price_as_float < 100:
    message = f"{title} está muito abaixo do valor!! {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login( " ", " ")
        connection.sendmail(
            from_addr=" ",
            to_addrs=" ",
            msg=f"Subject: Alerta de Preço Amazon!\n\n{message}\n{url}"
        )


