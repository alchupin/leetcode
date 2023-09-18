def trap(height) -> int:
        max_pos = 0
        for i in range(len(height)):
            if height[i] > height[max_pos]:
                max_pos = i
        result_sum = 0
        left_max_pos = 0
        for j in range(max_pos):
            if height[j] > height[left_max_pos]:
                left_max_pos = j
            else:
                result_sum += height[left_max_pos] - height[j]
        right_max_pos = len(height)-1
        for k in range(len(height)-1, max_pos, -1):
            if height[k] > height[right_max_pos]:
                right_max_pos = k
            else:
                result_sum += height[right_max_pos] - height[k]
        return result_sum



height = [4,2,3]

print(trap(height))