from dataclasses import dataclass, asdict
from typing import List, Dict, Any
from datetime import datetime


@dataclass
class Trip:
    tipo: str
    cliente: str
    precio: float
    precio_producto: float = 0.0
    forma_pago: str = ""
    zona: str = ""
    tienda: str = ""
    cantidad: int = 1
    fecha: str = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        if not d.get("fecha"):
            d["fecha"] = datetime.now().isoformat()
        return d


class TripManager:
    """Clase encargada de almacenar y operar sobre los viajes."""
    def __init__(self):
        self._viajes: List[Trip] = []

    def add_trip(self, trip: Trip):
        self._viajes.append(trip)

    def remove_trip(self, index: int):
        if 0 <= index < len(self._viajes):
            del self._viajes[index]

    def clear(self):
        self._viajes = []

    def get_all(self) -> List[Trip]:
        return list(self._viajes)

    def total_income(self) -> float:
        return sum(t.precio for t in self._viajes)

    def total_producto_efectivo(self) -> float:
        return sum(t.precio_producto for t in self._viajes if t.forma_pago == "Efectivo")

    def generate_summary(self) -> str:
        resumen = "=" * 80 + "\n"
        resumen += "RESUMEN DE VIAJES - REPARTIDOR\n"
        resumen += f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        resumen += "=" * 80 + "\n\n"

        viajes_cliente = [v for v in self._viajes if v.tipo == "Cliente"]
        viajes_compra = [v for v in self._viajes if v.tipo == "Compra"]
        viajes_interno = [v for v in self._viajes if v.tipo == "Interno"]

        resumen += "VIAJES A CLIENTES:\n"
        resumen += "-" * 80 + "\n"
        total_cliente = 0
        for v in viajes_cliente:
            resumen += f"  Zona: {v.zona:15} | Cliente: {v.cliente:20} | Prod: ${v.precio_producto:7.2f} | Pago: {v.forma_pago:12} | Viaje: ${v.precio:6.2f}\n"
            total_cliente += v.precio
        resumen += f"Subtotal: ${total_cliente:.2f}\n\n"

        resumen += "VIAJES A COMPRAS:\n"
        resumen += "-" * 80 + "\n"
        total_compra = 0
        for v in viajes_compra:
            resumen += f"  Tienda: {v.tienda:15} | Detalles: {v.cliente:20} | Prod: ${v.precio_producto:7.2f} | Pago: {v.forma_pago:12} | Viaje: ${v.precio:6.2f}\n"
            total_compra += v.precio
        resumen += f"Subtotal: ${total_compra:.2f}\n\n"

        resumen += "VIAJES INTERNOS:\n"
        resumen += "-" * 80 + "\n"
        total_interno = 0
        for v in viajes_interno:
            resumen += f"  {v.cliente:40} | Cantidad: {v.cantidad:2} | Precio Total: ${v.precio:6.2f}\n"
            total_interno += v.precio
        resumen += f"Subtotal: ${total_interno:.2f}\n\n"

        total_general = total_cliente + total_compra + total_interno
        resumen += "=" * 80 + "\n"
        resumen += f"TOTAL INGRESOS: ${total_general:.2f}\n"
        resumen += f"Total de viajes: {len(self._viajes)}\n"
        resumen += "=" * 80 + "\n"
        return resumen
