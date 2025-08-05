# Insider QA Test Raporu

Bu proje, gerçekleştirilen manuel ve otomasyon testlerini içermektedir. Bir web uygulamasının çeşitli fonksiyonları test edilmiş, hatalar raporlanmış ve otomasyon testi gerçekleştirilmiştir.

Manuel testler, bir ürün sayfasında gösterilen pop-up'ın işlevselliğini ve responsive tasarımını hedefleyen 6 farklı test senaryosundan oluşmaktadır.

---

### Test Senaryoları

* **TC-OEP-0001:** Pop-up'ın sadece ürün sayfasında gösterilip gösterilmediğinin kontrolü.
* **TC-OEP-0002:** Pop-up üzerinde doğru ürün bilgilerinin (ad, fiyat vb.) gösterilip gösterilmediğinin kontrolü.
* **TC-OEP-0003:** Pop-up'ı kapatma düğmesinin (çarpı işareti) doğru çalışıp çalışmadığının kontrolü.
* **TC-OEP-0004:** Pop-up üzerindeki "Add to Cart" (Sepete Ekle) butonunun doğru çalışıp çalışmadığının kontrolü.
* **TC-OEP-0005:** Pop-up üzerindeki sepet sayacının değerinin doğruluğunun kontrolü.
* **TC-OEP-0006:** Pop-up'ın mobil ve tablet görünümlerinde (responsive tasarım) doğru çalışıp çalışmadığının kontrolü.

---

### Hata Raporları

Manuel testler sırasında tespit edilen ve raporlanan hataların bir özeti aşağıdadır.

* **BUG-OEP-0001:** Pop-up, sadece ürün sayfasında değil, diğer tüm sayfalarda da görünmektedir.
* **BUG-OEP-0002:** Pop-up üzerinde gösterilen ürün fiyatı ve para birimi yanlıştır.
* **BUG-OEP-0003:** Pop-up'ı kapatma düğmesi işlevsel değildir.
* **BUG-OEP-0004:** Pop-up üzerindeki "Add to Cart" butonu çalışmamaktadır.
* **BUG-OEP-0005:** Pop-up üzerindeki sepet sayacının değeri yanlıştır.
* **BUG-OEP-0006:** Pop-up'ın responsive tasarımı hatalıdır; mobil ve tablet görünümlerinde düzgün çalışmamaktadır.

---

### Otomasyon Testleri

Otomasyon testleri, Insider web sitesinin ana sayfa, kariyer sayfaları ve iş başvuru süreçlerini Page Object Model (POM) tasarım deseni kullanarak test eder.

**Kullanılan Teknolojiler:**
* **Programlama Dili:** Python
* **Test Çatısı:** Pytest
* **Web Otomasyonu:** Selenium
* **Raporlama:** HTML formatında test raporu (`test_report.html`)

---

### Otomasyon Test Senaryoları

Otomasyon testleri, aşağıdaki adımları kontrol eder:

* **Ana Sayfa Ziyareti:** `https://useinsider.com/` adresine gidilmesi ve sayfanın başarılı bir şekilde yüklendiğinin doğrulanması.
* **Kariyer Sayfasına Navigasyon:** Ana sayfadan "Company" menüsü altındaki "Careers" seçeneği kullanılarak kariyer sayfasına geçiş yapılması ve sayfanın doğru şekilde görüntülendiğinin doğrulanması.
* **Kariyer Sayfası Kontrolleri:** "Locations", "Teams" ve "Life at Insider" bölümlerinin kariyer sayfasında var olduğunun doğrulanması.
* **Pozisyon Arama:** İstanbul, Türkiye lokasyonunda "Quality Assurance" pozisyonlarının filtrelenmesi ve sonuçların listelenmesi.
* **Pozisyon Detay Kontrolü:** Listelenen pozisyonlardan birinin detay sayfasına gidilmesi ve "Apply Now" butonunun görünür olduğunun doğrulanması.
