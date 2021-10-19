import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def training_loss():
    origin_iid_loss =[2.2335814559459686, 1.8632041013240812, 1.5188239312171936, 1.3798128098249438, 1.3075912612676621, 1.2262678635120392, 1.1802763921022417, 1.148407055735588, 1.0981623762845993, 1.0591661477088927, 1.0947851306200025, 1.0081277668476105, 0.9997859632968902, 0.9889611554145812, 0.9740384036302567, 0.9595105314254762, 0.9325663542747498, 0.9514110332727432, 0.9531751164793969, 0.9293372672796251, 0.9383069968223572, 0.9242871761322023, 0.888032984137535, 0.9206940528750419, 0.9193492284417154, 0.9033610352873801, 0.9047738325595855, 0.8994774371385574, 0.8775495767593384, 0.8882526397705078, 0.9257829618453979, 0.8878797620534897, 0.8886062252521516, 0.9302747240662574, 0.8715812528133393, 0.8894424971938133, 0.9007302778959275, 0.9016015726327895, 0.852920970916748, 0.8844267895817758, 0.9102232944965364, 0.9034761327505111, 0.9018634703755379, 0.9078845018148423, 0.9097233682870864, 0.8601839137077331, 0.90618928283453, 0.8703093892335891, 0.907135917544365, 0.9012112003564834, 0.8601828128099441, 0.8834898528456687, 0.9269638586044312, 0.9062034732103348, 0.860696674287319, 0.8941725981235503, 0.901996577978134, 0.8676821592450141, 0.8997173973917961, 0.8865058341622353, 0.8847835674881935, 0.9393755024671556, 0.8742124700546265, 0.911891478896141, 0.9073184782266617, 0.8876333719491958, 0.9028285974264143, 0.9129920065402984, 0.9158646523952484, 0.9041012993454933, 0.8947273343801498, 0.8903826639056206, 0.8694478225708007, 0.860962418615818, 0.9238360139727593, 0.918233204483986, 0.9094766026735306, 0.9266207760572434, 0.8970434457063673, 0.8937919586896899, 0.9088117241859436, 0.9081643378734588, 0.8855193197727204, 0.882602712213993, 0.9054904985427857, 0.8731005099415778, 0.9283861845731736, 0.9059635159373285, 0.9222889131307603, 0.88104218095541, 0.9025937166810035, 0.8895552656054496, 0.908658435344696, 0.8990200400352479, 0.8623596546053885, 0.889912848174572, 0.898641658127308, 0.9284055361151695, 0.879149715900421, 0.9362438452243804, 0.947031766474247, 0.9068357056379318, 0.9178813087940216, 0.8939455187320708, 0.9342558920383454, 0.889422689974308, 0.9337815555930137, 0.9285100749135019, 0.9181806838512419, 0.9186752715706825, 0.9045779773592949, 0.9169836476445198, 0.9082841944694519, 0.926353020966053, 0.930959621667862, 0.8879525744915009, 0.9409694111347198, 0.9298219197988511, 0.9163670149445533, 0.9516673690080643, 0.9576934394240377, 0.9244109103083609, 0.8970300662517549, 0.9164438202977181, 0.9295454365015029, 0.921479313969612, 0.9316262635588645, 0.9199108219146728, 0.9015535864233971, 0.9511293387413025, 0.9301204550266267, 0.9489481374621391, 0.9259846794605254, 0.8766164860129357, 0.9307372474670409, 0.9541184210777282, 0.9288982415199278, 0.9848882153630255, 0.9689805626869201, 0.9286060363054276, 0.9249047768115999, 0.933505811393261, 0.8901627260446547, 0.9218287259340286, 0.9213928937911987, 0.9372671765089035, 0.9420858705043791, 0.9163173291087151, 0.9868366125226021, 0.9405056190490722, 0.9299770647287369, 0.8892492485046386, 0.9175627917051316, 0.9571460679173469, 0.8962996160984039, 0.9032242283225059, 0.9278547304868698, 0.9420628523826599, 0.9550413063168527, 0.9423372837901116, 0.9110261261463167, 0.9198175224661826, 0.9902707144618035, 0.9356437158584596, 0.9573623251914978, 0.9282956537604333, 0.9101656144857406, 0.9348171156644822, 0.914874289929867, 0.979145993590355, 0.9143828603625297, 0.9592174035310747, 0.9397075867652894, 0.9129045596718788, 0.9442719188332559, 0.890720111131668, 0.9509490513801573, 0.9220333886146544, 0.9270931816101073, 0.9247326374053955, 1.00027703166008, 0.9508195957541465, 0.8986762028932571, 0.947326608002186, 0.9179374071955679, 0.953064469695091, 0.9178862810134888, 0.9240432193875314, 0.9405742999911307, 0.9372787934541703, 0.9587094628810882, 0.9341649132966994, 0.9491420879960062, 0.9241767072677612, 0.929336571097374, 0.8895401096343992, 0.933271143734455, 0.92785721629858, 0.9275834527611734, 0.9329814171791077]

    origin_non_iid_loss =[0.9813795438408851, 0.8683447862197877, 0.8982822786493383, 0.9771862781274943, 0.6678008688767307, 0.866442856917389, 0.428970727459369, 0.8688611254449212, 1.0515062451593986, 0.9213714116759615, 0.7739218845194025, 0.6770857502628281, 0.7155056302254524, 0.4969428959376316, 1.3966606537438753, 0.6529798512809794, 0.5554485494516179, 0.7516278180992231, 0.5140930099412799, 0.8605678945548881, 0.9737645479291677, 0.8054660256676289, 0.81627737742092, 0.4262765661384401, 0.5620245044857074, 0.6070704275697062, 0.6951437165758414, 0.585504409302031, 0.7196523876930587, 0.5129563173593488, 0.48829492881965847, 0.4118179264866285, 0.6495750416829406, 0.6656810967526996, 0.463342853095171, 0.49991978425359995, 0.5677729468687148, 0.58422698815893, 0.5711584453140972, 0.7057014764496125, 0.429314254093601, 0.5651203729924271, 0.5746436328822164, 0.45396421680856724, 0.817114919559681, 0.6480206178775553, 0.6449257381557254, 0.4903171979734907, 0.5105415155592833, 0.6142923551499597, 0.44001886717102023, 0.3666617033243256, 0.3132568250544165, 0.4079667374642181, 0.4003517787750752, 0.5256120492205193, 0.5386492966740015, 0.3069803314817998, 0.8156381553633356, 0.5426282397926216, 0.5181412169139367, 0.4822755598091074, 0.5406178423413075, 0.4677897465464037, 0.586475022468102, 0.4258858165596308, 0.6068620532228269, 0.3565438977225199, 0.6232313509617889, 0.44660807605529157, 0.6145015629912814, 0.3496244894196884, 0.7745503775117687, 0.4477620512904644, 0.6815348938233365, 0.5484065153992794, 0.4538505233025532, 0.7616828617326121, 0.43045996339411197, 0.4432422549450539, 0.5028966703636982, 0.5661773997570236, 0.8888881467440877, 0.34140937680957456, 0.49404444465375574, 0.285679942434855, 0.6846383740295108, 0.6797549065450585, 0.4627759278744895, 0.8146232957091083, 0.6108282703654548, 0.4410135933299898, 0.532760132306721, 0.465277391428969, 0.5222590915032078, 0.48243064759195314, 0.4399761706401707, 0.45359536369253545, 0.39434957675654914, 0.3573170444556372, 0.6311159506394983, 0.4983555876451601, 0.3755936920735292, 0.3709980786811867, 0.6104833641888825, 0.507160017073129, 0.45516390897459136, 0.3959061116900585, 0.39919490545876385, 0.5863640630851659, 0.5223574060969498, 0.4255097100514491, 0.5091400991629149, 0.6430289791159836, 0.40992502356634786, 0.5663773128088263, 0.4344769494353022, 0.4784621517905555, 0.6552553641945343, 0.44265037950209657, 0.4512430313064601, 0.5729933078289469, 0.4663144866680506, 0.46293028376657314, 0.5271874186292925, 0.5191784197775997, 0.6612375673244242, 0.3389333927433381, 0.49176815111961714, 0.4952118468458484, 0.5123845523992576, 0.49650668959594046, 0.30076088780660665, 0.3223411142215776, 0.2725562687170328, 0.7549099802924321, 0.45705405381522723, 0.5739837569886924, 0.6570169288909006, 0.38895161043786114, 0.31780023919737743, 0.8815881870746635, 0.3743729476816851, 0.4583656167674054, 0.5369347206686614, 0.4168597410485382, 0.5199748025521851, 0.49505559832701695, 0.37835738343396214, 0.5996524642146438, 0.6426961217035295, 0.4568142386029269, 0.3150726349572897, 0.5321808617796341, 0.4688000584801193, 0.5467871777615525, 1.037316044517723, 0.5702660602500016, 0.5525498746051428, 0.71181744524456, 0.52530936201023, 0.39873908499302957, 0.3045726197527603, 0.48494889902277355, 0.40594439596035103, 0.531407216829594, 0.38609519421348126, 0.41457120168932093, 0.5692864983956835, 0.3997060221971985, 0.44908614888082576, 0.46955888481480085, 0.5397634489869233, 0.44536462962157525, 0.7871916473425888, 0.31742204153843745, 0.605211303207252, 0.4720347322871974, 0.4474904943864068, 0.30045793119968445, 0.7368308470848635, 0.5490457888759431, 0.5374692357580273, 0.4078732366916878, 0.8433490263044077, 0.35824962216144085, 0.4697601698279141, 0.2952672128859149, 0.5095549259438799, 0.4129005395103743, 0.5020852146850484, 0.2695230004212351, 0.33928770774855077, 0.4728729037495606, 0.3448430671518713, 0.45592642531593813, 0.4874277681844882, 0.5631110134180926, 0.4007724872921893, 0.4128344105043686]

    alpha_1000_loss =[2.157939978837967, 1.7653291976451875, 1.4377663350105285, 1.2540500992536543, 1.1934843611717223, 1.1523990720510482, 1.0866601461172105, 1.067289274930954, 1.0176893270015719, 0.9925275021791459, 0.9965812343358994, 0.9746901509165763, 0.9359224194288253, 0.9533203250169754, 0.960437394976616, 0.9216829299926758, 0.9535613167285918, 0.9508061212301255, 0.8696245056390761, 0.9064771237969398, 0.94764750957489, 0.9533908754587174, 0.9138981109857559, 0.9120370757579803, 0.8883257031440734, 0.8952794206142427, 0.9093161016702652, 0.8308176544308662, 0.9155334037542342, 0.9228424835205079, 0.8975230205059053, 0.8727761062979699, 0.9137359565496442, 0.9323975348472595, 0.9068421590328217, 0.8809185391664505, 0.9079489174485207, 0.9181247851252557, 0.8844854590296745, 0.9206742769479751, 0.8561133179068564, 0.8680531337857247, 0.8710582834482192, 0.8386450588703156, 0.8785377544164656, 0.9116692930459976, 0.8780463653802872, 0.8756783038377763, 0.8304770049452783, 0.8887047597765922, 0.874698946774006, 0.8884398904442786, 0.8934405583143233, 0.8882100105285644, 0.8876884499192237, 0.8833069294691086, 0.9122853481769562, 0.8767591375112535, 0.9083112695813179, 0.9117351785302162, 0.8711405792832375, 0.9047065180540084, 0.9015807986259461, 0.8951105040311814, 0.8987334141135216, 0.92225430727005, 0.8847607254981993, 0.8952414396405219, 0.9022406953573224, 0.9086399328708648, 0.8843402630090713, 0.8627321064472199, 0.8792867717146873, 0.8708894437551498, 0.891790188550949, 0.9278576675057412, 0.9305236244201659, 0.8768927565217017, 0.9269339516758919, 0.9127387577295304, 0.8707364666461943, 0.8934145870804787, 0.8827886795997619, 0.8866700157523153, 0.885391217470169, 0.8883307880163194, 0.8729896411299706, 0.8660628494620323, 0.910429535508156, 0.8870808547735212, 0.9121349734067916, 0.8837612095475198, 0.8584815332293511, 0.8853494915366174, 0.8719753375649452, 0.9091389602422714, 0.8849936135113239, 0.8843020325899124, 0.8880697876214981, 0.920218941271305, 0.9398607316613198, 0.9286771664023398, 0.9327469903230666, 0.9427386337518693, 0.9001886105537416, 0.9147906744480132, 0.8779785019159316, 0.9328479140996933, 0.8899523049592972, 0.9239403590559959, 0.8834026688337324, 0.9204205721616745, 0.9305271655321121, 0.8828509315848351, 0.8645330724120142, 0.9270557940006257, 0.8923435324430466, 0.9425751978158949, 0.9068855080008508, 0.9143348470330238, 0.9072347995638846, 0.9450023031234741, 0.8873068469762803, 0.9442567849159239, 0.8539428022503852, 0.8900369489192961, 0.8832476192712784, 0.8892347349226475, 0.9337540343403816, 0.9014488574862479, 0.8885993599891663, 0.866223377287388, 0.9193178215622902, 0.9415447816252709, 0.8778460869193078, 0.9266352385282518, 0.944875811934471, 0.9018936669826507, 0.9013284194469451, 0.8968788650631906, 0.9483006232976914, 0.9560848867893219, 0.9012580472230912, 0.8727797648310661, 0.9084861192107201, 0.9034057229757309, 0.9329965618252754, 0.8434298160672189, 0.9056623253226281, 0.897904920578003, 0.9092879158258438, 0.9086411607265472, 0.863928057551384, 0.9121045786142348, 0.8966079419851305, 0.862660621702671, 0.8946672570705413, 0.8965416789054871, 0.9085097256302834, 0.9048845118284226, 0.9391305238008499, 0.9139750549197198, 0.941525857448578, 0.9301814255118369, 0.9464099851250648, 0.9064774483442306, 0.9312957173585893, 0.8976709893345832, 0.9645823365449905, 0.931926799416542, 0.9555925434827804, 0.9377762311697007, 0.9094224184751513, 0.9223426225781439, 0.9051459670066834, 0.896202253997326, 0.9134215411543846, 0.9050180596113204, 0.8846976605057716, 0.9420610928535462, 0.8889620819687842, 0.9339154937863349, 0.9274325424432754, 0.9129668077826498, 0.9284679079055789, 0.8614335775375366, 0.8705386695265769, 0.9124894690513612, 0.9580247887969018, 0.9362248498201369, 0.9518125599622727, 0.9666040700674057, 0.875626665353775, 0.9010159215331079, 0.8884716147184373, 0.94871436804533, 0.8754568767547608, 0.9095682764053346, 0.9086414107680321, 0.92737397223711]

    alpha_100_loss =[2.1085256600379947, 1.7978746724128722, 1.5097155129909514, 1.3872156459093095, 1.224329659342766, 1.1354782223701476, 1.1301487505435943, 1.028235794901848, 1.0456116515398026, 1.033713967204094, 0.9478918677568435, 0.9500611686706544, 0.9825700414180755, 0.9063938990235328, 0.9276299190521241, 0.9106756427884101, 0.9170923596620559, 0.8943987226486205, 0.8479270061850548, 0.8789257442951202, 0.8642541956901552, 0.9070241117477418, 0.8246823990345001, 0.8402323359251023, 0.8534433740377427, 0.8373326644301414, 0.8705770573019983, 0.8607140725851059, 0.9284507006406783, 0.8248486688733101, 0.7940995052456856, 0.918242184817791, 0.8294021290540696, 0.805961545407772, 0.8289308950304985, 0.8526466822624206, 0.8501699104905128, 0.8647428813576697, 0.8416131046414375, 0.831034489274025, 0.865763543844223, 0.8722592532634733, 0.8437081876397133, 0.8534733688831329, 0.8444009500741959, 0.8561930823326109, 0.8701209264993667, 0.8631947463750839, 0.8778655034303666, 0.8880875828862191, 0.8734872871637342, 0.8256992182135582, 0.8808393260836601, 0.846432095170021, 0.8466565680503845, 0.8420128339529038, 0.8712305796146392, 0.8468251985311508, 0.8463538709282876, 0.8745970362424851, 0.8684267187118531, 0.8229009452462195, 0.8415949535369872, 0.8236547979712487, 0.8986299163103103, 0.9038162064552306, 0.9008275178074836, 0.8397498658299447, 0.8085143992304802, 0.8730846890807152, 0.8137257531285285, 0.8596119242906571, 0.8691638916730879, 0.8573249626159669, 0.895803528726101, 0.8231212225556372, 0.8856846687197685, 0.8619967928528786, 0.8415637105703352, 0.8904700547456741, 0.8631712305545808, 0.8511077058315276, 0.895208246409893, 0.843459363281727, 0.8637090888619424, 0.8644884616136549, 0.8381767463684081, 0.8776790583133698, 0.8775481569766997, 0.8774467432498932, 0.8823149529099463, 0.9045490723848344, 0.903850201666355, 0.8612904900312424, 0.8808650803565978, 0.853639220893383, 0.9034470304846763, 0.9037305825948717, 0.8696637183427811, 0.8756133356690405, 0.8658056449890136, 0.8733234882354737, 0.8913097444176674, 0.8986939275264738, 0.8805481424927711, 0.8309944835305213, 0.8690471005439759, 0.861533864438534, 0.8649441248178483, 0.9076840287446976, 0.8923846703767777, 0.8651538494229317, 0.8606380388140679, 0.8666818949580193, 0.8210222551226616, 0.8359738147258758, 0.8612029972672461, 0.8972271317243574, 0.9095527991652489, 0.8333374813199044, 0.8411302891373633, 0.8034058085083962, 0.8639275804162025, 0.8488795363903046, 0.9071011963486673, 0.8792850881814956, 0.9155406162142754, 0.8895284175872803, 0.8873221063613892, 0.9035778844356537, 0.8603157335519789, 0.8599703964591028, 0.8637820991873741, 0.8966823750734327, 0.8710943415760994, 0.9157117518782615, 0.8800467869639398, 0.9281614193320273, 0.8861954534053803, 0.8184870108962057, 0.870732206106186, 0.8758646874129772, 0.9058200281858445, 0.8783257621526719, 0.9013856756687163, 0.9282783627510071, 0.8670944914221763, 0.8657415813207627, 0.8225416888296604, 0.8851150697469713, 0.8452984181046486, 0.8600024765729906, 0.874451932311058, 0.8797855058312416, 0.8793613776564598, 0.8176364785432815, 0.8358547559380533, 0.8387646958231926, 0.8367623841762543, 0.8480180366337299, 0.882435083389282, 0.9051632195711138, 0.9045582541823386, 0.896485792696476, 0.850665991306305, 0.8901046726107598, 0.8547443318367005, 0.8750027620792389, 0.8545245429873466, 0.9183877423405647, 0.8489505869150162, 0.8530879399180412, 0.8613713169097901, 0.8728649178147316, 0.8832897436618804, 0.9008938229084015, 0.8376118613779544, 0.8966046079993248, 0.8537483602762223, 0.8902158069610596, 0.8340040603280068, 0.9056915745139122, 0.8525722834467888, 0.8506976449489594, 0.8770755523443222, 0.8830623841285705, 0.9056073537468912, 0.9345758408308029, 0.8306759235262872, 0.9488708570599556, 0.8712312886118889, 0.9376750984787942, 0.9039076179265976, 0.9272519451379775, 0.8741310688853263, 0.8493250170350073, 0.8936005899310112, 0.8847285398840905, 0.9012167274951934, 0.9120591914653777]

    # alpha_10_loss =
    alpha_1_loss =[1.7748330035805702, 1.4157240265607833, 1.2071827340126036, 1.1128225064277648, 0.8956612064875662, 1.0486797386407853, 0.9080408856272697, 0.9585481452941893, 0.7982308462262153, 0.7972236803546549, 0.8799617065489294, 0.7767216509580612, 0.6643635327741504, 0.8411035561561585, 0.822099727243185, 0.74194113612175, 0.8468904501199722, 0.7945836727693676, 0.8005550187826156, 0.714121124446392, 0.7544194224476815, 0.6769744633603841, 0.8686029797792434, 0.7081380334496499, 0.7315571242570876, 0.8200900039076805, 0.7933891701698303, 0.6374429343640804, 0.783129188120365, 0.7370160457119346, 0.6762478689849377, 0.7331852059066295, 0.6765903670247646, 0.7320131465792656, 0.8078608673810959, 0.7664129704236984, 0.7044034349918367, 0.6770008677989244, 0.6906735286861657, 0.7229097180068493, 0.82242226973176, 0.6920078236423433, 0.736552886068821, 0.685426304936409, 0.8034182063490152, 0.7093941660225391, 0.6246852695941925, 0.7411710242182017, 0.652032618969679, 0.7478164494037628, 0.6566469031944872, 0.731347338631749, 0.7477029505372048, 0.7328183957934381, 0.6844147038459778, 0.7330967029929161, 0.6642522518336773, 0.7082998994737864, 0.6304582197219133, 0.7542143777012825, 0.7551432008837582, 0.6739838507026434, 0.6952277034521103, 0.7449204152822494, 0.7525369223952294, 0.7359246288239955, 0.6981925657391547, 0.7079970557242632, 0.7298095157742501, 0.7687483248114586, 0.6657907155156135, 0.72964879097417, 0.7659525013715028, 0.7374117449671029, 0.7011529390513898, 0.7205686224997044, 0.6171568807587027, 0.7333428339287639, 0.5678842697339131, 0.7823023204505443, 0.7472220845520497, 0.7556146301329136, 0.6724358897656203, 0.59927326757228, 0.6932735635340214, 0.6520167946815492, 0.7135989268124103, 0.6829702633619309, 0.600822064448148, 0.6977992095326772, 0.73639204159379, 0.7818187234550715, 0.7216646835207939, 0.7267669394612313, 0.6582909300923347, 0.6032453879807144, 0.6721978344395756, 0.6776258048415184, 0.6869199293851852, 0.6650821643322706, 0.5668574926257134, 0.6799265384674072, 0.7119317077100277, 0.7039879035949707, 0.6990476654469967, 0.7059354180842639, 0.6426241403818131, 0.6153182072937489, 0.6875009802728892, 0.7992972433567048, 0.6656960728764535, 0.7146173684298993, 0.6679621585085986, 0.707420498430729, 0.7147184398770332, 0.6039784874767065, 0.6978454641997814, 0.6542137005925179, 0.6428918929677456, 0.7004615740478038, 0.7249089395999909, 0.7025113706290723, 0.768997883349657, 0.6885875626001507, 0.656355577223003, 0.6042620136216282, 0.707643263414502, 0.6913271723687648, 0.7162413937598467, 0.7269990333914756, 0.6855725231766701, 0.6619131896831095, 0.7159577153623103, 0.7198883898556232, 0.6738970991969108, 0.6209849509596825, 0.7004147353768347, 0.6916344587504863, 0.669950683042407, 0.5652743415534497, 0.6772781148552894, 0.6012285640090704, 0.6991503404825925, 0.6424697925150393, 0.7522718275338411, 0.6537820517271757, 0.6429810440540313, 0.6753190067410467, 0.61970246873796, 0.6174522561579943, 0.6189580692350864, 0.6717210122942926, 0.6503370735794306, 0.6200424530357123, 0.6910995973646641, 0.7327591939270496, 0.6536530051380396, 0.796215595304966, 0.6553334869816899, 0.7083184567093849, 0.7648412483930589, 0.5765863054618239, 0.6563393240794541, 0.6941206584870815, 0.7116885530948639, 0.663928041011095, 0.5998988059163093, 0.6668161089718342, 0.7115055340528488, 0.675775575041771, 0.6845337118487805, 0.7334609347581863, 0.7710923571884633, 0.6466789647936821, 0.7223712830245496, 0.6907431089878082, 0.700976833254099, 0.5954923819005489, 0.704873734563589, 0.7248183020949364, 0.7363179571926592, 0.7236923624575138, 0.6805511796474457, 0.6361056557670236, 0.5874681982398032, 0.6533451890945434, 0.6913858244381845, 0.7575549037754536, 0.7413727486133574, 0.6354361313581467, 0.7412367777526379, 0.7047398617863656, 0.6860352422297, 0.7216282064840198, 0.7196235029399396, 0.6146808610856533, 0.6405587748158723, 0.6867813977599143, 0.5494146300666035, 0.657960416637361]

    alpha_01_loss =[1.4673161056637762, 1.4750781960183132, 1.3403106789290906, 1.0021788132206098, 1.0349651470547543, 1.0159541219472885, 0.9221381078287958, 0.9916083359718323, 0.8631868128478528, 0.7430902504580152, 0.7843721880570464, 0.8252423785999417, 0.6841206504404546, 0.6599806629808326, 0.7454396332800388, 0.7621082374453545, 0.6212873920798302, 0.6326697450410574, 0.7759847839921712, 0.6224517921614461, 0.6789488659799099, 0.7076283760741353, 0.6699265314638614, 0.6011043988289159, 0.7552231997251511, 0.7223187991976737, 0.6990977468248458, 0.5961079033464194, 0.6652821011509513, 0.7309181353449821, 0.5512610074563418, 0.5738116875040579, 0.5985899289851778, 0.6162250894028694, 0.6773383791744709, 0.7976543849706649, 0.5876273391745053, 0.5901879266917021, 0.5691823304770514, 0.6603318261634559, 0.6278508735820651, 0.6225581755116583, 0.5796073123970473, 0.651635463386774, 0.6036907851323485, 0.5889779968059156, 0.5881617532339977, 0.6803684061422246, 0.5375676116497197, 0.658598172425991, 0.6616024225950241, 0.5409775407996494, 0.6759721256047488, 0.5460324120066207, 0.530023685400447, 0.6032173560559749, 0.6524643617868422, 0.5756935660541058, 0.5803625286751777, 0.713675562745775, 0.7024440771341324, 0.6358736648969352, 0.503295867782149, 0.6606980468705297, 0.5599032372137299, 0.5954828598536552, 0.4802571034452502, 0.5859048211080334, 0.5304524514792883, 0.6475402823090552, 0.6552412658184766, 0.5801686637848614, 0.6050153942964971, 0.6625961654633283, 0.5843066287785769, 0.5627539885602892, 0.675710299362836, 0.5563562102033757, 0.5647550808638333, 0.5985753475129604, 0.567538928380108, 0.6294792667997535, 0.578752521664137, 0.6292745938152075, 0.7073284500127193, 0.46487379727758504, 0.6003338814643212, 0.706635919753462, 0.5555215498589678, 0.5698986610770226, 0.651999128088355, 0.6196019197511486, 0.5256884409373743, 0.5415108828750489, 0.49335120487048706, 0.6497615348616091, 0.688843718059361, 0.6141782426089049, 0.6028783344477415, 0.5527547291386872, 0.6544321559928357, 0.5432373232548844, 0.5507635166123509, 0.6342665395705263, 0.5820326633699004, 0.5677365497639403, 0.49461521149802135, 0.5715487984754145, 0.6235620039746846, 0.6710240274313402, 0.6060205219220369, 0.7129686551302438, 0.6416270069777965, 0.5990719710325356, 0.48950845261422726, 0.5810766733437777, 0.6349556115219854, 0.5676902637302521, 0.6128862710297107, 0.6121496127102591, 0.6173141691403725, 0.5847458499670029, 0.6103874860703946, 0.6224899278860538, 0.5819282658398152, 0.5178977736458183, 0.6546464256942273, 0.5517800490371882, 0.6543874711393676, 0.5531660758034558, 0.7401326632499694, 0.4710425365809351, 0.6976165509223937, 0.4871974159247475, 0.5306733271494524, 0.6344427712261677, 0.580359705860028, 0.609847277700901, 0.5679156458435137, 0.5286448200792074, 0.6529015259834705, 0.579204112120509, 0.6102200809314491, 0.57684130622074, 0.556231338698417, 0.5477445667237044, 0.6034883574761626, 0.4528132457379252, 0.649827495291829, 0.6754242543876171, 0.5419534139519238, 0.6029044469306245, 0.68536431863904, 0.6118087897449731, 0.5158198964883922, 0.5703686011582613, 0.6481699420511723, 0.567464383729748, 0.5676646053791046, 0.6016639965027571, 0.6715209988105926, 0.5710560107976198, 0.5725268574804068, 0.6194640888273717, 0.5619556651450693, 0.535907538495958, 0.6364801418036223, 0.5317914010814275, 0.4879986742264009, 0.5477315429598093, 0.609228475074051, 0.7442155681550504, 0.5309535050715242, 0.6904426404461265, 0.5575437580537709, 0.6043353508412839, 0.5864054052717983, 0.5461306770518422, 0.5721468591690064, 0.5896825416758658, 0.5269985364643208, 0.6233817138220183, 0.6289835707460714, 0.5611602172286303, 0.7409316549450159, 0.461540058989267, 0.5919495259225369, 0.653185183033347, 0.5041458640533862, 0.5767196522094309, 0.6128281893208622, 0.6913757792425168, 0.5252645186593146, 0.6318010172247888, 0.5556071060255635, 0.5684351643268019, 0.44599806210637327, 0.6303024994581938, 0.6142813972732983, 0.622027643956244]

    # alpha_001_loss =
    fig = plt.figure(num=1, figsize=(16, 9))
    ax = fig.add_subplot(111)
    _x = np.arange(0, 200, 1)

    ax.plot(_x, origin_iid_loss, 'grey', label='Origin_iid')
    ax.plot(_x, alpha_1000_loss, 'red', label='Non_iid_alpha_1000')
    ax.plot(_x, alpha_100_loss, 'lightcoral', label='Non_iid_alpha_100')
    # ax.plot(_x, alpha_10_loss, 'pink', label='Non_iid_alpha_10')
    ax.plot(_x, alpha_1_loss, 'orange', label='Non_iid_alpha_1')
    ax.plot(_x, alpha_01_loss, 'lightgreen', label='Non_iid_alpha_0.1')
    ax.plot(_x, origin_non_iid_loss, 'lightgrey', label='Origin_non_iid')
    # ax.plot(_x, alpha_001_loss, 'skyblue', label='Non_iid_alpha_0.01')
    ax.set_xlim([-5, 205])
    ax.set_ylim([0, 2.5])
    ax.set_xticks(np.linspace(0, 200, 11))
    ax.set_yticks(np.linspace(0, 2.5, 11))
    ax.set_xlabel('Global round')
    ax.set_ylabel('Training loss')
    ax.set_title('Training loss for variety data distribution')
    plt.legend()
    # plt.savefig('Training loss for variety data distribution.png')
    # plt.close()
    plt.show()


