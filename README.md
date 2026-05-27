# ML Cloud Project

## Proje Hakkında
Bu proje, makine öğrenmesi kullanarak trafik yoğunluğu tahmini yapan bulut tabanlı bir uygulamadır.

Sistem:
- Python
- Flask
- Scikit-learn
- AWS EC2
- AWS S3
- GitHub

teknolojileri kullanılarak geliştirilmiştir.

---

## Projenin Amacı

Sıcaklık ve nem verilerini analiz ederek trafik yoğunluğunu tahmin eden bir makine öğrenmesi modeli geliştirmek ve bu modeli AWS bulut ortamında çalıştırmaktır.

---

## Kullanılan Teknolojiler

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- RandomForestClassifier

### Cloud Services
- AWS EC2
- AWS S3

### Version Control
- GitHub

---

## Makine Öğrenmesi Modeli

Projede Random Forest algoritması kullanılmıştır.

Model:
- sıcaklık
- nem

verilerini kullanarak trafik yoğunluğunu tahmin etmektedir.

Tahmin sınıfları:
- low
- medium
- high

---

## API Endpoint

### Ana Sayfa

```bash
GET /