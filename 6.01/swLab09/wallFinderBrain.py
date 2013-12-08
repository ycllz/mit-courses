from lib601.plotWindow import PlotWindow as pw
from soar.io import io

#replace with your data
data = {'distances': [-0.001, -0.001, 0.002, 0.009000000000000001, 0.019000000000000003, 0.029000000000000012, 0.03900000000000002, 0.04900000000000003, 0.06100000000000004, 0.06900000000000005, 0.07900000000000006, 0.08900000000000007, 0.10100000000000008, 0.10900000000000008, 0.11900000000000009, 0.1290000000000001, 0.1410000000000001, 0.1490000000000001, 0.1590000000000001, 0.16900000000000012, 0.18100000000000013, 0.18900000000000014, 0.19900000000000015, 0.20900000000000016, 0.22100000000000017, 0.22900000000000018, 0.23900000000000018, 0.2490000000000002, 0.2610000000000002, 0.2690000000000002, 0.2790000000000002, 0.2890000000000002, 0.3010000000000002, 0.3090000000000002, 0.31900000000000023, 0.32900000000000024, 0.34100000000000025, 0.34900000000000025, 0.35900000000000026, 0.36900000000000027, 0.3810000000000003, 0.3890000000000003, 0.3990000000000003, 0.4090000000000003, 0.4210000000000003, 0.4290000000000003, 0.43900000000000033, 0.44900000000000034, 0.46100000000000035, 0.46900000000000036, 0.47900000000000037, 0.4890000000000004, 0.5010000000000003, 0.5090000000000003, 0.5190000000000003, 0.5290000000000004, 0.5410000000000004, 0.5490000000000004, 0.5590000000000004, 0.5690000000000004, 0.5810000000000004, 0.5910000000000004, 0.5990000000000004, 0.6090000000000004, 0.6210000000000004, 0.6310000000000004, 0.6390000000000005, 0.6490000000000005, 0.6610000000000005, 0.6710000000000005, 0.6790000000000005, 0.6890000000000005, 0.7010000000000005, 0.7110000000000005, 0.7190000000000005, 0.7290000000000005, 0.7410000000000005, 0.7510000000000006, 0.7590000000000006, 0.7690000000000006, 0.7810000000000006, 0.7910000000000006, 0.7990000000000006, 0.8090000000000006, 0.8210000000000006, 0.8310000000000006, 0.8390000000000006, 0.8490000000000006, 0.8610000000000007, 0.8710000000000007, 0.8790000000000007, 0.8890000000000007, 0.9010000000000007, 0.9110000000000007, 0.9180000000000007, 0.9290000000000007, 0.9410000000000007, 0.9510000000000007, 0.9610000000000007, 0.9690000000000007, 0.9800000000000008, 0.9910000000000008, 1.0010000000000008, 1.0090000000000006, 1.0200000000000005, 1.03, 1.041, 1.0479999999999998, 1.0609999999999995, 1.0709999999999993, 1.0799999999999992, 1.088999999999999, 1.1009999999999989, 1.1109999999999987, 1.1199999999999986, 1.1279999999999983, 1.140999999999998, 1.1499999999999977, 1.1599999999999977, 1.1679999999999977, 1.1799999999999977, 1.1899999999999975, 1.1999999999999975, 1.2079999999999975, 1.2199999999999975, 1.2299999999999975, 1.2399999999999975, 1.2489999999999974, 1.2599999999999973, 1.2699999999999974, 1.279999999999997, 1.287999999999997, 1.299999999999997, 1.3109999999999966, 1.3199999999999965, 1.3279999999999963, 1.3399999999999963, 1.3499999999999963, 1.3599999999999963, 1.3679999999999963, 1.3799999999999963, 1.3899999999999963, 1.3999999999999964, 1.4079999999999964, 1.4199999999999964, 1.4299999999999964, 1.4399999999999964, 1.4479999999999964, 1.4599999999999964, 1.4699999999999964, 1.4799999999999964, 1.4899999999999964, 1.4999999999999964, 1.5099999999999965, 1.5189999999999964, 1.5269999999999961, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957, 1.5309999999999957], 'voltages': [9.325513196480939, 9.305962854349952, 9.305962854349952, 9.325513196480939, 9.345063538611926, 9.345063538611926, 9.335288367546433, 9.335288367546433, 9.345063538611926, 9.345063538611926, 9.335288367546433, 9.345063538611926, 9.335288367546433, 9.315738025415445, 9.315738025415445, 9.345063538611926, 9.16911045943304, 8.172043010752688, 7.253176930596285, 6.5982404692082115, 5.806451612903226, 5.425219941348973, 4.926686217008798, 4.447702834799609, 4.027370478983382, 3.7829912023460412, 3.5483870967741935, 3.294232649071359, 3.0009775171065494, 2.8347996089931575, 2.6881720430107525, 2.5219941348973607, 2.346041055718475, 2.228739002932551, 2.101661779081134, 1.9745845552297165, 1.847507331378299, 1.76930596285435, 1.710654936461388, 1.6226783968719452, 1.5151515151515151, 1.466275659824047, 1.3880742913000979, 1.3294232649071358, 1.270772238514174, 1.2218963831867058, 1.1730205278592376, 1.1241446725317692, 1.075268817204301, 1.04594330400782, 1.0068426197458455, 0.9872922776148583, 0.9384164222873901, 0.9090909090909091, 0.8797653958944281, 0.8504398826979472, 0.8211143695014663, 0.8113391984359726, 0.7820136852394917, 0.7526881720430108, 0.7331378299120235, 0.7233626588465298, 0.7135874877810362, 0.7038123167155426, 0.6842619745845552, 0.6647116324535679, 0.6549364613880743, 0.635386119257087, 0.6256109481915934, 0.6060606060606061, 0.6060606060606061, 0.5865102639296188, 0.5767350928641252, 0.5571847507331378, 0.5571847507331378, 0.5376344086021505, 0.5278592375366569, 0.5180840664711632, 0.5083088954056696, 0.49853372434017595, 0.4887585532746823, 0.4789833822091887, 0.4789833822091887, 0.45943304007820135, 0.45943304007820135, 0.4398826979472141, 0.4398826979472141, 0.43010752688172044, 0.4203323558162268, 0.4203323558162268, 0.41055718475073316, 0.41055718475073316, 0.40078201368523947, 0.39100684261974583, 0.39100684261974583, 0.3812316715542522, 0.3812316715542522, 0.3812316715542522, 0.37145650048875856, 0.3812316715542522, 0.37145650048875856, 0.37145650048875856, 0.37145650048875856, 0.3616813294232649, 0.3616813294232649, 0.3519061583577713, 0.3616813294232649, 0.3519061583577713, 0.3519061583577713, 0.3519061583577713, 0.3519061583577713, 0.3519061583577713, 0.3519061583577713, 0.3519061583577713, 0.3519061583577713, 0.3421309872922776, 0.3421309872922776, 0.3421309872922776, 0.3421309872922776, 0.3421309872922776, 0.3421309872922776, 0.3421309872922776, 0.3421309872922776, 0.3421309872922776, 0.3421309872922776, 0.3421309872922776, 0.3421309872922776, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.3421309872922776, 0.33235581622678395, 0.33235581622678395, 0.3421309872922776, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.3225806451612903, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.33235581622678395, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3128054740957967, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903, 0.3225806451612903]}

def distanceFromVoltage(v):
    voltages = data['voltages']
    for i in xrange(len(voltages)-1):
        if voltages[i] >= v and v > voltages[i+1]:
            proportion = float(voltages[i] - v) / (voltages[i] - voltages[i+1])
            return data['distances'][i] + proportion*(data['distances'][i+1] - data['distances'][i])
    return data['distances'][-1]

# this function is called 10 times per second
def step():
    distance = distanceFromVoltage(io.getAnalogInputs()[0])
    print io.getSonars()[3], distance
    io.setForward((distance-0.5)*2) #replace with your code