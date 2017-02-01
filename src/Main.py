from Controller import Controller
from DataBase import DataBase
from Modelo import Modelo
from ConsoleView import ConsoleView

notesFile = "notes.xml"

dataBase = DataBase(notesFile)
modelo = Modelo(dataBase)
controller = Controller(modelo)
vistaConsola = ConsoleView(controller)


vistaConsola.display()

#controller.loadNotes()
#controller.createNote('Note 1', 'This is the note one')