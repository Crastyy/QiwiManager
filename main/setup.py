from rich import print as rprint
import os
import json

dic = {"TOKEN": None, "ADMIN": None}

def toke_validate():
    rprint("[bold yellow]Введите токен Telegram Бота: ", end="")
    TOKEN = input("")
    token_split = TOKEN.split(":")
    try:
        token_split[0] = int(token_split[0])
        dic["TOKEN"] = f"{TOKEN}"
        return True
    except:
        rprint("[bold red]Токен введён некорректно")
        return toke_validate()


def get_id():
    rprint("[bold yellow]Введите ваш telegram id: ", end="")
    try:
        ADMIN_ID = int(input())
        with open("config.json", "w") as file:
            dic["ADMIN"] = ADMIN_ID
            json.dump(dic, file, indent=4)
            file.close()
        return True
    except:
        rprint("[bold red]Не корректный ID")
        return get_id()
    
def install_lib():
    rprint("[bold green]Установка библиотек...")
    try:
        os.system('pip install -r req.txt')
        rprint("[bold green]Установка завершена, запустите bot.py и перейдите к боут")
    except:
        try:
            os.system('pip3 install -r req.txt')
        except:
            rprint("[bold red]Error #1")



rprint("""[bold yellow]
   ____  _          _ __  __                                   
  / __ \(_)        (_)  \/  |                                  
 | |  | |___      ___| \  / | __ _ _ __   __ _  __ _  ___ _ __ 
 | |  | | \ \ /\ / / | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |__| | |\ V  V /| | |  | | (_| | | | | (_| | (_| |  __/ |   
  \___\_\_| \_/\_/ |_|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                __/ |          
                                               |___/           
""")

rprint("[bold green]Добро пожаловать в QiwiManager")
toke_validate()
get_id()
install_lib()

