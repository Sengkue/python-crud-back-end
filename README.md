# FindLove User API - ລະບົບຈັດການຜູ້ໃຊ້

ລະບົບ Backend ທີ່ສົມບູນສຳລັບການຈັດການຜູ້ໃຊ້ ໃຊ້ FastAPI, SQLAlchemy, ແລະ PostgreSQL

## 📁 ໂຄງສ້າງໂປຣເຈັກ

```
findlove-backend/
│
├── config/
│   ├── __init__.py
│   └── database.py          # ການຕັ້ງຄ່າຖານຂໍ້ມູນ
│
├── models/
│   ├── __init__.py
│   └── user.py              # ແບບຈຳລອງຜູ້ໃຊ້
│
├── controllers/
│   ├── __init__.py
│   └── user_controller.py   # ລະບົບຄວບຄຸມຜູ້ໃຊ້
│
├── routes/
│   ├── __init__.py
│   └── user_routes.py       # ເສັ້ນທາງ API
│
├── schemas/
│   ├── __init__.py
│   └── user_schemas.py      # ການກວດສອບຂໍ້ມູນ
│
├── .env                     # ຕົວແປສະພາບແວດລ້ອມ
├── requirements.txt         # ລາຍການແພັກເກີຈ
├── main.py                  # ຈຸດເລີ່ມຕົ້ນແອັບພລິເຄຊັນ
└── README.md               # ໄຟລ໌ນີ້
```

## 🚀 ວິທີການເລີ່ມຕົ້ນ

### 1. ຄວາມຕ້ອງການເບື້ອງຕົ້ນ

- Python 3.8 ຂຶ້ນໄປ
- PostgreSQL
- pip

### 2. ການຕິດຕັ້ງ

```bash
# ສ້າງໂຟນເດີໂປຣເຈັກ
mkdir findlove-backend
cd findlove-backend

# ສ້າງສະພາບແວດລ້ອມເສມືອນ
python -m venv venv

# ເປີດໃຊ້ງານສະພາບແວດລ້ອມເສມືອນ
# ສຳລັບ Windows:
venv\Scripts\activate
# ສຳລັບ macOS/Linux:
source venv/bin/activate
```

### 3. ຕິດຕັ້ງແພັກເກີຈ

```bash
# ຕິດຕັ້ງແບບທີລະຕົວ
pip install fastapi
pip install uvicorn[standard]
pip install psycopg2-binary
pip install sqlalchemy
pip install pydantic
pip install python-dotenv
pip install python-multipart
```

### 4. ຕັ້ງຄ່າຖານຂໍ້ມູນ

ໃຫ້ແນ່ໃຈວ່າ PostgreSQL ກຳລັງເຮັດວຽກ ແລະ ສ້າງຖານຂໍ້ມູນ:

```sql
-- ເຊື່ອມຕໍ່ PostgreSQL ໃນຖານະຜູ້ບໍລິຫານ
psql -U postgres

-- ສ້າງຖານຂໍ້ມູນ
CREATE DATABASE findlovedb;

-- ສ້າງຜູ້ໃຊ້ (ບໍ່ບັງຄັບ)
CREATE USER findlove_user WITH PASSWORD '123';
GRANT ALL PRIVILEGES ON DATABASE findlovedb TO findlove_user;
```

### 5. ການຕັ້ງຄ່າສະພາບແວດລ້ອມ

ສ້າງໄຟລ໌ `.env` ໃນໂຟນເດີຫຼັກ:

```env
# ຖານຂໍ້ມູນ
DB_HOST=localhost
DB_PORT=5432
DB_NAME=findlovedb
DB_USER=postgres
DB_PASS=123

# ການຕັ້ງຄ່າແອັບພລິເຄຊັນ
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=True
```

### 6. ສ້າງໂຄງສ້າງໂຟນເດີ

```bash
# ສ້າງໂຟນເດີ
mkdir config models controllers routes schemas

# ສ້າງໄຟລ໌ __init__.py
touch config/__init__.py
touch models/__init__.py
touch controllers/__init__.py
touch routes/__init__.py
touch schemas/__init__.py
```

### 7. ເຮັດວຽກແອັບພລິເຄຊັນ

```bash
python main.py
```

API ຈະພ້ອມໃຊ້ງານທີ່: `http://localhost:8000`

## 📚 ເອກະສານ API

ເມື່ອເຊີເວີເຮັດວຽກແລ້ວ, ທ່ານສາມາດເຂົ້າເຖິງ:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔗 ເສັ້ນທາງ API

### ການຈັດການຜູ້ໃຊ້

| ວິທີ | ເສັ້ນທາງ | ຄຳອະທິບາຍ |
|------|----------|-------------|
| POST | `/api/users/` | ສ້າງຜູ້ໃຊ້ໃໝ່ |
| GET | `/api/users/` | ເອົາຜູ້ໃຊ້ທັງໝົດ |
| GET | `/api/users/{user_id}` | ເອົາຜູ້ໃຊ້ຕາມ ID |
| PUT | `/api/users/{user_id}` | ອັບເດດຜູ້ໃຊ້ |
| DELETE | `/api/users/{user_id}` | ລຶບຜູ້ໃຊ້ |
| POST | `/api/users/login` | ເຂົ້າສູ່ລະບົບ |
| GET | `/api/users/username/{username}` | ເອົາຜູ້ໃຊ້ຕາມຊື່ຜູ້ໃຊ້ |
| GET | `/api/users/email/{email}` | ເອົາຜູ້ໃຊ້ຕາມອີເມວ |

