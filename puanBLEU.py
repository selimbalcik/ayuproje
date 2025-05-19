import nltk
from nltk.translate.bleu_score import sentence_bleu
#nltk.download('punkt')
import stanza

# Türkçe modelini indir ve yükle
stanza.download("tr")
nlp = stanza.Pipeline(lang="tr", processors="tokenize")

def tokenize_text(text):
    doc = nlp(text)
    tokens = [word.text for sent in doc.sentences for word in sent.words]
    return tokens

# Örnek kullanım
# sentence = "Merhaba! Stanza ile cümleleri tokenlere ayırıyorum."
# tokenized_words = tokenize_text(sentence)
# print(tokenized_words)
def bul_puanBLEU(referans_metni,test_metni):

  kck_referans_metni = referans_metni.lower()
  kck_test_metni = test_metni.lower()

  arr_TokenRef=tokenize_text(kck_referans_metni)
  arr_TokenTxt=tokenize_text(kck_test_metni)
  # print (arr_TokenRef, arr_TokenTxt)

  arr_arrTokenRef = [arr_TokenRef]
# BLEU skoru hesaplama
  bleu_score = sentence_bleu(arr_arrTokenRef, arr_TokenTxt)

# Sonucu yazdır
#  print(f"BLEU Skoru: {bleu_score:.4f}")

  return(bleu_score)