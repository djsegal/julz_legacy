__precompile__()

module Application
  include("include_all.jl")
  include("export_all_except.jl")

  ordered_dirs_included = ["vendor", "config/initializers", "lib", "app"]
  for included_dir in ordered_dirs_included
    include_all(included_dir)
  end
  @export_all_except

  function main()
    println("done.")
  end
end
