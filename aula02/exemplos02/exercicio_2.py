from os import system
system('cls')
 
#Crie um programa que permita a um professor registrar as notas de uma turma. 
#O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. 
#O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.
#Notas = [] -> len(Notas)​

def registrar_notas():
    notas = []

    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim' para encerrar.")

    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f"\nQuantidade de notas registradas: {len(notas)}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota válida foi registrada.")

# Executa o programa
registrar_notas()
