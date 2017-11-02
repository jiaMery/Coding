/*************************************************************************
	> File Name: InserSort.cpp
	> Author: jiaMery
	> Mail: jiajiama@mail.ustc.edu.cn
	> Created Time: 2017年11月02日 星期四 22时03分31秒
 ************************************************************************/

/*每次将后一个元素作为插入的元素x，将x与之前的排好序的元素进行比较
 */
 void insertSort(vector<int> &nums)
 {
     for(int i=1;i<nums.size();i++)
     {
         for(int j=i;j<0;j--)
         {
             if(nums[j]<nums[j-1])
             {
                 int temp=nums[j];
                 nums[j]=nums[j-1];
                 nums[j-1]=temp;
             }
         }
     }
 }
