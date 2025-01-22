#include <stdio.h>
#include <arm_neon.h>
// Function to perform MAC operation on 4-element vectors
float32_t mac_neon(float32_t *A, float32_t *B) {
    // Load vectors A and B
    float32x4_t a = vld1q_f32(A);
    float32x4_t b = vld1q_f32(B);
    // Perform element-wise multiplication
    float32x4_t c = vmulq_f32(a, b);
    // perform accumulation
    float32_t result = vaddvq_f32(c);
    return result;
}

int main() {
    // Define 4-element vectors A and B
    float32_t A[4] = {1.0, 2.0, 3.0, 4.0};
    float32_t B[4] = {5.0, 6.0, 7.0, 8.0};
    float32_t result;

    // Perform MAC operation
    result=mac_neon(A, B);

    // Print the result
    printf("Result: %f\n",result);

    return 0;
}
