# SmartScaleForMarket
 
<h3>VERSION 1.0.1:</h3> <br>
    - Разделение на "Back" и "Front" <br>
    - Frontend - реализация архитектуры MVC <br>

<h3>VERSION 1.0.0:</h3> <br>
    - Для запуска приложения не требуется компилировать модель CNN,
    она запускается автоматически если не нашла её в каталоге. <br>
    - Добавлен ORM SQLAlchemy <br>
    - Данные из БД берутся согласно паттерну "Репозиторий" <br>

<h4>Описание каталогов:</h4><br>
backend: <br>
    /data_base - Каталог для хранения базы данныъ SQLite <br>
    /helpers - Помощники для вывода информации, взаимодействие с компьютером <br>
    /model - Модели базы данных <br>
    /modelDataCNN - Датасеты для обучения модели и обученая модель <br>
    /repository - Взаимодействие с БД <br>
    /service - Сервисы которые помогают создавать модели CNN, получение данных из репозитория <br>
    
frontend: <br>
    /view - Интерфейс пользователя <br>
    /controller - Контроллеры для взаимодейсвтия с UI и получения данных от модели  <br>
    /model - Получение данных от бека и возращение результата контроллеру 
requirements.txt - Зависимости проекта <br>