# Server Protokoll

## Generelles

- Es wird das Json-Format für die Datenübertragung verwendet.

- Ist Encodierung notwendig (Besipielsweise für Bilder), wird die Base-64 Kodierung verwendet

---

- da es sich um einen Broadcast Server handelt muss der Rezipient und der Absender bei Jeder Nachricht genannt werden


## Kodierung

```json
[
    "sender":"server|player1|player2",
    "receiver":"server|player1|player2",
    "game":"pong|...",
    "timestamp": /* timestamp in Unix millis */,
    "data": {
        // Ab Hier Protokoll nach Spiel
    }
]
```

