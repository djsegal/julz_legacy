function include_all(cur_item, relative_dir="..", ignoreTopFiles=false)
  if isfile(cur_item)
    if endswith(cur_item, ".jl")
      include("$relative_dir/$cur_item")
      return
    end
  end

  if !isdir(cur_item) ; throw(LoadError) ; end

  for sub_item in readdir(cur_item)
    if startswith(sub_item, ".") ; continue ; end
    if endswith(sub_item, ".jl") && ignoreTopFiles
      continue
    end
    include_all("$cur_item/$sub_item", relative_dir)
  end
end
