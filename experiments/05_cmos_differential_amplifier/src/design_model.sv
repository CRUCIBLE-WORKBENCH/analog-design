module differential_pair_model;
  function real differential_gain(input real gm, input real rd, input real ro);
    differential_gain = -gm * (rd * ro / (rd + ro));
  endfunction
endmodule
