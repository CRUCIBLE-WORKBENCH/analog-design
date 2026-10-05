module nand_family_model;
  function bit cmos_nand(input bit a, input bit b);
    cmos_nand = ~(a & b);
  endfunction
  function real pseudo_low(input real vdd, input real rn, input real rp);
    pseudo_low = vdd * rn / (rn + rp);
  endfunction
endmodule
