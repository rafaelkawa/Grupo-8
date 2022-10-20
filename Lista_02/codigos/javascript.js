const sortArray = (nums) => {
    // algoritimo bubble sort 
    // faz um loop dentro de um loop e vai comparando o valor da instancia atual com o prox valor, se for maior elas trocam de lugares, se for menor ela chama o proximo
    // O(n²)
    let tmp = 0;
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        for (let j = 1; j < n - i; ++j) {
            if (nums[j - 1] > nums[j]) {
                tmp = nums[j];
                nums[j] = nums[j - 1];
                nums[j - 1] = tmp;
            }
        }
    }
    return nums;
};
