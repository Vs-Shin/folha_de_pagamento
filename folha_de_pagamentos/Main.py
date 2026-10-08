import banco
import conta

def menu():
    banco.criar_tabelas()
    
    while True:
        print("\n=== SISTEMA DE FOLHA DE PAGAMENTO - PREFEITURA ===\n")
        print("1. Cadastrar Servidor")
        print("2. Listar Servidores e Gerar Holerite")
        print("3. Atualizar Dados do Servidor")
        print("4. Deletar Servidor")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário Base: R$ "))
            anos = int(input("Anos de Serviço Público: "))
            
            banco.salvar_servidor(nome, cargo, salario, anos)
            print("\n✓ Servidor cadastrado com sucesso!")

        elif opcao == "2":
            servidores = banco.listar_servidores()
            if not servidores:
                print("\nNenhum servidor cadastrado.")
                continue

            print("\n--- SERVIDORES CADASTRADOS ---")
            for s in servidores:
                print(f"ID: {s[0]} | Nome: {s[1]} | Cargo: {s[2]}")
            
            id_sel = int(input("\nDigite o ID do servidor para ver o Holerite (ou 0 para voltar): "))
            if id_sel == 0:
                continue

            servidor = next((s for s in servidores if s[0] == id_sel), None)
            
            if servidor:
                resultado = conta.calcular_folha(servidor[3], servidor[4])
                
                print("\n--- HOLERITE / CONTRACHEQUE ---\n")
                print(f"Servidor: {servidor[1]} ({servidor[2]})")
                print(f"Salário Base: R$ {servidor[3]:.2f}")
                print(f"Adicional Triênio: R$ {resultado['adicional']:.2f}")
                print(f"Salário Bruto: R$ {resultado['bruto']:.2f}")
                print(f"Desconto INSS: R$ {resultado['inss']:.2f}")
                print(f"Desconto IRRF: R$ {resultado['irrf']:.2f}")
                print(f"Salário Líquido: R$ {resultado['liquido']:.2f}")
                print("-------------------------------")
            else:
                print("Servidor não encontrado!")

        elif opcao == "3":
            servidores = banco.listar_servidores()
            if not servidores:
                print("Nenhum servidor cadastrado.")
                continue

            for s in servidores:
                print(f"ID: {s[0]} | Nome: {s[1]} | Cargo: {s[2]} | Salário: R$ {s[3]:.2f} | Anos: {s[4]}")

            id_sel = int(input("\nDigite o ID do servidor que deseja atualizar: "))
            novo_cargo = input("Novo Cargo: ")
            novo_salario = float(input("Novo Salário Base: R$ "))
            novos_anos = int(input("Novos Anos de Serviço: "))

            if banco.atualizar_servidor(id_sel, novo_cargo, novo_salario, novos_anos):
                print("✓ Dados atualizados com sucesso!")
            else:
                print("Servidor não encontrado!")

        elif opcao == "4":
            servidores = banco.listar_servidores()
            if not servidores:
                print("Nenhum servidor cadastrado.")
                continue

            for s in servidores:
                print(f"ID: {s[0]} | Nome: {s[1]}")

            id_sel = int(input("\nDigite o ID do servidor que deseja DELETAR: "))
            confirmacao = input(f"Tem certeza que deseja deletar o ID {id_sel}? (s/n): ").lower()

            if confirmacao == 's':
                if banco.deletar_servidor(id_sel):
                    print("✓ Servidor deletado com sucesso!")
                else:
                    print("Servidor não encontrado!")

        elif opcao == "5":
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    menu()
