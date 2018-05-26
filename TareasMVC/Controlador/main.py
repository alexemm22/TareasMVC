#!/usr/bin/env python3
"""
Módulo Main: Programa principal (controlador).

Gestion de Tareas - Alexander Emmanuel Orlandini Randazzo
Ejecute "ayuda" para más información
"""
from Modelo.Tareas import Tarea
from estante import Estante
from Vista.repl import REPL
from Vista.repl import strip


class Main:
    """Clase principal."""

    def __init__(self):
        """Constructor: Inicializa propiedades de instancia y ciclo REPL."""
        self.comandos = {
            "agregar": self.agregar,
            "borrar": self.borrar,
            "mostrar": self.mostrar,
            "listar": self.listar,
            "buscar": self.buscar,
            "ayuda": self.ayuda,
            "salir": self.salir
        }
        archivo = "tarea.db"
        introduccion = strip(__doc__)
        self.task = Estante(archivo)
        if not self.task.esarchivo():
            introduccion += '\nError: No se pudo abrir "{}"'.format(archivo)
        REPL(self.comandos, introduccion).ciclo()

    def agregar(self, nombre, vencimiento):
        """
        Agrega una Tarea  con su vencimiento.

        Ejemplo: agregar "nombre de Tarea"  "Vencimiento"
        """
        self.task[nombre] = Tarea(nombre, vencimiento)

    def borrar(self, nombre):
        """
        Borra una Tarea.

        Ejemplo: borrar "nombre de tarea"
        """
        del self.task[nombre]

    def mostrar(self, nombre):
        """
        Retorna una Tarea

          Ejemplo: mostrar "nombre de su Tarea"
        """
        return self.task[nombre]

    def listar(self):
        """
        Todas las Tareas

        Este comando no requiere de parámetros.
        """
        return (self.task[nombre]
                for nombre in sorted(self.task))

    def buscar(self, cadena):
        """
        Retorna una Tarea

          Ejemplo: buscar "nombre de su Tarea"
        """
        return (self.task[nombre]
                for nombre in sorted(self.task)
                if cadena in nombre)

    def ayuda(self, comando=None):
        """
        Retorna la lista de comandos disponibles.

        comando -- Comando del que se desea obtener ayuda (opcional).
        """
        if comando in self.comandos:
            salida = strip(self.comandos[comando].__doc__)
        else:
            salida = "Sintaxis: comando [parámetro1] [parámetro2] [..]\n" + \
                     "Comandos: " + \
                     ", ".join(sorted(self.comandos.keys()))
        return salida

    def salir(self):
        """
        Salir de la aplicación.

        Este comando no requiere de parámetros.
        """
        quit()


if __name__ == "__main__":
    Main()
