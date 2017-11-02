/*************************************************************************
	> File Name: SelectionSort.cpp
	> Author: jiaMery
	> Mail: jiajiama@mail.ustc.edu.cn
	> Created Time: 2017年11月02日 星期四 22时23分45秒
 ************************************************************************/

/*从左开始，选择后面元素中最小值，和最左元素交换
从当前已交换位置往后执行，直到最后一个元素*/
void selectionSort(vector<int> &nums)
{
    for(int i=0;i<nums.size()-1;i++)
    {
        int min=i;
        for(int j=i;j<nums.size();j++)
        {
            if(nums[j]<nums[min])
            {
                min=j;
            }
        }
        int temp=nums[i];
        nums[i]=nums[min];
        nums[min]=temp;
    }
}