### ຕົວຢ່າງການໃຊ້ງານ

#### ສ້າງຜູ້ໃຊ້ໃໝ່
```bash
curl -X POST "http://localhost:8000/api/users/" \
-H "Content-Type: application/json" \
-d '{
  "username": "somsak",
  "email": "somsak@example.com",
  "password": "123456",
  "first_name": "ສົມສັກ",
  "last_name": "ວົງສີ",
  "phone": "+8562012345678",
  "bio": "ສະບາຍດີ, ຂ້ອຍຊື່ສົມສັກ!"
}'
```

#### ເອົາຜູ້ໃຊ້ທັງໝົດ
```bash
curl -X GET "http://localhost:8000/api/users/?skip=0&limit=10"
```

#### ເອົາຜູ້ໃຊ້ຕາມ ID
```bash
curl -X GET "http://localhost:8000/api/users/1"
```

#### ອັບເດດຜູ້ໃຊ້
```bash
curl -X PUT "http://localhost:8000/api/users/1" \
-H "Content-Type: application/json" \
-d '{
  "first_name": "ສົມສັກ",
  "bio": "ອັບເດດຂໍ້ມູນໃໝ່"
}'
```

#### ເຂົ້າສູ່ລະບົບ
```bash
curl -X POST "http://localhost:8000/api/users/login" \
-H "Content-Type: application/json" \
-d '{
  "username": "somsak",
  "password": "123456"
}'
```

#### ລຶບຜູ້ໃຊ້
```bash
curl -X DELETE "http://localhost:8000/api/users/1"
```

## 🗃️ ໂຄງສ້າງຖານຂໍ້ມູນ

ຕາຕະລາງ `users` ປະກອບມີ:

- `id` - ຄີຫຼັກ (ເພີ່ມອັດຕະໂນມັດ)
- `username` - ຊື່ຜູ້ໃຊ້ທີ່ບໍ່ຊ້ຳກັນ (ສູງສຸດ 50 ຕົວອັກສອນ)
- `email` - ທີ່ຢູ່ອີເມວທີ່ບໍ່ຊ້ຳກັນ
- `password` - ລະຫັດຜ່ານທີ່ເຂົ້າລະຫັດແລ້ວ (SHA256)
- `first_name` - ຊື່ຕົວຈິງ (ບໍ່ບັງຄັບ)
- `last_name` - ນາມສະກຸນ (ບໍ່ບັງຄັບ)
- `phone` - ເບີໂທລະສັບ (ບໍ່ບັງຄັບ)
- `bio` - ຄຳບັນຍາຍຕົວ (ບໍ່ບັງຄັບ)
- `is_active` - ສະຖານະບັນຊີ (ຄ່າເລີ່ມຕົ້ນ: true)
- `is_verified` - ສະຖານະການຢືນຢັນອີເມວ (ຄ່າເລີ່ມຕົ້ນ: false)
- `created_at` - ເວລາທີ່ສ້າງ
- `updated_at` - ເວລາທີ່ອັບເດດຄັ້ງສຸດທ້າຍ

## 🔒 ຄຸນສົມບັດຄວາມປອດໄພ

- ການເຂົ້າລະຫັດລະຫັດຜ່ານດ້ວຍ SHA256
- ການກວດສອບຂໍ້ມູນນຳເຂົ້າດ້ວຍ Pydantic
- ການປ້ອງກັນ SQL injection ດ້ວຍ SQLAlchemy
- ການຈັດການຂໍ້ຜິດພາດ ແລະ ລະຫັດສະຖານະ HTTP ທີ່ຖືກຕ້ອງ
- CORS middleware ທີ່ຕັ້ງຄ່າແລ້ວ

## 🛠️ ການພັດທະນາ

### ການເຮັດວຽກໃນໂໝດພັດທະນາ