def test_acc():
    origin_iid_acc =[0.1981, 0.5982, 0.6366, 0.6707, 0.6977, 0.6854, 0.706, 0.6896, 0.7011, 0.7211, 0.7226, 0.731, 0.7371, 0.7451, 0.7365, 0.7509, 0.7437, 0.7529, 0.7615, 0.7575, 0.7546, 0.7567, 0.7629, 0.7643, 0.7693, 0.7652, 0.7732, 0.7618, 0.7733, 0.767, 0.768, 0.7719, 0.7739, 0.7785, 0.7804, 0.7796, 0.7801, 0.782, 0.7812, 0.7872, 0.7816, 0.7781, 0.7848, 0.7827, 0.7809, 0.78, 0.7949, 0.7857, 0.7858, 0.7947, 0.7874, 0.7958, 0.7906, 0.8013, 0.7928, 0.7851, 0.7914, 0.7974, 0.7969, 0.793, 0.7978, 0.7988, 0.7967, 0.7976, 0.7963, 0.8041, 0.7898, 0.8015, 0.7996, 0.7927, 0.8004, 0.7985, 0.7999, 0.7983, 0.7953, 0.7923, 0.8021, 0.8023, 0.8033, 0.8027, 0.7945, 0.8001, 0.7973, 0.8022, 0.8039, 0.8035, 0.8015, 0.8014, 0.7998, 0.8041, 0.7943, 0.7999, 0.7934, 0.7985, 0.7974, 0.8014, 0.8059, 0.8016, 0.8024, 0.8018, 0.7962, 0.7996, 0.804, 0.8006, 0.8, 0.8038, 0.7976, 0.7971, 0.8074, 0.8018, 0.803, 0.7986, 0.7918, 0.795, 0.8002, 0.8035, 0.7942, 0.8001, 0.7879, 0.8027, 0.7964, 0.7939, 0.7973, 0.7891, 0.7971, 0.7985, 0.7791, 0.8004, 0.7912, 0.7964, 0.791, 0.7888, 0.7944, 0.7946, 0.7949, 0.7979, 0.79, 0.7981, 0.7912, 0.797, 0.8003, 0.7978, 0.7953, 0.7889, 0.8005, 0.797, 0.7823, 0.7963, 0.7942, 0.7995, 0.7887, 0.7951, 0.7956, 0.7935, 0.7964, 0.7914, 0.7941, 0.7893, 0.7873, 0.7907, 0.7991, 0.793, 0.7993, 0.7937, 0.7935, 0.7909, 0.7925, 0.7907, 0.7868, 0.7894, 0.7999, 0.7866, 0.7955, 0.7931, 0.791, 0.7953, 0.7896, 0.7858, 0.7868, 0.7904, 0.7869, 0.7872, 0.7938, 0.7888, 0.7918, 0.7923, 0.7921, 0.7967, 0.79, 0.7908, 0.792, 0.7884, 0.7872, 0.7939, 0.7923, 0.7934, 0.7804, 0.7869, 0.796, 0.7847]

    origin_non_iid_acc =[0.1983, 0.1008, 0.1, 0.3479, 0.1919, 0.2385, 0.2065, 0.3506, 0.2834, 0.2709, 0.2547, 0.2835, 0.3392, 0.1495, 0.2982, 0.3001, 0.3816, 0.2965, 0.1, 0.2601, 0.3236, 0.1286, 0.3183, 0.3638, 0.3688, 0.2634, 0.2356, 0.245, 0.2947, 0.3842, 0.4771, 0.3345, 0.2676, 0.4039, 0.3327, 0.2901, 0.3133, 0.2372, 0.2242, 0.4178, 0.2818, 0.3199, 0.3016, 0.351, 0.4036, 0.3619, 0.3908, 0.4775, 0.3248, 0.3934, 0.5805, 0.5204, 0.5451, 0.4863, 0.4264, 0.2744, 0.568, 0.3725, 0.4589, 0.4162, 0.5682, 0.4252, 0.4818, 0.3778, 0.3578, 0.3845, 0.4308, 0.3806, 0.4133, 0.3753, 0.4946, 0.4193, 0.3268, 0.4368, 0.3438, 0.3905, 0.4908, 0.4031, 0.5308, 0.3665, 0.3331, 0.1992, 0.5241, 0.4557, 0.5552, 0.4653, 0.3004, 0.4492, 0.3311, 0.3441, 0.4762, 0.4841, 0.4973, 0.3566, 0.5004, 0.4593, 0.4699, 0.2979, 0.5112, 0.4467, 0.3147, 0.4989, 0.381, 0.3636, 0.2935, 0.4969, 0.3469, 0.3764, 0.4384, 0.4641, 0.562, 0.3478, 0.3293, 0.5813, 0.3818, 0.3661, 0.2986, 0.3892, 0.403, 0.59, 0.2626, 0.3959, 0.4022, 0.3126, 0.2671, 0.3158, 0.6783, 0.31, 0.3279, 0.4104, 0.486, 0.543, 0.5748, 0.5966, 0.3825, 0.312, 0.4906, 0.2717, 0.4586, 0.4844, 0.3043, 0.5245, 0.4443, 0.4209, 0.5119, 0.4375, 0.3736, 0.4393, 0.5085, 0.3153, 0.3238, 0.3933, 0.3483, 0.3813, 0.4043, 0.2659, 0.4182, 0.3907, 0.2927, 0.5164, 0.4831, 0.5054, 0.3889, 0.3921, 0.3385, 0.3803, 0.4731, 0.4605, 0.389, 0.4199, 0.4386, 0.3386, 0.4424, 0.3304, 0.3297, 0.3161, 0.4842, 0.4211, 0.4578, 0.3936, 0.1371, 0.3159, 0.4436, 0.4336, 0.3822, 0.5394, 0.4272, 0.403, 0.4507, 0.2727, 0.4969, 0.4806, 0.3121, 0.5517, 0.4187, 0.5012, 0.3961, 0.5064, 0.5321, 0.5691]

    alpha_1000_acc =[0.1279, 0.4727, 0.5204, 0.5736, 0.5881, 0.6356, 0.6138, 0.6399, 0.65, 0.6605, 0.6616, 0.6668, 0.6622, 0.6712, 0.674, 0.6744, 0.6709, 0.6841, 0.6627, 0.6896, 0.6595, 0.6942, 0.6963, 0.6954, 0.7015, 0.7026, 0.7043, 0.6929, 0.7064, 0.6833, 0.7109, 0.6958, 0.7037, 0.6941, 0.7057, 0.7069, 0.7016, 0.7062, 0.7124, 0.7053, 0.707, 0.7085, 0.713, 0.7115, 0.7185, 0.7016, 0.7176, 0.7137, 0.7108, 0.7198, 0.7169, 0.7109, 0.7174, 0.7159, 0.7148, 0.7151, 0.7197, 0.7096, 0.7211, 0.718, 0.7128, 0.7229, 0.7198, 0.714, 0.7211, 0.7237, 0.7274, 0.7175, 0.7116, 0.7124, 0.723, 0.7241, 0.7204, 0.7229, 0.7175, 0.7155, 0.7198, 0.7253, 0.7242, 0.713, 0.7236, 0.708, 0.7255, 0.7209, 0.715, 0.715, 0.7237, 0.721, 0.723, 0.7208, 0.7241, 0.7225, 0.7227, 0.7207, 0.7185, 0.7236, 0.7143, 0.7267, 0.7284, 0.7296, 0.7214, 0.7255, 0.7229, 0.7265, 0.715, 0.7262, 0.7303, 0.7168, 0.7258, 0.7192, 0.7189, 0.729, 0.723, 0.7283, 0.7304, 0.7241, 0.7204, 0.7316, 0.7294, 0.7343, 0.7306, 0.7195, 0.7313, 0.7183, 0.7217, 0.7237, 0.7272, 0.7335, 0.7279, 0.7208, 0.7284, 0.727, 0.7176, 0.7112, 0.7255, 0.7214, 0.7241, 0.7308, 0.7267, 0.7211, 0.7303, 0.7229, 0.7273, 0.7211, 0.7248, 0.7222, 0.7224, 0.7309, 0.726, 0.7289, 0.7309, 0.7277, 0.7271, 0.7273, 0.7311, 0.7138, 0.7213, 0.7353, 0.724, 0.7364, 0.7243, 0.7244, 0.723, 0.7246, 0.7328, 0.729, 0.7307, 0.7326, 0.7259, 0.7293, 0.7238, 0.7345, 0.7262, 0.7278, 0.7257, 0.7289, 0.7261, 0.7334, 0.7228, 0.732, 0.7258, 0.7229, 0.7314, 0.7272, 0.7243, 0.7339, 0.728, 0.7303, 0.7247, 0.7328, 0.7265, 0.7271, 0.7366, 0.7301, 0.7236, 0.7334, 0.7297, 0.7251, 0.7325, 0.7294]

    alpha_100_acc =[0.2155, 0.3629, 0.4701, 0.5937, 0.6013, 0.6395, 0.7113, 0.6663, 0.6748, 0.728, 0.7121, 0.7298, 0.7282, 0.739, 0.7294, 0.741, 0.7423, 0.7446, 0.7485, 0.7513, 0.7507, 0.7475, 0.7604, 0.7573, 0.7518, 0.7639, 0.7569, 0.7532, 0.7609, 0.7581, 0.7678, 0.7546, 0.7652, 0.7564, 0.7641, 0.7652, 0.7768, 0.7627, 0.771, 0.7645, 0.7693, 0.7697, 0.7708, 0.7723, 0.7626, 0.7736, 0.7674, 0.7633, 0.7684, 0.766, 0.7733, 0.7691, 0.7792, 0.7741, 0.7811, 0.7747, 0.7802, 0.7738, 0.7688, 0.7877, 0.7895, 0.7793, 0.7805, 0.7753, 0.7703, 0.7863, 0.7836, 0.7783, 0.773, 0.7842, 0.7766, 0.7806, 0.7849, 0.7671, 0.7936, 0.7705, 0.7796, 0.7824, 0.7902, 0.7792, 0.784, 0.7799, 0.7816, 0.7808, 0.7818, 0.7909, 0.7768, 0.7877, 0.7821, 0.787, 0.7846, 0.7909, 0.799, 0.7869, 0.7945, 0.7949, 0.7921, 0.7979, 0.7918, 0.7977, 0.7917, 0.788, 0.7941, 0.7881, 0.7821, 0.7948, 0.7884, 0.7952, 0.7971, 0.7881, 0.7891, 0.7948, 0.7909, 0.8033, 0.78, 0.7839, 0.7883, 0.787, 0.7929, 0.7988, 0.794, 0.779, 0.7862, 0.7857, 0.7941, 0.7995, 0.7843, 0.7927, 0.7939, 0.7914, 0.7846, 0.7987, 0.7906, 0.7987, 0.7836, 0.7928, 0.7941, 0.793, 0.7941, 0.7862, 0.7807, 0.7927, 0.8042, 0.7934, 0.7872, 0.7899, 0.7975, 0.8002, 0.7829, 0.7935, 0.7975, 0.796, 0.7844, 0.7789, 0.7751, 0.7774, 0.7891, 0.7981, 0.7819, 0.7916, 0.7904, 0.7906, 0.7723, 0.7781, 0.7892, 0.795, 0.7759, 0.7881, 0.7819, 0.7916, 0.7924, 0.7841, 0.7715, 0.7861, 0.7879, 0.7884, 0.7881, 0.7794, 0.7709, 0.7746, 0.7847, 0.7773, 0.7842, 0.7808, 0.7858, 0.7927, 0.7868, 0.7868, 0.798, 0.7867, 0.7819, 0.7915, 0.7812, 0.788, 0.7879, 0.7696, 0.7864, 0.7872, 0.7844, 0.7797]

    # alpha_10_acc =
    alpha_1_acc =[0.3216, 0.4287, 0.5872, 0.5502, 0.6128, 0.6328, 0.6574, 0.5863, 0.6791, 0.7001, 0.7174, 0.7142, 0.6992, 0.7016, 0.6692, 0.596, 0.7095, 0.7058, 0.702, 0.6642, 0.7277, 0.7047, 0.7098, 0.6697, 0.7391, 0.7449, 0.7368, 0.7576, 0.7351, 0.7518, 0.7229, 0.7416, 0.7144, 0.6964, 0.7397, 0.7717, 0.6663, 0.7775, 0.7105, 0.7223, 0.7304, 0.7416, 0.7512, 0.7277, 0.762, 0.7147, 0.7033, 0.7665, 0.7695, 0.6781, 0.7625, 0.7544, 0.7842, 0.7656, 0.7439, 0.7818, 0.7757, 0.7655, 0.7641, 0.7702, 0.7682, 0.744, 0.7497, 0.7483, 0.7745, 0.7558, 0.7562, 0.7664, 0.7873, 0.7466, 0.7774, 0.7572, 0.771, 0.7709, 0.7218, 0.7687, 0.7814, 0.777, 0.7263, 0.7236, 0.7929, 0.7954, 0.7406, 0.7416, 0.7875, 0.7723, 0.7753, 0.7809, 0.75, 0.6667, 0.7915, 0.7664, 0.7846, 0.7467, 0.7929, 0.7751, 0.7777, 0.7667, 0.7082, 0.7825, 0.7444, 0.768, 0.7666, 0.7575, 0.7854, 0.7329, 0.7905, 0.774, 0.7375, 0.7575, 0.7936, 0.7062, 0.7566, 0.7741, 0.7621, 0.7874, 0.7842, 0.756, 0.792, 0.7505, 0.7511, 0.7627, 0.7752, 0.791, 0.7648, 0.8015, 0.7984, 0.7731, 0.7166, 0.7786, 0.7273, 0.6894, 0.7705, 0.7643, 0.8007, 0.7407, 0.756, 0.7445, 0.753, 0.8033, 0.7432, 0.744, 0.7548, 0.763, 0.7288, 0.7721, 0.7808, 0.7833, 0.8079, 0.7889, 0.771, 0.7916, 0.7651, 0.7148, 0.725, 0.8064, 0.7483, 0.7977, 0.7935, 0.8004, 0.7999, 0.7844, 0.7774, 0.7622, 0.7807, 0.7782, 0.7916, 0.7977, 0.7895, 0.7663, 0.778, 0.78, 0.7652, 0.7568, 0.8105, 0.7732, 0.7932, 0.7236, 0.76, 0.7421, 0.7336, 0.7739, 0.7425, 0.7758, 0.7617, 0.7755, 0.7632, 0.709, 0.7906, 0.7895, 0.7548, 0.7988, 0.7997, 0.7144, 0.7243, 0.7926, 0.7828, 0.7856, 0.7391, 0.7582]

    alpha_01_acc =[0.1915, 0.1896, 0.2909, 0.4164, 0.3821, 0.4579, 0.5484, 0.6386, 0.583, 0.6401, 0.5543, 0.6068, 0.7129, 0.5355, 0.6617, 0.652, 0.6256, 0.6566, 0.7122, 0.6505, 0.6674, 0.6853, 0.6099, 0.6958, 0.676, 0.7163, 0.6294, 0.6653, 0.6609, 0.6271, 0.6712, 0.6919, 0.6264, 0.6752, 0.6481, 0.717, 0.6524, 0.6949, 0.6943, 0.635, 0.6358, 0.703, 0.7234, 0.7431, 0.7036, 0.7266, 0.6646, 0.6811, 0.7015, 0.7474, 0.6976, 0.7341, 0.676, 0.6702, 0.651, 0.6767, 0.7534, 0.7418, 0.6355, 0.7359, 0.7101, 0.7551, 0.7517, 0.7353, 0.7328, 0.7659, 0.6148, 0.7228, 0.7141, 0.6831, 0.712, 0.7239, 0.7382, 0.7332, 0.723, 0.6644, 0.7089, 0.7414, 0.7525, 0.757, 0.6596, 0.7118, 0.6679, 0.7097, 0.7245, 0.7648, 0.7115, 0.6831, 0.6798, 0.719, 0.7089, 0.7165, 0.7256, 0.6883, 0.7701, 0.6595, 0.735, 0.7322, 0.7044, 0.7581, 0.7356, 0.7258, 0.7011, 0.6027, 0.7345, 0.753, 0.7165, 0.7631, 0.661, 0.7453, 0.7099, 0.7678, 0.6864, 0.6739, 0.7282, 0.7717, 0.6275, 0.7714, 0.7566, 0.7478, 0.7354, 0.668, 0.7002, 0.6502, 0.7328, 0.7574, 0.7528, 0.6511, 0.7348, 0.7421, 0.7057, 0.7217, 0.7496, 0.7305, 0.6852, 0.7176, 0.772, 0.7566, 0.7303, 0.7497, 0.7544, 0.738, 0.7581, 0.7333, 0.7477, 0.7644, 0.7225, 0.7487, 0.7395, 0.7251, 0.7236, 0.722, 0.7418, 0.7658, 0.7465, 0.7709, 0.7381, 0.7535, 0.7572, 0.7699, 0.6013, 0.7823, 0.7353, 0.7214, 0.7439, 0.7103, 0.7445, 0.7374, 0.7544, 0.7004, 0.7532, 0.7494, 0.7757, 0.7577, 0.7652, 0.761, 0.7669, 0.757, 0.7311, 0.7304, 0.7762, 0.6644, 0.7838, 0.6557, 0.7554, 0.6657, 0.6651, 0.7384, 0.7626, 0.7715, 0.7648, 0.7685, 0.7205, 0.7541, 0.7678, 0.7838, 0.7524, 0.6814, 0.7708, 0.7344]

    # alpha_001_acc =
    fig = plt.figure(num=1, figsize=(16, 9))
    ax = fig.add_subplot(111)
    _x = np.arange(0, 200, 1)
    ax.plot(_x, origin_iid_acc, 'grey', label='Origin_iid')
    ax.plot(_x, alpha_1000_acc, 'yellow', label='Non_iid_alpha_1000')
    ax.plot(_x, alpha_100_acc, 'lightcoral', label='Non_iid_alpha_100')
    # ax.plot(_x, alpha_10_acc, 'pink', label='Non_iid_alpha_10')
    ax.plot(_x, alpha_1_acc, 'orange', label='Non_iid_alpha_1')
    ax.plot(_x, alpha_01_acc, 'lightgreen', label='Non_iid_alpha_0.1')
    ax.plot(_x, origin_non_iid_acc, 'lightgrey', label='Origin_non_iid')
    # ax.plot(_x, alpha_001_acc, 'skyblue', label='Non_iid_alpha_0.01')
    ax.set_xlim([-5, 205])
    ax.set_ylim([0.5, 1.05])
    ax.set_xticks(np.linspace(0, 200, 11))
    ax.set_yticks(np.linspace(0, 1.0, 21))
    ax.set_xlabel('Global round')
    ax.set_ylabel('Test accuracy')
    ax.set_title('Test accuracy for variety data distribution')
    plt.legend()
    # plt.savefig('Test accuracy for variety data distribution.png')
    # plt.close()
    plt.show()


# training_loss()
test_acc()
