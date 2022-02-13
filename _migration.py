import asyncio
import os

import aiogram.utils.exceptions as exc
import psycopg2
from aiogram.bot.bot import Bot

##############
# КОНФИГ:
API_TOKEN = os.getenv('BOT_TOKEN')
if not API_TOKEN:
    print('токена нет')
    exit(-1)

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    print('урла бд нет')
    exit(-1)
##############

##############
# БД
try:
    db = psycopg2.connect(DATABASE_URL, sslmode='require')
except Exception:
    db = None
    print('урла бд нет')
    exit(-1)

cursor = db.cursor()


def pre_process():
    full_names = dict()
    users_id = []

    # тащим все айдишники из бд:
    cursor.execute("SELECT id from users")
    for i in cursor.fetchall():
        users_id.append(i[0])

    # создаем БД:
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id BIGINT PRIMARY KEY, username TEXT, first_name TEXT, "
                   "last_name TEXT, full_name TEXT, join_date TIMESTAMP, messages INTEGER)")

    cursor.execute("CREATE TABLE IF NOT EXISTS messages(id BIGINT PRIMARY KEY, songs_ INTEGER, contacts_ INTEGER, "
                   "howto_ INTEGER, team_ INTEGER, memes_ INTEGER, credits_ INTEGER, help_ INTEGER, start_ INTEGER,"
                   "stop_ INTEGER, santa_ INTEGER, end_ INTEGER)")
    db.commit()

    ##############

    async def get_tg_names():
        b = Bot(token=API_TOKEN)
        for j in users_id:
            try:
                p = await b.get_chat_member(chat_id=-1001761177569, user_id=j)
            except exc.BadRequest:
                print('fail', j)
                continue
            full_names[p.user.id] = tuple(p.user.full_name.split())
        return

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_tg_names())
    loop.close()

    print(users_id)
    print(full_names)


FULL_NAMES = {1306294714: ('~твоя', 'мерзость.'), 912515292: ('Арсений',), 1202704228: ('Екатерина', 'Гребёнкина'),
              626301983: ('Александра',), 418107034: ('Кирилл', 'Кругликов'), 1242612463: ('kerauverk',),
              1827430974: ('nikki', 'vskrto'), 763718623: ("G'ayrat",), 1028047493: ('Маруся', 'Дощечкина'),
              984835432: ('🤍thevalery🤍',), 750857380: ('Sasha',), 859499774: ('barkosser',), 949449595: ('🐿️',),
              915293518: ('Arisha', 'Kopylova'), 604181224: ('Матвей', 'Янголенко'),
              1839290151: ('Allergic', 'to', 'People'), 1038986109: ('Анна', 'Ланских'),
              830920118: ('Aleksandr', 'Lopatko'), 684785002: ('Lena', 'D'), 1814854497: ('Алина☃️',),
              1339387850: ('Софья', 'Пошукайло'), 1298918427: ('Катя', 'Боева'), 808864993: ('Ксения', 'Клюева'),
              421770409: ('Аполлинария',), 1371458078: ('Ира',), 1167059277: ('Evgeha',), 476337160: ('Роман', 'Комов'),
              925184312: ('Rish',), 713815827: ('гриша', 'алфёров'), 1276954403: ('Никошка',),
              966452026: ('ullccceey',), 1180071373: ('irasubbotina_',), 886155515: ('Karina',),
              1044869530: ('Максим',), 1120695506: ('Дима',), 824548117: ('Даша',), 744431052: ('Анчоус', '🥸'),
              1636551595: ('Lolita',), 1535110493: ('Зубкова', 'Полина'), 800957236: ('Яна', 'Лукина'),
              1652732836: ('Рената',), 1554349219: ('Huge', 'Cat'), 1866809913: ('ксюша', 'хлопова'),
              735035167: ('Polina', 'Nosevich'), 895841296: ('Voytenko',), 941543842: ('Pyankova', 'Polina'),
              1511045033: ('слава🤙',), 992489503: ('Kristina', '•••'), 1503877841: ('Алиса',), 746600084: ('Matias',),
              1319044289: ('Юля', 'Арбузова'), 827835673: ('Диана', 'Полянская'), 1903810166: ('gay',),
              811742362: ('Карина',), 972919938: ('Валерия', 'Гукова'), 524027591: ('Antonina',),
              1007940091: ('Александра', 'Кузьменко', '🤍'), 670243686: ('🕊',), 1353175923: ('Анастасия', 'Сеничкина'),
              888661591: ('Katrine',), 2128827002: ('Кристина', 'makhoyni'), 970537793: ('Alina',),
              408444942: ('Peter', 'Lagutin'), 858518428: ('☄', 'Asmodeus', '🔱'), 911640801: ('Anna', 'Klimenteva'),
              750119071: ('Anastasia', 'Millagher'), 1112547975: ('Даниил', 'Бердышев'),
              1299812194: ('Катя', 'Сидорова'), 1329049699: ('valerolll',), 293182379: ('Svetlana',),
              1740178046: ('Екатерина', 'Боева'), 625991372: ('Денис', 'Бирюков'), 1399973118: ('Rrincess', 'Bich'),
              1424975200: ('Биз',), 597583721: ('Phoenix’s',), 324242509: ('Арсений', 'Бирюков'),
              575120780: ('ковальская-дефолтова',), 608316796: ('s', 'o', 's'), 1832602820: ('анна', 'семыкина'),
              1711263832: ('ᯓ', '𝑫𝑪', '|', '7𝗢𝗗𝗔✹', '⃝⃙🇲🇽'), 920248300: ('марияр',), 1037353382: ('даша', 'про'),
              499606837: ('Ylik', 'Zver🖇'), 175044465: ('Ioann', 'Chas'), 385056286: ('Dan', 'Sazonov'),
              407274643: ('Usman', 'Mughal'), 424185494: ('Vladislav', 'Kozub'), 1125531055: ('Михаил', 'Лобынцев'),
              1070984836: ('Darya', 'Sergeevna'), 843464775: ('𝒦ℴ𝓉', 'ℳ𝒶𝓉𝓇ℴ𝓈𝓀𝒾𝓃😡ツ✘'),
              1854799789: ('NVSPC', 'ADMIN'), 913289451: ('Baxora',), 500861553: ('M.M.M',),
              422419401: ('Stepan', 'Ikonnikov'), 439481645: ('.',), 622051454: ('Аленка', 'Токсик'),
              726058532: ('leramalyy',), 1399417506: ('Кира',)}
