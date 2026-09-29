module short_channel_nmos_model;
  function real drain_current(input real mucox, input real w, input real l, input real vov);
    drain_current = 0.5 * mucox * (w/l) * vov * vov;
  endfunction
endmodule
