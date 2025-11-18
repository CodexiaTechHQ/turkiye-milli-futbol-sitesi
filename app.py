# app.py

from flask import Flask, render_template, url_for

app = Flask(__name__)
# Statik dosyaların önbelleklemesini devre dışı bırakmak için (geliştirme aşaması için faydalı)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 

# Tek sayfalık sitenin ana rotası
@app.route('/')
def home():
    # Burada, gelecekte veri tabanı veya JSON dosyasından maç verilerini çekip 
    # 'render_template' fonksiyonuna argüman olarak gönderebilirsiniz. 
    # Şimdilik sadece template'i yüklüyoruz.
    return render_template('index.html')

# Flask uygulamasını çalıştırma
if __name__ == '__main__':
    # 'debug=True' geliştirme sırasında değişikliklerin otomatik yüklenmesini sağlar.
    app.run(debug=True)