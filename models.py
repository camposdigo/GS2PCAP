class Perfil:
    def __init__(self, nome):
        self.nome = nome
        self.competencias = {}

    def adicionar_competencia(self, competencia, nivel):
        if 0 <= nivel <= 10:
            self.competencias[competencia.lower()] = nivel
        else:
            print(f"Aviso: Nível {nivel} para '{competencia}' é inválido. Use 0-10.")


class Carreira:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.competencias_requeridas = {}

    def adicionar_requisito(self, competencia, nivel_minimo):
        self.competencias_requeridas[competencia.lower()] = nivel_minimo


class SistemaOrientacao:
    def __init__(self):
        self.carreiras = []
        self._inicializar_carreiras_base()

    def _inicializar_carreiras_base(self):
        print("Inicializando banco de carreiras...")

        c1 = Carreira("Analista de IA Ética",
                      "Garante que sistemas de IA operem de forma justa e transparente.")
        c1.adicionar_requisito("lógica", 8)
        c1.adicionar_requisito("adaptabilidade", 7)
        c1.adicionar_requisito("colaboração", 6)

        c2 = Carreira("Designer de Ecossistemas de IoT",
                      "Projeta a interação entre múltiplos dispositivos inteligentes.")
        c2.adicionar_requisito("criatividade", 7)
        c2.adicionar_requisito("lógica", 7)
        c2.adicionar_requisito("colaboração", 8)

        c3 = Carreira("Estrategista de Criatividade Computacional",
                      "Usa IA para aumentar a capacidade criativa de equipes.")
        c3.adicionar_requisito("criatividade", 9)
        c3.adicionar_requisito("lógica", 6)
        c3.adicionar_requisito("adaptabilidade", 8)

        self.carreiras.extend([c1, c2, c3])

    def analisar_perfil(self, perfil):
        resultados = {
            "recomendadas": [],
            "aprimoramento": []
        }

        for carreira in self.carreiras:
            pontos_fortes = 0
            competencias_a_melhorar = []

            for req_nome, req_nivel in carreira.competencias_requeridas.items():

                nivel_usuario = perfil.competencias.get(req_nome, 0)

                if nivel_usuario >= req_nivel:
                    pontos_fortes += 1
                else:
                    diferenca = req_nivel - nivel_usuario
                    competencias_a_melhorar.append({
                        "nome": req_nome,
                        "diferenca": diferenca,
                        "nivel_exigido": req_nivel
                    })

            total_requisitos = len(carreira.competencias_requeridas)

            if pontos_fortes == total_requisitos:
                resultados["recomendadas"].append({
                    "carreira": carreira,
                    "status": "Alinhamento Perfeito!"
                })
            elif pontos_fortes >= total_requisitos / 2:
                resultados["aprimoramento"].append({
                    "carreira": carreira,
                    "trilha_aprendizado": competencias_a_melhorar
                })

        return resultados