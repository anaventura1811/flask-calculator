from abc import ABC, abstractmethod


# Conceito de interface
'''
    Interface
    é uma estrutura de dados

    Python não tem uma espécie definida de interface

    Sobre uso de ABC e do decorator abstractmethod:
    Classe que recebe ABC como herança não pode ser instanciada como objeto,
    mas pode ser herança de outras classes

'''


# Classe de interface
# Define a regra de construção das demais classes nas quais ela é implementada
class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, msg: str) -> None: pass


class EmailNotificationSender(NotificationSender):
    def send_notification(self, msg: str) -> None:
        print(f"Email message: {msg}")


class SMSNotificationSender(NotificationSender):
    def send_notification(self, msg: str) -> None:
        print(f"SMS message: {msg}")


obj = SMSNotificationSender()
obj.send_notification(msg='Olá')


class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message: str):
        self.__notification_sender.send_notification(message)


# Conceito de injeção de dependências

obj_not = Notificator(EmailNotificationSender())
obj_not.send('OLÁ MUNDO')
