"""
Тексты всех сообщений
Файл могут редактировать неайтишники, все должно быть антивандально. Все функции по обработке пихаем в `handlers.py`
"""
import config


class Messages:
    """
    Тексты сообщений, отправляемые ботом
    """

    def __init__(self):
        # не лезь, оно сожрет тебя
        self.foo = 'bar'
        self.admin_id = config.ADMIN_CHAT
        self.start_polling = '🔔 Бот запущен'
        self.stop_polling = '🔔 Бот остановлен'

    class Songs:
        def __init__(self):
            self.mes_text = 'fuck'
            self.web_text = 'bitch'
            self.web_link = 'bitch'
            self.app_text = 'bitch'
            self.app_link = 'bitch'

    class Contacts:
        def __init__(self):
            self.mes_text = 'fuck'
            self.vk_text = 'bitch'
            self.vk_link = 'bitch'
            self.inst_text = 'bitch'
            self.inst_link = 'bitch'
            self.web_text = 'bitch'
            self.web_link = 'bitch'
            self.tt_text = 'bitch'
            self.tt_link = 'bitch'
            self.yt_text = 'bitch'
            self.yt_link = 'bitch'
            self.tg_text = 'bitch'
            self.tg_link = 'bitch'

    class HowTo:
        def __init__(self):
            self.mes_text = '''При составлении списка участников смены приоритет имеют дети, которые стали призерами или победителями:
✅ Всероссийской олимпиады школьников на региональном или всероссийском уровне;
✅ олимпиад, утверждённых перечнем Министерства просвещения Российской Федерации;
✅ других олимпиад и конкурсов регионального и всероссийского уровней.

В этом случае наша команда, скорее всего, самостоятельно пригласит вас в "Магистр" или свяжется через отдел молодёжной политики в вашем городе или районе. Чаще всего их зачисление производится на бюджетной основе.

Вы также можете купить путёвку в наш центр. Для этого свяжитесь с председателем КС КРОМО "Магистр" Лопатко Александром Игоревичем через соцсети "Магистра" или:
📱 по телефону +79102706680
📨 по электронной почте kromo-magistr@mail.ru
💡 лично по адресу 305000, г. Курск, ул. Радищева, 33, оф. 335
💡 по почте 305000, г. Курск, ул. Радищева, 33, каб. 36'''
