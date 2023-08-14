# docker-python-and-headlesschrome-scraping

dockerでつくる Pythonスクレイピングの例です。 selenium , headlesschrome, webdriver managerを使います

## 使っている各種

* Pythonパッケージはrequirements.txtが詳しいです
  * selenium
  * webdriver-manager
* docker pythonイメージ（debianベース）
* Google Chrome Stable(Linux amd64)

## 使い方

```sh
docker compose up -d
docker compose exec scraping python /app/example_scraping.py
// PyCon mini Shizuoka - connpass
// example_ss.png というファイルが生成されます
```

## 動作確認

* WLS2/Linuxだと問題ないと思います
* Apple Silicon（M1, M2系）は Docker Desktopの設定（2023-08-14時点でBetaにある）より、Rosseta2を利用するオプションを選択してください
  * 参考: （公式のドキュメントに記載が見つかったら追記します）
  * 参考: <https://applech2.com/archives/20230114-docker-for-mac-support-rosetta-2-beta.html>
