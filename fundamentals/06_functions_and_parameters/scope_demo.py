# Scope-Demo: Parameter vs. äußere Variable
spieler_leben = 100
print(f"Start HP: {spieler_leben}")


def hit_player(current_hp, damage=10):
    """Gibt die neue Lebenszahl zurück, verändert aber nichts global."""
    current_hp = current_hp - damage
    return current_hp


spieler_leben = hit_player(spieler_leben)
print(f"Nach dem Treffer: {spieler_leben}")
