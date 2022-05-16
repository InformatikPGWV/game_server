# Server Protokoll

## Generelles

- Es wird das Json-Format für die Datenübertragung verwendet.

- Ist Encodierung notwendig (Besipielsweise für Bilder), wird die Base-64 Kodierung verwendet

---

- da es sich um einen Broadcast Server handelt muss der Rezipient und der Absender bei Jeder Nachricht genannt werden


## Kodierung

```json
[
    "sender":"server|clientP1|clientP2",
    "reciever":"server|clientP1|clientP2",
    "timestamp":"timestamp in Unix millis",
    "data": {
        // Ab Hier Protokoll nach Spiel
    }
]

```

