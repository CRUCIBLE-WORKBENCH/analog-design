module common_source_model;
  function real gain(input real gm, input real rd, input real ro);
    gain = -gm * (rd * ro / (rd + ro));
  endfunction
endmodule
