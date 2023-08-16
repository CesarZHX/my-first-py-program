# Import Librery / Importar libreria.
import pandas as pd

def pd_test():
    # I: Load data into a dataframe / Cargar datos a un dataframe.
    print ('\n1. Cargando datos del documento de excel...')
    excel = 'Datos ventas.xlsx'
    try:
        dt = pd.read_excel(excel, header=0)
    except Exception as e:
        print("Error:", str(e),)
    else:
        print ('Datos cargados satisfactoriamente.')

    # II: Show first 5 rows / Mostrar las 5 priemrasfilas.
    print ('\n2. Exploracion inicial...')
    # Increase Index, to start at 1 / Aumentar el indice, para empezar por el 1.
    dt.index = dt.index + 1 
    try:
        print ('Filas 1-5:')
        print(dt.iloc[0:5]) 
    except Exception as e:
        print("Error:", str(e))
    else:
        print ('Exploración inicial completada satisfactoriamente.')

    # III. Show basic stats / Mostar las estadísticas básicas:

    try:
        # Title
        print ('\n3. Estadisticas basicas:')

        # A: The best-selling product and the least-selling product / El producto más vendido y el producto menos vendido.
        print ('3.1. Busqueda del producto más vendido y del producto menos vendido en términos de cantidad.')
        # Quantity sold by product / Cantidad vendida por producto.
        quantities = dt.groupby('Producto')['Cantidad Vendida'].sum()
        
        # Best-selling product ID / ID del producto mas vendido.
        best_selling = quantities.idxmax()
        # Quantity of Best-selling product / Cantidad del producto mas vendido.
        best_selling_quantity = max(quantities)
        print (' - Producto mas vendido:'+str(best_selling), '('+str(best_selling_quantity), ' ventas).')

        # Least-selling product ID / ID del producto menos vendido.
        least_selling = quantities.idxmin()
        # Quantity of least-selling product / Cantidad del producto menos vendido.
        least_selling_quantity = min(quantities)
        print (' - Producto menos vendido:'+str(least_selling), '('+str(least_selling_quantity), 'ventas).')

        # B: The most expensive product & cheaper product / El producto mas caro y el producto mas barato.
        print ('3.2. Busqueda del producto más costoso y del producto más económico de acuerdo a su precio unitario:')
        
        # Unit price per product / Precio unitario por producto.
        prices = dt.groupby('Producto')['Precio Unitario'].mean()
        
        # Most expensive product by ID / Producto mas caro por ID.
        expensive = prices.idxmax()
        # Price of most expensive product / Precio del producto mas caro.
        expensive_price = max(prices)
        print (' - Producto mas caro:'+str(expensive), '(S/.'+str(expensive_price)+').')
        
        # Cheaper product ID / ID del producto mas barato.
        cheaper = prices.idxmin()  
        # Price of cheaper product / Precio del producto mas barato.
        cheaper_price = min(prices)
        print (' - Producto mas economico:'+str(cheaper), '(S/.'+str(cheaper_price)+').')
    except Exception as e:
        print("Error:", str(e))
    else:
        print ('Estadisticas mostradas satisfactoriamente.')
    finally:
        print ('\n-- Programa finalizado. --\n')
        
# Powered by Cesar Albornoz - All right reserved.