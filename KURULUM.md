# Bu klasörü GitHub'a gönderme

Profil README'sinin görünmesi için repo adı **tam olarak** kullanıcı adınla aynı olmalı: `HaYToKoRaZ`

## 1) Repo'yu oluştur

GitHub'da **New repository** → Repository name: `HaYToKoRaZ` → **Public** → README ekleme → Create.

> Özel (private) repo olursa README profilde **görünmez**. Mutlaka public.

## 2) Bu klasörü o repoya bağla ve gönder

Bu klasörde PowerShell açıp sırayla:

```powershell
git init
git branch -M main
git remote add origin https://github.com/HaYToKoRaZ/HaYToKoRaZ.git
git add .
git commit -m "Profil README"
git push -u origin main
```

Zaten `git init` yapılmışsa sadece `git add .` satırından devam et.

## 3) Yılan animasyonunu bir kere çalıştır

`Assets` için: repo → **Actions** → sol menüden **Katkı Yılanı** → **Run workflow**.

Yaklaşık 1 dakika sonra `output` dalı oluşur ve README'deki yılan görünmeye başlar.
Her gün 03:00'te (UTC) kendini otomatik yeniler.

> Yılanı istemiyorsan: README'deki `<picture> ... </picture>` bloğunu ve
> `.github/workflows/snake.yml` dosyasını sil.

## 4) Kontrol

- https://github.com/HaYToKoRaZ → en üstte banner + README görünmeli
- Repo sayfasında "özel repo" (special repository) uyarısı çıkar, bu normal
- Değişiklik anında görünmezse 1-2 dakika bekle veya sayfayı `Ctrl+F5` ile yenile

## Notlar

- Pinlenen repo sınırı **6**'dır, artıramazsın. Ama README içinden istediğin kadar repoyu
  tablo/kart olarak gösterebilirsin — bu README'de öyle yapıldı.
- İstatistik kartları `github-readme-stats` gibi ücretsiz servislerden geliyor. Servis
  bazen yavaşlar; kart boş görünürse birkaç dakika sonra tekrar bak.
- Banner dosyası: `assets/banner.svg`. Renkleri/ yazıları değiştirmek için metin editörü yeterli.
