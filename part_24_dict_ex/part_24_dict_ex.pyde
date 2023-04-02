
from __future__ import division

# This is a random extract from a wikipedia page on COVID-19
words = """The COVID-19 pandemic is an ongoing global pandemic of coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The novel virus was first identified from an outbreak in the Chinese city of Wuhan in December 2019, and attempts to contain it there failed, allowing it to spread across the globe. The World Health Organization (WHO) declared a Public Health Emergency of International Concern on 30 January 2020 and a pandemic on 11 March 2020. As of 31 December 2021, the pandemic had caused more than 286 million cases and 5.42 million deaths, making it one of the deadliest in history.
COVID-19 symptoms range from none to deadly. Severe illness is more likely in elderly patients and those with certain underlying medical conditions. COVID-19 is airborne, spread via air contaminated by microscopic virions (viral particles). The risk of infection is highest among people in close proximity, but can occur over longer distances, particularly indoors in poorly ventilated areas. Transmission rarely occurs via contaminated surfaces or fluids. Infected persons are typically contagious for 10 days, often beginning before or without symptoms.[6][7] Mutations produced many strains (variants) with varying degrees of infectivity and virulence.
COVID-19 vaccines have been approved and widely distributed in various countries since December 2020. Other recommended preventive measures include social distancing, masking, improving ventilation and air filtration, and quarantining those who have been exposed or are symptomatic. Treatments include monoclonal antibodies[8] and symptom control. Governmental interventions include travel restrictions, lockdowns, business restrictions and closures, workplace hazard controls, quarantines, testing systems, and tracing contacts of the infected.
The pandemic triggered severe social and economic disruption around the world, including the largest global recession since the Great Depression.[9] Widespread supply shortages, including food shortages, were caused by supply chain disruption and panic buying. The resultant near-global lockdowns saw an unprecedented pollution decrease. Educational institutions and public areas were partially or fully closed in many jurisdictions, and many events were cancelled or postponed. Misinformation circulated through social media and mass media, and political tensions intensified. The pandemic raised issues of racial and geographic discrimination, health equity, and the balance between public health imperatives and individual rights.
"""

BAR_WIDTH = 25 # The thickness of each bar
GAP_WIDTH = 10 # Gap between two bars
LETTERS = 26 # Num of letters
WIDTH = 500 # window width
MAX_BAR_LEN = WIDTH - 100 # The max length of each bar
LEGEND_POS = 25 # The position of the text
AXIS_POS = 50 # The position at which the bar starts

freq = {} # The frequency dict. The star of the show!

pos = 0 # position of current letter read from words
num_alphas = 0 # number of alphabets (for percentage)

# count the letters in the text. Return True if more letters are left, False if done.
def count():
    global pos, num_alphas

    # case insensitive. current letter.
    l = words[pos].upper()
    # count only if alphabet
    if l.isalpha():
        num_alphas = num_alphas + 1
        freq[l] = freq[l] + 1

    pos = pos + 1  # Read the next letter
    # print(pos, len(words), num_alphas, freq)
    return len(words) != pos

# draw the letters (The legend for the graph)
def drawLegend():
    textAlign(CENTER, CENTER)
    textSize(20)
    fill(0)
    push()
    translate(LEGEND_POS, BAR_WIDTH)
    for l in range(ord('A'), ord('Z') + 1):
        text(chr(l), 0, -5)
        translate(0, BAR_WIDTH + GAP_WIDTH)
    pop()

# draw the bar graph
def drawGraph():
    fill(0)
    push()
    translate(AXIS_POS, GAP_WIDTH)
    for l in range(ord('A'), ord('Z') + 1):
        fill(255, 0, 0)
        letter = chr(l)
        ratio = freq[letter]/num_alphas
        rect(0, 0, ratio*MAX_BAR_LEN, BAR_WIDTH)
        translate(0, BAR_WIDTH + GAP_WIDTH)
    pop()

# draw a green vertical progress bar at the right end
def drawProgress():
    fill(0, 255, 0)
    rect(width-10, 0, 10, height*pos/len(words))

# setup sketch
def setup():
    size(WIDTH, GAP_WIDTH + LETTERS * (BAR_WIDTH + GAP_WIDTH))
    for l in range(ord('A'), ord('Z') + 1):
        freq[chr(l)] = 0

# draw sketch
def draw():
    if not count():
        noLoop()

    background("#ccccff")
    drawLegend()
    drawGraph()
    drawProgress()
