# 🧮 Mini Calculator (Python + Logging)

## 📌 Loyihaning tavsifi
Ushbu loyiha — oddiy **mini kalkulyator** dasturi bo‘lib, u `+`, `-`, `*`, `/` amallarini bajaradi va barcha jarayonlarni **logging** orqali `calc.log` fayliga yozib boradi.  
`logging` moduli yordamida foydalanuvchi amallari, xatoliklar va ogohlantirishlar log qilinadi.

---

## ⚡ Xususiyatlari
- ➕ Qo‘shish  
- ➖ Ayirish  
- ✖️ Ko‘paytirish  
- ➗ Bo‘lish (0 ga bo‘lish xatosi loglanadi)  
- ❌ Noto‘g‘ri amal yoki input kiritsangiz, log faylga yoziladi  
- 📜 Loglar `calc.log` fayliga saqlanadi

---

## 📂 Loyiha tuzilishi
```bash
mini-calculator/
│── calc.log        # Log fayl
│── calculator.py   # Asosiy kod
│── README.md       # Loyihaning hujjati
```

## 🚀 O‘rnatish va ishga tushirish
1. Repository’ni clone qiling:
```
git clone https://github.com/<username>/mini-calculator.git
cd mini-calculator
```

2. Dasturda logging moduli ishlatiladi (Python’da standart keladi). Qo‘shimcha kutubxona o‘rnatish shart emas.
3. Kalkulyatorni ishga tushiring:
```
python calculator.py
```
## 🖥️ Foydalanish
```
🧮 Mini Calculator
Amallar: +  -  *  /   |   chiqish uchun: exit
```
## Misol:
```
Amalni kiriting: +
Birinchi son: 5
Ikkinchi son: 3
Natija: 8.0
```
## Log fayldan namunalar (calc.log):
```
2025-10-02 09:15:43,128 - INFO - Qo‘shish: 5.0 + 3.0 = 8.0
2025-10-02 09:16:01,452 - ERROR - 0 ga bo‘lish xatosi!
2025-10-02 09:16:18,777 - WARNING - Noto‘g‘ri amal: ^
```
## 🛠️ Texnologiyalar
Python 3.x

logging (standart kutubxona)
