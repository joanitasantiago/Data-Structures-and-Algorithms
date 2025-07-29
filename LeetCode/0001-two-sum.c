// Given an array of integers nums and an integer target,
// return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution,
// and you may not use the same element twice.

// You can return the answer in any order.

// Constraints:

// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.

#include <stdio.h>
#include <stdlib.h>
#define TABLE_SIZE 2048 // p estudos 1024, 2048, ou 4096 é suficiente.

typedef struct
{
    int key;
    int value;
} HashMap;


int* solution1(int input[], int inputLength, int target){
    int* result1 = malloc(2 * sizeof(int));

    for (int i = 0; i < inputLength - 1; i++)
    {
        for (int j = i+1; j < inputLength; j++)
        {
            if (input[i] + input[j] == target)
            {
                result1[0] = i;
                result1[1] = j;
                return result1;
            }
            
        }
    }

    result1[0] = -1;
    result1[1] = -1;
    return result1;
}

int main() {
    int input[] = {3,2,4};
    int target = 6;
    int inputLength = sizeof(input) / sizeof(input[0]);

    int* result1 = solution1(input, inputLength, target);

    printf("[%d, %d]\n", result1[0], result1[1]);

    free(result1);

    return 0;
}



// Por que usar ponteiros?
// C não permite retornar arrays diretamente
// Arrays locais (tipo int resultado[2]) somem ao fim da função (vivem na stack)

// Se tentar retornar isso, o programa pode acessar lixo de memória.

// Ponteiros + malloc permitem retorno dinâmico
// Com malloc, é alocada memória na heap, que sobrevive após o return

// Assim você pode retornar um ponteiro que aponta pra um array seguro

// Por que liberar com free() depois?
// Porque malloc reserva memória manualmente

// Se você não liberar, vai vazar memória (memory leak)