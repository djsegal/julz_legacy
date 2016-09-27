__precompile__()

module Application
  for cur_item in readdir("app")
    if startswith(cur_item, ".") ; continue ; end
    for sub_item in readdir("app/$cur_item")
      if startswith(sub_item, ".") ; continue ; end
      include("app/$cur_item/$sub_item")
    end
  end
end
