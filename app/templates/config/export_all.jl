macro export_all()
  cur_module = current_module()

  cur_string = string(cur_module)
  curFunctions = Base.REPLCompletions.completions(cur_string * ".", length(cur_string)+1)
  curFunctions = filter(x-> x != "eval", curFunctions[1])

  cur_expression = quote end  # start out with a blank quoted expression
  for fun in curFunctions
    fname = Symbol("$(fun)")   # create your function name
    blk = quote
      export $(esc(fname))
    end
    append!(cur_expression.args, blk.args)
  end
  cur_expression
end
