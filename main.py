#1
class InvalidUrlError(Exception):
    def __init__(self, url):
        self.url = url
def fetch_data_from_url(url):
    if url != "https://mystat.itstep.org/ua/main/homework/page/index":
        raise InvalidUrlError(url)
    else:
        print("Успішно!")
        print()
try:
    print("Вхід до майстату")
    url = input("Введіть ключ до сайту Mystat:")
    fetch_data_from_url(url)
except InvalidUrlError as a:
    print(f"Невірна силка {a.url}\n"
          f"Введіть силку правильно")