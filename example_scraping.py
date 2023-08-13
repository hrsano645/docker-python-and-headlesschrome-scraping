# Ref: https://sushiringblog.com/chromedriver-error#index_id1
# Ref: https://qiita.com/DisneyAladdin/items/431e9fd0c1cf709347da

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():

    # headless modeを設定
    webdriver_options = Options()
    webdriver_options.add_argument("--headless=new")
    webdriver_options.add_argument("--no-sandbox")
    webdriver_options.add_argument("--disable-dev-shm-usage")
    # ChromeのWebDriverオブジェクトを作成
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=webdriver_options
    )

    # pycon mini shizuokaのcommpassページへアクセス

    driver.get("https://pycon-shizu.connpass.com")
    site_title = driver.title
    print(site_title)

    # ページ全体の縦横を取得してウィンドウサイズを設定
    driver.set_window_size(
        driver.execute_script("return document.body.scrollWidth;"),
        driver.execute_script("return document.body.scrollHeight;")
    )

    # スクリーンショット撮影
    driver.save_screenshot(Path("./example_ss.png"))

    driver.close()
   
if __name__ == "__main__":
    main()