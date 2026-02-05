from repartidor.core import TripManager, Trip

# Simulación no gráfica para verificar TripManager y la lógica
manager = TripManager()

# 1) Viaje a cliente Elche, producto pagado en efectivo
manager.add_trip(Trip(tipo='Cliente', cliente='Juan Pérez', precio=50.0, precio_producto=120.0, forma_pago='Efectivo', zona='Elche'))

# 2) Viaje compra en tienda Otros con precio personalizado
manager.add_trip(Trip(tipo='Compra', cliente='Compra: suministros', precio=40.0, precio_producto=0.0, forma_pago='Transferencia', tienda='Otros'))

# 3) Viajes internos: 3 internos -> 3 * 30 = 90
manager.add_trip(Trip(tipo='Interno', cliente='Internos', precio=3*30.0, cantidad=3))

# 4) Viaje a cliente en Centro con pago por transferencia
manager.add_trip(Trip(tipo='Cliente', cliente='María López', precio=40.0, precio_producto=0.0, forma_pago='Transferencia', zona='Centro'))

print('--- Resumen generado (simulado) ---')
print(manager.generate_summary())
print('Total ingresos:', manager.total_income())
print('Total productos en efectivo:', manager.total_producto_efectivo())
