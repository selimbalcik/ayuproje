# ayuproje
Ahmet Yesevi Üniversitesi tezsiz yüksek lisans proje ödevi için açılan alandır.

Proje konusu kapsamında geliştirilen bu yazılımın amacı, LLM çıktılarının Türkçe cümle yapısı açısından doğruluk ve akıcılığına ilişkin bir metrik oluşturmaktır.

Proje kapsamında yapılan çalışmaların tekrarı için şu adımlar uygulanır:
  1) Veri setini LLM'e vererek LLM cevapları oluşturma:
     1.1) LLM_oku_cevapla.py adlı modül içindeki input olarak verilen dosya ismi önce test verisini içeren "veri_test.txt" olarak belirlenir.
             # Veri setini oku
             input_file = "veriseti_test.txt"
             output_file = "veriseti_LLMcevaplar.txt"
     1.2) Program çalıştırılır ve "veriseti_LLMcevaplar.txt" dosyası oluşur.
  2) Metrik ölçümleri çalıştırılarak Referans ve LLM cevap veri setlerinden puan hesaplanması.
     2.1) odev.ipynb jupyter_notebook dosyası açılarak referans ve test dosyası isimleri belirlenir.
             referans_dosyasi = "veriseti_test.txt"
             test_dosyasi = "veriseti_LLMcevaplar.txt"
     2.2) Jupyter_notebook üzerinde zaten tek bir kod penceresi vardır. Bu kod penceresi çalıştırılır.
     2.3) Tüm puanlamaları içeren "output.txt" dosyası oluşur.

"tokenizer.py" adlı modüle bağımlılık bulunmamaktadır. Denemeler aşamasında kullanılmış sonrasında "stanza" kütüphanesinin tokenizer metodu tercih edilmiştir.
