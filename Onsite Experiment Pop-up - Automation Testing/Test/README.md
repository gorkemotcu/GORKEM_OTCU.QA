# Insider Test Automation

Bu proje, Insider web sitesi için otomatik test senaryosu uygulamasıdır. Page Object Model (POM) desenini kullanarak geliştirilmiştir.

## Test Senaryosu

Bu otomasyon aşağıdaki 5 adımı test eder:

1. **Ana Sayfa Ziyareti**: `https://useinsider.com/` adresine gidilir ve Insider ana sayfasının başarıyla açıldığı doğrulanır.

2. **Kariyer Sayfasına Navigasyon**: Navigasyon çubuğundaki "Company" menüsü seçilir, ardından "Careers" seçilir. Kariyer sayfasının görüntülendiği ve "Locations", "Teams", "Life at Insider" bloklarının görünür olduğu doğrulanır.

3. **QA İşlerini Filtreleme**: Doğrudan `https://useinsider.com/careers/quality-assurance/` adresine gidilir. "See all QA jobs" butonuna tıklanır. "Location: Istanbul, Turkey" ve "Department: Quality Assurance" filtreleri uygulanır. Filtreleme sonrası iş listesinin mevcut olduğu doğrulanır.

4. **İş Detaylarını Doğrulama**: Listelenen tüm işler için "Position" alanının "Quality Assurance" içerdiği, "Department" alanının "Quality Assurance" içerdiği ve "Location" alanının "Istanbul, Turkey" içerdiği kontrol edilir.

5. **Başvuru Formuna Yönlendirme**: "View Role" butonuna tıklanır ve bu işlemin kullanıcıyı Lever Application form sayfasına yönlendirdiği doğrulanır.

## Proje Yapısı

```
Test/
├── pages/
│   ├── __init__.py
│   ├── base_page.py          # Temel sayfa sınıfı
│   ├── home_page.py          # Ana sayfa işlemleri
│   ├── careers_page.py       # Kariyer sayfası işlemleri
│   └── jobs_page.py          # İş sayfası işlemleri
├── test_insider_automation.py # Ana test dosyası
├── requirements.txt           # Gerekli kütüphaneler
├── README.md                 # Bu dosya
```

## Gereksinimler

### Yazılım Gereksinimleri
- Python 3.7+
- Chrome tarayıcısı
- pip (Python paket yöneticisi)

### Python Kütüphaneleri
- selenium==4.15.2
- webdriver-manager==4.0.1
- pytest==7.4.3
- pytest-html==4.1.1

## Kurulum ve Çalıştırma

### 1. Sanal Ortam Oluşturma (Önerilen)
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Gerekli Kütüphaneleri Yükleme
```bash
pip install -r requirements.txt
```

### 3. Testleri Çalıştırma

#### Tüm testleri çalıştırmak için:
```bash
python test_insider_automation.py
```

#### Veya pytest ile:
```bash
pytest test_insider_automation.py -v
```

#### HTML raporu ile çalıştırmak için:
```bash
pytest test_insider_automation.py -v --html=test_report.html --self-contained-html
```

## Test Raporları

Testler çalıştırıldıktan sonra:
- Konsol çıktısında detaylı log mesajları görüntülenir
- Başarısız testler için otomatik olarak ekran görüntüsü alınır (`screenshots/` klasöründe)
- HTML raporu oluşturulur (`test_report.html`)

## Özellikler

### Gereksinimlere Uygunluk
- **Programlama Dili**: Python + Selenium
- **BDD Framework Kullanımı**: Yok (Cucumber, Quantum, Codeception kullanılmadı)
- **Hata Durumunda Ekran Görüntüsü**: Otomatik olarak alınır
- **POM Uyumluluğu**: Tam Page Object Model uygulandı

### Teknik Özellikler
- **Page Object Model**: Her sayfa için ayrı sınıf
- **Explicit Wait**: Güvenilir element bulma
- **Hata Yönetimi**: Kapsamlı exception handling
- **Screenshot**: Başarısız testler için otomatik ekran görüntüsü
- **HTML Raporlama**: Detaylı test raporları
- **WebDriver Manager**: Otomatik driver yönetimi

## Test Adımları Detayı

### Adım 1: Ana Sayfa Ziyareti
- Insider ana sayfasına gidilir
- Sayfa başlığı kontrol edilir
- Sayfa yüklenme durumu doğrulanır

### Adım 2: Kariyer Sayfasına Navigasyon
- Company menüsüne tıklanır
- Careers linkine tıklanır
- Kariyer sayfası yüklenme durumu kontrol edilir
- Gerekli blokların görünürlüğü doğrulanır

### Adım 3: QA İşlerini Filtreleme
- QA işleri sayfasına doğrudan gidilir
- "See all QA jobs" butonuna tıklanır
- Konum filtresi uygulanır (Istanbul, Turkey)
- Departman filtresi uygulanır (Quality Assurance)
- İş listesinin varlığı doğrulanır

### Adım 4: İş Detaylarını Doğrulama
- Tüm listelenen işler için:
  - Position alanında "Quality Assurance" kontrolü
  - Department alanında "Quality Assurance" kontrolü
  - Location alanında "Istanbul, Turkey" kontrolü

### Adım 5: Başvuru Formuna Yönlendirme
- "View Role" butonuna tıklanır
- Lever Application form sayfasına yönlendirme doğrulanır

## Sorun Giderme

### Yaygın Sorunlar

1. **ChromeDriver Hatası**: WebDriver Manager otomatik olarak uygun driver'ı indirir
2. **Element Bulunamadı**: Sayfa yapısı değişmiş olabilir, locator'ları güncelleyin
3. **Timeout Hatası**: İnternet bağlantısını kontrol edin

### Debug İpuçları
- `screenshots/` klasöründeki ekran görüntülerini inceleyin
- Konsol çıktısındaki detaylı log mesajlarını takip edin
- HTML raporunu tarayıcıda açarak detaylı sonuçları görün

## Destek

Herhangi bir sorun yaşarsanız:
1. Önce `screenshots/` klasöründeki ekran görüntülerini kontrol edin
2. Konsol çıktısındaki hata mesajlarını inceleyin
3. HTML raporunu detaylı olarak inceleyin