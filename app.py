import os
from flask import Flask,request, jsonify, render_template
import machine


template_dir = os.path.abspath('.')
app = Flask(__name__,template_folder=template_dir)
@app.route('/', methods = ['POST', 'GET'])
def runKeyword():
    text = """
    Inte sedan 1979 och 1993 har det varit så få sorkar i norra Sverige. I fjälltrakterna är dessutom lämlarna ovanligt få. I Västmanland är det däremot ett riktigt sorkår. Det visar resultaten från årets miljöövervakning av smågnagare.

    Sork och lämmel är en basföda för rovfåglar och ugglor och en av arterna som påverkas av årets små populationer i fjälltrakterna är pärlugglan.

    – I Ammarnäs och Vindelnområdet bedriver vi också miljöövervakning av pärlugglor, där vi inventerar ugglornas häckningsframgång i holkar. Som förväntat har vårens låga tätheter av lämlar och sorkar resulterat i mycket dålig häckningsframgång för ugglorna i dessa områden, säger Frauke Ecke, ansvarig för övervakningen av smågnagare, i ett pressmeddelande.

    Sveriges nationella miljöövervakning av smågnagare utförs av Sveriges lantbruksuniversitet på uppdrag av Naturvårdsverket. En vecka efter midsommar inventeras fjällämlar i tre områden i Vålådalen/Ljungdalen, Ammarnäs och Stora Sjöfallet. Sork inventeras även i bland annat Vindelnområdet i Västerbotten och i Västmanland. Under fältinventeringen i fjällområdena påträffades inte en enda fjällämmel.

    – Senaste gången vi hade ett riktigt lämmelår var år 2011 och det ser tyvärr ut att dröja innan vi får uppleva ett riktigt lämmelår igen. Det låga antalet som vi ser nu är en naturlig del av vad vi kallar för sorkcykler. Att bygga upp en stor population från årets låga antal kommer att ta cirka tre år, säger Frauke Ecke.

    Om det är ett sorkår eller inte beror alltså på var i landet vi befinner oss. I Västmanland är årets sorkpopulation den tredje största sedan övervakningen startade 1973. Sork- och lämmelpopulationerna påverkar inte bara ugglor och rovfåglar. Ett toppår för sork syns tydligt i till exempel rävstammen, både samma år och året efter. Under ett bra sorkår minskar också rävens predation på exempelvis hare, orre och tjäder.
    """
    keywords = machine.run(text)
    return jsonify(keywords)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)