IDS = [1306294714, 912515292, 24, 1202704228, 626301983, 418107034, 1242612463, 1827430974, 763718623, 1028047493,
       984835432, 750857380, 859499774, 949449595, 915293518, 604181224, 1839290151, 1038986109, 830920118, 684785002,
       1814854497, 1339387850, 1298918427, 808864993, 421770409, 1371458078, 1167059277, 476337160, 925184312,
       713815827, 1276954403, 966452026, 1180071373, 886155515, 1044869530, 1120695506, 824548117, 744431052,
       1636551595, 1535110493, 800957236, 1652732836, 1554349219, 1866809913, 735035167, 895841296, 941543842,
       1511045033, 992489503, 1503877841, 746600084, 1319044289, 827835673, 1903810166, 811742362, 972919938, 524027591,
       1007940091, 670243686, 1353175923, 888661591, 2128827002, 970537793, 408444942, 858518428, 911640801, 750119071,
       1112547975, 1299812194, 1329049699, 293182379, 1740178046, 625991372, 1399973118, 1424975200, 597583721,
       324242509, 575120780, 608316796, 1832602820, 1711263832, 920248300, 1037353382, 499606837, 175044465, 385056286,
       407274643, 424185494, 1125531055, 1070984836, 843464775, 1854799789, 913289451, 500861553, 422419401, 439481645,
       622051454, 726058532, 1399417506]


def process():
    # # создаем бд
    # cursor.execute("CREATE TABLE IF NOT EXISTS users(id BIGINT PRIMARY KEY, username TEXT, first_name TEXT, "
    #                "last_name TEXT, full_name TEXT, join_date TIMESTAMP, messages INTEGER)")
    #
    # cursor.execute("CREATE TABLE IF NOT EXISTS messages(id BIGINT PRIMARY KEY, songs_ INTEGER, contacts_ INTEGER, "
    #                "howto_ INTEGER, team_ INTEGER, memes_ INTEGER, credits_ INTEGER, help_ INTEGER, start_ INTEGER,"
    #                "stop_ INTEGER, santa_ INTEGER, end_ INTEGER)")
    # db.commit()

    users_write = []

    with open('messages_backup.csv') as f:
        for i in (f.readlines()[1:]):
            row = i.split(',')
            names = list(FULL_NAMES[int(row[0])]) if len(FULL_NAMES[int(row[0])]) == 2 else list(FULL_NAMES[int(row[0])]) + ['']
            row = row[0:2] + names + row[2:-1] + [row[-1].strip('\n')]
            print(row)

process()


