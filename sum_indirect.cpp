#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>


//setup
void 
setup(int64_t N, uint64_t A[])
{
   printf(" inside sum_indirect problem_setup, N=%lld \n", N);

   for(int64_t i = 0; i < N; ++i){
      A[i] = rand() % N;

   }


}

int64_t
sum(int64_t N, uint64_t A[])
{
   printf(" inside sum_indirect perform_sum, N=%lld \n", N);
   int64_t sum = 0;
   int64_t index = A[0];

    for (int64_t i = 0; i < N; ++i) {
        sum += A[index];
        index = A[index];
    }


    return sum;

}

