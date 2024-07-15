# Sprint_4 of qa_python

> ### 1. test_default_books_genre_is_empty_dictionary
> Проверяет стандартное значение атрибута {books_genre}

> ### 2. test_default_favorites_is_empty_list
>Проверяет стандартное значение атрибута {favorites}

> ### 3. test_default_genre_true
>Проверяет стандартное значение атрибута {genre}

> ### 4. test_default_genre_age_rating_true
> Проверяет стандартное значение атрибута {genre_age_rating}

> ### 5. test_add_new_book_add_one_book_with_name_in_1_and_2_and_13_and_39_and_40symbols_to_empty_collector_added_one_book_without_genre
> Проверяет добавление одной книги в **_пустой_** коллектор с кол-вом символов в названии:  
> * 1 символ 
> * 2 символа
> * 13 символов
> * 39 символов
> * 40 символов

> ### 6. test_add_new_book_add_one_book_with_name_in_1_and_2_and_13_and_39_and_40symbols_to_non_empty_collector_added_one_book_without_genre
> Проверяет добавление одной книги в ***непустой*** коллектор с кол-вом символов в названии:
> * 1 символ 
> * 2 символа
> * 13 символов
> * 39 символов
> * 40 символов

> ### 7. test_add_new_book_add_2_and_5books_to_empty_collector_added_books
> Проверяет добавление в _**пустой**_ коллектор:
> * 2 книг
> * 5 книг

> ### 8. test_add_new_book_add_2_and_5books_to_non_empty_collector_added_books
> Проверяет добавление в _**пустой**_ коллектор:
> * 2 книг
> * 5 книг

> ### 9. test_add_new_book_add_the_one_book_twice_to_empty_collector_added_one_book
> Проверяет добавление одной книги дважды

> ### 10. test_add_new_book_add_one_book_with_name_in_0_and_41_and_42_and_60_symbols_to_empty_collector_no_added_book
> Проверяет добавление одной книги в **_пустой_** коллектор с кол-вом символов в названии:  
> * 0 символов 
> * 41 символ
> * 42 символа
> * 60 символов

> ### 11. test_add_new_book_add_one_book_with_name_in_0_and_41_and_42symbols_to_non_empty_collector_no_added_book
> Проверяет добавление одной книги в **_непустой_** коллектор с кол-вом символов в названии:  
> * 0 символов 
> * 41 символ
> * 42 символа
> * 60 символов

> ### 12. test_set_book_genre_set_genre_of_1_to_5books_to_no_genre_books_added_genre_to_books
> Проверяет установку жанра от 1 до 5 книг книгам без жанра

> ### 13. test_set_book_genre_set_genre_of_1_to_5books_to_books_with_genres_added_genre_to_books
> Проверяет установку жанра от 1 до 5 книг книгам с жанром
 
> ### 14. test_set_book_genre_set_genre_of_not_added_book_not_added_book_and_not_set_genre
> Проверяет установку жанра книге, которой нет в коллекторе 

> ### 15. test_set_book_genre_set_not_added_genre_not_set_genre
> Проверяет установку жанра, которого нет в коллекторе

> ### 16. test_set_book_genre_set_not_added_genre_of_not_added_book_not_added_book_and_not_set_genre
> Проверяет установку отсутствующего в коллекторе жанра книге, которой нет в коллекторе 

> ### 17. test_get_book_genre_get_genre_of_1_to_5books_got_genres
> Проверяет получение жанра от 1 до 5 книг 

> ### 18. test_get_book_genre_get_genre_of_not_added_book_not_got_genre
> Проверяет получение жанра книги, которой нет в коллекторе

> ### 19. test_get_books_with_specific_genre_get_books_with_specific_genre_got_books_with_specific_genre
> Проверяет получение книг, с определенным жанром

> ### 20. test_get_books_with_specific_genre_get_books_with_not_added_genre_no_got_books
> Проверяет получение книг, с жанром, которого нет в коллекторе

> ### 21. test_get_books_genre_get_book_genre_with_or_without_genre_got_book_genre
> Проверяет получение словаря с книгами и их жанрами

> ### 22. test_get_books_genre_get_empty_book_genre_got_empty_book_genre
> Проверяет получение _**пустого**_ словаря с книгами и их жанрами

> ### 23. test_get_books_for_children_get_books_with_or_without_genre_got_books
> Проверяет получение книг для детей

> ### 24. test_add_book_in_favorites_add_of_1_to_5_books_got_books
> Проверяет добавление от 1 до 5 книг в избранные

> ### 25. test_add_book_in_favorites_add_the_one_book_twice_added_one_book
> Проверяет добавление книги в избранные дважды

> ### 26. test_add_book_in_favorites_add_not_added_book_not_added_book
> Проверяет добавление в избранные книги, которой нет в коллекторе

> ### 27. test_delete_book_from_favorites_delete_of_1_to_5_books_deleted_books
> Проверяет удаление от 1 до 5 книг из избранных

> ### 28. test_delete_book_from_favorites_delete_deleted_book_favorites_not_changed
> Проверяет удаление уже удаленной книги из избранных
 
> ### 29. test_delete_book_from_favorites_delete_not_favorite_book_favorites_not_changed
> Проверяет удаление из избранных книги, которой нет в избранных

> ### 30. test_delete_book_from_favorites_delete_not_added_book_favorites_not_changed
> Проверяет удаление из избранных книги, которой нет в коллекторе

> ### 31. test_get_list_of_favorites_books_get_0_and_1_and_2_and_5books_got_books
> Проверяет получения списка избранных книг от 0 до 5 избранных книг
