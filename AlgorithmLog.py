# Algorithm Logs

"""
the notes is above the coresponding code like this:

# notes
coresponding code

"""

#===============================================================================
# date: 2023/07/29
#===============================================================================
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        """"
        螺旋矩阵Ⅱ：
        这道题的难点就是如何改变旋转的方向, 与螺旋矩阵one类似, 采用一个数组保存四个方向(directions),
        然后设置初始方向为向右，所以启示坐标设置为(0,-1), 输出的矩阵初始化为全0, 更改前进方向的条件为:
        1.坐标在0到n-1之外;
        2.下一个坐标的矩阵值为0。
        从1循环到n**2+1输出矩阵就可得到答案。
        """

        matrix = [[0]*n for i in range(n)] # 初始化矩全为0
        directions = [(0,1),(1,0),(0,-1),(-1,0)] # 设置前进方向依次为右,下,左,上
        dir = 0 # 设置初始化方向
        i,j = 0,-1 # 设置初始坐标
        for key in range(1,n*n+1):
            di,dj = directions[dir%4] # 获得坐标改变量
            if not 0<=i+di<n or not 0<=j+dj<n or matrix[i+di][j+dj] != 0: # 判断下一坐标是否需要改变方向
                dir += 1 # 改变方向
                di,dj = directions[dir%4] # 获得新的坐标改变值
            i += di
            j += dj
            matrix[i][j] = key # 矩阵赋值
        return matrix

