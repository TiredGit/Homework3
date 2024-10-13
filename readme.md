1. Выполним запросы для получения всех записей и создадим новые объекты:
<br>Добавим категорию
![img.png](img.png)
<br>Добавим товары
![img_1.png](img_1.png)
![img_3.png](img_3.png)
<br>Добавим заказ
![img_2.png](img_2.png)
<br> Свяжем товар с заказом
![img_4.png](img_4.png)
2. Используем методы filter(), exclude(), order_by():
![img_6.png](img_6.png)
![img_7.png](img_7.png)
![img_8.png](img_8.png)
3. Выполним различные запросы используя в условиях связь
<br>Запрос всех заказов, сделанных определенным пользователем
![img_9.png](img_9.png)
<br>Запрос всех продуктов, которые относятся к определенному заказу
![img_10.png](img_10.png)
<br>Запрос всех заказов, у которых доставка в определённый город
![img_11.png](img_11.png)
<br>values()
![img_12.png](img_12.png)
![img_13.png](img_13.png)
![img_14.png](img_14.png)
<br>values_list()
![img_15.png](img_15.png)
![img_16.png](img_16.png)
![img_17.png](img_17.png)
4. Используем Q объекты для сложных условий:
![img_18.png](img_18.png)
![img_21.png](img_21.png)
![img_22.png](img_22.png)
![img_23.png](img_23.png)
<br>Объединим условия так, чтобы одно из условий исключало записи, а другое — фильтровало их
![img_19.png](img_19.png)
![img_20.png](img_20.png)
5. Используем методы annotate() и aggregate():
<br>annotate()
![img_24.png](img_24.png)
![img_25.png](img_25.png)
![img_26.png](img_26.png)
<br>aggregate()
![img_27.png](img_27.png)
![img_28.png](img_28.png)
![img_29.png](img_29.png)