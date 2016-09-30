__precompile__()

module Application
  for cur_item in readdir("app")
    if startswith(cur_item, ".") ; continue ; end
    for sub_item in readdir("app/$cur_item")
      if startswith(sub_item, ".") ; continue ; end
      include("../app/$cur_item/$sub_item")
    end
  end

  macro export_all()
    m = current_module()

    s = string(m)
    curFunctions = Base.REPLCompletions.completions(s * ".", length(s)+1)
    curFunctions = filter(x-> x != "eval", curFunctions[1])

    e = quote end  # start out with a blank quoted expression
    for fun in curFunctions
      fname = Symbol("$(fun)")   # create your function name
      blk = quote
        export $(esc(fname))
      end
      append!(e.args, blk.args)
    end
    e
  end

  @export_all

  function main()
    println("done.")
  end
end