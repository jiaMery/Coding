/*************************************************************************
	> File Name: BubbleSort.cpp
	> Author:jiaMery 
	> Mail:jiajiama@mail.ustc.edu.cn 
	> Created Time: 2017年11月02日 星期四 21时22分55秒
 ************************************************************************/


/*1. 从左开始比较相邻的两个元素x和y，如果 x > y 就交换两者
2. 执行比较和交换，直到到达数组的最后一个元素
3. 重复执行1和2，直到执行n次，也就是n个最大元素都排到了最后*/
void bubbleSort(vector<int> &nums)
{
    for(int i=0;i<nums.size()-1;i++)
    {
        for(int j=0;j<nums.size()-i-1;j++)
        {
            if(nums[j]>nums[j+1])
            {
                int temp=nums[j];
                nums[j]=nums[j+1];
                nums[j+1]=temp;
            }
        }
    }
}
