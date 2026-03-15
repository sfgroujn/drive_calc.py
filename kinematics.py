import math

class Manipulator2D:
    """Двухзвенный манипулятор"""
    
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    
    def forward(self, theta1_deg, theta2_deg):
        t1 = math.radians(theta1_deg)
        t2 = math.radians(theta2_deg)
        x = self.l1 * math.cos(t1) + self.l2 * math.cos(t1 + t2)
        y = self.l1 * math.sin(t1) + self.l2 * math.sin(t1 + t2)
        return (x, y)
    
    def inverse(self, x, y, elbow_up=True):
        r = math.sqrt(x**2 + y**2)
        if r > self.l1 + self.l2 or r < abs(self.l1 - self.l2):
            return None
        
        cos_theta2 = (r**2 - self.l1**2 - self.l2**2) / (2 * self.l1 * self.l2)
        cos_theta2 = max(-1, min(1, cos_theta2))
        theta2_rad = math.acos(cos_theta2)
        
        if not elbow_up:
            theta2_rad = -theta2_rad
        
        phi = math.atan2(y, x)
        psi = math.atan2(self.l2 * math.sin(theta2_rad), 
                        self.l1 + self.l2 * math.cos(theta2_rad))
        theta1_rad = phi - psi
        
        return (math.degrees(theta1_rad), math.degrees(theta2_rad))


# === Пример ===
robot = Manipulator2D(l1=4, l2=3)

print("="*50)
print("ПРЯМАЯ ЗАДАЧА")
print("="*50)
x, y = robot.forward(30, 45)
print(f"Углы: плечо=30°, локоть=45°")
print(f"Координаты схвата: ({x:.2f}, {y:.2f})")

print("\n" + "="*50)
print("ОБРАТНАЯ ЗАДАЧА")
print("="*50)
angles = robot.inverse(x, y)
print(f"Координаты: ({x:.2f}, {y:.2f})")
print(f"Найденные углы: плечо={angles[0]:.1f}°, локоть={angles[1]:.1f}°")

# Проверка
x_check, y_check = robot.forward(angles[0], angles[1])
print(f"\nПроверка: ({x_check:.2f}, {y_check:.2f})")
print(f"Ошибка: {math.sqrt((x_check-x)**2 + (y_check-y)**2):.6f}")