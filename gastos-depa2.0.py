import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

class GastosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Gastos Mensuales")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Color scheme
        self.bg_color = "#f0f0f0"
        self.accent_color = "#2196F3"
        self.text_color = "#333333"
        
        self.root.configure(bg=self.bg_color)
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = ttk.Label(
            self.main_frame, 
            text="💰 Calculadora de Gastos Mensuales", 
            font=("Arial", 18, "bold")
        )
        title.pack(pady=(0, 20))
        
        # Input fields frame
        input_frame = ttk.LabelFrame(
            self.main_frame, 
            text="Ingrese los gastos mensuales", 
            padding="15"
        )
        input_frame.pack(fill=tk.BOTH, pady=10)
        
        # Agua
        ttk.Label(input_frame, text="💧 Agua ($):", font=("Arial", 11)).grid(
            row=0, column=0, sticky=tk.W, pady=10
        )
        self.agua_entry = ttk.Entry(input_frame, font=("Arial", 11), width=20)
        self.agua_entry.grid(row=0, column=1, sticky=tk.W, padx=10)
        self.agua_entry.bind("<KeyRelease>", lambda e: self.calcular())
        
        # Luz
        ttk.Label(input_frame, text="💡 Luz ($):", font=("Arial", 11)).grid(
            row=1, column=0, sticky=tk.W, pady=10
        )
        self.luz_entry = ttk.Entry(input_frame, font=("Arial", 11), width=20)
        self.luz_entry.grid(row=1, column=1, sticky=tk.W, padx=10)
        self.luz_entry.bind("<KeyRelease>", lambda e: self.calcular())
        
        # Gas
        ttk.Label(input_frame, text="🔥 Gas ($):", font=("Arial", 11)).grid(
            row=2, column=0, sticky=tk.W, pady=10
        )
        self.gas_entry = ttk.Entry(input_frame, font=("Arial", 11), width=20)
        self.gas_entry.grid(row=2, column=1, sticky=tk.W, padx=10)
        self.gas_entry.bind("<KeyRelease>", lambda e: self.calcular())
        
        # Results frame
        results_frame = ttk.LabelFrame(
            self.main_frame, 
            text="Resultados", 
            padding="15"
        )
        results_frame.pack(fill=tk.BOTH, pady=10)
        
        # Total mensual
        ttk.Label(
            results_frame, 
            text="Total Mensual:", 
            font=("Arial", 11, "bold")
        ).grid(row=0, column=0, sticky=tk.W, pady=10)
        self.total_mensual_label = ttk.Label(
            results_frame, 
            text="$0.00", 
            font=("Arial", 14, "bold"),
            foreground=self.accent_color
        )
        self.total_mensual_label.grid(row=0, column=1, sticky=tk.W, padx=20)
        
        # Gasto diario promedio
        ttk.Label(
            results_frame, 
            text="Gasto Diario Promedio:", 
            font=("Arial", 11, "bold")
        ).grid(row=1, column=0, sticky=tk.W, pady=10)
        self.gasto_diario_label = ttk.Label(
            results_frame, 
            text="$0.00", 
            font=("Arial", 14, "bold"),
            foreground=self.accent_color
        )
        self.gasto_diario_label.grid(row=1, column=1, sticky=tk.W, padx=20)
        
        # Desglose frame
        desglose_frame = ttk.LabelFrame(
            self.main_frame, 
            text="Desglose Diario", 
            padding="15"
        )
        desglose_frame.pack(fill=tk.BOTH, pady=10)
        
        # Daily breakdown labels
        ttk.Label(
            desglose_frame, 
            text="💧 Agua diario:", 
            font=("Arial", 10)
        ).grid(row=0, column=0, sticky=tk.W, pady=8)
        self.agua_diario_label = ttk.Label(
            desglose_frame, 
            text="$0.00", 
            font=("Arial", 11, "bold"),
            foreground="#4CAF50"
        )
        self.agua_diario_label.grid(row=0, column=1, sticky=tk.W, padx=20)
        
        ttk.Label(
            desglose_frame, 
            text="💡 Luz diario:", 
            font=("Arial", 10)
        ).grid(row=1, column=0, sticky=tk.W, pady=8)
        self.luz_diario_label = ttk.Label(
            desglose_frame, 
            text="$0.00", 
            font=("Arial", 11, "bold"),
            foreground="#FF9800"
        )
        self.luz_diario_label.grid(row=1, column=1, sticky=tk.W, padx=20)
        
        ttk.Label(
            desglose_frame, 
            text="🔥 Gas diario:", 
            font=("Arial", 10)
        ).grid(row=2, column=0, sticky=tk.W, pady=8)
        self.gas_diario_label = ttk.Label(
            desglose_frame, 
            text="$0.00", 
            font=("Arial", 11, "bold"),
            foreground="#F44336"
        )
        self.gas_diario_label.grid(row=2, column=1, sticky=tk.W, padx=20)
        
        # Buttons frame
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.pack(fill=tk.X, pady=15)
        
        # Clear button
        ttk.Button(
            buttons_frame, 
            text="Limpiar", 
            command=self.limpiar
        ).pack(side=tk.LEFT, padx=5)
        
        # Info button
        ttk.Button(
            buttons_frame, 
            text="ℹ Info", 
            command=self.mostrar_info
        ).pack(side=tk.LEFT, padx=5)
    
    def calcular(self):
        """Calcula los gastos diarios basado en los valores ingresados"""
        try:
            # Get values from entries
            agua = float(self.agua_entry.get() or 0)
            luz = float(self.luz_entry.get() or 0)
            gas = float(self.gas_entry.get() or 0)
            
            # Calculate total
            total_mensual = agua + luz + gas
            
            # Get current month's days
            today = datetime.now()
            if today.month == 12:
                last_day = 31
            else:
                last_day = (datetime(today.year, today.month + 1, 1) - 
                           timedelta(days=1)).day
            
            # Calculate daily average
            gasto_diario = total_mensual / last_day if last_day > 0 else 0
            agua_diario = agua / last_day if last_day > 0 else 0
            luz_diario = luz / last_day if last_day > 0 else 0
            gas_diario = gas / last_day if last_day > 0 else 0
            
            # Update labels
            self.total_mensual_label.config(text=f"${total_mensual:,.2f}")
            self.gasto_diario_label.config(text=f"${gasto_diario:,.2f}")
            self.agua_diario_label.config(text=f"${agua_diario:,.2f}")
            self.luz_diario_label.config(text=f"${luz_diario:,.2f}")
            self.gas_diario_label.config(text=f"${gas_diario:,.2f}")
            
        except ValueError:
            # Clear labels if invalid input
            self.total_mensual_label.config(text="$0.00")
            self.gasto_diario_label.config(text="$0.00")
            self.agua_diario_label.config(text="$0.00")
            self.luz_diario_label.config(text="$0.00")
            self.gas_diario_label.config(text="$0.00")
    
    def limpiar(self):
        """Limpia todos los campos"""
        self.agua_entry.delete(0, tk.END)
        self.luz_entry.delete(0, tk.END)
        self.gas_entry.delete(0, tk.END)
        self.calcular()
    
    def mostrar_info(self):
        """Muestra información sobre la aplicación"""
        messagebox.showinfo(
            "Acerca de",
            "💰 Calculadora de Gastos Mensuales\n\n"
            "Ingrese los montos mensuales de:\n"
            "• Agua\n"
            "• Luz\n"
            "• Gas\n\n"
            "La aplicación calculará automáticamente:\n"
            "• Total mensual\n"
            "• Gasto diario promedio\n"
            "• Desglose por servicio\n\n"
            "v1.0"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = GastosApp(root)
    root.mainloop()
