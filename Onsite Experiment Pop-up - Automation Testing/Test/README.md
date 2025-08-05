Başlık: Test Otomasyonu Projesi

Giriş
Bu proje, Insider web sitesi için Python ve Selenium kullanarak geliştirilen bir otomatik test senaryosu uygulamasıdır. Proje, sürdürülebilir ve okunabilir olması için Page Object Model (POM) tasarım deseni kullanılarak oluşturuldu.

Test Senaryosu
Otomasyon aşağıdaki adımları test eder:

Ana Sayfa Kontrolü: https://useinsider.com/ adresine gidilmesi ve sayfanın başarılı bir şekilde açılması.

Kariyer Sayfası Navigasyonu: Navigasyon menüsünden "Company" -> "Careers" adımlarıyla kariyer sayfasına gidilmesi ve sayfanın doğru yüklendiğinin doğrulanması.

QA İşleri Filtreleme: İstanbul, Türkiye lokasyonundaki "Quality Assurance" pozisyonlarının filtrelenmesi ve sonuçların listelenmesi.

İş Detaylarını Doğrulama: Listelenen tüm pozisyonların konum ve departman bilgilerinin doğrulanması.

Başvuru Formuna Yönlendirme: Pozisyon detay sayfasındaki "View Role" butonuna tıklanarak başvuru sayfasına başarılı bir şekilde yönlendirildiğinin kontrolü.

Kurulum ve Çalıştırma

Gerekli Kütüphaneler: Proje için gerekli kütüphaneler requirements.txt dosyasından pip install -r requirements.txt komutu ile kurulabilir.

Testleri Çalıştırma: Testleri çalıştırmak için pytest test_insider_automation.py komutu kullanılabilir veya direkt IDE üzerinden run edilebilir. Detaylı bir HTML raporu almak istenirse, pytest test_insider_automation.py --html=test_report.html komutu çalıştırılabilir.

Proje Yapısı ve Ek Özellikler

Projeyi Page Object Model (POM) prensiplerine göre yapılandırıldı.

Başarısız test durumlarında otomatik olarak ekran görüntüsü alınır.

Güvenilir element bulma için Explicit Waits kullanıldı.

WebDriver yönetimi için WebDriver Manager kütüphanesinden faydalanıldı.
