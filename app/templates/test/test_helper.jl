__precompile__()

module TestHelper
  include("../config/application.jl")
  using .Application
  using Base.Test

  for cur_item in readdir("test")
    if startswith(cur_item, ".") ; continue ; end
    if endswith(cur_item, ".jl") ; continue ; end
    for sub_item in readdir("test/$cur_item")
      if startswith(sub_item, ".") ; continue ; end
      include("../test/$cur_item/$sub_item")
    end
  end

  function main()
    println("done.")
  end
end
