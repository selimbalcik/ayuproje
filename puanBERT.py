# Gerekli kütüphaneleri yükleyin
# pip install bert-score transformers

from bert_score import score

# Örnek referans ve test metinleri (Türkçe)
# referans_metni = ["BERT modeli doğal dil işleme alanında önemli bir gelişmedir."]
# test_metni = ["BERT, metin anlamını yakalamada güçlü bir yapay zeka modelidir."]

def bul_puanBERT(referans_metni, test_metni):
  model_name = "dbmdz/distilbert-base-turkish-cased"


# BERTScore hesaplama
  result = score(test_metni, referans_metni, model_type=model_name, lang="tr")
  # P, R, F1 = score(test_metni, referans_metni, model_type=model_name, lang="tr")

# Sonuçları yazdır
#   print(f"Presizyon (P): {P.mean():.4f}")
#   print(f"Recall (R): {R.mean():.4f}")
#   print(f"F1 Skoru: {F1.mean():.4f}")
 
#  print(result)
 
  return (result)