#===============================================================================
# date: 2023/07/30
#===============================================================================
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        旋转链表：
        这道题目要求向右旋转指定次数, 思路就是先将链表首尾相连, 然后根据次数移动现在相邻的首尾
        node, 最后将尾部节点指向None, 返回首节点即可。
        """
        
        # 空链表或者只有一个元素的链表直接返回头节点
        if not head or not head.next:
            return head
        # 利用pre记录链表首节点
        pre = head
        # 记录链表长度
        length = 1
        # 遍历链表找到尾节点，并计算链表长度
        while head.next:
            length += 1
            head = head.next
        # 首尾相连
        head.next = pre
        # 移动次数超过链表长度时取余
        k = k % length
        # 此时链表方向为向左, 用链表长度减去移动次数改变方向为向右(画图增加理解)
        k = length - k
        # 开始移动
        if k > 0:
            for i in range(k):
                head = pre
                pre = head.next
        # 移动结束，将尾部节点指向None
        head.next = None
        # 返回首节点
        return pre

#===============================================================================
# date: 2023/08/01
#===============================================================================
class Solution(object):
    def uniquePaths(self, m, n):
        """
        不同路径：
        这道题有很多解法，这里采用动态规划，先对每一行进行更新，然后对每一列进行更新：
        第一行只有一条路径，所以全为1，第一列同理全为1；
        其余位置只有有上一行或者上一列的位置达到，所以值等于二者之和dp[i] = dp[i-1] + dp[i]
        其中dp[i-1]为同行前一列的路径数，dp[i]为同列上一行的路径数；
        对所有列进行操作，返回dp最后一个数字即可。
        """
        # 一维空间，其大小为 n
        dp = [1] * n
        for i in range(1, m): # 对所有行进行更新
            for j in range(1, n): # 对一行中的所有位置进行更新
                # 等式右边的 dp[j]是上一次计算后的，加上左边的dp[j-1]即为当前结果
                dp[j] = dp[j] + dp[j - 1]
        return dp[-1]

#===============================================================================
# date: 2023/08/04
#===============================================================================
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        不同路径Ⅱ:
        思路和没有障碍相同，只是外加一个对当前点的判断，如果值为1就设为0，不能达到这里，
        不为1时更新路径总数: dp[j] = dp[j] + dp[j-1], 详情可ctrl+f搜索"不同路径"。
        """
        m = len(obstacleGrid) # 行
        n = len(obstacleGrid[0]) # 列
        # 动态规划第一个元素
        if obstacleGrid[0][0] == 1: # 动态规划第一个元素
            dp = [0]
        else:
            dp = [1]
        # 第一行的情况
        for i in range(1,n):
            if obstacleGrid[0][i] == 1:
                dp.append(0)
            else:
                dp.append(dp[-1])
        # 从第二行开始的情况
        for i in range(1,m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j == 0:
                    dp[j] = dp[j]
                else:
                    dp[j] = dp[j] + dp[j-1]
        return dp[-1]

#===============================================================================
# date: 2023/08/05
#===============================================================================
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        最小路径和：
        对于给出的grid中间的任意一个点，到达的最小路径为其前方点和上方点的最小路径加上
        该点的数字，所以可以使用动态规划更新标准为: dp[j] = min(dp[j],dp[j-1]) + grid[i][j]
        """
        # 获得网格信息
        r = len(grid)
        c = len(grid[0])
        #初始化dp
        dp = []
        dp.append(grid[0][0])
        for i in range(1,c):
            dp.append(grid[0][i] + dp[i-1])
        # 从第二行开始
        for i in range(1,r):
            # 第一个元素只能由上方元素得到
            dp[0] = dp[0] + grid[i][0]
            # 从第二列开始
            for j in range(1,c):
                # 更新dp
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]

#===============================================================================
# date: 2023/08/06
#===============================================================================
class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        简化路径：
        思路是通过split函数以'/'将path分开，然后依次判断每个字符串s：
        如果s在['.', '', '..']中，说明不是路径，所以不能加入到最终的输出结果res中，
        其实如果s等于'..', 还要进一步将res中的最后一个元素删除, 在res中还有元素的情况下,
        最后将res依次输出，加上'/'即可。
        """

        # 拆分路径
        tmp = path.split('/')
        # 不能加入到输出路径res中的元素
        target = ['.', '', '..']
        # 保存路径
        res = []
        # 开始遍历
        for s in tmp:
            # 可以加入输出路径的情况
            if s not in target:
                res.append(s)
                continue
            # 当输出路径res还有上一级时才返回上一级
            if s == '..' and len(res) > 0:
                res.pop()
        out = ''
        # 当res为空时表示为根目录
        if len(res) == 0:
            return '/'
        # 输出完整路径
        for s in res:
            out += '/'+s
        return out

#===============================================================================
# date: 2023/08/07
#===============================================================================

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        矩阵置零:
        开始使用了比较笨的办法，先遍历给0做标记，然后再遍历给有标记的所在行和列设置为0。
        改进是给零元素所在首行和首列做标记，然后单独设置标签表示首行是否存在零，第二次遍历时
        只需要判断该元素所在行头或列头是否为0。
        来自力扣-画图小匠
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = False   # 标记首行是否有0元素
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if i == 0 and item == 0:
                    first_row = True    # 首行出现0元素，用标志位标记
                elif item == 0:
                    matrix[i][0] = 0    # 非首行出现0元素，将对应的列首置为0，说明该列要置为0
                    matrix[0][j] = 0    # 将对应的行首置为0，说明该行要置为0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 从最后一个元素反向遍历，避免行首和列首的信息被篡改
                if i == 0 and first_row:
                    matrix[i][j] = 0    # 首行元素是否置为0看标志位
                elif i != 0 and (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0    # 非首行元素是否置为0看行首和列首是否为0

#===============================================================================
# date: 2023/08/08
#===============================================================================
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        搜索二维矩阵:
        每一行按照升序排列，每一列也按照升序排列, 所以左下和右上连线上上的点向右移动变大，向上移动变小,
        因此只需要遍历即可。
        """
        # 获得矩阵大小
        m,n = len(matrix),len(matrix[0])
        # 从左下点开始遍历
        i = m -1
        j = 0
        # 超出边界时说明没有找到target
        while i >=0 and j < n:
            # 找到相同时直接返回True
            if matrix[i][j] == target:
                return True
            # 小于target向右边移动
            elif matrix[i][j] < target:
                j += 1
            # 大于target向上方移动
            else:
                i -= 1
        return False

#===============================================================================
# date: 2023/08/10
#===============================================================================
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Classify the colors in order. In other words, sort the numbers in the list.
        Traverse the array once, the large one is exchanged with the last element 
        of the array, the small one is exchanged with the front of the array, and 
        the subscript is constantly indented.
        """
        # get the length of the list
        length = len(nums)
        # when the length of the list is less than 2, which means we don't need to change the list.
        if length < 2:
            return
        # set the left index to zero
        left = 0
        # set the right index to the lenght
        right = length
        i = 0
        while i < right:
            # when the current value equals to 0, exchange with the left number, move both i and left forward
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            # when the current value equals to 1, do nothing but move i forward
            elif nums[i] == 1:
                i += 1
            # when the current value equals to 2, exchange with the right number, move right backward
            else:
                right -= 1
                nums[right], nums[i] = nums[i], nums[right]

#===============================================================================
# date: 2023/08/10
#===============================================================================
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        组合：
        给定n和k，在1到n中的自然数中任取k个不同的数，输出不同的组合总数。
        利用最大深度搜索dfs
        """
        # 所有可以选择的数组合
        target = [i for i in range(1,n+1)]
        # 储存每个组合
        out = []
        # 储存所有组合
        res = []
        def dfs(target,k):
            # 如果待组合个数为0，那么一个组合已经完整，添加到输出中
            if k == 0:
                res.append(out.copy())
                return
            # 遍历后续的所有可取数字
            for i in range(len(target)):
                # 添加到组合中
                out.append(target[i])
                # 对剩下需要添加的数字进行同样的操作
                dfs(target[i+1:],k-1)
                # 删除最上面的数字开始回溯
                out.pop()
        dfs(target,k)
        return res

#===============================================================================
# date: 2023/08/14
#===============================================================================
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        子集:
        求出给定数组的所有子集, [1,2]: [[],[1],[1,2]]
        观察例子我们发现, 每增加一个数字，结果中增加原有元素与新增数字的所有组合，
        所以可以使用迭代的方法
        """
        # 初始化输出数组为空集
        res = [[]]
        # 增加一个数字，循环一次
        for i in nums:
            # 更新数组为原数组加上所有元素与新增数字的组合
            res = res + [[i] + num for num in res]
        return res

#===============================================================================
# date: 2023/08/27
#===============================================================================
class Solution(object):
    """
    单词搜索：
    在给定的二维数组里寻找是否存在给定的单词，单词必须按照字母顺序，通过相邻的单元格内的字母构成，
    其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
    类似于这种与相邻单元格相关的问题，都可以用遍历+递归的方法解决：首先依次遍历二维数组，找到与
    单词首字母相同的元素，递归开始，依次判断该位置的相邻元素是否与单词的第二个字母相同，直到找到
    单词最后一个字母，返回True，否则返回False。
    """
    # 初始化四个相邻位置
    direction = [(1,0), (0,1), (-1,0), (0,-1)]
    def exist(self, board, word):
        h = len(board)
        # 二维数组为空，直接返回False
        if h == 0:
            return False
        w = len(board[0])
        # 用一个全为0的相同大小的数组来记录当前元素是否被使用
        mark = [[0]*w for i in range(h)]
        # 遍历开始
        for i in range(h):
            for j in range(w):
                # 如果元素与单词首字母相同，开始递归
                if board[i][j] == word[0]:
                    # 标记该字母已经使用
                    mark[i][j] = 1
                    # 如果递归结果为True，说明找到了单词
                    if self.check(i,j,mark,board,word[1:]):
                        return True
                    # 如果没找到，重新设该字母为未使用
                    else:
                        mark[i][j] = 0
        return False
    
    def check(self, i, j, mark, board, word):
        # 如果待检查单词为空，说明已经找到单词
        if len(word) == 0:
            return True
        # 依次遍历四个相邻位置
        for coor in self.direction:
            # 更新下表
            ci, cj = i+coor[0], j+coor[1]
            # 判断是否满足下标，以及是否与单词目前的首字母相同
            if 0<=ci<len(board) and 0<=cj<len(board[0]) and board[ci][cj] == word[0]:
                # 如果已经使用过，跳过
                if mark[ci][cj] == 1:
                    continue
                # 标记为已经使用
                mark[ci][cj] = 1
                # 开始递归
                if self.check(ci,cj,mark,board,word[1:]):
                    return True
                # 如果未能找到单词，恢复之前使用的元素为未使用状态
                else:
                    mark[ci][cj] = 0
        return False

#===============================================================================
# date: 2023/08/28
#===============================================================================
class Solution:
    """
    删除有序数组中的重复项：
    前两个元素保持不变，从第三个元素开始，判断nums[i-2]是否与当前元素nums[i]相等，相等则表明重复，
    不相等则将元素赋值给坐标下的元素。
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        # 记录当前满足要求的元素下标
        u = 0
        # 遍历整个数组
        for x in nums:
            # 元素不足两个时或者判断为不重复时赋值
            if u < 2 or nums[u-2] != x:
                # 满足要求保存
                nums[u] = x
                # 满足要求的个数增加
                u += 1
        return u
