def groupSumClump(start, nums, target):
  if target == 0:
    return True
  elif start == len(nums):
    return False
  else:
    if nums[start] == target:
      return True 
    else:
      if start <= len(nums) - 2:
        counter = 0
        for i in range(start + 1, len(nums)):
          if nums[i] == nums[start]:
            counter += 1
          else:
            break
        if counter > 0:
          return(groupSumClump((start + counter + 1), nums, (target - (counter + 1)*nums[start])) or groupSumClump((start + counter + 1), nums, target))
        else:
          return(groupSumClump((start + 1), nums, target - nums[start]) or groupSumClump((start + 1), nums, target))
      else:
        return False 
def main():
  print(groupSumClump(0, [2, 4, 4, 8, 4, 4, 4, 7], 14))
main()