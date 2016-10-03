macro export_all_except(excluded_objects=[])
  excluded_objects = eval(excluded_objects)
  cur_module = current_module()

  cur_string = string(cur_module)
  cur_objects = Base.REPLCompletions.completions(cur_string * ".", length(cur_string)+1)
  cur_objects = filter(x-> x != "eval", cur_objects[1])

  cur_expression = quote end  # start out with a blank quoted expression
  for cur_obj in cur_objects
    if cur_obj in excluded_objects ; continue ; end
    oname = Symbol("$(cur_obj)")   # create your function name
    blk = quote
      export $(esc(oname))
    end
    append!(cur_expression.args, blk.args)
  end
  cur_expression
end
