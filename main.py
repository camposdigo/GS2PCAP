from models import Perfil, SistemaOrientacao
import time


def exibir_resultados(resultados, perfil):
    print("\n" + "=" * 40)
    print(f"Relatório de Orientação para: {perfil.nome}")
    print("=" * 40)

    if not resultados["recomendadas"]:
        print("\nNenhuma carreira com alinhamento perfeito encontrada no momento.")
    else:
        print("\nCarreiras com Alinhamento Perfeito:")
        for res in resultados["recomendadas"]:
            carreira = res["carreira"]
            print(f"  - {carreira.nome}: {carreira.descricao}")

    if not resultados["aprimoramento"]:
        print("\nNenhuma carreira próxima encontrada para aprimoramento.")
    else:
        print("\nCarreiras Próximas (Trilhas de Aprimoramento):")
        for res in resultados["aprimoramento"]:
            carreira = res["carreira"]
            print(f"\n  [ {carreira.nome} ]")
            print(f"  Descrição: {carreira.descricao}")
            print("  Trilha sugerida para esta carreira:")
            for trilha in res["trilha_aprendizado"]:
                print(f"    - {trilha['nome'].capitalize()}: (Seu nível: {perfil.competencias.get(trilha['nome'], 0)}, "
                      f"Exigido: {trilha['nivel_exigido']})")

    print("\n" + "=" * 40)


def coletar_competencias():
    competencias_base = ["lógica", "criatividade", "colaboração", "adaptabilidade"]
    perfil = Perfil(input("Digite seu nome: "))

    print(f"\nOlá, {perfil.nome}. Vamos analisar seu perfil.")
    print("Por favor, avalie de 0 a 10 as seguintes competências:")

    for comp in competencias_base:
        while True:
            try:
                nivel = int(input(f"  - {comp.capitalize()}: "))
                if 0 <= nivel <= 10:
                    perfil.adicionar_competencia(comp, nivel)
                    break
                else:
                    print("Por favor, digite um número entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    return perfil


def main():
    sistema = SistemaOrientacao()

    while True:
        print("\n--- FIAP Future Skills Lab ---")
        print("[1] Analisar meu Perfil Profissional")
        print("[2] Listar todas as Carreiras")
        print("[3] Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            perfil_usuario = coletar_competencias()

            print("\nProcessando seu perfil...")
            time.sleep(1)

            resultados = sistema.analisar_perfil(perfil_usuario)

            exibir_resultados(resultados, perfil_usuario)

        elif escolha == "2":
            print("\n--- Carreiras Cadastradas no Sistema ---")
            if not sistema.carreiras:
                print("Nenhuma carreira cadastrada.")
            for i, carreira in enumerate(sistema.carreiras):
                print(f"\n{i + 1}. {carreira.nome}")
                print(f"   {carreira.descricao}")
                print("   Requisitos:")
                for req, nivel in carreira.competencias_requeridas.items():
                    print(f"    - {req.capitalize()}: Nível {nivel}")

        elif escolha == "3":
            print("Obrigado por usar o Future Skills Lab! Até a próxima.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
