// declaramos as principais informacoes e estruturas numa BST e criamos alguns metodos essenciais para manuear, como add e print
public class ArvoreBinariaBusca {
    class No {
        int val;
        No esq, dir;
 
        public No(int item)
        {
            val = item;
            esq = dir = null;
        }
    }
 

    No raiz;
 

    ArvoreBinariaBusca() { raiz = null; }
 
    ArvoreBinariaBusca(int value) { raiz = new No(value); }
 
    void add(int val) { raiz = addRec(raiz, val); }
 

    No addRec(No raiz, int val)
    {

        if (raiz == null) {
            raiz = new No(val);
            return raiz;
        }
 

        else if (val < raiz.val)
            raiz.esq = addRec(raiz.esq, val);
        else if (val > raiz.val)
            raiz.dir = addRec(raiz.dir, val);
 

        return raiz;
    }
 

    void print() { printRec(raiz); }
 
   
    void printRec(No raiz)
    {
        if (raiz != null) {
            printRec(raiz.esq);
            System.out.println(raiz.val);
            printRec(raiz.dir);
        }
    }
    
    public boolean search(No raiz, int val) {        
        if(raiz == null){
            return false;
            }
        while (raiz != null && raiz.val !=val){
            raiz = val < raiz.val ? raiz.left : raiz.right; //terminatory condition if val smaller than raiz value then search in left side else on right side
        }
        return raiz;  
        }
    }
 
   
   public static void main(String[] args){
    ArvoreBinariaBusca tree = new ArvoreBinariaBusca();

    tree.add(50);
    tree.add(30);
    tree.add(20);
    tree.add(40);
    tree.add(70);
    tree.add(60);
    tree.add(80);
    

    tree.print();
    if(tree.search(tree.raiz, 40)) {
        System.out.println("O elemento foi achado");
    } else {
        System.out.println("O elemento ñ foi achado");
    }
    
}
}
