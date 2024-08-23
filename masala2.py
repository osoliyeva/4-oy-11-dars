class Telegram:
    def __init__(self,user_name):
        self.user_name=user_name
        self.send_chat_text=None
        self.accept_chat_text=None
        self.chat_status=None
        self.chat_time=None
    
    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_send_chat_text(self, text):
        self.send_chat_text = text

    def set_accept_chat_text(self, text):
        self.accept_chat_text = text

    def set_chat_status(self, status):
        self.chat_status = status

    def set_chat_time(self, time):
        self.chat_time = time

    def send(self, user):
        user.accept_chat_text = self.send_chat_text
        user.set_chat_status('sending')
        print(f"{self.user_name} foydalanuvchi {user.user_name} foydalanuvchiga habar jo'natdi")

    def read(self):
        print(f"{self.user_name} foydalanuvchi habarni o'qidi: {self.accept_chat_text}")
        self.set_chat_status('reading')

    def delete(self):
        self.accept_chat_text = None
        self.set_chat_status('deleting')
        print(f"{self.user_name} habar o'chirildi")



user1 = Telegram("Ali")
user2 = Telegram("Vali")

user1.set_send_chat_text("Salom, ishlar qalay?")
user1.send(user2)

user2.read()

user2.delete()