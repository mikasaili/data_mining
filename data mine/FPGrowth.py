class head_node(object):
    def __init__(self, head_name, num, soft_link):
        self.head_name = head_name
        self.num = num
        self.soft_link = soft_link

    def show(self):
        """Show the description of the present node"""
        pass


class FP_node(object):
    def __init__(self, node_name, val, parent, soft_link):
        self.node_name = node_name  # 当前节点的名称
        self.val = val  # 当前节点的次数
        self.parent = parent  # 当前节点的双亲结点
        self.children = {}  # 当前节点的孩子节点们，用字典存储，key为str，value为FP_node
        self.soft_link = soft_link  # 存储项头表指针的下一个节点

    def show(self):
        """show the description of the present FP_node"""
        pass


class FPGrowth(object):
    def __init__(self, ThresHold):
        self.ThresHold = ThresHold  # 设定阈值，对item进行过滤
        self.mapping = {}
        self.head_table = []  # 项头表
        self.root_node = FP_node("root", None, None, None)  # FP树的根节点

    def fit(self, dataset):
        """
        仿照sklearn写的fit接口
        :param dataset: 输入数据
        """
        self.scan_data(dataset)  # 扫描数据
        self.head_table_mapping = {}
        for name, num in self.mapping.items():
            node = head_node(name, num, None)
            self.head_table_mapping[name] = node
            self.head_table.append(node)

        # 对head_table 根据node值进行降序排序
        self.head_table = sorted(self.head_table, key=lambda x: x.num, reverse=True)

        # 对原始数据的第二次扫描, 改变数据集中的数据
        for sublist in dataset:
            # 仅保留在head_table中存在的字母
            sublist[:] = [item for item in sublist if item in [node.head_name for node in self.head_table]]

            # 按照 head_table 中的 num 值进行降序排序
            sublist.sort(key=lambda item: next((node.num for node in self.head_table if node.head_name == item), 0),
                         reverse=True)

        self.Create_FP_tree(dataset)  # 生成一个FP树

        self.cond_base = self.Search_FP_tree()  # 搜索FP树

    def predict(self):
        """输出条件模式基"""
        for key, inner_dict in self.cond_base.items():
            if inner_dict:  # 只输出非空字典
                # 对内部字典降序输出
                sorted_dict = dict(sorted(inner_dict.items(), key=lambda x: x[1], reverse=True))

                # Calculate confidence scores and print the result
                total_support = self.mapping[key]  # Total support for the item in the dataset
                for item, support in sorted_dict.items():
                    confidence = support / total_support
                    print(f"{key} -> {item} : Support = {support}, Confidence = {confidence:.2}")

    def scan_data(self, dataset):
        """扫描一遍数据并删除低于阈值的那一部分"""
        for sublist in dataset:
            for item in sublist:
                if item in self.mapping:
                    self.mapping[item] += 1
                else:
                    self.mapping[item] = 1

        # 删除低于阈值的部分
        self.N = len(dataset)
        to_del = []
        for item, nums in self.mapping.items():
            if nums / self.N <= self.ThresHold:
                to_del.append(item)

        for item in to_del:
            del self.mapping[item]

    def Create_FP_tree(self, dataset):
        """
        生成一个FP树
        """
        for sublist in dataset:
            pres_node = self.root_node  # 每个数据都从根节点重新生成
            for item in sublist:
                if item in pres_node.children:  # 当前的node在parent中存在了，只需要将val + 1即可
                    pres_node.children[item].val += 1
                    pres_node = pres_node.children[item]  # 往下走一步
                else:  # 如果不存在这个孩子节点
                    tmp_node = FP_node(item, 1, pres_node, None)
                    pres_node.children[item] = tmp_node

                    # z好到这个字母对应的软链接在哪
                    soft_node = self.head_table_mapping[item]
                    while soft_node.soft_link != None:
                        soft_node = soft_node.soft_link
                    soft_node.soft_link = tmp_node  # 上一个soft_node 接上这个tmp_node

                    pres_node = tmp_node  # 当前节点就到了 tmp_node 这儿

    def Search_FP_tree(self):
        """
        对FP树进行反向搜索, 生成条件模式基
        """
        result = {}
        for idx in range(len(self.head_table) - 1, -1, -1):
            HeadNode = self.head_table[idx]  # 获取当前的项头表中的点
            pres_cond_base = {}  # 存储当前节点的条件模式基
            soft_node = HeadNode.soft_link
            while soft_node != None:
                parent = soft_node.parent
                while parent.node_name != "root":
                    if parent.node_name not in pres_cond_base:
                        pres_cond_base[parent.node_name] = soft_node.val
                    else:
                        pres_cond_base[parent.node_name] += soft_node.val

                    parent = parent.parent  # 向上走到当前节点的双亲节点 直到走到root_node
                soft_node = soft_node.soft_link
            # 到这儿pres_cond_base已经生成了，但是要将低于Threshold的值给去掉
            to_del = []
            for item, nums in pres_cond_base.items():
                if nums / self.N <= self.ThresHold:
                    to_del.append(item)
            for item in to_del:
                del pres_cond_base[item]

            result[HeadNode.head_name] = pres_cond_base

        return result