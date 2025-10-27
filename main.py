import math
import matplotlib.pyplot as plt

# NIM = 24/544062/SV/25318
servo1 = 40
servo2 = 30
femur = 62
tibia = 18

servo1_rad = math.radians(servo1)
servo2_rad = math.radians(servo2)

x = femur * math.cos(servo1_rad) + tibia * math.cos(servo1_rad + servo2_rad)
y = femur * math.sin(servo1_rad) + tibia * math.sin(servo1_rad + servo2_rad)
print(' x: ', int(x),'\n','y: ', int(y))

x0, y0 = 0, 0
x1 = femur * math.cos(servo1_rad)
y1 = femur * math.sin(servo1_rad)
x2 = x
y2 = y

plt.plot([x0, x1], [y0, y1], 'b-', linewidth=6, label=f'Femur ({femur} cm)')
plt.plot([x1, x2], [y1, y2], 'r-', linewidth=6, label=f'Tibia ({tibia} cm)')
plt.plot(x0, y0, 'ko', markersize=12)
plt.plot(x1, y1, 'go', markersize=10)
plt.plot(x2, y2, 'mo', markersize=12)
plt.text(x2+2, y2+2, f'({x:.1f}, {y:.1f})', fontsize=12, fontweight='bold')
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

cos_theta2 = (x**2 + y**2 - femur**2 - tibia**2) / (2 * femur * tibia)
cos_theta2 = max(-1, min(1, cos_theta2))
theta2_ik = math.acos(cos_theta2)
k1 = femur + tibia * math.cos(theta2_ik)
k2 = tibia * math.sin(theta2_ik)
theta1_ik = math.atan2(y, x) - math.atan2(k2, k1)
print('theta1:', int(math.degrees(theta1_ik)), '°')
print('theta2:', int(math.degrees(theta2_ik)), '°')