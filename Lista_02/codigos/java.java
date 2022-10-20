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
 
    // chamada inicial para recursão
    void add(int val) {
        raiz = addRec(raiz, val); 
    }
 
    // adiciona recursivo na BST
    No addRec(No raiz, int val)
    {
 
        // se arovre vazia, cria primeiro nó/raiz
        if (raiz == null) {
            raiz = new No(val);
            return raiz;
        }
 
        //se nao, vai comparando o valor atual e navegandoo até achar a posicao correta de insercao
        else if (val < raiz.val)
            raiz.esq = addRec(raiz.esq, val);
        else if (val > raiz.val)
            raiz.dir = addRec(raiz.dir, val);
        return raiz;
    }
 
    // meotod inicial para print recursivo
    void print() { printRec(raiz); }
 
    // printa a arvore em ordem transversal
    void printRec(No raiz)
    {
        if (raiz != null) {
            printRec(raiz.esq);
            System.out.println(raiz.val);
            printRec(raiz.dir);
        }
    }
    
    // algoritimo de busca de nó
    public No search(No raiz, int val) {
        if(raiz == null ){
            return null;
        } 
        if (raiz.val == val) {
            return raiz;
        }
        if(raiz.val > val) {
            return search(raiz.esq, val);
        }
        return search(raiz.dir, val);
    }
 
   // main para executar
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
    System.out.println("O elemento" + tree.search(tree.raiz, 40).val + " foi achado");
}
}
