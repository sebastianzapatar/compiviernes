
from elcompifiles.repl import star_repel
def pantalla_bienvenida():
    mensaje = """
     ***     *   *   *****   *    *   *****
    *   *    *   *     *     **   *   *
    *        *   *     *     * *  *   *
    *        *   *     *     *  * *   ****
    *   *    *   *     *     *   **   *
     ***      ***      *     *    *   *****
    """

    print(mensaje)
    print("Bienvenido al compilador")
def main()->None:
    pantalla_bienvenida()
    star_repel()
if __name__ == "__main__":
    main()