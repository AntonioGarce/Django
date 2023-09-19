import json
import os
import shutil
from pprint import pprint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.getcwd()}/db.sqlite3"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
connection = engine.connect()


def get_q_from_data(values, q_type: str):
    shop_q = "INSERT INTO stores_stores(" \
             "id," \
             "img," \
             "name," \
             "rating," \
             "sold," \
             "deposit," \
             "description," \
             "works," \
             "rules," \
             "sales," \
             "forum," \
             "store_type," \
             "cover," \
             "is_crown) VALUES"
    good_q = "INSERT INTO item_s_goods(" \
             "id,img,name,description," \
             "min_price,rating,store_id,category) VALUES"
    loc_q = "INSERT INTO item_s_goodlocation(" \
            "good_id," \
            "location_id," \
            "type," \
            "price," \
            "amount) VALUES "
    com_q = "INSERT INTO item_s_comments(" \
            "purchase," \
            "raiting," \
            "nick_name," \
            "city," \
            "data," \
            "comment_text," \
            "good_id) VALUES"

    query = ""
    if q_type == "shop":
        query = shop_q
    if q_type == "good":
        query = good_q
    if q_type == "locs":
        query = loc_q
    if q_type == "coms":
        query = com_q
    values = [str(tuple(map(lambda x: str(x).replace("'",'"'), i))) for i in values]

    query += ",".join(values) + ";"
    query = query.replace("None", "null")
    query = query.replace("True", "true")
    query = query.replace("False", "false")
    query = query.replace("\\n", "<br>")
    query = query.replace(":", ': ')
    query = query.replace(":  ", ': ')

    return text(query + "\n")


def parce_good(good: dict, shop_id, path):
    g_values = (good["product_id"],
                f'goods_img\product_icon_{good["product_id"]}.png',
                good['name'],
                good["description"],
                good["price"],
                good['rate'],
                shop_id,
                good['category'])

    shutil.copyfile(path + f'\\shop_info_{shop_id}\\product_icon_{good["product_id"]}.png',
                    os.getcwd() + f'\\media\\goods_img\\product_icon_{good["product_id"]}.png')
    locs = []
    for loc in good["locations"]:
        citys_objs = list(connection.execute(text("SELECT * FROM item_s_city;")).all())
        citys = [i[1] for i in citys_objs]
        city, *loc_name = loc["city"].split("\n")[0].split(": ")
        loc_name=": ".join(loc_name)

        if city not in citys:
            connection.execute(text(f"INSERT INTO item_s_city(city) VALUES ('{city}')"))
            citys_objs += list(connection.execute(text(f"SELECT * FROM item_s_city WHERE city='{city}';")).all())
        db_city = [i for i in citys_objs if i[1] == city][0]

        loc_objs = connection.execute(text(f"SELECT * FROM item_s_location WHERE city_id={db_city[0]};")).all()
        locs_names = [i[1] for i in loc_objs]
        if loc_name not in locs_names:
            connection.execute(
                text(f"INSERT INTO item_s_location(name, city_id) VALUES ('{loc_name}', '{db_city[0]}')"))
            loc_objs += list(connection.execute(
                text(f"SELECT * FROM item_s_location WHERE name='{loc_name}' AND city_id={db_city[0]};")).all())
        db_loc = [i for i in loc_objs if i[1] == loc_name and i[2] == db_city[0]][0]
        locs.append((good["product_id"], db_loc[0], loc["loc_type"],loc["price"].split(" ")[0], loc["weight"]))

    coms = []
    for com in good["comments"]:
        if com["nick"] == "Ответ представителя":
            continue
        coms.append((
            com["buys"].split(" ")[-1],
            com["rate"].split(" ")[-1].split("%")[0],
            com["nick"],
            com["product_name"],
            com["date"],
            com["text"],
            good["product_id"]
        ))

    return g_values, locs, coms


def parse_page(page):
    path = os.getcwd() + f"\\data\\page_data_{page}"
    with open(f"data\\page_data_{page}\\info_page_{page}.json", "r") as f:
        data = json.loads(f.read())

    shops_refactored = []
    goods_refactored = []
    coms_refactored = []
    locs_refactored = []
    print(page, len(data))
    for shop in data:
        values = (shop["id"],
                  f'topstores_img\\icon_image_{shop["id"]}.png',
                  shop["name"],
                  shop["rate"],
                  shop["sell_count"],
                  shop["deposit"],
                  shop["description"],
                  shop["work"],
                  shop["rules"],
                  shop["promotions"],
                  shop["forum"],
                  shop["category"],
                  f'topstores_img\\head_image_{shop["id"]}.png',
                  shop["is_crown"])
        shops_refactored.append(values)
        shutil.copyfile(path + f'\\shop_info_{shop["id"]}\\head_image_{shop["id"]}.png',
                        os.getcwd() + f'\\media\\topstores_img\\head_image_{shop["id"]}.png')
        shutil.copyfile(path + f'\\shop_info_{shop["id"]}\\icon_image_{shop["id"]}.png',
                        os.getcwd() + f'\\media\\topstores_img\\icon_image_{shop["id"]}.png')
        for good in shop["products"]:
            try:
                good_str, locs, coms = parce_good(good, shop["id"], path)
                locs_refactored += locs
                coms_refactored += coms
                goods_refactored.append(good_str)
            except Exception as e:
                pprint(good)
                raise e
    try:
        if shops_refactored:
            connection.execute(get_q_from_data(shops_refactored, "shop"))
    except Exception as e:
        if "UNIQUE" not in str(e):
            raise e
    try:
        if goods_refactored:
            connection.execute(get_q_from_data(goods_refactored, "good"))
    except Exception as e:
        if "UNIQUE" not in str(e):
            raise e
    try:
        if coms_refactored:
            connection.execute(get_q_from_data(coms_refactored, "coms"))
    except Exception as e:
        if "UNIQUE" not in str(e):
            raise e
    try:
        if locs_refactored:
            connection.execute(get_q_from_data(locs_refactored, "locs"))
    except Exception as e:
        if "UNIQUE" not in str(e):
            raise e


def main():
    pages = [f.split("_")[-1] for f in os.listdir("data")]
    for page in pages:
        parse_page(page)
    connection.commit()

main()