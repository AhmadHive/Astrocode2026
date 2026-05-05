FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# تحديث حزم النظام وتثبيت المتطلبات لـ Pillow و Postgres و MySQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \
    # متطلبات Pillow (معالجة الصور)
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    # متطلبات mysqlclient و pkg-config التي ظهرت في سجل الخطأ
    pkg-config \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ملاحظة: إذا فشل هذا السطر، تأكد من نقل "import os" لأعلى ملف settings.py
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "AstroCode2026.wsgi:application"]