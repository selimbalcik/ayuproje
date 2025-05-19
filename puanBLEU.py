import nltk
from nltk.translate.bleu_score import sentence_bleu
#nltk.download('punkt')
import tokenizer

def bul_puanBLEU(referans_metni,test_metni):

  kck_referans_metni = referans_metni.lower()
  kck_test_metni = test_metni.lower()

  tokenizer_instance = tokenizer.Tokenizer()
  arr_TokenRef=tokenizer_instance.tokenize(kck_referans_metni)
  arr_TokenTxt=tokenizer_instance.tokenize(kck_test_metni)
  # print (arr_TokenRef, arr_TokenTxt)

  arr_arrTokenRef = [arr_TokenRef]
# BLEU skoru hesaplama
  bleu_score = sentence_bleu(arr_arrTokenRef, arr_TokenTxt)

# Sonucu yazdır
#  print(f"BLEU Skoru: {bleu_score:.4f}")

  return(bleu_score)