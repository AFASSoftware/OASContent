# AFAS API Documentatie - Content Repository

Dit is de content repository van [docs.afas.help](https://docs.afas.help) – de plek waar alle AFAS API documentatie vandaan komt. Je vindt hier de ruwe markdown-bestanden, OpenAPI specs en voorbeelden die de basis vormen van onze API documentatie voor Profit en SB.

## Waarom is dit publiek?

We maken de documentatie openbaar zodat je actief kunt bijdragen. Zie je een fout? Mis je een voorbeeld? Kan een uitleg duidelijker? Dan kun je dat hier direct aanpassen. Daarnaast kun je deze content gebruiken om bijvoorbeeld je eigen LLM te voeden met accurate AFAS API kennis.

**Let op**: Dit is alleen de content. Wil je de documentatie lezen en gebruiken? Ga naar [docs.afas.help](https://docs.afas.help).

## Wat zit in deze repository?

### 📚 Documentatie (`markdownpages/`)
Alle markdown-bestanden met conceptuele uitleg, how-to's en releasenotes voor:
- **Profit API** - GetConnectors, UpdateConnectors, authenticatie, etc.
- **SB API** - Filtering, pagination, change tracking
- Beschikbaar in Nederlands én Engels

### 🔌 OpenAPI Specificaties (`OpenApiSpecs/`)
Complete technische specs met:
- Endpoint definities
- Request/response schemas
- Praktische voorbeelden

### 🗂️ Metadata (`menustructures/`)
Menu-structuren, redirects en navigatie-informatie

### 📷 Media (`media/`)
Afbeeldingen, diagrammen en visuele hulpmiddelen

### 🛠️ Scripts (`scripts/`)
Validatie- en verwerkingsscripts voor de content

## Hoe kun je bijdragen?

Dit is waar het interessant wordt. Jouw ervaring met de AFAS API is waardevol.

### 🐛 Fout gevonden in de documentatie?
Open een [issue](../../issues) en vertel ons:
- Op welke pagina (bijvoorbeeld `markdownpages/profit/nl/authentication.md`)
- Wat er niet klopt
- Hoe het zou moeten zijn

### 💡 Voorbeelden toevoegen?
Heb je een werkend voorbeeld van een integratie? Een slimme oplossing voor een veelvoorkomend probleem? Deel het!
- Voeg een nieuw how-to bestand toe
- Of voeg een voorbeeld toe aan bestaande documentatie

### 📝 Direct een fix maken?
1. Fork deze repository
2. Maak je wijzigingen in een feature branch
3. Houd je aan de [markdown naming conventions](scripts/README.md) (kebab-case)
4. Open een pull request
5. We kijken ernaar en geven feedback
6. Let op: voor aanpassingen aan documentatiepagina’s accepteren we wijzigingen alleen in `markdownpages/` (voor `OpenApiSpecs/`, `menustructures/`, `media/` of `scripts/`: open eerst een issue).

**Tip**: Begin klein. Een typo fix, een verduidelijking, een extra voorbeeld – het maakt allemaal verschil.

## Repository structuur

```
OASContent/
├── markdownpages/          # Alle content in Markdown
│   ├── profit/            # Profit API docs (NL + EN)
│   ├── sb/               # SB API docs (NL + EN)
│   └── endpoint/         # Endpoint-specifieke pagina's
├── OpenApiSpecs/          # Technische API specs
├── menustructures/        # Navigatie en redirects
├── media/                # Afbeeldingen
└── scripts/              # Validatie en tooling
```

## Voor wie is dit?

Deze repository is bedoeld voor:
- **API developers** die fouten tegenkomen of verbeteringen zien
- **System integrators** die voorbeelden willen delen
- **AFAS partners** die de documentatie willen verbeteren
- **AI/LLM developers** die training data nodig hebben

Je hoeft geen AFAS medewerker te zijn om bij te dragen. Community input maakt de documentatie beter voor iedereen.

## Belangrijke links

- 📖 **Documentatie lezen**: [docs.afas.help](https://docs.afas.help)
- 🧪 **API testen**: [connect.afas.nl](https://connect.afas.nl)
- 🤝 **Partner worden**: [partner.afas.nl](https://partner.afas.nl)
- 📚 **AFAS kennisbank**: [help.afas.nl](https://help.afas.nl)

## Veelgestelde vragen

**Kan ik deze content gebruiken voor mijn eigen project?**  
Ja, de content is publiek beschikbaar. Voor gebruik van de AFAS API zelf heb je wel een geldig AFAS abonnement nodig.

**Hoe snel worden wijzigingen doorgevoerd?**  
We bekijken pull requests regelmatig. Kleine fixes gaan vaak binnen een paar dagen live, grotere aanpassingen kunnen wat langer duren.

**Moet ik Nederlands én Engels aanpassen?**  
Idealiter wel, maar het is geen blokkade. We kunnen vertalingen ook intern afhandelen.

**Wie beslist wat er wordt gemerged?**  
Het AFAS API documentatie team beoordeelt alle voorstellen. We waarderen alle input, maar behouden ons het recht voor om aanpassingen te maken of af te wijzen als dat nodig is voor consistentie en kwaliteit.

---

**Over AFAS**: AFAS maakt software voor ondernemingen die hun administratie foutloos en automatisch willen laten verlopen. Wij bouwen software die werkt zoals het moet: makkelijk, slim en met de focus op wat écht belangrijk is. Zodat jij je kunt richten op je werk, je klanten en je mensen.
