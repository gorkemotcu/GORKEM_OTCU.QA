# Test Otomasyonu Projesi

Bu proje, Insider web sitesi için Python ve Selenium kullanılarak geliştirilmiş bir otomatik test senaryosu uygulamasıdır. Projenin sürdürülebilir ve okunabilir olması için **Page Object Model (POM)** tasarım deseni kullanılmıştır.

---

### Test Senaryosu

Bu otomasyon aşağıdaki adımları test etmektedir:

1.  **Ana Sayfa Kontrolü:** `https://useinsider.com/` adresine gidilmiş ve sayfanın başarıyla açıldığı doğrulanmıştır.

2.  **Kariyer Sayfasına Navigasyon:** Navigasyon çubuğundaki "Company" menüsü seçilmiş, ardından "Careers" seçeneğine tıklanmıştır. Kariyer sayfasının görüntülendiği ve "Locations", "Teams", "Life at Insider" bloklarının görünür olduğu doğrulanmıştır.

3.  **QA İşlerinin Filtrelenmesi:** İstanbul, Türkiye lokasyonunda "Quality Assurance" pozisyonları filtrelenmiş ve sonuçların listesi elde edilmiştir.

4.  **İş Detaylarının Doğrulanması:** Listelenen tüm pozisyonların konum ve departman bilgilerinin doğru olduğu kontrol edilmiştir.

5.  **Başvuru Formuna Yönlendirme:** "View Role" butonuna tıklandığında kullanıcının Lever Application form sayfasına başarılı bir şekilde yönlendirildiği doğrulanmıştır.

---

### Kurulum ve Çalıştırma

Gerekli kütüphaneler, `requirements.txt` dosyasından `pip install -r requirements.txt` komutu ile kurulabilir.

**Testlerin Çalıştırılması**

* Tüm testleri çalıştırmak için `pytest test_insider_automation.py` komutu kullanılmıştır.
* Detaylı bir HTML raporu almak için `pytest test_insider_automation.py --html=test_report.html` komutu çalıştırılmıştır.

---

### Proje Yapısı ve Ek Özellikler

* **Page Object Model (POM):** Proje, POM prensiplerine göre yapılandırılmıştır.
* **Hata Yönetimi:** Başarısız test durumlarında otomatik olarak ekran görüntüsü alınması sağlanmıştır.
* **Explicit Waits:** Güvenilir element bulma için `Explicit Waits` kullanılmıştır.
* **WebDriver Manager:** WebDriver yönetimini otomatik hale getirmek için `WebDriver Manager` kütüphanesinden faydalanılmıştır.
