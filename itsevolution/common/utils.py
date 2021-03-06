class Popcontrol:
    def __init__(self,dm,df,rhm,rhf):
        self.deathMale = dm
        self.deathFemale = df
        self.repHandcapMale = rhm
        self.repHandcapFemale = rhf

def startpops():

    pops = [None] * 120

    pops[0] = Popcontrol (0.006322,0.005313,1,1)
    pops[1] = Popcontrol (0.000396,0.000346,1,1)
    pops[2] = Popcontrol (0.000282,0.000221,1,1)
    pops[3] = Popcontrol (0.000212,0.000162,1,1)
    pops[4] = Popcontrol (0.000186,0.000131,1,1)
    pops[5] = Popcontrol (0.000162,0.000116,1,1)
    pops[6] = Popcontrol (0.000144,0.000106,1,1)
    pops[7] = Popcontrol (0.000129,0.000098,1,1)
    pops[8] = Popcontrol (0.000114,0.000091,1,1)
    pops[9] = Popcontrol (0.000100,0.000086,1,1)
    pops[10] = Popcontrol (0.000093,0.000084,1,1)
    pops[11] = Popcontrol (0.000101,0.000087,1,1)
    pops[12] = Popcontrol (0.000136,0.000100,1,1)
    pops[13] = Popcontrol (0.000205,0.000124,0,0)
    pops[14] = Popcontrol (0.000299,0.000157,0,0)
    pops[15] = Popcontrol (0.000401,0.000194,0,0)
    pops[16] = Popcontrol (0.000505,0.000232,0,0)
    pops[17] = Popcontrol (0.000620,0.000269,0,0)
    pops[18] = Popcontrol (0.000747,0.000304,0,0)
    pops[19] = Popcontrol (0.000879,0.000338,0,0)
    pops[20] = Popcontrol (0.001019,0.000373,0,0)
    pops[21] = Popcontrol (0.001151,0.000409,0,0)
    pops[22] = Popcontrol (0.001252,0.000442,0,0)
    pops[23] = Popcontrol (0.001309,0.000471,0,0)
    pops[24] = Popcontrol (0.001335,0.000497,0,0)
    pops[25] = Popcontrol (0.001349,0.000524,0,0)
    pops[26] = Popcontrol (0.001369,0.000553,0,0)
    pops[27] = Popcontrol (0.001391,0.000582,0,0)
    pops[28] = Popcontrol (0.001422,0.000611,0,0)
    pops[29] = Popcontrol (0.001459,0.000641,0,0)
    pops[30] = Popcontrol (0.001498,0.000673,0.1,0.4)
    pops[31] = Popcontrol (0.001536,0.000710,0.1,0.4)
    pops[32] = Popcontrol (0.001576,0.000753,0.1,0.4)
    pops[33] = Popcontrol (0.001616,0.000805,0.1,0.4)
    pops[34] = Popcontrol (0.001661,0.000864,0.1,0.4)
    pops[35] = Popcontrol (0.001716,0.000932,0.1,0.4)
    pops[36] = Popcontrol (0.001782,0.001005,0.1,0.4)
    pops[37] = Popcontrol (0.001854,0.001082,0.1,0.4)
    pops[38] = Popcontrol (0.001931,0.001160,0.1,0.4)
    pops[39] = Popcontrol (0.002018,0.001243,0.1,0.4)
    pops[40] = Popcontrol (0.002123,0.001336,0.1,0.4)
    pops[41] = Popcontrol (0.002252,0.001442,0.1,0.4)
    pops[42] = Popcontrol (0.002413,0.001562,0.1,0.4)
    pops[43] = Popcontrol (0.002611,0.001698,0.1,0.4)
    pops[44] = Popcontrol (0.002845,0.001849,0.1,0.4)
    pops[45] = Popcontrol (0.003109,0.002014,0.1,0.4)
    pops[46] = Popcontrol (0.003402,0.002195,0.2,0.8)
    pops[47] = Popcontrol (0.003736,0.002402,0.2,0.8)
    pops[48] = Popcontrol (0.004114,0.002639,0.2,0.8)
    pops[49] = Popcontrol (0.004533,0.002903,0.2,0.8)
    pops[50] = Popcontrol (0.004987,0.003189,0.2,0.8)
    pops[51] = Popcontrol (0.005473,0.003488,0.2,0.8)
    pops[52] = Popcontrol (0.005997,0.003795,0.2,0.8)
    pops[53] = Popcontrol (0.006560,0.004105,0.2,0.8)
    pops[54] = Popcontrol (0.007159,0.004423,0.2,0.8)
    pops[55] = Popcontrol (0.007803,0.004775,0.2,0.8)
    pops[56] = Popcontrol (0.008480,0.005153,0.2,0.8)
    pops[57] = Popcontrol (0.009170,0.005528,0.2,0.8)
    pops[58] = Popcontrol (0.009863,0.005893,0.2,0.8)
    pops[59] = Popcontrol (0.010572,0.006266,0.2,0.8)
    pops[60] = Popcontrol (0.011354,0.006688,0.2,0.8)
    pops[61] = Popcontrol (0.012202,0.007176,0.6,1)
    pops[62] = Popcontrol (0.013061,0.007724,0.6,1)
    pops[63] = Popcontrol (0.013920,0.008339,0.6,1)
    pops[64] = Popcontrol (0.014819,0.009034,0.6,1)
    pops[65] = Popcontrol (0.015826,0.009832,0.6,1)
    pops[66] = Popcontrol (0.016986,0.010740,0.6,1)
    pops[67] = Popcontrol (0.018295,0.011754,0.6,1)
    pops[68] = Popcontrol (0.019776,0.012881,0.6,1)
    pops[69] = Popcontrol (0.021448,0.014141,0.6,1)
    pops[70] = Popcontrol (0.023380,0.015612,0.6,1)
    pops[71] = Popcontrol (0.025549,0.017275,0.6,1)
    pops[72] = Popcontrol (0.027885,0.019047,0.6,1)
    pops[73] = Popcontrol (0.030374,0.020909,0.6,1)
    pops[74] = Popcontrol (0.033099,0.022939,0.6,1)
    pops[75] = Popcontrol (0.036254,0.025297,0.6,1)
    pops[76] = Popcontrol (0.039882,0.028045,0.6,1)
    pops[77] = Popcontrol (0.043879,0.031131,0.6,1)
    pops[78] = Popcontrol (0.048256,0.034582,0.6,1)
    pops[79] = Popcontrol (0.053123,0.038467,0.6,1)
    pops[80] = Popcontrol (0.058711,0.043008,0.6,1)
    pops[81] = Popcontrol (0.065081,0.048175,0.6,1)
    pops[82] = Popcontrol (0.072139,0.053772,0.6,1)
    pops[83] = Popcontrol (0.079912,0.059770,0.6,1)
    pops[84] = Popcontrol (0.088529,0.066367,0.6,1)
    pops[85] = Popcontrol (0.098148,0.073828,0.6,1)
    pops[86] = Popcontrol (0.108902,0.082382,0.6,1)
    pops[87] = Popcontrol (0.120886,0.092183,0.6,1)
    pops[88] = Popcontrol (0.134149,0.103305,0.6,1)
    pops[89] = Popcontrol (0.148699,0.115746,0.6,1)
    pops[90] = Popcontrol (0.164525,0.129475,0.6,1)
    pops[91] = Popcontrol (0.181600,0.144443,0.6,1)
    pops[92] = Popcontrol (0.199884,0.160590,0.6,1)
    pops[93] = Popcontrol (0.219331,0.177853,0.6,1)
    pops[94] = Popcontrol (0.239886,0.196165,0.6,1)
    pops[95] = Popcontrol (0.260269,0.214677,0.6,1)
    pops[96] = Popcontrol (0.280109,0.233091,0.6,1)
    pops[97] = Popcontrol (0.299013,0.251082,0.6,1)
    pops[98] = Popcontrol (0.316578,0.268304,0.6,1)
    pops[99] = Popcontrol (0.332406,0.284403,0.6,1)
    pops[100] = Popcontrol (0.349027,0.301467,0.6,1)
    pops[101] = Popcontrol (0.366478,0.319555,0.6,1)
    pops[102] = Popcontrol (0.384802,0.338728,0.6,1)
    pops[103] = Popcontrol (0.404042,0.359052,0.6,1)
    pops[104] = Popcontrol (0.424244,0.380595,0.6,1)
    pops[105] = Popcontrol (0.445456,0.403431,0.6,1)
    pops[106] = Popcontrol (0.467729,0.427637,0.6,1)
    pops[107] = Popcontrol (0.491116,0.453295,0.6,1)
    pops[108] = Popcontrol (0.515671,0.480492,0.6,1)
    pops[109] = Popcontrol (0.541455,0.509322,0.6,1)
    pops[110] = Popcontrol (0.568528,0.539881,0.6,1)
    pops[111] = Popcontrol (0.596954,0.572274,0.6,1)
    pops[112] = Popcontrol (0.626802,0.606611,0.6,1)
    pops[113] = Popcontrol (0.658142,0.643007,0.6,1)
    pops[114] = Popcontrol (0.691049,0.681588,0.6,1)
    pops[115] = Popcontrol (0.725602,0.722483,0.6,1)
    pops[116] = Popcontrol (0.761882,0.761882,0.6,1)
    pops[117] = Popcontrol (0.799976,0.799976,0.6,1)
    pops[118] = Popcontrol (0.839975,0.839975,0.6,1)
    pops[119] = Popcontrol (0.881973,0.881973,0.6,1)

    return pops
