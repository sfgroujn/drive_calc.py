"""
Простая программа для расчета характеристик электропривода
"""

import math

def calculate_motor_parameters():
    """Основная функция расчета"""
    
    print("\n" + "="*50)
    print("РАСЧЕТ ЭЛЕКТРОПРИВОДА")
    print("="*50)
    
    # Ввод данных
    print("\n1. ВВЕДИТЕ ПАРАМЕТРЫ ДВИГАТЕЛЯ:")
    print("-" * 40)
    
    P = float(input("Мощность двигателя (кВт): "))
    n = float(input("Скорость вращения (об/мин): "))
    U = float(input("Напряжение (В): "))
    cos_f = float(input("Коэффициент мощности (cos φ): "))
    eff = float(input("КПД (0.85 = 85%): "))
    
    # Основные расчеты
    print("\n2. РАСЧЕТНЫЕ ХАРАКТЕРИСТИКИ:")
    print("-" * 40)
    
    # Угловая скорость (рад/с)
    omega = 2 * math.pi * n / 60
    
    # Момент (Н·м)
    M = (P * 1000) / omega
    
    # Ток (А) для трехфазного двигателя
    I = (P * 1000) / (1.73 * U * eff * cos_f)
    
    # Пусковой ток (обычно в 5-7 раз больше)
    I_start = I * 6
    
    # Пусковой момент (обычно в 1.5-2.5 раза больше)
    M_start = M * 2
    
    print(f"Угловая скорость: {omega:.1f} рад/с")
    print(f"Номинальный момент: {M:.1f} Н·м")
    print(f"Номинальный ток: {I:.1f} А")
    print(f"Пусковой ток: {I_start:.1f} А")
    print(f"Пусковой момент: {M_start:.1f} Н·м")
    
    # Вопрос про редуктор
    print("\n3. РАСЧЕТ С РЕДУКТОРОМ:")
    print("-" * 40)
    
    answer = input("Добавить редуктор? (да/нет): ")
    
    if answer.lower() == 'да':
        i = float(input("Передаточное число: "))
        eff_red = float(input("КПД редуктора (0.95 = 95%): "))
        
        # Выходные параметры после редуктора
        n_out = n / i
        M_out = M * i * eff_red
        P_out = P * eff * eff_red
        
        omega_out = 2 * math.pi * n_out / 60
        
        print(f"\nВыходная скорость: {n_out:.1f} об/мин")
        print(f"Выходной момент: {M_out:.1f} Н·м")
        print(f"Выходная мощность: {P_out:.2f} кВт")
    
    # Расчет энергопотребления
    print("\n4. ЭНЕРГОПОТРЕБЛЕНИЕ:")
    print("-" * 40)
    
    hours = float(input("Часов работы в день: "))
    days = float(input("Дней работы в году: "))
    cost = float(input("Стоимость 1 кВт·ч (руб): "))
    
    energy_day = P * hours
    energy_year = energy_day * days
    cost_year = energy_year * cost
    
    print(f"\nПотребление в день: {energy_day:.1f} кВт·ч")
    print(f"Потребление в год: {energy_year:.1f} кВт·ч")
    print(f"Затраты на электроэнергию: {cost_year:.2f} руб/год")
    
    # Дополнительные расчеты
    print("\n5. ДОПОЛНИТЕЛЬНЫЕ РАСЧЕТЫ:")
    print("-" * 40)
    
    # Расчет времени разгона
    J = float(input("Момент инерции механизма (кг·м²): "))
    
    # Время разгона t = J * ω / (M_start - M_load)
    M_load = M * 0.8  # нагрузка 80% от номинала
    t_acc = J * omega / (M_start - M_load)
    
    print(f"Время разгона: {abs(t_acc):.2f} с")
    
    # Завершение
    print("\n" + "="*50)
    print("РАСЧЕТ ЗАВЕРШЕН")
    print("="*50)

def example_calculation():
    """Пример готового расчета"""
    
    print("\n" + "="*50)
    print("ПРИМЕР РАСЧЕТА (двигатель 5.5 кВт)")
    print("="*50)
    
    # Параметры двигателя
    P = 5.5  # кВт
    n = 1450  # об/мин
    U = 380  # В
    cos_f = 0.85
    eff = 0.85
    
    print(f"\nИсходные данные:")
    print(f"  Мощность: {P} кВт")
    print(f"  Скорость: {n} об/мин")
    print(f"  Напряжение: {U} В")
    print(f"  cos φ: {cos_f}")
    print(f"  КПД: {eff*100}%")
    
    # Расчеты
    omega = 2 * math.pi * n / 60
    M = (P * 1000) / omega
    I = (P * 1000) / (1.73 * U * eff * cos_f)
    
    print(f"\nРезультаты:")
    print(f"  Угловая скорость: {omega:.1f} рад/с")
    print(f"  Момент: {M:.1f} Н·м")
    print(f"  Ток: {I:.1f} А")
    
    # С редуктором
    i = 10
    eff_red = 0.95
    
    n_out = n / i
    M_out = M * i * eff_red
    
    print(f"\nС редуктором (i={i}, КПД={eff_red*100}%):")
    print(f"  Выходная скорость: {n_out:.1f} об/мин")
    print(f"  Выходной момент: {M_out:.1f} Н·м")

def main():
    """Главное меню программы"""
    
    while True:
        print("\n" + "█"*50)
        print("ПРОГРАММА РАСЧЕТА ЭЛЕКТРОПРИВОДА")
        print("█"*50)
        print("\nВыберите режим:")
        print("1 - Ввести свои данные")
        print("2 - Посмотреть пример")
        print("3 - Выйти")
        
        choice = input("\nВаш выбор (1-3): ")
        
        if choice == '1':
            calculate_motor_parameters()
        elif choice == '2':
            example_calculation()
        elif choice == '3':
            print("\nДо свидания!")
            break
        else:
            print("\nНеверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()