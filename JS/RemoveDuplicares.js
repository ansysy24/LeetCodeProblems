var removeDuplicates = function(nums) {
    let i = 0
    let j = 1
    while (j<nums.length){
        console.log(i,j)
        if (nums[i] == nums[j]){
            j += 1
        } else {
            nums[i+1] = nums[j]
            i += 1
        }
    }
    return i+1
};