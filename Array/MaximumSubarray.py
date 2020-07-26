"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


思路：
O(n)

这个与https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
二叉树中最大的路径和相似。

到了数组中显得更加清晰：
每个点都有两个向上返回的状态：
大于0就向上，否则不向上。

不大于0时还要进行一次取最大值。

第一次写的时候把路径也带上了，后面发现没有必要。

带上路径比较慢 500ms - 700ms.

不带的话可以跑 28 ms.

测试地址：
https://leetcode.com/problems/maximum-subarray/description/

"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxes = nums[0]
        current = nums[0]
        
        for i in nums[1:]:
            maxes = max(maxes, current + i,  i)
            if current + i < i:
                current = i
            else:
                current = current + i
        
        return maxes
    
    
    class Solution:
      # @param A, a list of integers
      # @return an integer
     def maxSubArray(self, A):
          curr_sum = 0
          max_sum = -100000
          for i in range(len(A)):
              if curr_sum < 0 :
                  curr_sum = 0
             curr_sum = curr_sum + A[i]
             max_sum = max(curr_sum, max_sum)
         return max_sum
    
    
    
 public int maxSubArray(int[] A) 
    {    if(A==null || A.length==0)
            return 0;    
            int global = A[0];    
            int local = A[0];    
            for(int i=1;i<A.length;i++)    
                    {
                          local = Math.max(A[i],local+A[i]);
                          global = Math.max(local,global);    
                    }    
            return global;
    }
————————————————
版权声明：本文为CSDN博主「Code_Ganker」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/linhuanmars/java/article/details/21314059

        # if not nums:
        #     return 0
        
        # maxes = ([nums[0]], nums[0])
        # current = ([nums[0]], nums[0])
        
        # for i in nums[1:]:
        #     maxes = max(maxes, (current[0]+[i], current[1] + i), ([i], i), key=lambda x: x[1])
        #     if current[1] + i < i:
        #         current = ([i], i)
        #     else:
        #         current = (current[0]+[i], current[1] + i)
        
        # return maxes[1]
