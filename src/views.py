from .services import TaskService

class ConsoleView:
    def __init__(self, service: TaskService):
        self.service = service
        
    def show_menu(self):
        print("\n--- Sistema de Gestão de Tarefas ---")
        print("1. Nova Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Sair")
        
    def start(self):
        while True:
            self.show_menu()
            choice = input("Escolha: ")
            
            if choice == '1':
                title = input("Título: ")
                desc = input("Descrição: ")
                owner = input("Responsável: ")
                self.service.create_new_task(title, desc, owner)
                print("Tarefa criada!")
            elif choice == '2':
                tasks = self.service.list_tasks()
                for idx, t in enumerate(tasks):
                    print(f"{idx}. {t}")
            elif choice == '3':
                idx = int(input("ID da tarefa para concluir: "))
                self.service.complete_task(idx)
            elif choice == '4':
                break