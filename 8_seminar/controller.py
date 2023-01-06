import view
import model
import logging


# Если мы хотим, чтобы логи записывались в файл
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

def main():
    select = view.show_menu()
    if select == 1:
        logging.info("Выбран просмотр списка сотрудников")
        sotr = model.get_list()
        view.show_employees(sotr)
        logging.info("Показан список сотрудников")
    elif select ==2:
        logging.info("Выбрано добавление сотрудника")
        data=view.add_employees()
        model.add_eployee_to_list(data)
        logging.info("Сотрудник добавлен")
    elif select == 3:
        logging.info("Выбрано изменить запись")
        change, string = view.change_employees()
        model.update_employees(change, string)
        logging.info("Изменения внесены")
    elif select == 4:
       logging.info("Выбрано удаление сотрудника")
       number = view.delete()
       model.delete(number)
       logging.info("Сотрудник удален")
    elif select == 5:
       logging.info("Выбран экспорт в txt")
       model.export_list_txt()
       logging.info("Список сотрудников экспортирован в корневой каталог программы")
    elif select == 6:
        logging.info("Выбран импорт из txt")
        model.import_list_txt()
        logging.info("Список сотрудников из txt импортирован")
    elif select == 7:
        logging.info("Выбран импорт из csv")
        model.import_list_csv()
        logging.info("Список сотрудников из csv импортирован")
    else:
        print("Произошла неизвестная ошибка")
    logging.info("Действия успешно выполнены!")