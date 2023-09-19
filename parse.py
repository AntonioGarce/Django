import os
import json
import time
from pprint import pprint

from PIL import Image

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from loguru import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


def get_image_by_url(driver, url, path_to_load, path_to_save):

    paths = path_to_load.split('\\')
    paths2 = path_to_save.split('\\')
    cur_cp = ''
    for cp in range(len(paths) - 1):
        cur_cp = os.path.join(cur_cp, paths[cp])
        if not os.path.exists(cur_cp):
            os.mkdir(cur_cp)
    cur_cp = ''
    for cp in range(len(paths2) - 1):
        cur_cp = os.path.join(cur_cp, paths2[cp])
        if not os.path.exists(cur_cp):
            os.mkdir(cur_cp)
    driver.get(url)
    driver.save_screenshot(path_to_load)
    time.sleep(10)
    raw_image = Image.open(path_to_load)
    crop_x_0 = 0
    crop_x_1 = 800
    crop_y_0 = 0
    crop_y_1 = 600
    ls = True
    for i in range(raw_image.width):
        all_black = True
        for j in range(raw_image.height):
            if raw_image.getpixel((i, j)) != (14, 14, 14, 255):
                all_black = False
        if all_black and ls:
            crop_x_0 = i + 1
        elif not all_black and not ls:
            crop_x_1 = i + 1
        else:
            ls = False

    ts = True

    for i in range(raw_image.height):
        all_black = True
        for j in range(raw_image.width):
            if raw_image.getpixel((j, i)) != (14, 14, 14, 255):
                all_black = False
        if all_black and ts:
            crop_y_0 = i + 1
        elif not all_black and not ts:
            crop_y_1 = i + 1
        else:
            ts = False

    prepared_image = raw_image.crop((crop_x_0, crop_y_0, crop_x_1, crop_y_1))
    prepared_image.save(path_to_save)
    os.remove(path_to_load)


json_file_path = 'page_data_{page_num}'
shop_path = 'shop_info_{shop_num}'
json_file_name = json_file_path + '\\' + 'info_page_{page_num}.json'

# настройки
logger.add('logs.log', level='DEBUG')
logger.info('Настройка браузера')
options = Options()
options.add_argument('--headless')

# открытие браузера
logger.info('Открытие браузера')
browser = webdriver.Chrome(options=options)

# настройка ожидания загрузки элемента
logger.info('Настройка ожидания загрузки элемента')
wait = WebDriverWait(browser, 14)
wait_small = WebDriverWait(browser, 5)

# открытие ссылки
logger.info('Открытие страницы')
browser.get('https://vdb.bsbot.ltd')

# ввод капчи
while True:
    # скрин
    logger.info('Сохранение скриншота')
    browser.save_screenshot('captcha.png')

    # ввод капчи
    captcha_text = input('Введите текст с каринки: ')

    # отправка капчи
    logger.info('Отправка капчи')
    captcha_input_line = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div[2]/input')))
    captcha_input_line.send_keys(captcha_text)
    captcha_input_line.send_keys(Keys.ENTER)

    logger.info('Проверка на успешность ввода')
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div[1]/img')))
        print('Капча введена неудачно')
    except:
        print('Капча введена успешно')
        break

login = input('Введите логин для входа: ')
password = input('Введите пароль для входа: ')

# костыль
captcha_input_line = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div[4]/input')))
captcha_input_line.send_keys('huy')
login_line = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div[1]/input')))
login_line.send_keys('huy')
password_line = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div[2]/input')))
password_line.send_keys('huy')
accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/button')))
accept_button.click()

# вход
while True:
    logger.info('Ввод данных для входа')
    # ввод логина
    login_line = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div[2]/input')))
    login_line.send_keys(login)
    # ввод пароля
    password_line = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div[3]/input')))
    password_line.send_keys(password)

    # скрин
    logger.info('Сохранение скриншота')
    browser.save_screenshot('captcha.png')

    # ввод капчи
    captcha_text = input('Введите текст с картинки: ')
    logger.info('Отправка капчи')
    captcha_input_line = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div[5]/input')))
    captcha_input_line.send_keys(captcha_text)

    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/button')))
    accept_button.click()

    logger.info('Проверка на успешность ввода')
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/form/div/div[4]/img')))
        print('Капча введена неудачно')
    except:
        print('Капча введена успешно')
        break

