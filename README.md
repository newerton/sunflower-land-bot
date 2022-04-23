<h1 align="center">

![Sunflower Land Banner](https://raw.githubusercontent.com/newerton/sunflower-land-bot/main/images/readme/banner.jpg)

  <a>
    🌻 Sunflower Land Bot 🌻 
  </a>
</h1>

## ⚠️ Warning

### I am not responsible for any penalties incurred by those who use the bot, use it at your own risk.
## This BOT is completely secure, it does not ask for your metamask password or private key.

## 📌 Glossary

  * [Donation](#donation)
  * [About](#about)
  * [Robot - Preview](#robot-preview)
  * [Installation](#installation)
    * [Terminal commands](#commands)
  * [How to works](#how-to-works)
  * [Tests](#tests)
  * [Configs](#configs)

# 🎁 <a id="donation"></a>Donation (for support)
## BUSD/USDC/BNB/MATIC: 0x4847C29561B6682154E25c334E12d156e19F613a  
## PIX (Brazil Payment): 08912d17-47a6-411e-b7ec-ef793203f836   

## 📋 <a id="about"></a>About

This bot contains code from other developers, this bot was just refactored, to facilitate new implementations and maintenance.

This bot is free and open source.

## 🤖 <a id="robot-preview"></a>Robot - Preview
![Screenshot - Preview](https://raw.githubusercontent.com/newerton/sunflower-land-bot/main/images/readme/bot_working.jpg)

## 🪟 <a id="installation"></a>Installation

### **Python**

🖥️ Computer/Laptop High or Medium Profile  
🐍 Install the Python 3.9.9

🖥️ Computer/Laptop Low Profile or Low Profile with Windows 7 Pro  
🐍 Install the Python 3.8.10

🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

⚠️ **It is important to check the option to add python to PATH**

### <a id="commands"></a>Commands
Install the dependencies by running the command below into the project folder:

```
pip install -r requirements.txt
```
Ready! Now just start the bot with the command, inside the project folder

```
python index.py
```

### <a id="how-to-works"></a>**How to works?**

The bot doesn't change any of the game's source code, it just takes a screenshot of the game's screen to find the buttons and simulates mouse movements.

⚠️ Some settings can be changed in the /config/config.yaml file, don't forget to restart the bot if you change the settings, some changes in the /config/config.yaml file may cause the bot to stop, such as activating the telegram when the bot is running. 

The waiting time for harvesting the sunflower is 1 minute, and for the other plants it is 5 minutes. 

## 🧪 <a id="tests"></a>Tests
**Desktop Medium Profile**  
Intel i5-3570k @ 3.4Ghz, 24GB RAM  
Windows 11, Resolution@1920x1080  
Python 3.9.9  

**Laptop Low Profile**  
Laptop Samsumg RV411, Pentium P6200 @ 2.13Ghz, 2GB RAM  
Windows 7, Resolution@1366x768  
Python 3.8.10

## <a id="configs"></a>🧑‍🌾 Config

### ⚠️ Don't forget to rename /config/EXAMPLE-farn.yaml file, to /config/farm.yaml.  
### Use the enable option to activate which seed you want to use and the sell option to deactivate the sale of the seed, in this case it is for you not to sell the seed, if you are accumulating to buy some NFT.

```
{
  crops:
    [
      { position: 0, enable: true, title: "sunflower", sell: true },
      { position: 1, enable: true, title: "potato", sell: true },
      { position: 2, enable: true, title: "pumpkin", sell: true },
      { position: 3, enable: true, title: "carrot", sell: true },
      { position: 4, enable: true, title: "cabbage", sell: true },
      { position: 5, enable: true, title: "beetroot", sell: true },
      { position: 6, enable: true, title: "cauliflower", sell: true },
      { position: 7, enable: false, title: "parsnip", sell: false },
      { position: 8, enable: false, title: "radish", sell: false },
      { position: 9, enable: false, title: "wheat", sell: false },
    ],
  forest: [],
  water: [],
}

```

## 👍 Did you like it? :)

### BUSD/USDC/BNB/MATIC: 0x4847C29561B6682154E25c334E12d156e19F613a  
### PIX (Brazil Payment): 08912d17-47a6-411e-b7ec-ef793203f836