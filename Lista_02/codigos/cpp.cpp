#include <iostream>
using namespace std;

int main() {
#define size 10
  char arr1[] = {'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'};
  char arr2[size];

  for (int i = 0; i < size; i++) {
    arr2[i] = arr1[i];
    cout << arr2[i] + string("\n");
  }

  return 0;
}
