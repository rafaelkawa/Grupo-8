// declaramos as principais informacoes e estruturas numa BST e criamos alguns metodos essenciais para manuear, como add e print
public class BinarySearchTree {
    class Node {
        int val;
        Node left, right;
 
        public Node(int item)
        {
            val = item;
            left = right = null;
        }
    }
 
    // Root of BST
    Node root;
 
    // Constructor
    BinarySearchTree() { root = null; }
 
    BinarySearchTree(int value) { root = new Node(value); }
 
    // This method mainly calls addRec()
    void add(int val) { root = addRec(root, val); }
 
    /* A recursive function to
       add a new val in BST */
    Node addRec(Node root, int val)
    {
 
        /* If the tree is empty,
           return a new node */
        if (root == null) {
            root = new Node(val);
            return root;
        }
 
        /* Otherwise, recur down the tree */
        else if (val < root.val)
            root.left = addRec(root.left, val);
        else if (val > root.val)
            root.right = addRec(root.right, val);
 
        /* return the (unchanged) node pointer */
        return root;
    }
 
    // This method mainly calls printRec()
    void print() { printRec(root); }
 
    // A utility function to
    // do print traversal of BST
    void printRec(Node root)
    {
        if (root != null) {
            printRec(root.left);
            System.out.println(root.val);
            printRec(root.right);
        }
    }
    
    public Node search(Node root, int val) {
        if(root == null ){
            return null;
        } 
        if (root.val == val) {
            return root;
        }
        if(root.val > val) {
            return search(root.left, val);
        }
        return search(root.right, val);
    }
 
   
   public static void main(String[] args){
    BinarySearchTree tree = new BinarySearchTree();

    tree.add(50);
    tree.add(30);
    tree.add(20);
    tree.add(40);
    tree.add(70);
    tree.add(60);
    tree.add(80);
    
    // print print traversal of the BST
    tree.print();
    System.out.println("O elemento" + tree.search(tree.root, 40).val + " foi achado");
}
}
