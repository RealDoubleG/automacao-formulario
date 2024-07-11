import pyautogui
import time
import pandas 

## delay entre cada comando
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

## define um delay apenas nessa parte do código
time.sleep(5)

pyautogui.click(x=-1038, y=376)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("login")
pyautogui.press("tab")
pyautogui.hotkey("ctrl", "a")
pyautogui.write("senha")
pyautogui.press("enter")

time.sleep(1.5)
pyautogui.press("esc")

csv = pandas.read_csv("./produtos.csv")

pyautogui.click(x=-1149, y=254)

for index, row in csv.iterrows():
  pyautogui.write(row["codigo"])
  pyautogui.press("tab")
  pyautogui.write(row["marca"])
  pyautogui.press("tab")
  pyautogui.write(row["tipo"])
  pyautogui.press("tab")
  pyautogui.write(str(row["categoria"]))
  pyautogui.press("tab")
  pyautogui.write(str(row["preco_unitario"]))
  pyautogui.press("tab")
  pyautogui.write(str(row["custo"]))
  pyautogui.press("tab")
  if pandas.isna(row["obs"]):
    pyautogui.press("tab")
  else :
    pyautogui.write(str(row["obs"]))
    pyautogui.press("tab")
  pyautogui.press("enter")
  pyautogui.scroll(1000)
  pyautogui.click(x=-1149, y=254)