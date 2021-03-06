import shapefile

class Lengkong:

    def __init__(self):
        self.kelurahan = shapefile.Writer(
            'kecamatan_lengkong', shapeType=shapefile.POLYGON)
        self.kelurahan.shapeType
        self.kelurahan.field('nama_kelurahan', 'C')

        self.kantor = shapefile.Writer(
            'kantor_lengkong', shapeType=shapefile.POINT)
        self.kantor.shapeType
        self.kantor.field('nama_kantor', 'C')

        self.jalan = shapefile.Writer(
            'jalan_lengkong', shapeType=shapefile.POLYLINE)
        self.jalan.shapeType
        self.jalan.field('nama_jalan', 'C')

        # Kelurahan
    def kelurahanBurangrang(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6175816,-6.9222478,0],
            [107.617367,-6.9252725,0],
            [107.6170666,-6.9263589,0],
            [107.6165946,-6.9285529,0],
            [107.6161869,-6.9297884,0],
            [107.6160581,-6.930438,0],
            [107.6157684,-6.9314924,0],
            [107.6154024,-6.9319746,0],
            [107.6161534,-6.9325817,0],
            [107.6164216,-6.9328266,0],
            [107.6166791,-6.9331781,0],
            [107.617001,-6.9334337,0],
            [107.6170439,-6.9335402,0],
            [107.6170439,-6.9336893,0],
            [107.6172585,-6.9338277,0],
            [107.6174301,-6.9340088,0],
            [107.617457,-6.934094,0],
            [107.6174945,-6.9342378,0],
            [107.6175589,-6.9343656,0],
            [107.6175803,-6.9344934,0],
            [107.6176447,-6.9346265,0],
            [107.6177413,-6.9347703,0],
            [107.6178593,-6.9351963,0],
            [107.6179022,-6.9354732,0],
            [107.618031,-6.9358779,0],
            [107.6180739,-6.9360004,0],
            [107.6180739,-6.9360643,0],
            [107.6181597,-6.9361974,0],
            [107.6185406,-6.9365329,0],
            [107.6189751,-6.9367619,0],
            [107.6192379,-6.9368152,0],
            [107.6193211,-6.9368178,0],
            [107.6196081,-6.9369004,0],
            [107.6196591,-6.936911,0],
            [107.6198361,-6.9364424,0],
            [107.6199487,-6.936059,0],
            [107.620276,-6.9356543,0],
            [107.6206944,-6.9352123,0],
            [107.6209251,-6.9350312,0],
            [107.6193365,-6.9333658,0],
            [107.6179846,-6.9318322,0],
            [107.6184353,-6.931534,0],
            [107.6186927,-6.9313636,0],
            [107.6192292,-6.9313849,0],
            [107.6195511,-6.9302985,0],
            [107.6197227,-6.9298938,0],
            [107.6195725,-6.9288927,0],
            [107.6194652,-6.9277637,0],
            [107.6194652,-6.9270821,0],
            [107.6195511,-6.9260596,0],
            [107.6197871,-6.9250585,0],
            [107.6198944,-6.9243129,0],
            [107.6199158,-6.9234609,0],
            [107.6197656,-6.9229923,0],
            [107.6194223,-6.9226514,0],
            [107.6175816,-6.9222478,0]
        ]])

    def kelurahanCijagra(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6196591,-6.936911,0],
            [107.619868,-6.9369543,0],
            [107.6199244,-6.9369836,0],
            [107.6199995,-6.9370022,0],
            [107.6200746,-6.9370182,0],
            [107.6201926,-6.9370395,0],
            [107.6203294,-6.9370821,0],
            [107.6204045,-6.9371487,0],
            [107.6204232,-6.9371993,0],
            [107.620434,-6.9372472,0],
            [107.6204367,-6.9373191,0],
            [107.6204393,-6.9373484,0],
            [107.6204273,-6.9373843,0],
            [107.6204246,-6.9374149,0],
            [107.6204004,-6.9374429,0],
            [107.6203736,-6.9374775,0],
            [107.6203455,-6.9374975,0],
            [107.6203294,-6.9375055,0],
            [107.6202784,-6.9374962,0],
            [107.6202415,-6.9375016,0],
            [107.6202201,-6.9375282,0],
            [107.6202952,-6.9377679,0],
            [107.620314,-6.9378105,0],
            [107.6203488,-6.9379063,0],
            [107.6205875,-6.93854,0],
            [107.6205983,-6.9387264,0],
            [107.620668,-6.9388861,0],
            [107.6207002,-6.9390299,0],
            [107.6208236,-6.9392216,0],
            [107.6209148,-6.939376,0],
            [107.6211186,-6.9396849,0],
            [107.6212956,-6.9398606,0],
            [107.6213386,-6.9400257,0],
            [107.6214029,-6.9401961,0],
            [107.621478,-6.9404517,0],
            [107.6215317,-6.9407552,0],
            [107.6217248,-6.9416232,0],
            [107.6217623,-6.9424699,0],
            [107.6216872,-6.9430184,0],
            [107.6216712,-6.9433273,0],
            [107.6215263,-6.9437107,0],
            [107.6214566,-6.9439769,0],
            [107.6212796,-6.9442592,0],
            [107.621242,-6.944371,0],
            [107.6213386,-6.9445201,0],
            [107.621639,-6.9446585,0],
            [107.6216926,-6.9448183,0],
            [107.6215853,-6.9450632,0],
            [107.6216497,-6.9453082,0],
            [107.6216604,-6.9454466,0],
            [107.6215424,-6.9455744,0],
            [107.6215961,-6.9460004,0],
            [107.6215639,-6.9461282,0],
            [107.621639,-6.946288,0],
            [107.6215961,-6.9464903,0],
            [107.6217355,-6.9468631,0],
            [107.6216819,-6.9471613,0],
            [107.6217033,-6.9475234,0],
            [107.6217677,-6.9478855,0],
            [107.6217677,-6.9482689,0],
            [107.6218535,-6.9486843,0],
            [107.6218857,-6.9489079,0],
            [107.6218965,-6.9490677,0],
            [107.6218965,-6.9492381,0],
            [107.6249971,-6.9494937,0],
            [107.6278295,-6.9494511,0],
            [107.6306619,-6.9489079,0],
            [107.6333441,-6.947992,0],
            [107.6298143,-6.9444136,0],
            [107.6264884,-6.9409203,0],
            [107.6229693,-6.9372566,0],
            [107.6209251,-6.9350312,0],
            [107.620371,-6.9355788,0],
            [107.6199487,-6.936059,0],
            [107.6196591,-6.936911,0]
        ]])

    def kelurahanCikawao(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6154024,-6.9319746,0],
            [107.6157684,-6.9314924,0],
            [107.6160581,-6.930438,0],
            [107.6163355,-6.9293238,0],
            [107.6165179,-6.9287594,0],
            [107.6133421,-6.9273748,0],
            [107.6130632,-6.9267571,0],
            [107.6124624,-6.9260328,0],
            [107.6117114,-6.9251595,0],
            [107.6116899,-6.9249465,0],
            [107.6117328,-6.9242222,0],
            [107.6118401,-6.9231998,0],
            [107.6120118,-6.9217726,0],
            [107.6087931,-6.9213253,0],
            [107.6086215,-6.9223264,0],
            [107.6087287,-6.9227951,0],
            [107.6093081,-6.9238175,0],
            [107.6095227,-6.9242648,0],
            [107.6096514,-6.9249465,0],
            [107.6104454,-6.9253299,0],
            [107.6105526,-6.9255642,0],
            [107.6103595,-6.9261393,0],
            [107.6099304,-6.9270553,0],
            [107.610102,-6.9275878,0],
            [107.6107243,-6.9280351,0],
            [107.6111535,-6.9282694,0],
            [107.6117757,-6.9286103,0],
            [107.6122907,-6.9290363,0],
            [107.613031,-6.9296008,0],
            [107.6132885,-6.9299416,0],
            [107.613546,-6.9302398,0],
            [107.6138142,-6.9305806,0],
            [107.6139751,-6.930751,0],
            [107.6143346,-6.9310226,0],
            [107.6146886,-6.9313048,0],
            [107.6149837,-6.9317362,0],
            [107.6150748,-6.9317628,0],
            [107.6154024,-6.9319746,0]
        ]])

    def kelurahanPaledang(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.612001,-6.9217833,0],
            [107.6116373,-6.9250911,0],
            [107.6130524,-6.9267678,0],
            [107.6133313,-6.9273855,0],
            [107.6165071,-6.9287701,0],
            [107.6165393,-6.9287019,0],
            [107.6170558,-6.9263696,0],
            [107.6173562,-6.9252832,0],
            [107.6174512,-6.9238985,0],
            [107.6175708,-6.9222585,0],
            [107.617183,-6.9223541,0],
            [107.6157239,-6.9222476,0],
            [107.612001,-6.9217833,0]
        ]])
    
    def kelurahanTurangga(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6333441,-6.947992,0],
            [107.6344077,-6.9476714,0],
            [107.6357917,-6.9472241,0],
            [107.6361243,-6.9471283,0],
            [107.6359741,-6.9468407,0],
            [107.6356093,-6.9460526,0],
            [107.635384,-6.9454988,0],
            [107.6350943,-6.9448066,0],
            [107.6350085,-6.9445084,0],
            [107.6349656,-6.9441569,0],
            [107.634869,-6.9438587,0],
            [107.6348368,-6.9423251,0],
            [107.634869,-6.9419736,0],
            [107.6345793,-6.941931,0],
            [107.6347403,-6.940866,0],
            [107.6346973,-6.9399927,0],
            [107.6347724,-6.9386934,0],
            [107.634751,-6.9376177,0],
            [107.6352499,-6.9377828,0],
            [107.6352499,-6.9375644,0],
            [107.6352284,-6.9375112,0],
            [107.6352284,-6.9374153,0],
            [107.6352713,-6.9372769,0],
            [107.6351211,-6.9371437,0],
            [107.6350782,-6.9351734,0],
            [107.6351211,-6.9347687,0],
            [107.6350997,-6.9347101,0],
            [107.6338498,-6.9344013,0],
            [107.6324336,-6.9342202,0],
            [107.6310066,-6.9340498,0],
            [107.6301054,-6.9337836,0],
            [107.6293115,-6.9335812,0],
            [107.6267258,-6.9329528,0],
            [107.62561,-6.9326546,0],
            [107.6257388,-6.9323777,0],
            [107.6224128,-6.9309719,0],
            [107.6221339,-6.9322286,0],
            [107.6219622,-6.9328676,0],
            [107.6217047,-6.9332723,0],
            [107.6203314,-6.9345078,0],
            [107.626125,-6.9405785,0],
            [107.6333441,-6.947992,0]
        ]])

    def kelurahanLingkarSelatan(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6350997,-6.9347101,0],
            [107.6356436,-6.9324493,0],
            [107.6358046,-6.9319115,0],
            [107.6366951,-6.9279708,0],
            [107.6341416,-6.9266076,0],
            [107.6323177,-6.925649,0],
            [107.6318671,-6.9255851,0],
            [107.6314594,-6.9255638,0],
            [107.6277687,-6.92452,0],
            [107.624314,-6.9238384,0],
            [107.6239277,-6.9252443,0],
            [107.6233269,-6.9275874,0],
            [107.6224042,-6.931166,0],
            [107.6257388,-6.9323777,0],
            [107.62561,-6.9326546,0],
            [107.6310066,-6.9340498,0],
            [107.6320817,-6.934212,0],
            [107.6335622,-6.9343824,0],
            [107.6350997,-6.9347101,0]
        ]])

    def kelurahanMalabar(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6203856,-6.9344563,0],
            [107.6215658,-6.9333806,0],
            [107.6217047,-6.9332723,0],
            [107.6219622,-6.9328676,0],
            [107.6223114,-6.9314795,0],
            [107.6225796,-6.9304783,0],
            [107.624314,-6.9238384,0],
            [107.624822,-6.9220751,0],
            [107.6248434,-6.9218407,0],
            [107.6242426,-6.9187094,0],
            [107.6175816,-6.9222478,0],
            [107.6194223,-6.9226514,0],
            [107.6197656,-6.9229923,0],
            [107.6199158,-6.9234609,0],
            [107.6198223,-6.924546,0],
            [107.6195863,-6.9259093,0],
            [107.6194652,-6.9270821,0],
            [107.6195434,-6.9286571,0],
            [107.6197227,-6.9298938,0],
            [107.6192292,-6.9313849,0],
            [107.6186927,-6.9313636,0],
            [107.6179846,-6.9318322,0],
            [107.6203856,-6.9344563,0]
        ]])

    # Kantor Kelurahan
    def kantorBurangrang(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.619467,-6.9298909)

    def kantorCijagra(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6262318,-6.9448688)

    def kantorCikawao(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6143362,-6.9287054)

    def kantorPaledang(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6164365,-6.928284)

    def kantorTurangga(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6312447,-6.9395021)

    def kantorLingkarSelatan(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6235179,-6.9306665)

    def kantorMalabar(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6226998,-6.920669)

    def kantorKecamatanLengkong(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6228089,-6.9283266)
        
    
    # Jalan
    def jalanLengkong(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6099852,-6.92157,0],
            [107.6097652,-6.9228161,0],
            [107.610468,-6.9228853,0],
            [107.6118466,-6.9230451,0],
            [107.6126996,-6.9231835,0],
            [107.6144591,-6.9234019,0],
            [107.6173559,-6.9237959,0],
            [107.6174471,-6.9238092,0],
            [107.6174578,-6.923117,0],
            [107.6175708,-6.9222585,0],
            [107.6186004,-6.9218123,0],
            [107.6213202,-6.9203478,0],
            [107.6241741,-6.9188141,0],
            [107.6242228,-6.9187925,0],
            [107.6243221,-6.9192292,0],
            [107.6243998,-6.9197564,0],
            [107.6244937,-6.9204434,0],
            [107.6245474,-6.9208854,0],
            [107.6246225,-6.9212981,0],
            [107.6247271,-6.9216709,0],
            [107.6247914,-6.9218945,0],
            [107.6247163,-6.9223126,0],
            [107.6245447,-6.9228877,0],
            [107.6242872,-6.9237397,0],
            [107.6235979,-6.9235613,0],
            [107.6227825,-6.9231886,0],
            [107.6219081,-6.922917,0],
            [107.62098,-6.9228797,0],
            [107.6199071,-6.9227253,0],
            [107.6175468,-6.9223871,0],
            [107.6155888,-6.9222593,0],
            [107.6135771,-6.9219984,0],
            [107.6120033,-6.9218022,0],
            [107.6118262,-6.9234025,0],
            [107.6116373,-6.9250911,0],
            [107.6119639,-6.9254916,0],
            [107.6125433,-6.9261546,0],
            [107.6130632,-6.9267571,0],
            [107.613128,-6.9269507,0],
            [107.6131092,-6.9273315,0],
            [107.6130717,-6.9282501,0],
            [107.6129322,-6.9294696,0],
            [107.6131253,-6.9295814,0],
            [107.6133399,-6.9298423,0],
            [107.6141338,-6.9302258,0],
            [107.6148741,-6.9304015,0],
            [107.6151853,-6.9303323,0],
            [107.6154213,-6.9301192,0],
            [107.6155608,-6.9302471,0],
            [107.6157003,-6.9303589,0],
            [107.6158826,-6.9304281,0],
            [107.6159792,-6.9304601,0],
            [107.6159041,-6.9308541,0],
            [107.6157163,-6.931376,0],
            [107.6155554,-6.9316689,0],
            [107.6156708,-6.9316369,0],
            [107.6156976,-6.9317062,0],
            [107.6157405,-6.9319325,0],
            [107.6158558,-6.9321748,0],
            [107.6160838,-6.9323452,0],
            [107.6163601,-6.9325955,0],
            [107.6166015,-6.9327978,0],
            [107.6169314,-6.9329949,0],
            [107.6174544,-6.9330987,0],
            [107.6181008,-6.9332478,0],
            [107.6182859,-6.9332984,0],
            [107.6182966,-6.9334795,0],
            [107.6183556,-6.9338842,0],
            [107.6184683,-6.9343475,0],
            [107.6187413,-6.9353745,0],
            [107.6189371,-6.9360188,0],
            [107.6191624,-6.9365007,0],
            [107.6193367,-6.9366339,0],
            [107.6196344,-6.936767,0],
            [107.6196881,-6.9367803,0],
            [107.6200019,-6.9368282,0],
            [107.6201414,-6.9368549,0],
            [107.6204311,-6.936964,0],
            [107.6207073,-6.9370306,0],
            [107.6208093,-6.9370785,0],
            [107.6208441,-6.9371291,0],
            [107.6208951,-6.9372489,0],
            [107.620904,-6.9372837,0],
            [107.6206304,-6.9373716,0],
            [107.6206196,-6.9374435,0],
            [107.6206974,-6.9377284,0],
            [107.6207967,-6.9379547,0],
            [107.6227292,-6.9369096,0],
            [107.6237591,-6.9380811,0],
            [107.6253792,-6.9397585,0],
            [107.6270368,-6.9414626,0],
            [107.6275786,-6.9421122,0],
            [107.6270207,-6.9444766,0],
            [107.6265272,-6.9467663,0],
            [107.6264199,-6.9472243,0],
            [107.6263877,-6.947416,0],
            [107.6264628,-6.9476503,0],
            [107.6265272,-6.9478313,0],
            [107.6265164,-6.9480656,0],
            [107.626554,-6.9483745,0],
            [107.6265808,-6.9484597,0],
            [107.6268598,-6.9484331,0],
            [107.6269456,-6.9483745,0],
            [107.6271119,-6.9477089,0],
            [107.6276537,-6.947842,0],
            [107.6277181,-6.9478207,0],
            [107.6278254,-6.9475012,0],
            [107.6282706,-6.9476343,0],
            [107.6292308,-6.9479964,0],
            [107.629322,-6.9480284,0],
            [107.6294132,-6.9479112,0],
            [107.6295259,-6.9478793,0],
            [107.6300784,-6.9479591,0],
            [107.6307758,-6.948071,0],
            [107.6310118,-6.9468888,0],
            [107.6310762,-6.9462392,0],
            [107.6313176,-6.9459463,0],
            [107.6328625,-6.9475012,0],
            [107.632892,-6.9472057,0],
            [107.6329001,-6.9467264,0],
            [107.6328894,-6.9464921,0],
            [107.6328679,-6.9463696,0],
            [107.6344397,-6.9452673,0],
            [107.6349064,-6.9450011,0],
            [107.6347723,-6.9446443,0],
            [107.6346435,-6.9441757,0],
            [107.6346382,-6.9440479,0],
            [107.6345416,-6.9429829,0],
            [107.6345201,-6.9422267,0],
            [107.6345232,-6.9421799,0],
            [107.6343609,-6.9421693,0],
            [107.6336193,-6.9420748,0],
            [107.6330372,-6.9419443,0],
            [107.6323533,-6.9417366,0],
            [107.6319563,-6.9416168,0],
            [107.6316451,-6.941497,0],
            [107.6318182,-6.9409688,0],
            [107.6317968,-6.9408783,0],
            [107.6310028,-6.9406599,0],
            [107.6300319,-6.9403511,0],
            [107.6303537,-6.93935,0],
            [107.6318236,-6.9400848,0],
            [107.6329179,-6.940841,0],
            [107.6341732,-6.9415013,0],
            [107.6342376,-6.941267,0],
            [107.6342912,-6.9409368,0],
            [107.6343771,-6.9392009,0],
            [107.6342608,-6.9391499,0],
            [107.6343145,-6.9383857,0],
            [107.6343359,-6.9376828,0],
            [107.6342179,-6.9373527,0],
            [107.6339443,-6.9369267,0],
            [107.6337405,-6.9366977,0],
            [107.6331987,-6.9366764,0],
            [107.6328768,-6.9366604,0],
            [107.632276,-6.9363143,0],
            [107.6323994,-6.935851,0],
            [107.6324423,-6.935212,0],
            [107.6325979,-6.9341895,0],
            [107.6343252,-6.9345144,0],
            [107.6348456,-6.9346155,0],
            [107.6350977,-6.9337635,0],
            [107.6352908,-6.9329701,0],
            [107.6354946,-6.9322405,0],
            [107.6356288,-6.9316441,0],
            [107.6356985,-6.9316814,0],
            [107.6359077,-6.9309571,0],
            [107.635901,-6.931025,0],
            [107.6359587,-6.9308999,0],
            [107.6360137,-6.9307455,0],
            [107.6360767,-6.9303993,0],
            [107.6361196,-6.9302715,0],
            [107.6361867,-6.9299919,0],
            [107.6363047,-6.9295819,0],
            [107.6363744,-6.9291745,0],
            [107.6364629,-6.9288364,0],
            [107.6364924,-6.9286952,0],
            [107.6365997,-6.9282453,0],
            [107.6366534,-6.9280349,0],
            [107.6359453,-6.9277101,0],
            [107.6356663,-6.928879,0],
            [107.6355805,-6.9292304,0],
            [107.6313211,-6.9280589,0],
            [107.6287248,-6.9274305,0],
            [107.6289179,-6.9265571,0],
            [107.6290037,-6.9260246,0],
            [107.6281883,-6.9257903,0],
            [107.627845,-6.9272388,0],
            [107.627727,-6.9273559,0],
            [107.6275875,-6.9279737,0],
            [107.6273407,-6.9289216,0],
            [107.6272201,-6.9289301,0],
            [107.6270163,-6.9296543,0],
            [107.6269411,-6.9298194,0],
            [107.6266783,-6.9308259,0],
            [107.626571,-6.9311614,0],
            [107.6264423,-6.9316673,0],
            [107.6264744,-6.9317684,0],
            [107.6275205,-6.93204,0],
            [107.6274669,-6.9323276,0],
            [107.6274722,-6.9324128,0],
            [107.6278638,-6.9325566,0],
            [107.6279014,-6.9325646,0],
            [107.6277565,-6.9331823,0],
            [107.6256698,-6.9326391,0],
            [107.6260775,-6.9311694,0],
            [107.6273339,-6.925989,0],
            [107.6270872,-6.9259251,0],
            [107.6265936,-6.9258505,0],
            [107.6258104,-6.9256481,0],
            [107.6257997,-6.9255523,0],
            [107.6250058,-6.9253073,0],
            [107.6247483,-6.9252221,0],
            [107.6244693,-6.9253073,0],
            [107.6239277,-6.9252443,0],
            [107.6238041,-6.9255523,0],
            [107.6234045,-6.927283,0],
            [107.6230424,-6.928625,0],
            [107.6209516,-6.9281084,0],
            [107.6201899,-6.9279699,0],
            [107.6194389,-6.9279912,0],
            [107.6194818,-6.9267345,0],
            [107.6196534,-6.9256481,0],
            [107.6198036,-6.9247535,0],
            [107.6199002,-6.9242103,0],
            [107.6198197,-6.9242263,0],
            [107.6196642,-6.9245085,0],
            [107.6193369,-6.9248866,0],
            [107.6189078,-6.9251635,0],
            [107.6184894,-6.9252221,0],
            [107.6180978,-6.9251529,0],
            [107.6173146,-6.9250996,0],
            [107.6171322,-6.9259144,0],
            [107.6169981,-6.9266706,0],
            [107.6168586,-6.9273256,0],
            [107.6166869,-6.9279007,0],
            [107.6164616,-6.928806,0],
            [107.6170952,-6.9290962,0],
            [107.6170737,-6.9293438,0],
            [107.6170388,-6.9297059,0],
            [107.6170603,-6.9303742,0],
            [107.6173178,-6.9310239,0],
            [107.6174948,-6.93137,0],
            [107.6180527,-6.9319505,0],
            [107.6185516,-6.9324883,0],
            [107.6187984,-6.9328238,0],
            [107.6193365,-6.9333658,0],
            [107.620059,-6.9341551,0],
            [107.6205525,-6.9346716,0],
            [107.6211534,-6.935316,0],
            [107.6219795,-6.9362213,0],
            [107.6222692,-6.9358166,0],
            [107.6225266,-6.9354118,0],
            [107.6228807,-6.9347515,0],
            [107.6233957,-6.9340273,0],
            [107.6222906,-6.9330581,0],
            [107.6205418,-6.9318227,0],
            [107.6204345,-6.9316949,0],
            [107.6211212,-6.9303742,0],
            [107.6197371,-6.9297991,0],
            [107.619646,-6.9292985,0],
            [107.6193187,-6.9294103,0],
            [107.6190612,-6.9295328,0],
            [107.6188359,-6.929208,0],
            [107.6187179,-6.9288778,0],
            [107.618734,-6.9287553,0],
            [107.6188735,-6.9281429,0],
            [107.6185784,-6.9282068,0],
            [107.6185382,-6.9280577,0],
            [107.6184068,-6.9279805,0],
            [107.6177684,-6.92785,0],
            [107.6182834,-6.9261353,0],
            [107.6185033,-6.9251981,0],
            [107.6182217,-6.9251768,0],
            [107.617873,-6.9251342,0],
            [107.6173205,-6.9251049,0],
            [107.617358,-6.9248839,0],
            [107.6171703,-6.9248785,0],
            [107.6168001,-6.9248572,0],
            [107.6166982,-6.9247933,0],
            [107.6165909,-6.9246922,0],
            [107.6165695,-6.9248253,0],
            [107.6164246,-6.9250969,0],
            [107.6163656,-6.9253312,0],
            [107.616312,-6.9255229,0],
            [107.6154376,-6.9254111,0],
            [107.6153839,-6.9262951,0],
            [107.6156307,-6.9263164,0],
            [107.6156951,-6.9266252,0],
            [107.6156521,-6.92703,0],
            [107.6154805,-6.9274986,0],
            [107.6151479,-6.9281589,0],
            [107.6158345,-6.9284252,0],
            [107.6157648,-6.9286222,0],
            [107.6156039,-6.928979,0],
            [107.6163495,-6.929176,0],
            [107.6162905,-6.9293624,0],
            [107.6160277,-6.9293624,0],
            [107.6157433,-6.929437,0],
            [107.6156253,-6.9297671,0],
            [107.6154107,-6.9300494,0],
            [107.6152713,-6.9299375,0],
            [107.6152284,-6.9297512,0],
            [107.615341,-6.9295328,0],
            [107.6148314,-6.929405,0],
            [107.6146383,-6.9293837,0],
            [107.6146865,-6.9292772,0],
            [107.6147295,-6.9286701,0],
            [107.6148207,-6.9284678,0],
            [107.6147348,-6.9283879,0],
            [107.6144344,-6.928292,0],
            [107.6145524,-6.927898,0],
            [107.6144559,-6.9278713,0],
            [107.6149119,-6.9266625,0],
            [107.6157702,-6.9268063,0],
            [107.6158506,-6.9269075,0],
            [107.6162583,-6.9268755,0],
            [107.6167733,-6.9269927,0],
            [107.6182592,-6.9274187,0],
            [107.6186079,-6.9275678,0],
            [107.6187796,-6.9274933,0],
            [107.6194465,-6.9275124,0],
            [107.6195538,-6.9285935,0],
            [107.6199025,-6.9285615,0],
            [107.6211202,-6.9286893,0],
            [107.6222306,-6.928897,0],
            [107.6223647,-6.9289449,0],
            [107.6224077,-6.9290408,0],
            [107.6222682,-6.9296585,0],
            [107.6221126,-6.9300313,0],
            [107.6218766,-6.9306117,0],
            [107.6218176,-6.9307129,0],
            [107.6223755,-6.9309153,0],
            [107.6228298,-6.9311118,0],
            [107.6225294,-6.9304089,0],
            [107.6227681,-6.9297965,0],
            [107.6231946,-6.9299163,0],
            [107.6235272,-6.9300468,0],
            [107.6238142,-6.930305,0],
            [107.6238759,-6.9301613,0],
            [107.6240851,-6.9293731,0],
            [107.6242245,-6.9289311,0],
            [107.624879,-6.9290696,0],
            [107.6250614,-6.9284625,0],
            [107.6257266,-6.9259224,0],
            [107.6259572,-6.9252567,0],
            [107.6262469,-6.9251395,0],
            [107.6274807,-6.9253952,0]
        ]])
    
    def close(self):
        self.kelurahan.close()
        self.kantor.close()
        self.jalan.close()

    


