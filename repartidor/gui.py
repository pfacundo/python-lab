import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from repartidor.core import TripManager, Trip


class RepartidorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Viajes - Repartidor")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")

        # manager para viajes
        self.manager = TripManager()

        # Precios por zona (clientes)
        self.precios_zonas = {
            "Elche": 50,
            "Centro": 40,
            "5ta": 50,
            "Playacar": 70,
            "Selvanova": 70,
            "Palmas": 80,
            "Otros": 0
        }

        # Tiendas de compra
        self.tiendas = ["Chedraui", "Aki", "Plasticos Reyes", "Cafe Express", "DAC", "Otros"]
        self.precio_compra = 40
        self.precio_interno = 30

        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz de usuario"""

        # Frame superior para entrada de datos
        frame_entrada = ttk.LabelFrame(self.root, text="Registrar Nuevo Viaje", padding=10)
        frame_entrada.pack(fill="x", padx=10, pady=10)

        # Tipo de viaje
        ttk.Label(frame_entrada, text="Tipo de Viaje:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.tipo_viaje_var = tk.StringVar(value="Cliente")
        tipo_combo = ttk.Combobox(frame_entrada, textvariable=self.tipo_viaje_var, 
                                   values=["Cliente", "Compra", "Interno"], state="readonly", width=20)
        tipo_combo.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        tipo_combo.bind("<<ComboboxSelected>>", self.actualizar_campos)

        # Frame para campos dinámicos
        self.frame_dinamico = ttk.Frame(frame_entrada)
        self.frame_dinamico.grid(row=1, column=0, columnspan=4, sticky="ew", pady=10)

        # Campo para cliente/detalles
        ttk.Label(frame_entrada, text="Cliente/Detalles:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.cliente_entry = ttk.Entry(frame_entrada, width=30)
        self.cliente_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # Precio del viaje (se actualiza automáticamente)
        ttk.Label(frame_entrada, text="Precio Viaje ($):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.precio_var = tk.StringVar(value="50")
        self.precio_entry = ttk.Entry(frame_entrada, textvariable=self.precio_var, width=10)
        self.precio_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        # Precio del producto
        ttk.Label(frame_entrada, text="Precio Producto ($):").grid(row=3, column=2, sticky="w", padx=5, pady=5)
        self.precio_producto_var = tk.StringVar(value="0")
        self.precio_producto_entry = ttk.Entry(frame_entrada, textvariable=self.precio_producto_var, width=10)
        self.precio_producto_entry.grid(row=3, column=3, sticky="w", padx=5, pady=5)

        # Forma de pago
        ttk.Label(frame_entrada, text="Forma de Pago:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.pago_var = tk.StringVar(value="Efectivo")
        pago_combo = ttk.Combobox(frame_entrada, textvariable=self.pago_var,
                                  values=["Efectivo", "Transferencia", "Descuento"], state="readonly", width=15)
        pago_combo.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

        # Botón para agregar viaje
        ttk.Button(frame_entrada, text="Agregar Viaje", command=self.agregar_viaje).grid(row=5, column=0, columnspan=4, pady=10)

        frame_entrada.columnconfigure(1, weight=1)

        # Frame para la tabla de viajes
        frame_tabla = ttk.LabelFrame(self.root, text="Viajes Registrados", padding=10)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Crear tabla con scrollbar
        tabla_scroll = ttk.Scrollbar(frame_tabla)
        tabla_scroll.pack(side="right", fill="y")

        self.tabla = ttk.Treeview(frame_tabla, columns=("Tipo", "Zona/Tienda", "Cliente", "Precio"), 
                                   height=15, yscrollcommand=tabla_scroll.set)
        tabla_scroll.config(command=self.tabla.yview)

        self.tabla.column("#0", width=50, anchor="center")
        self.tabla.column("Tipo", width=100, anchor="center")
        self.tabla.column("Zona/Tienda", width=150, anchor="center")
        self.tabla.column("Cliente", width=250, anchor="w")
        self.tabla.column("Precio", width=80, anchor="center")

        self.tabla.heading("#0", text="#")
        self.tabla.heading("Tipo", text="Tipo")
        self.tabla.heading("Zona/Tienda", text="Zona/Tienda")
        self.tabla.heading("Cliente", text="Cliente/Detalles")
        self.tabla.heading("Precio", text="Precio Viaje ($)")

        self.tabla.pack(fill="both", expand=True)

        # Frame inferior para totales y acciones
        self.frame_inferior = ttk.Frame(self.root)
        self.frame_inferior.pack(fill="x", padx=10, pady=10)

        # Total
        ttk.Label(self.frame_inferior, text="Total Ingresos:", font=("Arial", 12, "bold")).pack(side="left", padx=5)
        self.total_var = tk.StringVar(value="$0.00")
        ttk.Label(self.frame_inferior, textvariable=self.total_var, font=("Arial", 14, "bold"), 
                  foreground="green").pack(side="left", padx=5)

        # Separador
        ttk.Separator(self.frame_inferior, orient="vertical").pack(side="left", fill="y", padx=10)

        # Total de productos en efectivo
        ttk.Label(self.frame_inferior, text="Prod. Efectivo:", font=("Arial", 12, "bold")).pack(side="left", padx=5)
        self.total_producto_efectivo_var = tk.StringVar(value="$0.00")
        ttk.Label(self.frame_inferior, textvariable=self.total_producto_efectivo_var, font=("Arial", 14, "bold"), 
                  foreground="blue").pack(side="left", padx=5)

        # Botones de acciones
        ttk.Button(self.frame_inferior, text="Eliminar Seleccionado", command=self.eliminar_viaje).pack(side="right", padx=5)
        ttk.Button(self.frame_inferior, text="Limpiar Todo", command=self.limpiar_todo).pack(side="right", padx=5)
        ttk.Button(self.frame_inferior, text="Exportar Resumen", command=self.exportar_resumen).pack(side="right", padx=5)

        # Actualizar campos iniciales
        self.actualizar_campos()

    def actualizar_campos(self, event=None):
        """Actualiza los campos dinámicos según el tipo de viaje seleccionado"""
        
        # Limpiar frame dinámico
        for widget in self.frame_dinamico.winfo_children():
            widget.destroy()
        
        tipo = self.tipo_viaje_var.get()
        
        if tipo == "Cliente":
            ttk.Label(self.frame_dinamico, text="Zona:").pack(side="left", padx=5)
            self.zona_var = tk.StringVar(value="Elche")
            zona_combo = ttk.Combobox(self.frame_dinamico, textvariable=self.zona_var,
                                       values=list(self.precios_zonas.keys()), state="readonly", width=20)
            zona_combo.pack(side="left", padx=5)
            zona_combo.bind("<<ComboboxSelected>>", self.actualizar_precio)
            # Establecer precio según zona (no conservar valores previos)
            self.actualizar_precio()
        
        elif tipo == "Compra":
            ttk.Label(self.frame_dinamico, text="Tienda:").pack(side="left", padx=5)
            self.tienda_var = tk.StringVar(value="Chedraui")
            tienda_combo = ttk.Combobox(self.frame_dinamico, textvariable=self.tienda_var,
                                         values=self.tiendas, state="readonly", width=20)
            tienda_combo.pack(side="left", padx=5)
            # Precio fijo por defecto para compras; si se elige 'Otros' se permite editar
            self.precio_var.set(str(self.precio_compra))
            tienda_combo.bind("<<ComboboxSelected>>", self.actualizar_precio_compra)
            self.actualizar_precio_compra()
        
        elif tipo == "Interno":
            ttk.Label(self.frame_dinamico, text="Cantidad de Internos:").pack(side="left", padx=5)
            # usar IntVar para manejar cantidad
            self.cantidad_internos_var = tk.IntVar(value=1)
            cantidad_spin = ttk.Spinbox(self.frame_dinamico, from_=1, to=20, textvariable=self.cantidad_internos_var, width=10)
            cantidad_spin.pack(side="left", padx=5)
            # traza para actualizar el precio cuando cambie la cantidad
            try:
                self.cantidad_internos_var.trace_add('write', lambda *args: self.actualizar_precio_internos())
            except Exception:
                pass
            # establecer precio fijo por internos y bloquear edición
            self.actualizar_precio_internos()
            self.precio_entry.config(state="readonly")

    def actualizar_precio(self, event=None):
        """Actualiza el precio según la zona seleccionada"""
        zona = self.zona_var.get()
        precio = self.precios_zonas[zona]
        if zona == "Otros":
            # Permitir edición manual y reiniciar precio para que no conserve valores previos
            self.precio_entry.config(state="normal")
            self.precio_var.set("0")
        else:
            # Establecer precio de zona y bloquear edición
            self.precio_var.set(str(precio))
            self.precio_entry.config(state="readonly")

    def actualizar_precio_compra(self, event=None):
        """Ajusta el precio para viajes de compra según la tienda seleccionada"""
        tienda = self.tienda_var.get()
        if tienda == "Otros":
            # permitir edición manual y reiniciar para evitar conservar precio
            self.precio_entry.config(state="normal")
            self.precio_var.set("0")
        else:
            # precio fijo para compras
            self.precio_var.set(str(self.precio_compra))
            self.precio_entry.config(state="readonly")

    def actualizar_precio_internos(self, event=None):
        """Actualiza el precio según la cantidad de viajes internos"""
        try:
            cantidad = int(self.cantidad_internos_var.get())
            precio_total = cantidad * self.precio_interno
            # precio fijo por interno: 30 * cantidad
            self.precio_var.set(str(precio_total))
            self.precio_entry.config(state="readonly")
        except Exception:
            self.precio_var.set(str(self.precio_interno))
            self.precio_entry.config(state="readonly")

    def agregar_viaje(self):
        """Agrega un nuevo viaje a la lista"""
        tipo = self.tipo_viaje_var.get()
        cliente = self.cliente_entry.get().strip()
        
        try:
            precio_producto = float(self.precio_producto_var.get())
        except ValueError:
            messagebox.showerror("Error", "Precio inválido")
            return

        try:
            if tipo == "Interno":
                cantidad = int(self.cantidad_internos_var.get())
                precio = float(cantidad * self.precio_interno)
            else:
                precio = float(self.precio_var.get())
        except Exception:
            messagebox.showerror("Error", "Precio inválido")
            return
        
        forma_pago = self.pago_var.get()

        # Si la forma de pago es Efectivo, el precio del producto es obligatorio (>0)
        if forma_pago == "Efectivo":
            try:
                if float(precio_producto) <= 0:
                    messagebox.showwarning("Advertencia", "Para pagos en efectivo, ingresa el precio del producto")
                    return
            except Exception:
                messagebox.showwarning("Advertencia", "Para pagos en efectivo, ingresa el precio del producto válido")
                return

        if tipo == "Cliente":
            if not cliente:
                messagebox.showwarning("Advertencia", "Por favor ingresa el nombre del cliente")
                return
            zona = self.zona_var.get()
            if zona == "Otros" and precio == 0:
                messagebox.showwarning("Advertencia", "Debes especificar un precio para la zona 'Otros'")
                return
            viaje = {
                "tipo": tipo,
                "zona": zona,
                "cliente": cliente,
                "precio": precio,
                "precio_producto": precio_producto,
                "forma_pago": forma_pago
            }
            zona_tienda = zona
        
        elif tipo == "Compra":
            if not cliente:
                messagebox.showwarning("Advertencia", "Por favor ingresa detalles de la compra")
                return
            tienda = self.tienda_var.get()
            viaje = {
                "tipo": tipo,
                "tienda": tienda,
                "cliente": cliente,
                "precio": precio,
                "precio_producto": precio_producto,
                "forma_pago": forma_pago
            }
            zona_tienda = tienda
        
        elif tipo == "Interno":
            cantidad = int(self.cantidad_internos_var.get())
            viaje = {
                "tipo": tipo,
                "cantidad": cantidad,
                "cliente": cliente if cliente else f"Viajes Internos ({cantidad})",
                "precio": precio,
                "precio_producto": precio_producto,
                "forma_pago": forma_pago
            }
            zona_tienda = "-"

        # construir Trip y agregar via manager
        t = Trip(
            tipo=viaje.get("tipo",""),
            cliente=viaje.get("cliente",""),
            precio=viaje.get("precio",0.0),
            precio_producto=viaje.get("precio_producto",0.0),
            forma_pago=viaje.get("forma_pago",""),
            zona=viaje.get("zona",""),
            tienda=viaje.get("tienda",""),
            cantidad=viaje.get("cantidad",1)
        )
        self.manager.add_trip(t)

        # Actualizar tabla
        self.actualizar_tabla()

        # Limpiar campos
        self.cliente_entry.delete(0, tk.END)
        self.precio_producto_var.set("0")
        self.pago_var.set("Efectivo")

    def actualizar_tabla(self):
        """Actualiza la tabla de viajes"""
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        # Agregar viajes
        total = 0
        total_producto_efectivo = 0
        for i, viaje in enumerate(self.manager.get_all(), 1):
            tipo = viaje.tipo if hasattr(viaje, 'tipo') else viaje["tipo"]
            precio = viaje.precio if hasattr(viaje, 'precio') else viaje["precio"]
            cliente = viaje.cliente if hasattr(viaje, 'cliente') else viaje.get("cliente", "")
            precio_producto = viaje.precio_producto if hasattr(viaje, 'precio_producto') else viaje.get("precio_producto", 0)
            forma_pago = viaje.forma_pago if hasattr(viaje, 'forma_pago') else viaje.get("forma_pago", "")
            
            # Contar productos en efectivo
            if forma_pago == "Efectivo":
                total_producto_efectivo += precio_producto
            
            if tipo == "Cliente":
                zona = viaje.zona if hasattr(viaje, 'zona') else viaje.get("zona", "")
                cliente_info = f"{cliente} | Prod: ${precio_producto:.2f} | {forma_pago}"
                self.tabla.insert("", "end", text=str(i), 
                                 values=(tipo, zona, cliente_info, f"${precio:.2f}"))
            elif tipo == "Compra":
                tienda = viaje.tienda if hasattr(viaje, 'tienda') else viaje.get("tienda", "")
                cliente_info = f"{cliente} | Prod: ${precio_producto:.2f} | {forma_pago}"
                self.tabla.insert("", "end", text=str(i),
                                 values=(tipo, tienda, cliente_info, f"${precio:.2f}"))
            elif tipo == "Interno":
                cantidad = viaje.cantidad if hasattr(viaje, 'cantidad') else viaje.get("cantidad", 1)
                cliente_info = f"{cliente}"
                self.tabla.insert("", "end", text=str(i),
                                 values=(tipo, "-", cliente_info, f"${precio:.2f}"))
            
            total += precio
        
        # Actualizar totales usando manager
        self.total_var.set(f"${self.manager.total_income():.2f}")
        self.total_producto_efectivo_var.set(f"${self.manager.total_producto_efectivo():.2f}")

    def eliminar_viaje(self):
        """Elimina el viaje seleccionado"""
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un viaje para eliminar")
            return
        
        # Obtener el índice
        item = seleccion[0]
        indice = int(self.tabla.item(item, "text")) - 1
        
        # Eliminar usando manager
        self.manager.remove_trip(indice)
        self.actualizar_tabla()
        messagebox.showinfo("Éxito", "Viaje eliminado")

    def limpiar_todo(self):
        """Limpia todos los viajes"""
        if not self.manager.get_all():
            messagebox.showinfo("Información", "No hay viajes para limpiar")
            return
        
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas limpiar todos los viajes?"):
            self.manager.clear()
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "Todos los viajes han sido eliminados")

    def exportar_resumen(self):
        """Exporta un resumen de los viajes"""
        if not self.manager.get_all():
            messagebox.showwarning("Advertencia", "No hay viajes para exportar")
            return
        
        resumen = self.manager.generate_summary()
        
        # Guardar a archivo
        nombre_archivo = f"resumen_viajes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as f:
                f.write(resumen)
            messagebox.showinfo("Éxito", f"Resumen exportado a {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar: {e}")
