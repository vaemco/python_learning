"""
Purpose: Demonstrating variable scope (local vs global).
Status: Educational / Completed
Topics: Scope, Parameters, Return Values
"""

# Scope Demo: Parameter vs. external variable
spieler_leben = 100
print(f"Start HP: {spieler_leben}")


def hit_player(current_hp, damage=10):
    """Returns the new HP, but does not modify anything globally."""
    current_hp = current_hp - damage
    return current_hp


spieler_leben = hit_player(spieler_leben)
print(f"Nach dem Treffer: {spieler_leben}")
