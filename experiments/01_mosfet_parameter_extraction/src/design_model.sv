package mosfet_parameter_model;
  parameter real COX = 8.42e-3;
  function real gm_from_id_vov(input real id, input real vov);
    gm_from_id_vov = 2.0 * id / vov;
  endfunction
  function real ro_from_lambda_id(input real lambda, input real id);
    ro_from_lambda_id = 1.0 / (lambda * id);
  endfunction
endpackage
