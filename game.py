# game.py

# Estrutura de dados contendo os 3 níveis
NIVEIS = {
    1: {
        "palavras": [
            "SISTEMA", "USUARIO", "CPU", "DISCO", "MEMORIA",
            "ARQUIVO", "TERMINAL", "GABINETE", "LINUX", "WINDOWS"
        ],
        "grade": [
            "S","I","S","T","E","M","A","Q","W","E","R","T","Y","U","I","O","P","A","S","D",
            "Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z",
            "U","S","U","A","R","I","O","Z","X","C","V","B","N","M","Q","W","E","R","T","Y",
            "A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","Q","W","E","R",
            "C","P","U","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J",
            "D","I","S","C","O","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N",
            "M","E","M","O","R","I","A","Q","W","E","R","T","Y","U","I","O","P","A","S","D",
            "Z","X","C","V","B","N","M","Q","W","E","R","T","Y","U","I","O","P","A","S","D",
            "A","R","Q","U","I","V","O","L","K","J","H","G","F","D","S","A","Q","W","E","R",
            "Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z",
            "T","E","R","M","I","N","A","L","Q","W","E","R","T","Y","U","I","O","P","A","S",
            "Z","X","C","V","B","N","M","Q","W","E","R","T","Y","U","I","O","P","A","S","D",
            "G","A","B","I","N","E","T","E","Q","W","E","R","T","Y","U","I","O","P","A","S",
            "Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z",
            "L","I","N","U","X","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N",
            "Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z",
            "W","I","N","D","O","W","S","Z","X","C","V","B","N","M","Q","W","E","R","T","Y",
            "A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","Q","W","E","R",
            "Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z",
            "Z","X","C","V","B","N","M","Q","W","E","R","T","Y","U","I","O","P","A","S","D"
        ]
    },
    2: {
        "palavras": [
        "PYTHON", "JAVA", "API", "SQL", "REACT",
        "MONITOR", "TECLADO", "JAVASCRIPT", "MOUSE",
        "GITHUB", "HTML", "NAVEGADOR"
    ],
        "grade": [
        "P","Y","T","H","O","N","X","A","B","C","G","I","T","H","U","B","X","Y","Z","A",
        "Q","M","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","N","P",
        "Z","O","H","T","M","L","C","V","B","N","M","Q","W","E","R","T","Y","U","A","I",
        "X","N","Z","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","V","Z",
        "C","I","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","E","X",
        "V","T","A","R","E","A","C","T","J","K","L","Z","X","C","V","B","N","M","G","C",
        "B","O","S","D","F","G","H","J","K","L","Q","W","E","R","T","Y","U","I","A","V",
        "N","R","Z","X","C","V","B","N","M","A","S","D","F","G","H","J","K","L","D","B",
        "M","P","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","O","N",
        "A","L","Z","X","C","V","B","N","M","Q","W","E","R","T","Y","U","I","O","R","M",
        "S","X","K","J","A","V","A","S","C","R","I","P","T","A","S","D","F","G","H","L",
        "D","C","L","Z","X","C","V","B","N","M","Q","W","E","R","T","Y","U","I","J","K",
        "F","V","M","A","S","D","F","G","H","M","J","K","L","Z","X","C","V","B","Q","J",
        "G","B","N","Q","W","E","R","T","Y","O","I","O","P","A","S","D","F","G","W","H",
        "H","N","O","Z","X","C","V","B","N","U","M","Q","W","E","R","T","Y","U","E","G",
        "J","M","P","A","S","Q","L","S","B","S","H","J","K","L","J","Z","X","C","R","F",
        "K","Q","Q","A","S","D","F","G","H","E","J","K","L","Z","A","X","C","V","T","D",
        "L","W","R","Q","W","E","R","T","Y","Z","X","C","V","B","V","N","M","Q","Y","S",
        "Z","E","T","E","C","L","A","D","O","A","S","D","F","G","A","H","J","K","U","A",
        "X","R","Y","U","I","O","P","L","K","J","H","G","F","D","S","A","Q","W","E","R"
  ]
},
    3:{
        "palavras": [
        "ALGORITMO", "BACKEND", "FRONTEND", "DEBUG", "ARRAY", 
        "STRING", "BOOLEAN", "COMPILADOR", "DADOS", "CAFE", 
        "WIFI", "CLASSES", "PROGRAMACAO"
  ],
        "grade": [ 
        "P","X","L","A","L","G","O","R","I","T","M","O","Y","Z","A","B","C","D","E","C",
        "R","C","A","F","E","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","O",
        "O","A","B","D","E","B","U","G","C","D","E","F","G","H","I","J","K","L","M","M",
        "G","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","P",
        "R","F","R","O","N","T","E","N","D","F","G","H","A","S","K","L","M","N","O","I",
        "A","P","Q","R","S","T","U","V","W","X","Y","Z","T","T","B","C","D","E","F","L",
        "M","G","H","I","J","B","K","L","M","N","O","P","R","R","R","S","T","U","V","A",
        "A","W","X","Y","Z","A","A","B","C","D","E","F","Q","I","H","I","J","K","L","D",
        "C","M","N","O","P","C","Q","B","O","O","L","E","A","N","R","S","T","U","V","O",
        "A","W","X","Y","Z","K","A","B","C","D","E","F","G","G","I","J","K","L","M","R",
        "O","N","O","P","Q","E","R","S","T","U","C","V","W","X","Y","Z","A","B","C","D",
        "J","K","L","M","N","N","O","P","Q","R","L","S","T","U","V","W","X","Y","Z","A",
        "B","C","D","E","F","D","G","H","I","J","A","R","R","A","Y","K","L","M","N","O",
        "P","Q","R","S","T","U","V","W","X","Y","S","Z","A","B","C","D","E","F","G","H",
        "I","J","K","L","M","N","O","P","Q","R","S","S","T","U","V","W","X","Y","Z","A",
        "B","C","D","A","D","O","S","D","E","F","E","G","H","I","J","K","L","M","N","O",
        "P","Q","R","S","T","U","V","W","X","Y","S","Z","A","B","C","D","E","F","G","H",
        "I","J","K","L","M","N","O","P","Q","R","W","I","F","I","S","T","U","V","W","X",
        "Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
        "S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L"
  ]
}
}

def get_dados_nivel(nivel):
    # Retorna os dados do nível solicitado, ou do nível 1 se não existir
    return NIVEIS.get(nivel, NIVEIS[1])

def verificar_palavra(nivel, sequencia):
    dados = NIVEIS.get(nivel)
    if dados:
        return sequencia in dados["palavras"]
    return False