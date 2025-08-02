Türkçe Duygu Analizi Projesi (NLP)

Bu proje, Hugging Face Transformers kütüphanesi ve Streamlit kullanılarak geliştirilmiş, Türkçe metinlerin duygu durumunu (pozitif/negatif) anlık olarak analiz eden interaktif bir web uygulamasıdır.

Uygulama, karmaşık eğitim süreçlerine gerek kalmadan, savasy/bert-base-turkish-sentiment-cased adlı, Türkçe için özel olarak hazır eğitilmiş bir modeli kullanır.
🚀 Özellikler

    Türkçe metinlerin pozitif veya negatif olarak sınıflandırılması.

    Hazır eğitilmiş, yüksek performanslı bir model sayesinde hızlı ve tutarlı sonuçlar.

    Streamlit ile geliştirilmiş, basit, modern ve kullanıcı dostu web arayüzü.

    Tahmin sonuçlarının güven skoru (confidence score) ile birlikte anlık olarak gösterilmesi.

📸 Uygulama Arayüzü

(Buraya app.py çalışırken çektiğin bir ekran görüntüsü veya kısa bir GIF eklemen çok profesyonel durur!)
🛠️ Kullanılan Teknolojiler

    Python 3.12

    Streamlit

    PyTorch

    Hugging Face Transformers

⚙️ Kurulum ve Başlatma

Projeyi yerel makinenizde çalıştırmak için gereken adımlar oldukça basittir.

1. Projeyi İndirin veya Klonlayın

git clone https://github.com/SuleymanToklu/Turkce-Duygu-Analizi-Uygulamasi.git
cd Turkce-Duygu-Analizi-Uygulamasi

2. Sanal Ortam Oluşturun ve Aktive Edin

# Sanal ortamı oluştur
python -m venv venv

# Sanal ortamı aktive et (Windows)
venv\Scripts\activate

# Sanal ortamı aktive et (Linux/MacOS)
# source venv/bin/activate

3. Gerekli Kütüphaneleri Yükleyin

Projenin çalışması için gereken tüm kütüphaneler requirements.txt dosyasında listelenmiştir.

pip install -r requirements.txt

🚀 Kullanım

Uygulamayı başlatmak için tek yapmanız gereken aşağıdaki komutu çalıştırmaktır:

streamlit run app.py

Bu komutu çalıştırdıktan sonra tarayıcınızda otomatik olarak bir sekme açılacaktır. İlk çalıştırmada, model internetten indirileceği için kısa bir bekleme süresi olabilir. İndirme tamamlandıktan sonra uygulama kullanıma hazır olacaktır.
📂 Proje Yapısı

Proje, gereksiz dosyalardan arındırılmış ve basit bir yapıya sahiptir:

.
├── venv/                 # Sanal ortam klasörü
├── app.py                # Streamlit uygulamasını çalıştıran ana script
├── requirements.txt      # Gerekli kütüphanelerin listesi
└── README.md             # Bu dosya

👤 Yazar

Süleyman Toklu
