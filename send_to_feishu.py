import json, urllib.request, os

TOKEN = os.environ.get('FEISHU_TOKEN', '')
DOC_ID = 'QxzudaKAcoDUwBxAW7XcYo3Hn0e'

def add_blocks(parent_id, blocks):
    url = f'https://open.feishu.cn/open-apis/docx/v1/documents/{DOC_ID}/blocks/{parent_id}/children'
    data = json.dumps({"children": blocks, "index": -1}, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Authorization', f'Bearer {TOKEN}')
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    try:
        resp = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8')
        print(f"HTTP {e.code}: {body[:1000]}")
        return []
    result = json.loads(resp.read().decode('utf-8'))
    if result['code'] != 0:
        print(f"Error: {result}")
        return []
    return [b['block_id'] for b in result['data']['children']]

def H1(text):
    return {"block_type": 3, "heading1": {"elements": [{"text_run": {"content": text}}], "style": {}}}

def H2(text):
    return {"block_type": 4, "heading2": {"elements": [{"text_run": {"content": text}}], "style": {}}}

def H3(text):
    return {"block_type": 5, "heading3": {"elements": [{"text_run": {"content": text}}], "style": {}}}

def P(text):
    return {"block_type": 2, "text": {"elements": [{"text_run": {"content": text}}], "style": {}}}

def bullet(text):
    return {"block_type": 2, "text": {"elements": [{"text_run": {"content": '• ' + text}}], "style": {}}}

L = '“'  # "
R = '”'  # "

blocks = []

# === 世界观与系统 ===
blocks.append(H1('世界观与系统'))
blocks.append(P('系统名称：心动狩猎'))
blocks.append(bullet('功能一：实时显示目标好感度'))
blocks.append(bullet('功能二：分析目标偏好，自动推荐匹配攻略人设'))
blocks.append(bullet('功能三：好感度达阈值解锁新技能'))
blocks.append(P('奖励递进链：魅惑光环 → 读心碎片 → 距离感知 → SSS级终极奖励'))
blocks.append(P(f'核心规则：系统不惩罚宿主，只奖励。因为它要的不是{L}任务完成{R}，是{L}越玩越大{R}。'))

# === 核心设定 ===
blocks.append(H1('核心设定'))
blocks.append(P('女主：时染，24岁，S级天赋觉醒者'))
blocks.append(P('核心能力：读得懂每个男人心里缺的那一块——他缺什么，她就给什么。他怕什么，她就避什么。'))
blocks.append(P('性格机制：对不同类型的目标切换不同的人设脸孔。对冷面CFO是暖愈甜妹，对艺术家是同类灵魂，对电竞明星是若即若离姐姐，对心理医生是破碎感谜题。'))
blocks.append(P('骨子里始终是同一个人：不走心、不内疚、不洗白。享受的不是爱情，是狩猎过程本身。'))

# === 男人线 ===
blocks.append(H1('四大目标'))
blocks.append(bullet('[001 陆司砚] 冷面CFO，31岁。缺轻松——身边的人都在跟数字博弈，没人让他笑。攻略人设：暖愈甜妹'))
blocks.append(bullet(f'[002 顾砚声] 艺术策展人，28岁。缺共鸣——前女友说他{L}爱画胜过爱人{R}。攻略人设：同类灵魂'))
blocks.append(bullet('[003 江辞野] 电竞明星，22岁。缺征服感——所有女生都主动，她偏不。攻略人设：若即若离姐姐'))
blocks.append(bullet(f'[004 温屿] 心理医生，35岁。缺失控——分析别人一辈子，她让他分析不了。攻略人设：病弱破碎感'))

# === 分集大纲 ===
blocks.append(H1('分集大纲'))

blocks.append(H2('第一幕：狩猎开场（第1-4集）'))

blocks.append(P('【第1集 · 系统激活】'))
blocks.append(P('分手现场 → 系统觉醒 → 十分钟内连撩两人。江边的陆司砚用暖愈脸——笑得比他轻松的人；顾砚声用同类脸——两个等不到人的陌生人在同一盏路灯下沉默。发现天赋：对不同男人可以换不同的脸。钩子：系统提示目标002的前女友自称是时染的双胞胎妹妹——但她是独生女。'))

blocks.append(P('【第2集 · 嫉妒杠杆】'))
blocks.append(P(f'陆司砚中午在楼下等她送饭，看见她肩上的男款围巾——好感度从34%直接飙到41%。核心手段：让他吃醋比让他开心涨分更快。男人对嫉妒没有防御机制，因为嫉妒不需要理性。钩子：顾砚声在展馆问她{L}你等的人是谁{R}，她没有回答。他看着她的眼神说了一句话——我知道你在演。'))

blocks.append(P('【第3集 · 极限双线】'))
blocks.append(P(f'陆司砚约晚餐，顾砚声约看展——同一条街，只隔一栋楼。极限时间管理，精确到分钟。从餐桌到展厅靠一辆出租车完成转移，差三十秒撞车。钩子：逃出餐厅大门时撞上一个人——{L}你刚才在陆司砚那桌说的话，我全听到了。{R} APP弹出：目标003 江辞野触发。身份需求判定中——无法分析。'))

blocks.append(P('【第4集 · 反套路电竞男】'))
blocks.append(P(f'江辞野追着她不放——职业电竞选手，直觉比普通人准太多，所有演技他都能感知。她切了一张新脸：完全不撩他，反而怼他——{L}你以为我在套路他们？是他们需要一个套路，不然怎么解释自己为什么沦陷？{R}江辞野被说服。好感度从0跳到22%。三个男人，同一天，全在涨。'))

# 第二幕
blocks.append(H2('第二幕：四线并行（第5-8集）'))

blocks.append(P('【第5集 · 正面遭遇】'))
blocks.append(P(f'陆司砚公司年会，顾砚声同时在场。两人第一次正面遭遇。她抢先出手——在陆司砚开口前走到两人中间：{L}给你们介绍一下，这位是……{R}一句废话把两人关系岔开。两个男人都觉得自己是{L}被正式介绍的那个{R}。钩子：年会上第三个人走进来——陆司砚的私人心理顾问温屿，目光在她身上停了四秒。APP弹出目标004。'))

blocks.append(P('【第6集 · 画里的她】'))
blocks.append(P(f'顾砚声画展开幕，她发现整个展厅的画——全是她。对艺术男不能感动，要沉默。她站在最大那幅画前三分钟没说话，他在她身后站了三分钟。最终她开口：{L}你画错了一个地方。我没那么脆弱。{R}把他的真心堵回去——越不领情，他越着迷。钩子：画展门口，江辞野粉丝灯牌上印着一张照片——是她。不知道谁拍的。'))

blocks.append(P('【第7集 · 热搜引爆】'))
blocks.append(P(f'照片事件发酵。四个男人同时看到热搜。她不对任何人解释，不回复，让他们自己猜、自己吵。粉丝在网上扒她，反而替她造了万人迷人设。陆司砚看到热搜后反而加快表白节奏——男人看到竞争对手时才不会退缩。钩子：温屿私信——{L}你不需要来看病。但如果你愿意来，我只是想听你说话。我是心理医生，但我看不懂你。{R}'))

blocks.append(P('【第8集 · 心理医生反杀】'))
blocks.append(P(f'温屿诊所——她装病入场，编造一个{L}童年缺爱的故事{R}。他听完说：{L}这是你刚编的，对吧。{R}被拆穿的瞬间她没有慌，反而笑起来：{L}对。那你告诉我，真的那个在哪。{R}温屿沉默很久——{L}你是反社会人格的娱乐型变体。你不是感受不到，你是不在乎。{R}钩子：他把诊断写进了病历。她回去看了三遍，第一次在镜子里看自己看了很久。'))

# 第三幕
blocks.append(H2('第三幕：翻车与翻盘（第9-13集）'))

blocks.append(P('【第9集 · 反制诊断】'))
blocks.append(P(f'她回去找温屿，直接问：{L}你是来治我的，还是来追我的？{R}温屿看着她——{L}都是。{R}她已经反过来把他的诊断当成了一个新角色：被看穿的人，你还离得开我吗？钩子：温屿诊所记录被人调取。调取人——顾砚声。他已经开始查她了。'))

blocks.append(P('【第10集 · 四男同城】'))
blocks.append(P(f'四个男人在同一天集中在CBD方圆两公里——陆司砚公司、顾砚声画廊、江辞野比赛、温屿诊所。她设计四人的时间差，精确到分钟。最后一步出差错：江辞野比赛提前结束。她用粉丝围堵转移注意，顺手把顾砚声推进陆司砚的电梯——两人在密闭空间里聊了十二层楼。钩子：电梯门开，陆司砚说——{L}她骗了我们所有人。但我没有不高兴，你知道为什么吗？{R}'))

blocks.append(P('【第11集 · 联手逼宫】'))
blocks.append(P(f'陆司砚和顾砚声联手把她约出来。她一个人赴约，对面坐着两个男人。全场高光台词：{L}你们在等我崩溃吗？我不觉得我做错了什么。你们要道歉我可以给——但先说清楚，道什么歉？{R}没有人答得上来。因为她从头到尾没说过一句喜欢——她只是让他们以为有可能。'))

blocks.append(P('【第12集 · 全网吃瓜】'))
blocks.append(P(f'江辞野在直播里公开表白。全网扒出她同时撩三个男人。她不躲——开小号在评论区跟网友一起分析自己。坏到极致反而成了人设。钩子：温屿发消息——{L}别人都在骂你。但你知道吗，你反而更受欢迎了。坏到让人想看看你到底多坏。{R}'))

blocks.append(P('【第13集 · 系统真相】'))
blocks.append(P(f'终极任务解锁。系统给出选择：①删除系统回归正常生活 ②永久绑定成为系统管理员。她选②。系统揭示真相——它是一个{L}猎人选拔系统{R}。上一任管理员退休了，它在全球筛了一万多人才找到她。它测试的不是她能不能攻略男人，是她会不会爱上攻略本身。APP界面变换：管理员模式已激活。可查看附近所有人好感度。可下发任务给其他宿主。可——修改好感度数值。她打开{L}附近猎物{R}名单。'))

# 第四幕
blocks.append(H2('第四幕：终局（第14-20集）'))

blocks.append(P('【第14集】成为管理员第一天。四个男人实时好感度没有一个低于60%。她可以修改数字。但她关掉界面——改了还叫什么狩猎。'))
blocks.append(P('【第15集】江辞野战队经理来找她做公关顾问。她接了。不是因为需要工作——下一批猎物在电竞圈。'))
blocks.append(P(f'【第16集】温屿辞职——{L}我诊断了太多人，只有一个人让诊断这个行为本身失效。{R}来找她合伙。一个心理医生和一个猎人，开了间情感咨询公司。'))
blocks.append(P(f'【第17集】公司开张。第一批客户是三个被渣男伤害的女生。她教的不是怎么挽回——是{L}怎么让他以为你在挽回，其实你在练手{R}。'))
blocks.append(P('【第18-19集】新猎物：顶流爱豆，全网女友粉千万。经纪公司请她摆平一个蹭流量的女演员。她接了活，反手把女演员招进自己公司。'))
blocks.append(P('【第20集 · 大结局】没有跟任何男人在一起。城市最高层开工作室，系统投射全息屏幕——几百个头像浮动，每一张脸都是可以开始也可以终止的狩猎。温屿在隔壁写了本书《论反社会人格的情感应用》。顾砚声画了一幅画挂墙上——画的是她们第一次见面，她站在江边，笑得轻飘飘的，像一个没有重量的谜。'))

blocks.append(P('终场：时染站在落地窗前。手机弹出新消息——新目标检测：下一城市。难度：SSS级。建议立即出发。她拿起包，对着镜子补口红。镜子里的笑和第一集被分手时一模一样——不同的是，这次是她自己选的。'))

# 节奏总览
blocks.append(H1('节奏总览'))
blocks.append(P('Ep 1-4  →  开局：四目标初现，多线并行展开'))
blocks.append(P('Ep 5-8  →  升温：四线深度纠缠，修罗场雏形'))
blocks.append(P('Ep 9-12 →  爆发：翻车、联手、全网吃瓜、系统真相'))
blocks.append(P('Ep 13   →  转折：升级管理员，规则重写'))
blocks.append(P('Ep 14-20 → 终局：不是她选男人，是整个游戏归她写规则'))

# Send in batches
batch_size = 50
all_ids = []
for i in range(0, len(blocks), batch_size):
    batch = blocks[i:i+batch_size]
    ids = add_blocks(DOC_ID, batch)
    all_ids.extend(ids)
    print(f'Batch {i//batch_size + 1}: sent {len(batch)} blocks, got {len(ids)} IDs')

print(f'\nDone! Document URL: https://bytedance.feishu.cn/docx/{DOC_ID}')
