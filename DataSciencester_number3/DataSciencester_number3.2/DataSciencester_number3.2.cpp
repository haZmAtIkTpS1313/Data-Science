#include <tuple>
#include <iostream>
#include <map>
#include <unordered_map>
#include <string>
#include <utility>

// В C++ мы должны явно указать типы возвращаемых значений
std::tuple<int, int> sum_and_product(int x, int y) {
    return std::make_tuple(x + y, x * y);
}

int main() {
    // C++17: Распаковка работает точно так же элегантно, как в Python!
    auto [s, p] = sum_and_product(4, 5);
        
    std::cout << s << " " << p << "\n"; // Выведет 9 20
    
    std::tuple<int, int> my_tuple = {1, 2};
    std::get<0>(my_tuple) = 3; // АБСОЛЮТНО ЛЕГАЛЬНО! Теперь кортеж равен (3, 2)
    
    // Переименовано в my_tuple2, чтобы избежать ошибки переопределения (redefinition)
    std::tuple<int, double, std::string> my_tuple2 = {10, 3.14, "Hi"};

    auto val = std::get<1>(my_tuple2); // 3.14

    // int i = 1;
    // std::get<i>(my_tuple2); // ОШИБКА КОМПИЛЯЦИИ! Индекс не может быть переменной.

    // Для упорядоченного словаря (дерева) работает из коробки:
    std::map<std::tuple<int, int>, std::string> d;
    d[{1, 2}] = "Data"; 

    // А вот для хеш-таблицы (std::unordered_map) НЕ сработает из коробки!
    // В стандартной библиотеке C++ нет готового хешера для кортежей.
    
    // Чтобы это заработало, нужно написать свой хешер (вот так это делается в C++):
    struct TupleHash {
        template <class T1, class T2>
        std::size_t operator() (const std::tuple<T1, T2>& t) const {
            auto h1 = std::hash<T1>{}(std::get<0>(t));
            auto h2 = std::hash<T2>{}(std::get<1>(t));
            return h1 ^ (h2 << 1); // Простое комбинирование хешей
        }
    };
    
    // Теперь unordered_map скомпилируется и будет работать!
    std::unordered_map<std::tuple<int, int>, std::string, TupleHash> ud;
    ud[{1, 2}] = "Data";

    int a = 1, b = 2;
    std::swap(a, b); // Стандартный и самый быстрый способ
    
    return 0;
}