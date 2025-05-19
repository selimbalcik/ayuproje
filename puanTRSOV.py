import stanza
import string

# Türkçe NLP modeli yükle
stanza.download("tr")
nlp = stanza.Pipeline(lang="tr", processors="tokenize,mwt,pos,lemma,depparse")

# Geçerli sıralamalar ve puanlar
valid_orders = {
    ("S", "O", "V"): 0.99,
    ("O", "S", "V"): 0.66,
    ("S", "V"): 0.66,
    ("O", "V"): 0.33,
    ("V",): 0.11
}

def bul_puanSOV(sentence):
    # Noktalama işaretlerini kaldır
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    doc = nlp(sentence)
    word_order = []
    dependencies = {}  # Kelimelerin bağımlılık ilişkilerini saklamak için
    root_word = None   # Gerçek yüklem ("V") kelimesini saklamak için

    for sent in doc.sentences:
        for word in sent.words:
            dependencies[word.text] = word.head  # Bağımlı olduğu kelimeyi sakla
            
            if word.deprel == "nsubj":
                word_order.append("S")  # Özne
            elif word.deprel == "root":
                root_word = word.text  # Gerçek yüklem olarak işaretle
                if "V" not in word_order:  # Fazladan "V" eklemeyi önler
                    word_order.append("V")
            elif word.deprel == "compound":
                # Eğer yüklem yanlış şekilde "compound" olarak etiketlenmişse, gerçek yüklem olarak kabul et
                root_word = word.text  
                if "V" not in word_order:
                    word_order.append("V")
            else:
                word_order.append("O")  # Diğer tüm öğeler nesne olarak sınıflanır

    # **Son "O" öğesinin bağımlılık kontrolü**
    if word_order[-1] == "O":
        last_word = doc.sentences[0].words[-1].text  # Son kelimeyi al
        last_V_index = word_order.index("V") if "V" in word_order else -1
        last_V_word = root_word  # Güncellenmiş gerçek yüklem kelimesini kullan

        # Eğer son kelime yüklem ("V") ile bağlantılı değilse son "O" kaldır
        if dependencies.get(last_word) == last_V_index or dependencies.get(last_word) == dependencies.get(last_V_word):
            word_order.pop()

    # **Doğru sıralama kontrolü**
    order_tuple = tuple(word_order)
    puan = valid_orders.get(order_tuple, 0.0)

    # Eğer "V"den sonra başka bir öğe varsa puanı sıfırla
    if word_order.index("V") < len(word_order) - 1:
        puan = 0.00

    # **Doğru sıralama kontrolü ve puan hesaplama**
    if "S" in word_order and "V" in word_order:
        first_S_index = word_order.index("S")
        last_V_index = word_order.index("V")

        if first_S_index < last_V_index:
            if any(elem == "O" for elem in word_order[first_S_index:last_V_index]):
                puan = valid_orders.get(("S", "O", "V"), 0.99)  # "S", "O", "V" olarak kabul et
            else:
                puan = valid_orders.get(("S", "V"), 0.66)  # "S", "V" olarak kabul et
        else:
            puan = 0.00  # Eğer "V" önce gelirse geçersiz
    elif "V" in word_order and all(elem == "O" for elem in word_order[:-1]):  
        puan = valid_orders.get(("O", "V"), 0.33)  # "O", "V" olarak kabul et
    elif word_order == ["V"]:  
        puan = valid_orders.get(("V",), 0.11)  # Tek başına "V" ise 0.11 puan ver
    else:
        puan = valid_orders.get(tuple(word_order), 0.0)



    # print(f"✅ Güncellenmiş Puan: {puan}")  # Hata olup olmadığını görmek için ekleme!        
    
    # # Bağımlılık ilişkilerini ekrana yazdır
    # print("\n📌 Bağımlılık Analizi:")
    # for word in doc.sentences[0].words:
    #     print(f"Kelime: {word.text} -> Başlı Kelime ID: {word.head} -> Etiket: {word.deprel}")
     
    return {
        "sentence": sentence,
        "word_order": word_order,
        "Puan": puan
    }