```bash
# ດ້ວຍການໂຫຼດອັດຕະໂນມັດ
python main.py

# ຫຼື ໃຊ້ uvicorn ໂດຍກົງ
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### ການທົດສອບ API

ທ່ານສາມາດທົດສອບ API ໂດຍໃຊ້:

1. **Swagger UI**: http://localhost:8000/docs
2. **ຄຳສັ່ງ curl** (ຕົວຢ່າງຂ້າງເທິງ)
3. **Postman** ຫຼື ເຄື່ອງມືຄ້າຍຄືກັນ
4. **Python requests library**

### ການເພີ່ມຄຸນສົມບັດໃໝ່

1. **Models**: ເພີ່ມແບບຈຳລອງໃໝ່ໃນໂຟນເດີ `models/`
2. **Schemas**: ກຳນົດ Pydantic schemas ໃນໂຟນເດີ `schemas/`
3. **Controllers**: ຂຽນລະບົບຄວບຄຸມໃນໂຟນເດີ `controllers/`
4. **Routes**: ສ້າງເສັ້ນທາງ API ໃນໂຟນເດີ `routes/`
5. **Update**: ລວມ router ໃໝ່ໃນ `main.py`

## 📦 ແພັກເກີຈທີ່ໃຊ້

- **FastAPI**: Framework ທີ່ທັນສະໄໝສຳລັບ APIs
- **SQLAlchemy**: SQL toolkit ແລະ ORM
- **psycopg2-binary**: PostgreSQL adapter
- **pydantic**: ການກວດສອບຂໍ້ມູນໂດຍໃຊ້ Python type annotations
- **uvicorn**: ASGI server
- **python-dotenv**: ໂຫຼດຕົວແປສະພາບແວດລ້ອມ

## 🚨 ໝາຍເຫດສຳລັບການນຳໃຊ້ຈິງ

ສຳລັບການນຳໄປໃຊ້ຈິງ:

1. ປ່ຽນ `SECRET_KEY` ໃນ `.env`
2. ຕັ້ງ `DEBUG=False`
3. ຕັ້ງຄ່າ CORS origins ທີ່ຖືກຕ້ອງ
4. ໃຊ້ຕົວແປສະພາບແວດລ້ອມສຳລັບຂໍ້ມູນລັບ
5. ຈັດຕັ້ງການຢືນຢັນຕົວຕົນທີ່ເໝາະສົມ (JWT tokens)
6. ເພີ່ມການຈຳກັດອັດຕາ
7. ໃຊ້ production ASGI server ຄື Gunicorn
8. ຕັ້ງຄ່າ database connection pooling
9. ຈັດຕັ້ງການບັນທຶກ log
10. ເພີ່ມການແບ່ງເວີຊັນ API

## 🆘 ການແກ້ໄຂບັນຫາ

### ບັນຫາທົ່ວໄປ

1. **ຂໍ້ຜິດພາດການເຊື່ອມຕໍ່ຖານຂໍ້ມູນ**
   - ກວດສອບວ່າ PostgreSQL ກຳລັງເຮັດວຽກ
   - ຢືນຢັນຂໍ້ມູນປະຈຳຕົວຖານຂໍ້ມູນໃນ `.env`
   - ໃຫ້ແນ່ໃຈວ່າຖານຂໍ້ມູນມີຢູ່

2. **ຂໍ້ຜິດພາດ Module Import**
   - ກວດສອບໄຟລ໌ `__init__.py` ມີຢູ່ໃນທຸກໂຟນເດີ
   - ຢືນຢັນວ່າ virtual environment ຖືກເປີດໃຊ້ງານ

3. **Port ຖືກໃຊ້ແລ້ວ**
   - ປ່ຽນ port ໃນ `main.py` ຫຼື ປິດ process ທີ່ໃຊ້ port 8000

4. **ຂໍ້ຜິດພາດສິດທິ**
   - ກວດສອບສິດທິຜູ້ໃຊ້ຖານຂໍ້ມູນ
   - ໃຫ້ແນ່ໃຈວ່າມີສິດທິຂຽນໃນໂຟນເດີໂປຣເຈັກ

## 🎯 ການໃຊ້ງານ

### ເຂົ້າໄປທີ່ Swagger UI:
http://localhost:8000/docs

### ທົດສອບການສ້າງຜູ້ໃຊ້:
1. ຄລິກທີ່ `POST /api/users/`
2. ຄລິກ "Try it out"
3. ໃສ່ຂໍ້ມູນ:
```json
{
  "username": "ໂຄງ",
  "email": "khong@example.com",
  "password": "123456",
  "first_name": "ໂຄງ",
  "last_name": "ລາວ"
}
```
4. ຄລິກ "Execute"

### ກວດສອບຜົນລັບ:
ທ່ານຈະເຫັນຜົນຕອບກັບທີ່ມີ status code 201 ແລະຂໍ້ມູນຜູ້ໃຊ້ທີ່ສ້າງໃໝ່

## 📞 ການສະໜັບສະໜູນ

ຖ້າມີບັນຫາ:
1. ກວດສອບ logs ເພື່ອເບິ່ງຂໍ້ຄວາມຜິດພາດລະອຽດ
2. ຢືນຢັນວ່າແພັກເກີຈທັງໝົດຖືກຕິດຕັ້ງ
3. ໃຫ້ແນ່ໃຈວ່າການເຊື່ອມຕໍ່ຖານຂໍ້ມູນເຮັດວຽກ
4. ກວດສອບເອກະສານ API ທີ່ `/docs`

## 📄 ໃບອະນຸຍາດ

ໂປຣເຈັກນີ້ແມ່ນສຳລັບການສຶກສາ. ສາມາດແກ້ໄຂຕາມຄວາມເໝາະສົມສຳລັບການໃຊ້ງານຂອງທ່ານ.

---

🎉 **ຂໍໃຫ້ມີຄວາມສຸກກັບການພັດທະນາ!** 🎉