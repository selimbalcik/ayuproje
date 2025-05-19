import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import csv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Model ve tokenizer yükleme
MODEL_NAME = "vngrs-ai/VBART-Large-Paraphrasing"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Veri setini oku
#input_file = "veriseti_referans.txt"
input_file = "veriseti_test.txt"
output_file = "veriseti_LLMcevaplar.txt"


# Cümleleri içeren listeyi oluştur
sentences = []
groups = []  # Grupları saklamak için

with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")  # Ayracı ";" olarak belirtiyoruz
    next(reader)  # Başlık satırını geç
    for row in reader:
        groups.append(row[0])  # GRUP bilgisini sakla
        sentences.append(row[1])  # CUMLE bilgisini sakla

# Her cümleyi paraphrase et ve yeni dosyaya yaz
with open(output_file, "w", encoding="utf-8") as file:
    file.write("GRUP;CUMLE\n")  # Başlık satırı

    for group, sentence in zip(groups, sentences):
        token_input = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
        del token_input["token_type_ids"]  # Uyumsuz parametreyi kaldır

        # Paraphrased cümle oluştur
        outputs = model.generate(**token_input)
        paraphrased_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        file.write(f"{group};{paraphrased_text}\n")  # Yeni dosyaya yaz

print(f"LLM_cevaplar.txt başarıyla oluşturuldu ve paraphrased cümleler kaydedildi!")