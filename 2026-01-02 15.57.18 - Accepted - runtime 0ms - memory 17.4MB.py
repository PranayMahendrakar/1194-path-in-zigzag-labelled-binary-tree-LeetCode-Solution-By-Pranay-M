class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # First, find the level of the label
        level = 0
        n = label
        while n > 0:
            n //= 2
            level += 1
        
        result = []
        
        while label >= 1:
            result.append(label)
            
            # Move to parent
            # First, find the "normal" position at this level
            # Level starts from 1: level 1 has 1 node, level 2 has 2, etc.
            level_start = 2 ** (level - 1)
            level_end = 2 ** level - 1
            
            # If this level is "reversed" (even levels are reversed, 1-indexed)
            # The zigzag pattern alternates: level 1 is normal, level 2 reversed, level 3 normal, etc.
            
            # Find the "mirror" position
            mirror_label = level_start + level_end - label
            
            # Parent of mirror position in normal tree
            parent = mirror_label // 2
            
            label = parent
            level -= 1
        
        return result[::-1]