__precompile__()

module Application
  include("include_all.jl")
  include("export_all.jl")

  ordered_dirs_included = ["vendor", "lib", "app"]
  for included_dir in ordered_dirs_included
    include_all(included_dir)
  end
  @export_all

  function main()
    println("done.")
  end
end