from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>SMM Paneli</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f9f9f9; }
        h1 { color: #333; }
        form, .services { background: white; padding: 20px; border-radius: 8px; margin-top: 20px; }
        label { display: block; margin-top: 10px; }
        input, select, textarea { width: 100%; padding: 10px; margin-top: 5px; }
        button { margin-top: 15px; padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; }
        .message { background: #d4edda; color: #155724; padding: 10px; border-radius: 5px; margin-top: 10px; }
    </style>
</head>
<body>
    <h1>Kimsebaşgöz SMM Paneli</h1>

    {% if message %}
        <div class="message">{{ message }}</div>
    {% endif %}

    <div class="services">
        <h2>Hizmetler</h2>
        <ul> düşme yoktur
            <li>✅ Instagram Takipçi - 250tl / 1000</li>
            <li>✅ Instagram Beğeni - 80tl / 1000</li>
            <li>✅ TikTok Takipçi - 325tl / 1000</li>
        </ul>
    </div>

    <form method="post">
        <h2>Sipariş Ver</h2>
        <label for="service">Hizmet:</label>
        <select name="service" id="service" required>
            <option value="takipci">Instagram Takipçi</option>
            <option value="begeni">Instagram Beğeni</option>
            <option value="izlenme">TikTok Takipçi</option>
        </select>

        <label for="link">Gönderi Linki / Kullanıcı Adı:</label>
        <input type="text" name="link" id="link" required>

        <label for="amount">Miktar:</label>
        <input type="number" name="amount" id="amount" required>

        <label for="email">E-posta (Bilgi için):</label>
        <input type="email" name="email" id="email">

        <button type="submit">Sipariş Ver</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def panel():
    message = None
    if request.method == "POST":
        service = request.form.get("service")
        link = request.form.get("link")
        amount = request.form.get("amount")
        email = request.form.get("email")

        # Siparişi dosyaya yaz
    with open("siparisler.txt", "a", encoding="utf-8") as f:
        f.write(f"{service},{amount},{link},{email}\n")

    message = f"✅ Sipariş alındı: {service} - {amount} adet ({link})"
        # Burada siparişi kaydedebilirsin, veri tabanına yazmak gibi

        message = f"✅ Sipariş alındı: {service} - {amount} adet ({link})"

    return render_template_string(HTML_PAGE, message=message)
