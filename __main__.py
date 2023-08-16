# Import module / Importar modulo.
from app.screen import tk_console

# Main / Programa
def main():
    try:
        tk_console()
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()

# Powered by Cesar Albornoz - All right reserved. 