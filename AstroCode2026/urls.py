from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AstroCode2026/', include('App.urls')),
]

# هذا الجزء هو المسؤول عن تشغيل الـ CSS والـ JS محلياً
if settings.DEBUG:
    # لخدمة ملفات الـ static (بما فيها الـ Admin)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # لخدمة ملفات الـ media (الصور المرفوعة)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # إذا كنت تستخدم مجلد Assits بشكل خاص داخل تطبيق App
    # يفضل دمج هذه الملفات ضمن الـ static، ولكن إذا أردت مساراً منفصلاً:
    urlpatterns += static('/Assits/', document_root=settings.BASE_DIR / 'App/Assits')