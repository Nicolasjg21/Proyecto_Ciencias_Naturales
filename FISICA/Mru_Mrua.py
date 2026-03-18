print(
    """
\n ========== SENA MRU/MRUA ==========\n     
Sistema creado para instruir informacion basica
acerca del movimiento Rectilineo Uniforme y 
el Movimuento Rectilineo Uniformemente Acelerado
(MRU y MRUA).
\n ===================================\n
      """
)
opcion = int(
    input(
        """
=======================================  
    1. Info acerca de MRU.
    2. Info acerca de MRUA.
    3. Info de los dos (MRU y MRUA).
======================================= 
A continuacion, selecioone que desea:   
                   """
    )
)

match opcion:
    case 1:
        import MRU
    case 2:
        import MRUA
    case 3:
        import MRU
        import MRUA
    case _:
        print(
            "El valor digitado no existe, el numero 1 y el 2 son los unicos valores digitables"
        )
print(MRU, MRUA)
