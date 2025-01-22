int32_t main(void) {
  uint32_t i,k;
  float32_t *inputF32, *outputF32;
  inputF32 = &testInput_f32_1kHz_15kHz[0];
  outputF32 = &testOutput[0];
  for (i=0; i < TEST_LENGTH_SAMPLES; i++) {
    outputF32[i] = 0.f;
    for (k=0; k < NUM_TAPS_ARRAY_SIZE; k++) {
      outputF32[i] += inputF32[i+k]*firCoeffs32[k];
    }
  }
}
