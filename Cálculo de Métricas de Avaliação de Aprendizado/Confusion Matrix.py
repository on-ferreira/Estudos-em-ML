'''

                     Classe Prevista
                 |   Positiva   |   Negativa   |
------------------------------------------------
Classe Real  |    40 (VP)    |    5 (FP)     |  Positiva
------------------------------------------------
Classe Real  |    25 (FN)    |    30 (VN)    |  Negativa
------------------------------------------------


Neste exemplo, temos:

40 verdadeiros positivos (VP): foram classificados corretamente como positivos.
30 verdadeiros negativos (VN): foram classificados corretamente como negativos.
5 falsos positivos (FP): foram classificados incorretamente como positivos, quando deveriam ser negativos.
25 falsos negativos (FN): foram classificados incorretamente como negativos, quando deveriam ser positivos.


'''


def calcula_metricas_2v2(confusion_matrix):
    VP = confusion_matrix[0][0]
    VN = confusion_matrix[1][1]
    FP = confusion_matrix[0][1]
    FN = confusion_matrix[1][0]
    Total = VP + VN + FP + FN

    S = VP / (VP + FN)
    E = VN / (FP + VN)
    Acc = (VP + VN) / Total
    P = VP / (VP + FP)
    Fscore = 2 * (P * S) / (P + S)

    return S, E, Acc, P, Fscore


confusion_matrix = [[40, 5], [25, 30]]
S, E, Acc, P, FScore = calcula_metricas_2v2(confusion_matrix)

print(f'''
    As métricas da matriz são:
    Sensibilidade = {S*100:.2f}%
    Especificidade = {E*100:.2f}%
    Acurácia = {Acc*100:.2f}%
    Precisão = {P*100:.2f}%
    F-Score = {FScore*100:.2f}%
''')
