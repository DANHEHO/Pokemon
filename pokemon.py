class Pokemon:
    # Variable de clase para rastrear el total de Pokémon creados
    total_creados = 0

    def __init__(self, nombre: str, tipo: str, ataque: int = 10, defensa: int = 10, salud: int = 50):
        # Atributos de instancia
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        self.salud_maxima = salud

        # Aumentamos el contador global/de clase
        Pokemon.total_creados += 1
        print(f"\n ¡Has capturado a {self.nombre} (Tipo: {self.tipo})! ")

    def __del__(self):
        # Destructor que se ejecuta al eliminar el objeto o restar referencia
        Pokemon.total_creados -= 1
        print(f"\n {self.nombre} ha sido liberado en la naturaleza. ")

    def mostrar_info(self):
        """Muestra la información detallada del Pokémon."""
        print("-" * 35)
        print(f" Nombre:  {self.nombre}")
        print(f"  Tipo:    {self.tipo}")
        print(f" Nivel:   {self.nivel}")
        print(f"  Ataque:  {self.ataque}")
        print(f"  Defensa: {self.defensa}")
        print(f"  Salud:   {self.salud}/{self.salud_maxima}")
        print("-" * 35)

    def entrenar(self, *stats):
        """
        Sobrecarga de método mediante *args:
        - Si no se pasan argumentos, sube estadísticas de forma general.
        - Se pueden especificar las estadísticas a mejorar mediante texto:
          ej. entrenar('ataque', 'defensa') o entrenar('salud')
        """
        self.nivel += 1
        print(f"\n ¡{self.nombre} ha subido al Nivel {self.nivel}!")

        if not stats:
            # Mejora por defecto
            self.ataque += 3
            self.defensa += 3
            self.salud_maxima += 5
            self.salud = self.salud_maxima
            print("   Se han incrementado todas sus estadísticas equilibradamente (+3 Ataque, +3 Defensa, +5 Salud).")
        else:
            for stat in stats:
                stat_clean = stat.strip().lower()
                if stat_clean == 'ataque':
                    self.ataque += 5
                    print("     Ataque aumentó +5")
                elif stat_clean == 'defensa':
                    self.defensa += 5
                    print("     Defensa aumentó +5")
                elif stat_clean == 'salud':
                    self.salud_maxima += 10
                    self.salud += 10
                    print("    Salud máxima aumentó +10")

    def atacar(self, objetivo):
        """
        Simula un ataque a otro Pokémon (paso de parámetro por referencia).
        Modifica el objeto 'objetivo' recibido.
        """
        dano_base = self.ataque - (objetivo.defensa // 2)
        dano = max(1, dano_base)  # Al menos inflige 1 de daño

        objetivo.salud -= dano
        if objetivo.salud < 0:
            objetivo.salud = 0

        print(f"\n {self.nombre} ataca a {objetivo.nombre} e inflige {dano} puntos de daño.")
        print(f" Salud restante de {objetivo.nombre}: {objetivo.salud}/{objetivo.salud_maxima}")

    @classmethod
    def total_pokemons(cls):
        """Método de clase que informa el total de Pokémon creados actualmente."""
        print(f"\n Total de Pokémon registrados actualmente: {cls.total_creados}")
        return cls.total_creados