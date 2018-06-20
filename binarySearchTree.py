class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        new_node = Node(new_val)
        if self.root is None:
            self.root = new_node
        else:
            parent_node = self.root
            child_node = self.root
            while child_node != None:
                parent_node = child_node
                if new_val < parent_node.value:
                    child_node = parent_node.left
                elif new_val > parent_node.value:
                    child_node = parent_node.right
            if  new_val < parent_node.value:
                parent_node.left = new_node
            elif new_val > parent_node.value:
                parent_node.right = new_node


    def search(self, find_val):
        if self.root is None:
            return False
        curr_node = self.root
        while curr_node != None and  curr_node.value != find_val:
            if find_val < curr_node.value:
                curr_node = curr_node.left
            elif find_val > curr_node.value:
                curr_node = curr_node.right
        if  curr_node == None:
            return False
        return True

    
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a in-order traversal."""
        return self.inorder_print(self.root, "")

    
    def inorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start == None:
            return traversal
        traversal = self.inorder_print(start.left, traversal)
        if len(traversal) == 0:
            traversal = str(start.value)
        else:
            traversal += "-" + str(start.value)
        traversal = self.inorder_print(start.right, traversal)
        return traversal

# Test cases
def main():
    # Set up tree
    tree = BST(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    # Check search
    # Should be True
    print(tree.search(4))
    # Should be False
    print(tree.search(6))
    #should print the BST nodes in ascending order
    print(tree.print_tree())

if __name__ == "__main__":
    main()