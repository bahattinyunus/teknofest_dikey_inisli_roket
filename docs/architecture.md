# 🏗️ Vertical-Arch Sistem Mimarisi

> **Yazar:** Bahattin Yunus Çetin  
> **Tarih:** 2025  
> **Durum:** DRAFT v1.0

## 🎯 Vizyon vs. Gerçeklik

Vertical-Arch projesi, ileri seviye otonom roket iniş sistemlerinin bir simülasyonu ve kavramsal tasarımıdır. Bu döküman, projenin nihai hedefindeki mimari ile mevcut simülasyon ortamı arasındaki ilişkiyi açıklar.

### 1. Kontrol Döngüsü Mimarisi

#### İdeal Senaryo (RTOS - Real Time Operating System)
Gerçek bir roket uçuş bilgisayarında (örneğin STM32H7 veya Zynq FPGA üzerinde), işlemler katı zaman kısıtlamaları altında **RTOS** (FreeRTOS veya ChibiOS) üzerinde koşar.

- **Navigation (400Hz):** Sensörlerden (IMU, Barometre, GPS) ham veriyi okur ve Kalman Filtresi ile durum kestirimi yapar.
- **Control (100Hz):** Navigasyon verisini alır, hedef yörünge ile karşılaştırır ve PID/LQR algoritmaları ile motor komutlarını üretir.
- **Actuation (50Hz):** TVC (Thrust Vector Control) servolarına PWM sinyalleri gönderir.

#### Mevcut Simülasyon (Python)
Şu anki `sim/flight_sim.py` dosyamız, bu karmaşık yapıyı basitleştirilmiş bir döngüde modellemektedir:
- **Tek Thread:** Tüm fizik, kontrol ve sensör işlemleri sıralı çalışır.
- **Floating Point:** Gerçek donanımdaki sabit noktalı sayı aritmetiği yerine Python'ın yüksek hassasiyetli float değerleri kullanılır.

### 2. Algoritmik Derinlik

#### Navigasyon
- **Teori:** Extended Kalman Filter (EKF) kullanılarak GPS gecikmeleri ve İvmeölçer bias'ları kompanse edilir.
- **Simülasyon:** `src/sensor_fusion.py` içerisinde lineer bir 1D Kalman Filtresi uygulanmıştır. Sadece dikey eksendeki (Z) gürültüyü filtreler.

#### Kontrol
- **Teori:** Model Predictive Control (MPC) ile gelecekteki rotayı tahmin ederek yakıt optimizasyonu yapılır.
- **Simülasyon:** `src/controller.py` içerisinde klasik PID (Oransal-İntegral-Türev) kontrolcüsü kullanılmıştır. İniş hızı profilini takip etmek için yeterlidir.

## 🛠️ Gelecek Geliştirme Haritası (Roadmap)

1. **3DOF Simülasyon:** Roketi sadece yukarı-aşağı değil, yana yatma (pitch/yaw) davranışlarını da içerecek şekilde modellemek.
2. **Monte Carlo Analizi:** Rüzgar, sensör hatası ve motor tepki süresi gibi belirsizlikleri rastgele değiştirerek 1000+ iniş denemesi yapmak.
3. **C++ Port:** Python prototipinin, gömülü sistemlerde çalışabilecek C++ koduna dönüştürülmesi.

---
*Bu döküman, TEKNOFEST 2025 dikey iniş kategorisi teknik tasarım raporu referans alınarak hazırlanmıştır.*
