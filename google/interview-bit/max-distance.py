
import operator

class Element:
    def __init__(self, value, index, diff=0):
        self.value = value
        self.index = index
        self.diff = diff


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        elements = [Element(value, index) for index, value in enumerate(A)]
        elements = sorted(elements, key=operator.attrgetter('value'))
        max_index = len(elements) - 1
        visited = set()
        for index, start in enumerate(elements):
            if start == len(elements) - 1:
                break
            start.diff = max_index - start.index
            visited.add(start.index)
            if start.index == max_index:
                max_index = self.get_next_max(visited, max_index)
        return max([element.diff for element in elements])

    def get_next_max(self, visited, current_max):
        _max = current_max
        while _max in visited:
            _max -= 1
        return _max





A = [ 69953237, 59183787, 16962742, 53647827, 80157178, 51106992, 58228227, 45131842, 70499719, 70765861, 43961028, 6698667, 99911553, 79107222, 67571988, 39721137, 78088316, 3759045, 19395856, 29387266, 68084358, 62564561, 24736359, 13212412, 66665326, 38724565, 61088241, 21263259, 89291805, 88650356, 58518225, 86449553, 78979492, 39596282, 43927666, 35451400, 80068197, 23391371, 25433080, 5888423, 67042527, 15586432, 57608751, 75903078, 95593533, 15702947, 39691466, 92690796, 18015358, 95172428, 72245309, 15424690, 41199673, 71322081, 27606512, 2347516, 1354382, 9924819, 63458285, 13170098, 40075662, 31237137, 45236128, 74375452, 92722404, 80087546, 23399482, 86945189, 3780890, 1963037, 76980637, 41676736, 74194802, 64788125, 88954508, 95737994, 21365859, 71092491, 67365387, 62345424, 77276892, 53193048, 30131824, 5365626, 66817225, 64511810, 46917019, 80497257, 20853093, 26175229, 85887940, 85764880, 78262084, 609284, 92269014, 46385693, 53718740, 17486900, 98427277, 92911988, 32225164, 72512163, 88678886, 65347756, 40460802, 33132933, 88603373, 26890724, 87077147, 99305881, 55925130, 83289365, 54166373, 50920143, 4427534, 29179799, 91572049, 95103705, 56304651, 69828935, 76914922, 33694020, 15575017, 77664401, 91393916, 96189668, 82107391, 95777779, 22244308, 65701218, 23227429, 98614556, 43407558, 67137144, 34515594, 89248417, 47520685, 14084016, 91725069, 94236666, 61860638, 82315091, 88113674, 31949150, 11718471, 51617813, 41754631, 15588021, 8130184, 52515921, 20663946, 70850137, 85578292, 93271926, 46273611, 27972346, 16865457, 94763722, 28780820, 52198047, 39535546, 9854737, 56888868, 82035778, 88667377, 71915993, 23061619, 71237088, 38215964, 99455111, 84338139, 9438659, 87387886, 35325804, 36964271, 40598041, 83828315, 30761279, 26893177, 19907874, 70129736, 62700567, 91806797, 11958671, 98578052, 8205009, 47197783, 53336153, 36819554, 47426225, 60695466, 55323353, 23435249, 16782401, 37928333, 19599390, 39797644, 9436396, 69658044, 45212110, 48265238, 14183162, 74865579, 58521415, 21894773, 65729368, 91458346, 39977875, 42236097, 12766362, 92049518, 13196912, 18064381, 89025324, 18154460, 77179251, 84814940, 3021813, 25547069, 65821055, 64653709, 94102131, 68518939, 46556175, 82058200, 80932197, 46454512, 62876026, 59675187, 4157064, 56677982, 76761579, 58446935, 51180436, 16416645, 65330136, 39435329, 81388109, 15522197, 78011106, 67617066, 34445170, 75555584, 87940550, 29128931, 61824105, 63418827, 21298249, 19352955, 91556471, 92675461, 888811, 61724633, 69153235, 83033789, 60689257, 54479401, 27546578, 66335535, 38378169, 6852142, 76001740, 64337900, 84778273, 7063943, 20469454, 8897942, 81095011, 89277538, 89473685, 13442135, 54332314, 99428305, 49227963, 1550084, 58626108, 3149845, 9592847, 63553909, 64442175, 52746464, 71731610, 68109474, 12014994, 28405025, 342244, 77415207, 6554496, 29199336, 24816541, 86021818, 93254912, 70091579, 24906579, 50431415, 92218181, 96921595, 70001355, 69278435, 48183386, 4909222, 9784895, 59239264, 82952057, 54807579, 85365017, 10747717, 36328910, 99503949, 25462804, 1948980, 54007615, 93059997, 96143890, 87526013, 36668467, 6585021, 59026699, 42437483, 49977217, 10735602, 29201394, 54519214, 94548380, 46479340, 50083557, 9899537, 43429844, 62002345, 57109791, 15539611, 37100828, 96624737, 58882555, 18287280, 73908899, 58094409, 31628808, 7279505, 87539497, 35968234, 73051936, 9182618, 6399914, 85644731, 13422910, 6027207, 40194013, 49063637, 47973273, 98583990, 4494264, 54221620, 99760871, 52094275, 44298611, 98771831, 39244836, 20234483, 63104483, 17667669, 77220658, 97536077, 67203516, 9567573, 96789571, 6954478, 9245869, 82742448, 72371341, 57459624, 25406080, 52099423, 49750024, 77497879, 16327199, 39571526, 14570597, 76246637, 93751329, 86339423, 97188050, 48457113, 52455837, 77244782, 81308324, 74575702, 31144906, 30685803, 21269958, 31958563, 20917120, 52658082, 33778983, 85532378, 6177062, 35138461, 27377273, 68310047, 27164914, 24236293, 90140894, 26903650, 31650250, 45975378, 10537609, 11918603, 92943222, 77479401, 42865540, 50885917, 57892395, 55161914, 82804155, 16502312, 25439804, 2105003, 52617639, 69471748, 48335908, 17352118, 36510341, 55222894, 6319593, 79662620, 37402118, 68949184, 48515926, 12224685, 8095432, 36227103, 37292769, 79979610, 78482598, 23728343, 26166144, 41593189, 44829841, 44241275, 43522523, 63777807, 3827324, 2683674, 3824814, 35307572, 1837804, 12651831, 24382914, 44014481, 16990793, 41894672, 33681016 ]


s = Solution()
print s.maximumGap(A)
