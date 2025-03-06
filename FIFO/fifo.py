# FIFO: o primeiro a funcionar é o primeiro a ser escolhido
from collections import deque

class FifoScheduler:
   # Inicializador(construtor de classe) 
    def __init__(self):
        self.fila_processos = deque()
        
    def adicionar_processos(self,pid, tempo_exec):
        processo = (pid, tempo_exe)
        self.fila_processos.append(processo)
        
    def remover_processo(self):
        if self.fila_processos:
            return self.fila_processos.popleft()
        
        else:
            print("Nenhum processo para remover")
            return
    
    # Função  que simula o comportamento do agendamento
    def fifo_scheduling(self):
        tempo_atual = 0 
        tempos_espera = {}
        tempos_retorno = {}
        
        print('\nExecução dos processos (FIFO):')
        
        while self.fila_processos:
            pid, tempo_exec = self.remover_processo ()
            
            tempos_espera [pid] = tempo_atual
            tempos_retorno [pid] = tempo_atual + tempo_exec
            
            print(f'Processo {pid} executando ... (Tempo: {tempo_atual} {tempo_atual + tempo_exec})')
            
            tempo_atual += tempo_exec
            
            print('\nResumo do escalonamento:')
            print('PID | Tempo de Espera | Tempo de Retorno')
            for pid in tempos_espera:
                print(f'{pid:^3} | {tempos_espera[pid]:^15} | {tempos_retorno [pid]:^14}')
                
                scheduler = FifoScheduler ()
                scheduler.adicionar_processos(1, 5)
                scheduler.adicionar_processos(2, 3)
                scheduler.adicionar_processos(3, 8)
                scheduler.adicionar_processos(4, 6)
                scheduler.fifo_scheduling()
                