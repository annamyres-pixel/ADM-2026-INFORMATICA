"""Atividade Modulo 4 - ADM 2026 Informatica."""
import sys


def iniciar():
    print("=" * 50)
    print("Atividade Modulo 4 - INICIADA")
    print("=" * 50)
    print("Ola! Script atividade_modulo4.py executado com sucesso.")
    print("Comando recebido: iniciar")


def ajuda():
    print("Uso: python atividade_modulo4.py [iniciar|ajuda]")
    print("  iniciar - inicia a atividade do modulo 4")
    print("  ajuda   - mostra esta mensagem")


def main():
    comando = sys.argv[1].lower() if len(sys.argv) > 1 else "iniciar"
    if comando == "iniciar":
        iniciar()
    elif comando in ("ajuda", "--help", "-h"):
        ajuda()
    else:
        print(f"Comando desconhecido: {comando}")
        ajuda()
        sys.exit(1)


if __name__ == "__main__":
    main()