logger.info('Вход выполнен успешно')

page_num_to_start = int(input('Введите номер страницы с котрой начнется парсинг: '))
page_num_to_finish = int(input('Введите номер страницы, на которой закончится парсинг: '))

logger.info('Запуск парсинга')

page_url = 'https://vdb.bsbot.ltd/stores?page={page_num}'

for current_page in range(page_num_to_start, page_num_to_finish+1):
    browser.get(page_url.format(page_num=current_page))
    logger.info(f'Открыта страница {current_page}')

    logger.info(f'Создание json файла для страницы: {current_page}')
    json_obj = json.loads('[]')
    if not os.path.exists(json_file_path.format(page_num=current_page)):
        os.mkdir(json_file_path.format(page_num=current_page))
        with open(json_file_name.format(page_num=current_page), 'w') as f:
            json.dump(json_obj, f)

    shops_urls = []
    for current_shop in range(1, 17):
        print(wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[{current_shop}]/a'))).get_attribute('href'))
        shop = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[{current_shop}]/a')))
        shops_urls.append(shop.get_attribute('href'))
        try:
            src = wait_small.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[{current_shop}]/a/div/div[2]/img'))).get_attribute('src')
        except:
            src = wait_small.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[{current_shop}]/a/div/div[1]/img'))).get_attribute('src')
        raw_shop_icon_path = os.path.join(json_file_path.format(page_num=current_page), shop_path.format(shop_num=shops_urls[current_shop-1].split('/')[-1]),  f'raw_icon_image_{shops_urls[current_shop - 1].split("/")[-1]}.png')
        shop_icon_image = os.path.join(json_file_path.format(page_num=current_page), shop_path.format(shop_num=shops_urls[current_shop-1].split('/')[-1]), f'icon_image_{shops_urls[current_shop - 1].split("/")[-1]}.png')
        get_image_by_url(driver=browser, url=src, path_to_load=raw_shop_icon_path, path_to_save=shop_icon_image)
        browser.get(page_url.format(page_num=current_page))

    for current_shop in range(1, 17):
        shop_url = shops_urls[current_shop-1]
        logger.debug(f'Сбор данных для магазина: "{current_page}, {current_shop}": "{shop_url}"')

        shop_id = shop_url.split('/')[-1]

        browser.get(shop_url)

        shop_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[2]/div[1]/h5'))).text

        try:
            wait_small.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[2]/div[1]/h5/img')))
            is_crown = True
        except:
            is_crown = False

        shop_rate = wait.until((EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[2]/div[1]/span[1]/span/strong')))).text
        shop_sell_count = wait.until((EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[2]/div[1]/span[2]/span/strong')))).text
        shop_deposit = wait.until((EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[2]/div[1]/span[3]/span/strong')))).text

        src = wait_small.until((EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[1]/img')))).get_attribute('src')
        shop_head_path = json_file_path.format(page_num=current_page) + '\\' + shop_path.format(shop_num=shops_urls[current_shop-1].split('/')[-1]) + '\\' + f'head_image_{shop_id}.png'
        raw_shop_head_path = json_file_path.format(page_num=current_page) + '\\' + shop_path.format(shop_num=shops_urls[current_shop-1].split('/')[-1]) + '\\' + f'raw_head_image_{shop_id}.png'
        get_image_by_url(driver=browser, url=src, path_to_load=raw_shop_head_path, path_to_save=shop_head_path)

        try:
            shop_category = wait_small.until((EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[2]/div[1]/span[4]/strong')))).text
        except:
            shop_category = None
        try:
            shop_description = wait_small.until((EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/section[2]/div/div/div/div[2]')))).text
        except:
            shop_description = None
        try:
            browser.get(f'{shop_url}/rules')
            shop_rules = wait_small.until((EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/section/div/div/div/div[2]/div')))).text
        except:
            shop_rules = None
        try:
            browser.get(f'{shop_url}/work')
            shop_work = wait_small.until((EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/section/div/div/div/div[2]/div')))).text
        except:
            shop_work = None
        try:
            shop_forum = wait_small.until((EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[3]/div[1]/a[4]')))).get_attribute('href')
        except:
            shop_forum = None
        try:
            browser.get(f'{shop_url}/promotions')
            shop_promotions = wait_small.until((EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/section/div/div/div/div[2]/div')))).text
        except:
            shop_promotions = None

        browser.execute_script("window.scrollTo(0, 3000)")

        browser.get(shop_url)
        products_info = []
        products_ids = []
        for current_product in range(1, 1000):
            try:
                logger.info(f'Сохранение информации о фото для товара с номером {current_product}')
                src = wait_small.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div[2]/div/section[1]/div/div/div/div[3]/div[{current_product}]/div/a/div[2]/img'))).get_attribute('src')
                products_ids.append(browser.find_element(By.XPATH, f'/html/body/div/div[1]/div[2]/div/section[1]/div/div/div/div[3]/div[{current_product}]/a').get_attribute('href').split('/')[-1])
                product_icon_path = json_file_path.format(page_num=current_page) + '\\' + shop_path.format(shop_num=shops_urls[current_shop-1].split('/')[-1]) + '\\' + f'product_icon_{products_ids[current_product-1]}.png'
                raw_product_icon_path = json_file_path.format(page_num=current_page) + '\\' + shop_path.format(shop_num=shops_urls[current_shop-1].split('/')[-1]) + '\\' + f'raw_product_icon_{products_ids[current_product-1]}.png'
                get_image_by_url(driver=browser, url=src, path_to_load=raw_product_icon_path, path_to_save=product_icon_path)
                browser.get(shop_url)
            except:
                break
        i = 0
        for current_product_id in products_ids:
            browser.get('https://vdb.bsbot.ltd/products/' + current_product_id)
            products_info.append({})
            products_info[i]['product_id'] = current_product_id
            products_info[i]['price'] = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div[2]/span[1]/strong'))).text
            try:
                products_info[i]['weight'] = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div[2]/span[2]'))).text
            except:
                products_info[i]['weight'] = None
                logger.debug('HUY, нет веса')
            try:
                products_info[i]['description'] = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div[3]'))).text
            except:
                logger.debug('HUY, нет описания')
                products_info[i]['description'] = None
            locations = []
            for current_loc in range(1, 1000):
                try:
                    city = wait_small.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div[2]/div/div[3]/div[2]/div/table/tbody/tr[{current_loc}]/td[1]'))).text
                    weight = wait_small.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div[2]/div/div[3]/div[2]/div/table/tbody/tr[{current_loc}]/td[2]'))).text
                    loc_type = wait_small.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div[2]/div/div[3]/div[2]/div/table/tbody/tr[{current_loc}]/td[3]'))).text
                    price = wait_small.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div[2]/div/div[3]/div[2]/div/table/tbody/tr[{current_loc}]/td[4]'))).text
                    locations.append({'city': city, 'weight': weight, 'loc_type': loc_type, 'price': price})
                except:
                    break

            products_info[i]['locations'] = locations

            i += 1

        with open(json_file_name.format(page_num=current_page), 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        shop_data = {"id": shop_id, "name": shop_name, "is_crown": is_crown, "head_image": shop_head_path, "rate": shop_rate, "sell_count": shop_sell_count, "deposit": shop_deposit, "category": shop_category, "forum": shop_forum, "description": shop_description, "rules": shop_rules, "work": shop_work, "promotions": shop_promotions, "products": products_info}

        json_data.append(shop_data)
        pprint(str(shop_data))
        pprint(str(json_data))
        with open(json_file_name.format(page_num=current_page), 'w', encoding='utf-8') as f:
            json.dump(json_data, f)
        browser.get(page_url.format(page_num=current_page))
    # except Exception as e:
    #         with open('shops_with_error.txt', 'a') as f:
    #             f.write(f'Shop "{shops_urls[current_shop-1]}" have error: "{e}"\n')
    #         logger.error(e)

browser.quit()

# test_parse_1239384
