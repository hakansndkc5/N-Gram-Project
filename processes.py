import json
import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('punkt')

def process_json_files(input_folder, output_file):
    # Türkçe stopword listesi
    stop_words = set(stopwords.words('turkish'))

    # Tüm düzenlenmiş ictihat metinlerini saklayacağımız bir liste oluşturun
    processed_texts = []

    # İçinde JSON dosyalarının olduğu klasörde dolaş
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(input_folder, filename)

            # JSON dosyasını oku
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # 'ictihat' alanını al
            ictihat_text = data['ictihat']

            # Noktalama işaretlerini kaldır
            text_without_punctuation = ictihat_text.translate(str.maketrans("", "", string.punctuation))

            # Küçük harfe dönüştür
            lowercase_text = text_without_punctuation.lower()

            # Kelimeleri ayır ve stopwords'leri filtrele
            words = word_tokenize(lowercase_text)
            filtered_words = [word for word in words if word not in stop_words]

            # Düzenlenmiş metni birleştir ve listeye ekle
            processed_text = ' '.join(filtered_words)
            processed_texts.append(processed_text)

    # Tüm düzenlenmiş metinleri tek bir TXT dosyasına yaz
    with open(output_file, 'w', encoding='utf-8') as output:
        for text in processed_texts:
            output.write(text + '\n')


input_folder ="test"
output_file = "processed_ictihatstest.txt"

process_json_files(input_folder, output_file)
