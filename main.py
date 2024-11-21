def calcular_imc():
    print("Bem-vindo ao Calculador de IMC!")
    
    try:
        
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        
        imc = peso / (altura ** 2)
        
        
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 34.9:
            classificacao = "Obesidade grau I"
        elif 35 <= imc < 39.9:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III ou mórbida"
        
        
        print(f"\nSeu IMC é {imc:.2f}. Classificação: {classificacao}")
    except ValueError:
        print("Por favor, insira valores válidos para peso e altura.")


if __name__ == "__main__":
    calcular_imc()
