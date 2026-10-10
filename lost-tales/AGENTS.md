# Verbindliche Arbeitsanweisungen für Codex

Diese Anweisungen gelten für die Arbeit an der Comicserie „Lost Tales from the Dystopia“ im Verzeichnis `lost-tales/` und seinen Unterverzeichnissen.

## Arbeitsweise und Projektkanon

- GitHub ist die maßgebliche Quelle des Projektkanons. Arbeite auf Grundlage der aktuellen kanonischen Quelldateien im Repository `kollmeier/DieDystopie`.
- Lies vor redaktionellen Änderungen `lost-tales/README.md`, `lost-tales/RULES.md`, `lost-tales/THEMES.md` und `lost-tales/LORE-GUARD.md`.
- Berücksichtige bei Bedarf zusätzlich die README- und Dialogdateien der betroffenen Strips, Figuren und Orte.
- Erfinde keine kanonischen Fakten, Figurenmerkmale, Beziehungen oder Handlungen. Stelle unbelegte Annahmen nicht als Kanon dar.
- Dokumentiere Widersprüche mit Verweisen auf die betroffenen Quellen, statt sie eigenmächtig aufzulösen. Beachte dabei den jeweils erlaubten Änderungsumfang; wenn keine passende Datei geändert werden darf, dokumentiere den Widerspruch im Pull Request.
- Respektiere die Regeln zur Eigenständigkeit gegenüber fremden Werken aus `RULES.md` und `LORE-GUARD.md`. Übernimm keine geschützten Namen, Figuren oder Organisationen, schreibe keine fremde Lore fort und verwende keine ikonischen Figuren als Ersatz oder Variante. Allgemeine Genre-Motive dürfen nur im Rahmen dieser Regeln verwendet werden.

## Kontextpflege: Projektbriefing aktualisieren

Wenn der Nutzer dazu auffordert, das Projektbriefing zu aktualisieren:

1. Vergleiche `lost-tales/context-briefing.md` mit den aktuellen kanonischen Quelldateien auf GitHub. Lies dazu die oben genannten Grundlagen sowie die für das Briefing relevanten README- und Dialogdateien der Strips, Figuren und Orte.
2. Ergänze neue relevante Informationen und korrigiere veraltete Aussagen ausschließlich anhand dieser Quellen. Dokumentiere erkannte Widersprüche, ohne sie eigenmächtig aufzulösen.
3. Halte das Briefing kompakt, gut strukturiert und für ChatGPT als Einstieg verständlich.
4. Verändere ausschließlich `lost-tales/context-briefing.md`.
5. Verändere weder `lost-tales/context-index.md` noch `lost-tales/context.md`. Diese Dateien werden durch GitHub Actions erzeugt.
6. Nimm keine eigenständigen Kanonänderungen vor.

## Git-Workflow

- Arbeite auf einem separaten Branch.
- Prüfe vor dem Commit den Diff und stelle sicher, dass nur die für den Auftrag erlaubten Dateien geändert wurden.
- Erstelle einen Pull Request zur Prüfung und beschreibe die Änderungen sowie gegebenenfalls festgestellte Widersprüche.
- Merge Änderungen nicht eigenständig nach `main`.
