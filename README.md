# **Book Store Project**

Bu loyiha oddiy **Flask** va **MySQL** asosida ishlaydigan kitob qo'shish tizimini yaratish uchun mo'ljallangan. Loyihaning asosiy tuzilmasi (fayllar va papkalar) tayyorlangan, siz faqat kerakli kodlarni yozib, ishlatishingiz kerak.

---

## **Loyiha funksiyalari**  
1. Foydalanuvchilar `books` jadvaliga kitob ma'lumotlarini qo'sha oladi.  
2. HTML form orqali foydalanuvchidan ma'lumot olish.  
3. MySQL ma'lumotlar bazasi bilan integratsiya.

---

## **Texnologiyalar**  
- **Python** (Flask)  
- **MySQL** (`mysql-connector-python` kutubxonasi)

---

## **Loyiha tuzilmasini olish**  

### **1. Repository-ni klonlash**
1. Repository ni fork qiling  

2. Repository ni clone qiling

---

### **2. Virtual muhitni sozlash**  
1. Virtual muhitni yarating va faollashtiring (Shart emas, ixtiyoriy):  
   ```bash
   python -m venv venv
   source venv/bin/activate    # Windows uchun: venv\Scripts\activate
   ```

2. Loyihada kerakli kutubxonalarni o'rnating (majburiy):  
   ```bash
   pip install flask mysql-connector-python
   ```

3. O'rnatilgan kutubxonalarni `requirements.txt` fayliga saqlang (majburiy):  
   ```bash
   pip freeze > requirements.txt
   ```

---

### **3. MySQL ma'lumotlar bazasini sozlash**
1. MySQL serverga ulaning va `library` nomli ma'lumotlar bazasini yarating:  
   ```sql
   CREATE DATABASE library;
   ```

2. `books` jadvalini yarating:  
   ```sql
   CREATE TABLE books (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255),
       author VARCHAR(255),
       pages INT,
       published_year INT
   );
   ```

---

### **4. Flask bilan ishlash**
1. `app.py` faylida Flask dasturini sozlang. Quyidagi funksiyalarni qo'shing:
   - MySQL ulanishi uchun konfiguratsiya.
   - `/add-book` marshrutini yaratish (`GET` va `POST` so'rovlarini qabul qilish uchun).  
   - Foydalanuvchi kiritgan ma'lumotlarni `books` jadvaliga yozish.  

2. Form HTML kodi uchun `templates/add_book.html` faylini to'ldiring.  

---

### **5. Flask serverni ishga tushirish**
1. Flask serverni ishga tushiring:  
   ```bash
   python app.py
   ```

2. Brauzeringizda quyidagi manzilga o'ting:  
   ```
   http://127.0.0.1:5000/add-book
   ```

---

## **Loyihaning ishlash tartibi**
1. `/add-book` sahifasiga kiring.  
2. HTML form orqali quyidagi ma'lumotlarni kiriting:
   - Kitob nomi (`title`)
   - Muallif (`author`)
   - Sahifalar soni (`pages`)
   - Nashr yili (`published_year`)
3. Formni yuborgandan so'ng ma'lumotlar `books` jadvaliga yoziladi.  

---

## **Qo'shimcha vazifalar (ixtiyoriy)**
1. Kitoblarni ro'yxat qilish uchun `/books` marshrutini yarating.  
2. `books` jadvalidan barcha ma'lumotlarni olib HTML sahifada ko'rsating.  

---

## **Fayllar tuzilishi**
```
bookstore/
│
├── app.py                # Flask dasturi (tugatishingiz kerak)
├── requirements.txt      # Kutubxonalar ro'yxati
├── templates/            # HTML fayllar uchun papka
│   └── add_book.html     # Kitob qo'shish formasi (bo'sh)
└── README.md             # Loyihaga oid ma'lumotlar
```

---

## **Talablar**
- Python 3.7+  
- MySQL server  
- Flask  
- mysql-connector-python  

---
