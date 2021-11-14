
import machine

text = """
En bra svampsäsong letar sig många ut i skogen. Men svamparna vi plockar är bara toppen på isberget. Den som lär sig läsa svamparnas underjordiska atlas kan också förutspå var kantarellerna kommer att titta fram.

På flera håll i landet är det ett riktigt karljohanår i år och bilderna på fulla svampkorgar är många i sociala medier. Anders Dahlberg, professor i mykologi vid Sveriges lantbruksuniversitet, tror att det handlar om instinkten att samla kombinerat med en tävlingsinstinkt eller känsla av skattjakt.

– Man kan bli duktigare på att hitta svamp, det är absolut lite av en sport. Jag har också sett att intresset för svamp har vuxit väldigt de senaste åren. Till den grundkurs i mykologi som jag håller i på universitetet har vi 500 sökande till 30 platser.

I boken ”Svamparnas förunderliga liv” går han tillsammans med journalisten Anna Froster igenom naturens kanske viktigaste kugge – svamparna. De tar kantarellen, karljohansvampen, röksvampen och ytterligare ett antal svampar till hjälp för att visa på det enorma arbete som pågår bakom kulisserna – under jorden. Det handlar om promiskuösa murklor och onda parasiter.

– Syns man inte så finns man inte, och det gäller i högsta grad i naturen. Vi ser träd och iögonfallande växter. Men det mikroskopiska livet som är så mycket mer sett till både biomassa och aktivitet, det behöver vi lära oss att se.

– Jag skulle önska att fler fick en förståelse för svamparnas betydelse. Svamparna är allt annat än kusinen från landet som får armbåga sig in för att få vara med på ett hörn – de spelar en av huvudrollerna i naturen.

Ett kaninhål ner i underlandet
Anders DahlbergAnders Dahlberg, professor i mykologi. Foto: Johan Samuelsson
Den viktigaste delen av svampen är inte det vi ser utan de många tunna, underjordiska trådar, hyfer, som tillsammans bildar svampens mycel. Mycelet är svampens kropp, som växer fram under jorden och bryter ner och äter det som kommer i dess väg.

Anders Dahlberg beskriver varje svamphatt som ett kaninhål ner i underlandet, där varje kvadratmeter rymmer många hundratusentals meter svamptrådar, en fortfarande relativt outforskad värld. Vetenskapen känner i dag till ungefär fem procent av alla svamparter som finns.

I ”Svamparnas förunderliga liv” berättar Anders Dahlberg om två brittiska forskare som i en vanlig mataffär köpte en påse torkad svamp från Kina och DNA-analyserade de 15 svampbitarna. Bitarna visade sig vara från tre olika arter – alla nya för vetenskapen.

En relativt ny företeelse
Anders Dahlberg och hans kollegor har använt liknande DNA-teknik för att analysera prover från 1 500 av de skogar som ingår i den så kallade Markinventeringen, som ska visa hur marken i svenska skogar mår. Varje matsked skogsjord rymmer omkring 100 svamparter och de har bland annat kunnat konstatera att Sveriges vanligaste svamp är den lilla nedbrytande Penicillium spinnulosum. Ovan mark är den vanligaste svampen en skinnsvamp och tillika mykorrhizasvamp, som syns som ett vitt ludd på undersidan av fallna träd.

– Vi håller på att få en bra bild av vilka svampar som finns i marken och tittar samtidigt på hur deras förekomst korrelerar till skogens egenskaper, markens kolinlagring, hur träden har vuxit med mera. Det är kunskap som kan få stor betydelse för skogsskötseln, säger Anders Dahlberg.

Möjligen hänger den begränsade kunskapen om svampar ihop med att det svampintresse som Anders Dahlberg vittnar om är en relativt ny företeelse. Länge var mykofobi, svampfobi, ett relevant begrepp för att beskriva svenskarnas förhållande till svamp. Carl von Linne kallade till exempel svamparna för en motbjudande röra och ”Floras strövande pack”. Så småningom blev det en delikatess för överklassen, men först på 1970-talet vaknade intresset för svampplockning på allvar.

En sport som går att lära sig
I dag lockar svampletandet allt fler, och det är en sport som går att lära sig, säger Anders Dahlberg. Men någon quickfix finns inte, det handlar om att läsa av träd, miljö och väderlek. Är det mykorrhizasvampar, som de allra flesta av våra matsvampar är, måste träden finnas där. Är det torrt letar man där det är fuktigt, har det regnat mycket går man där det vanligtvis är torrt.

– Alla kan lära sig, absolut. Men det är komplext att förklara och svårt att ge konkreta, säkra råd. Det är som att headhunta till ett fotbollslag: var hittar jag talangerna? Miljön ska vara rätt, förutsättningarna ska vara rätt – då finns de där. Ibland.

Det vi ger oss ut på jakt efter i höstsolen är svampens fruktkropp, den lilla del av svampen som ibland dyker upp ovan jord. Men för svampen spelar det ingen roll om de bildar fruktkroppar eller inte. Är inte väderleken den rätta väntar de bara – och de kan vänta länge.

– Oavsett om vi hittar svamp eller inte så tror jag att svamparna är en bra ingång för att uppleva komplexiteten i naturen. Att lära sig mer om dem kan ge en fiktiv känsla av att man förstår hur det hänger ihop."""
keywords = machine.run(text, 'all')
print(keywords)