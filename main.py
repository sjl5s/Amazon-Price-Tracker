from bs4 import BeautifulSoup
import requests


url = "https://www.amazon.com/release-bigger-vibrant-helpful-routines/dp/B09B93ZDG4/ref=sr_1_7_ffob_sspa?dib=eyJ2IjoiMSJ9.V86oEKKLIRKtkqPOiCvQQoeB4CKqJNkj-NhQ64E1HuV9qs5T64SHZsgCJkIfhhAH8yLRMiWScPocmdagcgixOjLyQRj8giSNboc-BZoYiAUY5d7--SNeJNU9UeF5WBbHW8walneJD7rjB7vwbaXXr0C5QyqXC1iIPHMuUHSOVpVsOIhB0-T_3IXq0APVJ5mMfsW9MulL7ujfzr47a_E8DC71U2lTg2TuzJWtci2TxZg.CuETp77opTbarprOFG76qy5camvjdqx3PIxC4E3vblM&dib_tag=se&keywords=speaker&qid=1723195094&sr=8-7-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
num_price = float(price.split("$")[1])

print(num_price)