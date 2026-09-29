module square_wave_oscillator_model;
  function real frequency(input real r, input real c, input real beta);
    frequency = 1.0 / (2.0 * r * c * $ln((1.0 + beta) / (1.0 - beta)));
  endfunction
endmodule
