import pytest
from arithmetic_operators import calculate_metrics

# Definimos uma lista de casos de teste: (entrada_a, entrada_b, saida_esperada)
test_cases = [
    # Caso do Exemplo da imagem
    (3, 5, (8, -2, 15)),
    
    # Caso do Sample Input 0
    (3, 2, (5, 1, 6)),
    
    # Caso com zeros
    (10, 0, (10, 10, 0)),
    
    # Caso com números negativos
    (-5, -5, (-10, 0, 25)),
    
    # Caso de borda: Constraints Grandes (10^10)
    (10**10, 10**10, (2 * 10**10, 0, 10**20))
]

@pytest.mark.parametrize("a, b, expected", test_cases)
def test_calculate_metrics(a, b, expected):
    """
    Testa se a função retorna a tupla correta de (soma, subtração, produto)
    para diversos inputs.
    """
    result = calculate_metrics(a, b)
    assert result == expected