function include_all(cur_item)
  if isfile(cur_item)
    if endswith(cur_item, ".jl")
      include("../$cur_item")
      return
    end
  end

  if !isdir(cur_item) ; throw(LoadError) ; end

  for sub_item in readdir(cur_item)
    if startswith(sub_item, ".") ; continue ; end
    include_all("$cur_item/$sub_item")
  end
end
